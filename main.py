#!/usr/bin/env python3
"""
🧪 茚三酮检测 - 移动应用主程序
基于 Kivy 框架，支持 Android 和 iOS
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

# Kivy 导入
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.metrics import dp

# 图像处理
try:
    from PIL import Image as PILImage
    import numpy as np
    import colorsys
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("⚠️  Pillow 未安装，使用模拟模式")

# 相机（移动端）
try:
    from kivy.uix.camera import Camera
    HAS_CAMERA = True
except:
    HAS_CAMERA = False

# 文件选择器
try:
    from kivy.uix.filechooser import FileChooserListView
    HAS_FILECHOOSER = True
except:
    HAS_FILECHOOSER = False

# 数据目录
DATA_DIR = Path.home() / ".ninhydrin_app"
DATA_DIR.mkdir(exist_ok=True)
HISTORY_FILE = DATA_DIR / "history.json"


# ==================== 图像分析核心 ====================

class NinhydrinAnalyzer:
    """茚三酮图像分析器"""
    
    @staticmethod
    def analyze(image_path: str) -> dict:
        """分析图像"""
        if not HAS_PIL:
            return NinhydrinAnalyzer._mock_result()
        
        try:
            # 加载图像
            img = PILImage.open(image_path).convert('RGB')
            img_resized = img.resize((200, 200), PILImage.LANCZOS)
            img_np = np.array(img_resized)
            
            # 中心区域分析
            h, w = img_np.shape[:2]
            cy, cx = h // 2, w // 2
            radius = h // 4
            
            y, x = np.ogrid[:h, :w]
            mask = (x - cx)**2 + **(y - cy)2 <= radius**2
            
            # 平均 RGB
            avg_r = np.mean(img_np[:,:,0][mask])
            avg_g = np.mean(img_np[:,:,1][mask])
            avg_b = np.mean(img_np[:,:,2][mask])
            
            # HSV 转换
            r_norm, g_norm, b_norm = avg_r/255, avg_g/255, avg_b/255
            h_val, s_val, v_val = colorsys.rgb_to_hsv(r_norm, g_norm, b_norm)
            
            # 颜色检测
            is_purple_blue = 0.55 <= h_val <= 0.85
            purple_score = s_val if is_purple_blue else 0
            
            is_yellow = 0.1 <= h_val <= 0.18
            yellow_score = s_val if is_yellow else 0
            
            # 强度计算
            blue_score = (avg_b / 255) * 60
            purple_bonus = purple_score * 40
            yellow_penalty = yellow_score * 20
            
            intensity = max(0, min(100, blue_score + purple_bonus - yellow_penalty))
            
            # 判断结果
            if intensity < 20:
                result = "阴性"
                color = "#22c55e"
                advice = "偶联完成，可进行下一步反应"
            elif intensity < 40:
                result = "弱阳性"
                color = "#f97316"
                advice = "接近完成，建议延长反应 10-15 分钟"
            elif intensity < 70:
                result = "阳性"
                color = "#ef4444"
                advice = "未完全，继续偶联反应"
            else:
                result = "强阳性"
                color = "#a855f7"
                advice = "偶联失败，建议重新处理"
            
            confidence = min(0.98, 0.70 + (purple_score + yellow_score) * 0.20)
            
            return {
                'intensity': round(intensity, 1),
                'result': result,
                'r': int(avg_r),
                'g': int(avg_g),
                'b': int(avg_b),
                'confidence': round(confidence, 2),
                'color': color,
                'advice': advice,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'sample_id': f"#{datetime.now().strftime('%H%M%S')}"
            }
            
        except Exception as e:
            print(f"分析错误：{e}")
            return NinhydrinAnalyzer._mock_result()
    
    @staticmethod
    def _mock_result():
        """模拟结果（用于测试）"""
        return {
            'intensity': 45.0,
            'result': '阳性',
            'r': 180,
            'g': 190,
            'b': 220,
            'confidence': 0.85,
            'color': '#ef4444',
            'advice': '未完全，继续偶联反应',
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'sample_id': f"#{datetime.now().strftime('%H%M%S')}"
        }


# ==================== 历史数据管理 ====================

def load_history():
    """加载历史记录"""
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_history(data):
    """保存历史记录"""
    history = load_history()
    history.insert(0, data)
    history = history[:100]
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def clear_history():
    """清空历史"""
    if HISTORY_FILE.exists():
        HISTORY_FILE.unlink()


# ==================== 界面 - 检测页面 ====================

class DetectScreen(Screen):
    """检测页面"""
    
    image_path = StringProperty('')
    result_data = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(20)
        self.spacing = dp(10)
        
        # 标题
        title = Label(
            text='🧪 茚三酮检测',
            size_hint=(1, 0.1),
            font_size=dp(24),
            bold=True
        )
        self.add_widget(title)
        
        # 图像显示区域
        self.image_widget = Image(
            source='',
            size_hint=(1, 0.4),
            allow_stretch=True,
            keep_ratio=True
        )
        self.add_widget(self.image_widget)
        
        # 操作按钮
        btn_layout = BoxLayout(
            size_hint=(1, 0.1),
            spacing=dp(10)
        )
        
        self.camera_btn = Button(
            text='📷 拍照',
            font_size=dp(18)
        )
        self.camera_btn.bind(on_press=self.take_photo)
        btn_layout.add_widget(self.camera_btn)
        
        self.gallery_btn = Button(
            text='🖼️ 相册',
            font_size=dp(18)
        )
        self.gallery_btn.bind(on_press=self.select_from_gallery)
        btn_layout.add_widget(self.gallery_btn)
        
        self.add_widget(btn_layout)
        
        # 分析按钮
        self.analyze_btn = Button(
            text='🔬 开始分析',
            font_size=dp(18),
            size_hint=(1, 0.08)
        )
        self.analyze_btn.bind(on_press=self.analyze)
        self.analyze_btn.disabled = True
        self.add_widget(self.analyze_btn)
        
        # 进度条
        self.progress = ProgressBar(
            size_hint=(1, 0.05),
            value=0
        )
        self.add_widget(self.progress)
        
        # 结果区域（初始隐藏）
        self.result_layout = BoxLayout(
            orientation='vertical',
            size_hint=(1, 0.27),
            spacing=dp(5),
            opacity=0
        )
        
        self.result_label = Label(
            text='',
            size_hint=(1, 0.4),
            font_size=dp(28),
            bold=True
        )
        self.result_layout.add_widget(self.result_label)
        
        self.intensity_label = Label(
            text='',
            size_hint=(1, 0.2),
            font_size=dp(16)
        )
        self.result_layout.add_widget(self.intensity_label)
        
        self.advice_label = Label(
            text='',
            size_hint=(1, 0.4),
            font_size=dp(14),
            color=(0.3, 0.3, 0.3, 1)
        )
        self.result_layout.add_widget(self.advice_label)
        
        self.add_widget(self.result_layout)
    
    def take_photo(self, instance):
        """拍照"""
        if not HAS_CAMERA:
            self.show_message("相机不可用")
            return
        
        # 创建相机弹窗
        self.show_camera_popup()
    
    def show_camera_popup(self):
        """显示相机弹窗"""
        from kivy.uix.popup import Popup
        
        popup = Popup(
            title='拍照',
            size_hint=(0.9, 0.9)
        )
        
        layout = BoxLayout(orientation='vertical')
        
        if HAS_CAMERA:
            camera = Camera(
                index=0,
                resolution=(640, 480),
                play=True
            )
            layout.add_widget(camera)
        
        btn_layout = BoxLayout(size_hint=(1, 0.1))
        
        capture_btn = Button(text='📸 拍摄')
        
        def on_capture(instance):
            if HAS_CAMERA:
                # 保存照片
                photo_path = str(DATA_DIR / f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg")
                # camera.export_to_png(photo_path)  # 需要实际相机支持
                self.image_path = photo_path
                self.image_widget.source = photo_path
                self.analyze_btn.disabled = False
                popup.dismiss()
        
        capture_btn.bind(on_press=on_capture)
        btn_layout.add_widget(capture_btn)
        
        cancel_btn = Button(text='取消')
        cancel_btn.bind(on_press=popup.dismiss)
        btn_layout.add_widget(cancel_btn)
        
        layout.add_widget(btn_layout)
        popup.content = layout
        popup.open()
    
    def select_from_gallery(self, instance):
        """从相册选择"""
        from kivy.uix.popup import Popup
        
        popup = Popup(
            title='选择照片',
            size_hint=(0.9, 0.9)
        )
        
        layout = BoxLayout(orientation='vertical')
        
        # 文件选择器
        if HAS_FILECHOOSER:
            chooser = FileChooserListView(
                path=str(Path.home()),
                filters=['*.jpg', '*.jpeg', '*.png']
            )
            layout.add_widget(chooser)
            
            def on_select(instance):
                if chooser.selection:
                    self.image_path = chooser.selection[0]
                    self.image_widget.source = self.image_path
                    self.analyze_btn.disabled = False
                    popup.dismiss()
        else:
            # 简化版本
            label = Label(text='文件选择器不可用\n请使用拍照功能')
            layout.add_widget(label)
        
        btn_layout = BoxLayout(size_hint=(1, 0.1))
        
        if HAS_FILECHOOSER:
            select_btn = Button(text='选择')
            select_btn.bind(on_press=lambda x: None)  # 已在上面绑定
            btn_layout.add_widget(select_btn)
        
        cancel_btn = Button(text='取消')
        cancel_btn.bind(on_press=popup.dismiss)
        btn_layout.add_widget(cancel_btn)
        
        layout.add_widget(btn_layout)
        popup.content = layout
        popup.open()
    
    def analyze(self, instance):
        """分析图像"""
        if not self.image_path:
            return
        
        # 显示进度
        self.progress.value = 50
        
        def do_analyze(dt):
            # 执行分析
            self.result_data = NinhydrinAnalyzer.analyze(self.image_path)
            
            # 保存历史
            save_history(self.result_data)
            
            # 更新进度
            self.progress.value = 100
            
            # 显示结果
            self.show_result()
            
            # 重置进度条
            Clock.schedule_once(lambda dt: setattr(self.progress, 'value', 0), 1)
        
        Clock.schedule_once(do_analyze, 0.5)
    
    def show_result(self):
        """显示结果"""
        if not self.result_data:
            return
        
        data = self.result_data
        color = data['color']
        
        # 解析颜色
        r = int(color[1:3], 16) / 255
        g = int(color[3:5], 16) / 255
        b = int(color[5:7], 16) / 255
        
        # 设置结果区域背景色
        self.result_layout.canvas.before.clear()
        from kivy.graphics import Color, Rectangle
        with self.result_layout.canvas.before:
            Color(r, g, b, 0.2)
            self.result_rect = Rectangle(
                pos=self.result_layout.pos,
                size=self.result_layout.size
            )
        
        # 更新文本
        self.result_label.text = f"{data['result']}"
        self.result_label.color = (r, g, b, 1)
        
        self.intensity_label.text = f"反应强度：{data['intensity']} / 100"
        
        self.advice_label.text = f"💡 {data['advice']}"
        
        # 显示结果区域
        self.result_layout.opacity = 1
    
    def show_message(self, msg):
        """显示消息"""
        from kivy.uix.popup import Popup
        
        popup = Popup(
            title='提示',
            content=Label(text=msg),
            size_hint=(0.8, 0.3)
        )
        popup.open()


# ==================== 界面 - 历史页面 ====================

class HistoryScreen(Screen):
    """历史页面"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(20)
        self.spacing = dp(10)
        
        # 标题
        title = Label(
            text='📊 检测历史',
            size_hint=(1, 0.1),
            font_size=dp(24),
            bold=True
        )
        self.add_widget(title)
        
        # 历史记录列表
        self.history_layout = BoxLayout(
            orientation='vertical',
            size_hint=(1, 0.8),
            spacing=dp(5)
        )
        self.add_widget(self.history_layout)
        
        # 操作按钮
        btn_layout = BoxLayout(
            size_hint=(1, 0.1),
            spacing=dp(10)
        )
        
        export_btn = Button(
            text='📥 导出 CSV',
            font_size=dp(16)
        )
        export_btn.bind(on_press=self.export_csv)
        btn_layout.add_widget(export_btn)
        
        clear_btn = Button(
            text='🗑️ 清空',
            font_size=dp(16)
        )
        clear_btn.bind(on_press=self.clear_history)
        btn_layout.add_widget(clear_btn)
        
        self.add_widget(btn_layout)
    
    def on_enter(self):
        """进入页面时加载历史"""
        self.load_history()
    
    def load_history(self):
        """加载历史记录"""
        # 清空
        self.history_layout.clear_widgets()
        
        history = load_history()
        
        if not history:
            label = Label(
                text='暂无历史记录',
                color=(0.5, 0.5, 0.5, 1)
            )
            self.history_layout.add_widget(label)
            return
        
        # 添加历史记录项
        for item in history[:20]:  # 只显示最新 20 条
            item_layout = self.create_history_item(item)
            self.history_layout.add_widget(item_layout)
    
    def create_history_item(self, item):
        """创建历史项"""
        layout = BoxLayout(
            size_hint=(1, None),
            height=dp(60),
            spacing=dp(10)
        )
        
        # 结果标签
        result_label = Label(
            text=item['result'],
            size_hint=(0.3, 1),
            font_size=dp(18),
            bold=True
        )
        
        # 设置颜色
        color = item.get('color', '#999999')
        r = int(color[1:3], 16) / 255
        g = int(color[3:5], 16) / 255
        b = int(color[5:7], 16) / 255
        result_label.color = (r, g, b, 1)
        
        layout.add_widget(result_label)
        
        # 详情
        detail_layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.7, 1)
        )
        
        intensity_label = Label(
            text=f"强度：{item['intensity']}",
            size_hint=(1, 0.5),
            font_size=dp(14),
            halign='left'
        )
        detail_layout.add_widget(intensity_label)
        
        time_label = Label(
            text=item.get('timestamp', ''),
            size_hint=(1, 0.5),
            font_size=dp(12),
            color=(0.5, 0.5, 0.5, 1),
            halign='left'
        )
        detail_layout.add_widget(time_label)
        
        layout.add_widget(detail_layout)
        
        return layout
    
    def export_csv(self, instance):
        """导出 CSV"""
        history = load_history()
        
        if not history:
            return
        
        csv_lines = ["时间，样品 ID，强度，结果，R,G,B，置信度"]
        for item in history:
            csv_lines.append(
                f"{item['timestamp']},{item['sample_id']},{item['intensity']},"
                f"{item['result']},{item['r']},{item['g']},{item['b']},{item['confidence']}"
            )
        
        csv_path = DATA_DIR / f"history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        with open(csv_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(csv_lines))
        
        # 显示成功消息
        from kivy.uix.popup import Popup
        popup = Popup(
            title='导出成功',
            content=Label(text=f'文件已保存至:\n{csv_path}'),
            size_hint=(0.8, 0.4)
        )
        popup.open()
    
    def clear_history(self, instance):
        """清空历史"""
        from kivy.uix.popup import Popup
        
        confirm = Popup(
            title='确认',
            content=Label(text='确定清空所有历史记录？'),
            size_hint=(0.8, 0.3)
        )
        
        def do_clear(instance):
            clear_history()
            self.load_history()
            confirm.dismiss()
        
        btn_layout = BoxLayout(size_hint=(1, 0.2))
        
        yes_btn = Button(text='确定')
        yes_btn.bind(on_press=do_clear)
        btn_layout.add_widget(yes_btn)
        
        no_btn = Button(text='取消')
        no_btn.bind(on_press=confirm.dismiss)
        btn_layout.add_widget(no_btn)
        
        confirm.content = btn_layout
        confirm.open()


# ==================== 主应用 ====================

class NinhydrinApp(App):
    """茚三酮检测应用"""
    
    def build(self):
        # 设置窗口大小（桌面模式）
        if not self.is_mobile:
            Window.size = (400, 700)
        
        # 创建屏幕管理器
        sm = ScreenManager()
        
        # 添加页面
        sm.add_widget(DetectScreen(name='detect'))
        sm.add_widget(HistoryScreen(name='history'))
        
        return sm
    
    @property
    def is_mobile(self):
        """是否运行在移动端"""
        return sys.platform in ('android', 'ios')
    
    def on_start(self):
        """应用启动时"""
        print("🧪 茚三酮检测 启动")
        print(f"数据目录：{DATA_DIR}")


# ==================== 入口 ====================

if __name__ == '__main__':
    NinhydrinApp().run()
