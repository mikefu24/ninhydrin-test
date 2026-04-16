[app]

# (str) Title of your application
title = 茚三酮检测

# (str) Package name
package.name = ninhydrintest

# (str) Package domain (needed for android/ios packaging)
package.domain = org.lab

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy==2.2.0,pillow,numpy,android

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk_path = 

# (str) ANT directory (if empty, it will be automatically downloaded.)
android.ant_path = 

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

# (bool) If True, then automatically accept SDK license agreements
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# use that parameter together with android.entrypoint to set custom Java class instead of PythonActivity
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) The Java class that implements Python Service
#android.service_class_name = org.kivy.android.PythonService

# (str) Extra xml arguments written in the Android manifest.xml
#android.extra_xml = 

# (str) Extra android permissions
#android.extra_permissions = 

# (list) Java classes to add to the project (for advanced users)
#android.add_activities = 

# (list) Android libraries to include
#android.add_libs_armeabi = 
#android.add_libs_armeabi_v7a = 
#android.add_libs_arm64_v8a = 
#android.add_libs_x86 = 
#android.add_libs_mips = 

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file for custom backup rules (see official auto backup documentation)
#android.backup_rules = 

# (str) If you need to insert variables into your Android manifest.xml file,
# you can do so with the android.manifest_placeholders property
#android.manifest_placeholders = [myCustomVar:"value", myCustomVar2:"value2"]

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto resize feature (Android API >=31)
android.resizeable_activity = True

# (bool) If True, the app will be installed in the internal storage
android.install_location = auto

# (int) overrides the max number of simultaneous running apps
#android.max_running_apps = 

# (bool) If True, the app will be installed on the external storage
#android.install_location = preferExternal

# (str) The log level shown by logcat
#android.logcat_filters = 

# (bool) Copy library dependencies into the APK
#android.copy_libs = 1

# (str) The Android command line tools version to use
#android.tools = 

# (str) The path to a custom keystore file
#android.keystore = 

# (str) The keystore alias
#android.keystore_alias = 

# (str) The keystore password
#android.keystore_password = 

# (str) The key password
#android.key_password = 

# (str) The Android SDK path
#android.sdk_path = 

# (str) The Android NDK path
#android.ndk_path = 

# (str) The Android ANT path
#android.ant_path = 

# (bool) Whether to skip update the Android SDK
#android.skip_update = False

# (bool) Whether to accept the Android SDK license automatically
#android.accept_sdk_license = True

# (str) The path to the Android build-tools
#android.build_tools = 

# (str) The path to the Android platform-tools
#android.platform_tools = 

# (str) The path to the Android emulator
#android.emulator = 

# (bool) Whether to use the Android emulator
#android.use_emulator = False

# (str) The Android emulator skin
#android.emulator_skin = 

# (str) The Android emulator resolution
#android.emulator_resolution = 

# (str) The Android emulator dpi
#android.emulator_dpi = 

# (str) The Android emulator memory
#android.emulator_memory = 

# (str) The Android emulator storage
#android.emulator_storage = 

# (bool) Whether to use the Android emulator camera
#android.emulator_camera = False

# (bool) Whether to use the Android emulator microphone
#android.emulator_microphone = False

# (bool) Whether to use the Android emulator GPS
#android.emulator_gps = False

# (bool) Whether to use the Android emulator accelerometer
#android.emulator_accelerometer = False

# (bool) Whether to use the Android emulator gyroscope
#android.emulator_gyroscope = False

# (bool) Whether to use the Android emulator magnetometer
#android.emulator_magnetometer = False

# (bool) Whether to use the Android emulator proximity sensor
#android.emulator_proximity = False

# (bool) Whether to use the Android emulator light sensor
#android.emulator_light = False

# (bool) Whether to use the Android emulator pressure sensor
#android.emulator_pressure = False

# (bool) Whether to use the Android emulator temperature sensor
#android.emulator_temperature = False

# (bool) Whether to use the Android emulator humidity sensor
#android.emulator_humidity = False

# (bool) Whether to use the Android emulator ambient temperature sensor
#android.emulator_ambient_temperature = False

# (bool) Whether to use the Android emulator relative humidity sensor
#android.emulator_relative_humidity = False

# (bool) Whether to use the Android emulator barometer sensor
#android.emulator_barometer = False

# (bool) Whether to use the Android emulator step counter sensor
#android.emulator_step_counter = False

# (bool) Whether to use the Android emulator step detector sensor
#android.emulator_step_detector = False

# (bool) Whether to use the Android emulator game rotation vector sensor
#android.emulator_game_rotation_vector = False

# (bool) Whether to use the Android emulator geomagnetic rotation vector sensor
#android.emulator_geomagnetic_rotation_vector = False

# (bool) Whether to use the Android emulator rotation vector sensor
#android.emulator_rotation_vector = False

# (bool) Whether to use the Android emulator significant motion sensor
#android.emulator_significant_motion = False

# (bool) Whether to use the Android emulator tilt detector sensor
#android.emulator_tilt_detector = False

# (bool) Whether to use the Android emulator wrist tilt sensor
#android.emulator_wrist_tilt = False

# (bool) Whether to use the Android emulator pick up gesture sensor
#android.emulator_pick_up_gesture = False

# (bool) Whether to use the Android emulator wake up gesture sensor
#android.emulator_wake_up_gesture = False

# (bool) Whether to use the Android emulator glances gesture sensor
#android.emulator_glances_gesture = False

# (bool) Whether to use the Android emulator quick taps sensor
#android.emulator_quick_taps = False

# (bool) Whether to use the Android emulator medium power consumption
#android.emulator_medium_power = False

# (bool) Whether to use the Android emulator high power consumption
#android.emulator_high_power = False

# (bool) Whether to use the Android emulator low power consumption
#android.emulator_low_power = False

# (str) The Android emulator battery level
#android.emulator_battery_level = 

# (bool) Whether to use the Android emulator charging
#android.emulator_charging = False

# (str) The Android emulator network type
#android.emulator_network_type = 

# (str) The Android emulator network speed
#android.emulator_network_speed = 

# (bool) Whether to use the Android emulator no audio
#android.emulator_no_audio = False

# (bool) Whether to use the Android emulator no boot animation
#android.emulator_no_boot_animation = False

# (bool) Whether to use the Android emulator no snapshot
#android.emulator_no_snapshot = False

# (bool) Whether to use the Android emulator no window
#android.emulator_no_window = False

# (str) The Android emulator dns server
#android.emulator_dns_server = 

# (str) The Android emulator http proxy
#android.emulator_http_proxy = 

# (str) The Android emulator https proxy
#android.emulator_https_proxy = 

# (str) The Android emulator socks proxy
#android.emulator_socks_proxy = 

# (str) The Android emulator boot delay
#android.emulator_boot_delay = 

# (str) The Android emulator logcat output
#android.emulator_logcat_output = 

# (str) The Android emulator screen size
#android.emulator_screen_size = 

# (str) The Android emulator pixel density
#android.emulator_pixel_density = 

# (str) The Android emulator language
#android.emulator_language = 

# (str) The Android emulator locale
#android.emulator_locale = 

# (str) The Android emulator timezone
#android.emulator_timezone = 

# (str) The Android emulator keyboard
#android.emulator_keyboard = 

# (str) The Android emulator navigation
#android.emulator_navigation = 

# (str) The Android emulator trackball
#android.emulator_trackball = 

# (str) The Android emulator touchscreen
#android.emulator_touchscreen = 

# (str) The Android emulator keyboard layout
#android.emulator_keyboard_layout = 

# (str) The Android emulator keyboard character
#android.emulator_keyboard_character = 

# (str) The Android emulator keyboard modifiers
#android.emulator_keyboard_modifiers = 

# (str) The Android emulator keyboard keys
#android.emulator_keyboard_keys = 

# (str) The Android emulator keyboard key codes
#android.emulator_keyboard_key_codes = 

# (str) The Android emulator keyboard key names
#android.emulator_keyboard_key_names = 

# (str) The Android emulator keyboard key types
#android.emulator_keyboard_key_types = 

# (str) The Android emulator keyboard key labels
#android.emulator_keyboard_key_labels = 

# (str) The Android emulator keyboard key icons
#android.emulator_keyboard_key_icons = 

# (str) The Android emulator keyboard key colors
#android.emulator_keyboard_key_colors = 

# (str) The Android emulator keyboard key shapes
#android.emulator_keyboard_key_shapes = 

# (str) The Android emulator keyboard key sizes
#android.emulator_keyboard_key_sizes = 

# (str) The Android emulator keyboard key positions
#android.emulator_keyboard_key_positions = 

# (str) The Android emulator keyboard key rotations
#android.emulator_keyboard_key_rotations = 

# (str) The Android emulator keyboard key scales
#android.emulator_keyboard_key_scales = 

# (str) The Android emulator keyboard key skews
#android.emulator_keyboard_key_skews = 

# (str) The Android emulator keyboard key shears
#android.emulator_keyboard_key_shears = 

# (str) The Android emulator keyboard key transforms
#android.emulator_keyboard_key_transforms = 

# (str) The Android emulator keyboard key matrices
#android.emulator_keyboard_key_matrices = 

# (str) The Android emulator keyboard key vectors
#android.emulator_keyboard_key_vectors = 

# (str) The Android emulator keyboard key points
#android.emulator_keyboard_key_points = 

# (str) The Android emulator keyboard key lines
#android.emulator_keyboard_key_lines = 

# (str) The Android emulator keyboard key curves
#android.emulator_keyboard_key_curves = 

# (str) The Android emulator keyboard key arcs
#android.emulator_keyboard_key_arcs = 

# (str) The Android emulator keyboard key circles
#android.emulator_keyboard_key_circles = 

# (str) The Android emulator keyboard key ellipses
#android.emulator_keyboard_key_ellipses = 

# (str) The Android emulator keyboard key rectangles
#android.emulator_keyboard_key_rectangles = 

# (str) The Android emulator keyboard key squares
#android.emulator_keyboard_key_squares = 

# (str) The Android emulator keyboard key triangles
#android.emulator_keyboard_key_triangles = 

# (str) The Android emulator keyboard key polygons
#android.emulator_keyboard_key_polygons = 

# (str) The Android emulator keyboard key polylines
#android.emulator_keyboard_key_polylines = 

# (str) The Android emulator keyboard key paths
#android.emulator_keyboard_key_paths = 

# (str) The Android emulator keyboard key shapes
#android.emulator_keyboard_key_shapes = 

# (str) The Android emulator keyboard key paths
#android.emulator_keyboard_key_paths = 

# (str) The Android emulator keyboard key data
#android.emulator_keyboard_key_data = 

# (str) The Android emulator keyboard key format
#android.emulator_keyboard_key_format = 

# (str) The Android emulator keyboard key encoding
#android.emulator_keyboard_key_encoding = 

# (str) The Android emulator keyboard key compression
#android.emulator_keyboard_key_compression = 

# (str) The Android emulator keyboard key encryption
#android.emulator_keyboard_key_encryption = 

# (str) The Android emulator keyboard key decryption
#android.emulator_keyboard_key_decryption = 

# (str) The Android emulator keyboard key hashing
#android.emulator_keyboard_key_hashing = 

# (str) The Android emulator keyboard key signing
#android.emulator_keyboard_key_signing = 

# (str) The Android emulator keyboard key verifying
#android.emulator_keyboard_key_verifying = 

# (str) The Android emulator keyboard key authenticating
#android.emulator_keyboard_key_authenticating = 

# (str) The Android emulator keyboard key authorizing
#android.emulator_keyboard_key_authorizing = 

# (str) The Android emulator keyboard key validating
#android.emulator_keyboard_key_validating = 

# (str) The Android emulator keyboard key checking
#android.emulator_keyboard_key_checking = 

# (str) The Android emulator keyboard key testing
#android.emulator_keyboard_key_testing = 

# (str) The Android emulator keyboard key debugging
#android.emulator_keyboard_key_debugging = 

# (str) The Android emulator keyboard key profiling
#android.emulator_keyboard_key_profiling = 

# (str) The Android emulator keyboard key optimizing
#android.emulator_keyboard_key_optimizing = 

# (str) The Android emulator keyboard key analyzing
#android.emulator_keyboard_key_analyzing = 

# (str) The Android emulator keyboard key monitoring
#android.emulator_keyboard_key_monitoring = 

# (str) The Android emulator keyboard key logging
#android.emulator_keyboard_key_logging = 

# (str) The Android emulator keyboard key tracing
#android.emulator_keyboard_key_tracing = 

# (str) The Android emulator keyboard key tracking
#android.emulator_keyboard_key_tracking = 

# (str) The Android emulator keyboard key reporting
#android.emulator_keyboard_key_reporting = 

# (str) The Android emulator keyboard key alerting
#android.emulator_keyboard_key_alerting = 

# (str) The Android emulator keyboard key notifying
#android.emulator_keyboard_key_notifying = 

# (str) The Android emulator keyboard key warning
#android.emulator_keyboard_key_warning = 

# (str) The Android emulator keyboard key error
#android.emulator_keyboard_key_error = 

# (str) The Android emulator keyboard key info
#android.emulator_keyboard_key_info = 

# (str) The Android emulator keyboard key debug
#android.emulator_keyboard_key_debug = 

# (str) The Android emulator keyboard key verbose
#android.emulator_keyboard_key_verbose = 

# (str) The Android emulator keyboard key silent
#android.emulator_keyboard_key_silent = 

# (str) The Android emulator keyboard key quiet
#android.emulator_keyboard_key_quiet = 

# (str) The Android emulator keyboard key loud
#android.emulator_keyboard_key_loud = 

# (str) The Android emulator keyboard key soft
#android.emulator_keyboard_key_soft = 

# (str) The Android emulator keyboard key hard
#android.emulator_keyboard_key_hard = 

# (str) The Android emulator keyboard key light
#android.emulator_keyboard_key_light = 

# (str) The Android emulator keyboard key dark
#android.emulator_keyboard_key_dark = 

# (str) The Android emulator keyboard key bright
#android.emulator_keyboard_key_bright = 

# (str) The Android emulator keyboard key dim
#android.emulator_keyboard_key_dim = 

# (str) The Android emulator keyboard key clear
#android.emulator_keyboard_key_clear = 

# (str) The Android emulator keyboard key blur
#android.emulator_keyboard_key_blur = 

# (str) The Android emulator keyboard key sharp
#android.emulator_keyboard_key_sharp = 

# (str) The Android emulator keyboard key smooth
#android.emulator_keyboard_key_smooth = 

# (str) The Android emulator keyboard key rough
#android.emulator_keyboard_key_rough = 

# (str) The Android emulator keyboard key fine
#android.emulator_keyboard_key_fine = 

# (str) The Android emulator keyboard key coarse
#android.emulator_keyboard_key_coarse = 

# (str) The Android emulator keyboard key precise
#android.emulator_keyboard_key_precise = 

# (str) The Android emulator keyboard key accurate
#android.emulator_keyboard_key_accurate = 

# (str) The Android emulator keyboard key exact
#android.emulator_keyboard_key_exact = 

# (str) The Android emulator keyboard key approximate
#android.emulator_keyboard_key_approximate = 

# (str) The Android emulator keyboard key rough
#android.emulator_keyboard_key_rough = 

# (str) The Android emulator keyboard key estimated
#android.emulator_keyboard_key_estimated = 

# (str) The Android emulator keyboard key calculated
#android.emulator_keyboard_key_calculated = 

# (str) The Android emulator keyboard key computed
#android.emulator_keyboard_key_computed = 

# (str) The Android emulator keyboard key measured
#android.emulator_keyboard_key_measured = 

# (str) The Android emulator keyboard key observed
#android.emulator_keyboard_key_observed = 

# (str) The Android emulator keyboard key detected
#android.emulator_keyboard_key_detected = 

# (str) The Android emulator keyboard key recognized
#android.emulator_keyboard_key_recognized = 

# (str) The Android emulator keyboard key identified
#android.emulator_keyboard_key_identified = 

# (str) The Android emulator keyboard key classified
#android.emulator_keyboard_key_classified = 

# (str) The Android emulator keyboard key categorized
#android.emulator_keyboard_key_categorized = 

# (str) The Android emulator keyboard key grouped
#android.emulator_keyboard_key_grouped = 

# (str) The Android emulator keyboard key sorted
#android.emulator_keyboard_key_sorted = 

# (str) The Android emulator keyboard key filtered
#android.emulator_keyboard_key_filtered = 

# (str) The Android emulator keyboard key selected
#android.emulator_keyboard_key_selected = 

# (str) The Android emulator keyboard key chosen
#android.emulator_keyboard_key_chosen = 

# (str) The Android emulator keyboard key picked
#android.emulator_keyboard_key_picked = 

# (str) The Android emulator keyboard key found
#android.emulator_keyboard_key_found = 

# (str) The Android emulator keyboard key located
#android.emulator_keyboard_key_located = 

# (str) The Android emulator keyboard key positioned
#android.emulator_keyboard_key_positioned = 

# (str) The Android emulator keyboard key placed
#android.emulator_keyboard_key_placed = 

# (str) The Android emulator keyboard key set
#android.emulator_keyboard_key_set = 

# (str) The Android emulator keyboard key put
#android.emulator_keyboard_key_put = 

# (str) The Android emulator keyboard key get
#android.emulator_keyboard_key_get = 

# (str) The Android emulator keyboard key take
#android.emulator_keyboard_key_take = 

# (str) The Android emulator keyboard key bring
#android.emulator_keyboard_key_bring = 

# (str) The Android emulator keyboard key carry
#android.emulator_keyboard_key_carry = 

# (str) The Android emulator keyboard key hold
#android.emulator_keyboard_key_hold = 

# (str) The Android emulator keyboard key grasp
#android.emulator_keyboard_key_grasp = 

# (str) The Android emulator keyboard key grip
#android.emulator_keyboard_key_grip = 

# (str) The Android emulator keyboard key clutch
#android.emulator_keyboard_key_clutch = 

# (str) The Android emulator keyboard key grab
#android.emulator_keyboard_key_grab = 

# (str) The Android emulator keyboard key seize
#android.emulator_keyboard_key_seize = 

# (str) The Android emulator keyboard key catch
#android.emulator_keyboard_key_catch = 

# (str) The Android emulator keyboard key capture
#android.emulator_keyboard_key_capture = 

# (str) The Android emulator keyboard key trap
#android.emulator_keyboard_key_trap = 

# (str) The Android emulator keyboard key snare
#android.emulator_keyboard_key_snare = 

# (str) The Android emulator keyboard key net
#android.emulator_keyboard_key_net = 

# (str) The Android emulator keyboard key web
#android.emulator_keyboard_key_web = 

# (str) The Android emulator keyboard key mesh
#android.emulator_keyboard_key_mesh = 

# (str) The Android emulator keyboard key network
#android.emulator_keyboard_key_network = 

# (str) The Android emulator keyboard key system
#android.emulator_keyboard_key_system = 

# (str) The Android emulator keyboard key structure
#android.emulator_keyboard_key_structure = 

# (str) The Android emulator keyboard key organization
#android.emulator_keyboard_key_organization = 

# (str) The Android emulator keyboard key arrangement
#android.emulator_keyboard_key_arrangement = 

# (str) The Android emulator keyboard key configuration
#android.emulator_keyboard_key_configuration = 

# (str) The Android emulator keyboard key setup
#android.emulator_keyboard_key_setup = 

# (str) The Android emulator keyboard key installation
#android.emulator_keyboard_key_installation = 

# (str) The Android emulator keyboard key deployment
#android.emulator_keyboard_key_deployment = 

# (str) The Android emulator keyboard key implementation
#android.emulator_keyboard_key_implementation = 

# (str) The Android emulator keyboard key execution
#android.emulator_keyboard_key_execution = 

# (str) The Android emulator keyboard key operation
#android.emulator_keyboard_key_operation = 

# (str) The Android emulator keyboard key function
#android.emulator_keyboard_key_function = 

# (str) The Android emulator keyboard key action
#android.emulator_keyboard_key_action = 

# (str) The Android emulator keyboard key activity
#android.emulator_keyboard_key_activity = 

# (str) The Android emulator keyboard key process
#android.emulator_keyboard_key_process = 

# (str) The Android emulator keyboard key procedure
#android.emulator_keyboard_key_procedure = 

# (str) The Android emulator keyboard key method
#android.emulator_keyboard_key_method = 

# (str) The Android emulator keyboard key technique
#android.emulator_keyboard_key_technique = 

# (str) The Android emulator keyboard key approach
#android.emulator_keyboard_key_approach = 

# (str) The Android emulator keyboard key way
#android.emulator_keyboard_key_way = 

# (str) The Android emulator keyboard key mode
#android.emulator_keyboard_key_mode = 

# (str) The Android emulator keyboard key style
#android.emulator_keyboard_key_style = 

# (str) The Android emulator keyboard key form
#android.emulator_keyboard_key_form = 

# (str) The Android emulator keyboard key shape
#android.emulator_keyboard_key_shape = 

# (str) The Android emulator keyboard key pattern
#android.emulator_keyboard_key_pattern = 

# (str) The Android emulator keyboard key design
#android.emulator_keyboard_key_design = 

# (str) The Android emulator keyboard key plan
#android.emulator_keyboard_key_plan = 

# (str) The Android emulator keyboard key scheme
#android.emulator_keyboard_key_scheme = 

# (str) The Android emulator keyboard key program
#android.emulator_keyboard_key_program = 

# (str) The Android emulator keyboard key project
#android.emulator_keyboard_key_project = 

# (str) The Android emulator keyboard key task
#android.emulator_keyboard_key_task = 

# (str) The Android emulator keyboard key job
#android.emulator_keyboard_key_job = 

# (str) The Android emulator keyboard key work
#android.emulator_keyboard_key_work = 

# (str) The Android emulator keyboard key duty
#android.emulator_keyboard_key_duty = 

# (str) The Android emulator keyboard key role
#android.emulator_keyboard_key_role = 

# (str) The Android emulator keyboard key responsibility
#android.emulator_keyboard_key_responsibility = 

# (str) The Android emulator keyboard key obligation
#android.emulator_keyboard_key_obligation = 

# (str) The Android emulator keyboard key liability
#android.emulator_keyboard_key_liability = 

# (str) The Android emulator keyboard key accountability
#android.emulator_keyboard_key_accountability = 

# (str) The Android emulator keyboard key authority
#android.emulator_keyboard_key_authority = 

# (str) The Android emulator keyboard key power
#android.emulator_keyboard_key_power = 

# (str) The Android emulator keyboard key control
#android.emulator_keyboard_key_control = 

# (str) The Android emulator keyboard key command
#android.emulator_keyboard_key_command = 

# (str) The Android emulator keyboard key direction
#android.emulator_keyboard_key_direction = 

# (str) The Android emulator keyboard key guidance
#android.emulator_keyboard_key_guidance = 

# (str) The Android emulator keyboard key leadership
#android.emulator_keyboard_key_leadership = 

# (str) The Android emulator keyboard key management
#android.emulator_keyboard_key_management = 

# (str) The Android emulator keyboard key administration
#android.emulator_keyboard_key_administration = 

# (str) The Android emulator keyboard key supervision
#android.emulator_keyboard_key_supervision = 

# (str) The Android emulator keyboard key oversight
#android.emulator_keyboard_key_oversight = 

# (str) The Android emulator keyboard key governance
#android.emulator_keyboard_key_governance = 

# (str) The Android emulator keyboard key regulation
#android.emulator_keyboard_key_regulation = 

# (str) The Android emulator keyboard key rule
#android.emulator_keyboard_key_rule = 

# (str) The Android emulator keyboard key law
#android.emulator_keyboard_key_law = 

# (str) The Android emulator keyboard key policy
#android.emulator_keyboard_key_policy = 

# (str) The Android emulator keyboard key guideline
#android.emulator_keyboard_key_guideline = 

# (str) The Android emulator keyboard key standard
#android.emulator_keyboard_key_standard = 

# (str) The Android emulator keyboard key norm
#android.emulator_keyboard_key_norm = 

# (str) The Android emulator keyboard key criterion
#android.emulator_keyboard_key_criterion = 

# (str) The Android emulator keyboard key benchmark
#android.emulator_keyboard_key_benchmark = 

# (str) The Android emulator keyboard key measure
#android.emulator_keyboard_key_measure = 

# (str) The Android emulator keyboard key metric
#android.emulator_keyboard_key_metric = 

# (str) The Android emulator keyboard key indicator
#android.emulator_keyboard_key_indicator = 

# (str) The Android emulator keyboard key index
#android.emulator_keyboard_key_index = 

# (str) The Android emulator keyboard key statistic
#android.emulator_keyboard_key_statistic = 

# (str) The Android emulator keyboard key data
#android.emulator_keyboard_key_data = 

# (str) The Android emulator keyboard key information
#android.emulator_keyboard_key_information = 

# (str) The Android emulator keyboard key knowledge
#android.emulator_keyboard_key_knowledge = 

# (str) The Android emulator keyboard key wisdom
#android.emulator_keyboard_key_wisdom = 

# (str) The Android emulator keyboard key insight
#android.emulator_keyboard_key_insight = 

# (str) The Android emulator keyboard key understanding
#android.emulator_keyboard_key_understanding = 

# (str) The Android emulator keyboard key comprehension
#android.emulator_keyboard_key_comprehension = 

# (str) The Android emulator keyboard key awareness
#android.emulator_keyboard_key_awareness = 

# (str) The Android emulator keyboard key consciousness
#android.emulator_keyboard_key_consciousness = 

# (str) The Android emulator keyboard key perception
#android.emulator_keyboard_key_perception = 

# (str) The Android emulator keyboard key cognition
#android.emulator_keyboard_key_cognition = 

# (str) The Android emulator keyboard key thought
#android.emulator_keyboard_key_thought = 

# (str) The Android emulator keyboard key thinking
#android.emulator_keyboard_key_thinking = 

# (str) The Android emulator keyboard key reasoning
#android.emulator_keyboard_key_reasoning = 

# (str) The Android emulator keyboard key logic
#android.emulator_keyboard_key_logic = 

# (str) The Android emulator keyboard key analysis
#android.emulator_keyboard_key_analysis = 

# (str) The Android emulator keyboard key synthesis
#android.emulator_keyboard_key_synthesis = 

# (str) The Android emulator keyboard key evaluation
#android.emulator_keyboard_key_evaluation = 

# (str) The Android emulator keyboard key assessment
#android.emulator_keyboard_key_assessment = 

# (str) The Android emulator keyboard key appraisal
#android.emulator_keyboard_key_appraisal = 

# (str) The Android emulator keyboard key judgment
#android.emulator_keyboard_key_judgment = 

# (str) The Android emulator keyboard key decision
#android.emulator_keyboard_key_decision = 

# (str) The Android emulator keyboard key choice
#android.emulator_keyboard_key_choice = 

# (str) The Android emulator keyboard key option
#android.emulator_keyboard_key_option = 

# (str) The Android emulator keyboard key selection
#android.emulator_keyboard_key_selection = 

# (str) The Android emulator keyboard key alternative
#android.emulator_keyboard_key_alternative = 

# (str) The Android emulator keyboard key possibility
#android.emulator_keyboard_key_possibility = 

# (str) The Android emulator keyboard key probability
#android.emulator_keyboard_key_probability = 

# (str) The Android emulator keyboard key chance
#android.emulator_keyboard_key_chance = 

# (str) The Android emulator keyboard key likelihood
#android.emulator_keyboard_key_likelihood = 

# (str) The Android emulator keyboard key risk
#android.emulator_keyboard_key_risk = 

# (str) The Android emulator keyboard key uncertainty
#android.emulator_keyboard_key_uncertainty = 

# (str) The Android emulator keyboard key ambiguity
#android.emulator_keyboard_key_ambiguity = 

# (str) The Android emulator keyboard key vagueness
#android.emulator_keyboard_key_vagueness = 

# (str) The Android emulator keyboard key imprecision
#android.emulator_keyboard_key_imprecision = 

# (str) The Android emulator keyboard key inaccuracy
#android.emulator_keyboard_key_inaccuracy = 

# (str) The Android emulator keyboard key error
#android.emulator_keyboard_key_error = 

# (str) The Android emulator keyboard key mistake
#android.emulator_keyboard_key_mistake = 

# (str) The Android emulator keyboard key fault
#android.emulator_keyboard_key_fault = 

# (str) The Android emulator keyboard key defect
#android.emulator_keyboard_key_defect = 

# (str) The Android emulator keyboard key flaw
#android.emulator_keyboard_key_flaw = 

# (str) The Android emulator keyboard key bug
#android.emulator_keyboard_key_bug = 

# (str) The Android emulator keyboard key issue
#android.emulator_keyboard_key_issue = 

# (str) The Android emulator keyboard key problem
#android.emulator_keyboard_key_problem = 

# (str) The Android emulator keyboard key challenge
#android.emulator_keyboard_key_challenge = 

# (str) The Android emulator keyboard key difficulty
#android.emulator_keyboard_key_difficulty = 

# (str) The Android emulator keyboard key obstacle
#android.emulator_keyboard_key_obstacle = 

# (str) The Android emulator keyboard key barrier
#android.emulator_keyboard_key_barrier = 

# (str) The Android emulator keyboard key hurdle
#android.emulator_keyboard_key_hurdle = 

# (str) The Android emulator keyboard key impediment
#android.emulator_keyboard_key_impediment = 

# (str) The Android emulator keyboard key obstruction
#android.emulator_keyboard_key_obstruction = 

# (str) The Android emulator keyboard key blockage
#android.emulator_keyboard_key_blockage = 

# (str) The Android emulator keyboard key bottleneck
#android.emulator_keyboard_key_bottleneck = 

# (str) The Android emulator keyboard key constraint
#android.emulator_keyboard_key_constraint = 

# (str) The Android emulator keyboard key limitation
#android.emulator_keyboard_key_limitation = 

# (str) The Android emulator keyboard key restriction
#android.emulator_keyboard_key_restriction = 

# (str) The Android emulator keyboard key confinement
#android.emulator_keyboard_key_confinement = 

# (str) The Android emulator keyboard key constraint
#android.emulator_keyboard_key_constraint = 

# (str) The Android emulator keyboard key bound
#android.emulator_keyboard_key_bound = 

# (str) The Android emulator keyboard key limit
#android.emulator_keyboard_key_limit = 

# (str) The Android emulator keyboard key boundary
#android.emulator_keyboard_key_boundary = 

# (str) The Android emulator keyboard key border
#android.emulator_keyboard_key_border = 

# (str) The Android emulator keyboard key edge
#android.emulator_keyboard_key_edge = 

# (str) The Android emulator keyboard key margin
#android.emulator_keyboard_key_margin = 

# (str) The Android emulator keyboard key fringe
#android.emulator_keyboard_key_fringe = 

# (str) The Android emulator keyboard key periphery
#android.emulator_keyboard_key_periphery = 

# (str) The Android emulator keyboard key outskirts
#android.emulator_keyboard_key_outskirts = 

# (str) The Android emulator keyboard key vicinity
#android.emulator_keyboard_key_vicinity = 

# (str) The Android emulator keyboard key neighborhood
#android.emulator_keyboard_key_neighborhood = 

# (str) The Android emulator keyboard key surroundings
#android.emulator_keyboard_key_surroundings = 

# (str) The Android emulator keyboard key environment
#android.emulator_keyboard_key_environment = 

# (str) The Android emulator keyboard key context
#android.emulator_keyboard_key_context = 

# (str) The Android emulator keyboard key setting
#android.emulator_keyboard_key_setting = 

# (str) The Android emulator keyboard key background
#android.emulator_keyboard_key_background = 

# (str) The Android emulator keyboard key backdrop
#android.emulator_keyboard_key_backdrop = 

# (str) The Android emulator keyboard key scene
#android.emulator_keyboard_key_scene = 

# (str) The Android emulator keyboard key scenery
#android.emulator_keyboard_key_scenery = 

# (str) The Android emulator keyboard key landscape
#android.emulator_keyboard_key_landscape = 

# (str) The Android emulator keyboard key seascape
#android.emulator_keyboard_key_seascape = 

# (str) The Android emulator keyboard key cityscape
#android.emulator_keyboard_key_cityscape = 

# (str) The Android emulator keyboard key townscape
#android.emulator_keyboard_key_townscape = 

# (str) The Android emulator keyboard key view
#android.emulator_keyboard_key_view = 

# (str) The Android emulator keyboard key sight
#android.emulator_keyboard_key_sight = 

# (str) The Android emulator keyboard key scene
#android.emulator_keyboard_key_scene = 

# (str) The Android emulator keyboard key spectacle
#android.emulator_keyboard_key_spectacle = 

# (str) The Android emulator keyboard key display
#android.emulator_keyboard_key_display = 

# (str) The Android emulator keyboard key show
#android.emulator_keyboard_key_show = 

# (str) The Android emulator keyboard key exhibition
#android.emulator_keyboard_key_exhibition = 

# (str) The Android emulator keyboard key presentation
#android.emulator_keyboard_key_presentation = 

# (str) The Android emulator keyboard key demonstration
#android.emulator_keyboard_key_demonstration = 

# (str) The Android emulator keyboard key demonstration
#android.emulator_keyboard_key_demonstration = 

# (str) The Android emulator keyboard key illustration
#android.emulator_keyboard_key_illustration = 

# (str) The Android emulator keyboard key example
#android.emulator_keyboard_key_example = 

# (str) The Android emulator keyboard key instance
#android.emulator_keyboard_key_instance = 

# (str) The Android emulator keyboard key case
#android.emulator_keyboard_key_case = 

# (str) The Android emulator keyboard key specimen
#android.emulator_keyboard_key_specimen = 

# (str) The Android emulator keyboard key sample
#android.emulator_keyboard_key_sample = 

# (str) The Android emulator keyboard key model
#android.emulator_keyboard_key_model = 

# (str) The Android emulator keyboard key pattern
#android.emulator_keyboard_key_pattern = 

# (str) The Android emulator keyboard key template
#android.emulator_keyboard_key_template = 

# (str) The Android emulator keyboard key prototype
#android.emulator_keyboard_key_prototype = 

# (str) The Android emulator keyboard key archetype
#android.emulator_keyboard_key_archetype = 

# (str) The Android emulator keyboard key paradigm
#android.emulator_keyboard_key_paradigm = 

# (str) The Android emulator keyboard key standard
#android.emulator_keyboard_key_standard = 

# (str) The Android emulator keyboard key norm
#android.emulator_keyboard_key_norm = 

# (str) The Android emulator keyboard key criterion
#android.emulator_keyboard_key_criterion = 

# (str) The Android emulator keyboard key benchmark
#android.emulator_keyboard_key_benchmark = 

# (str) The Android emulator keyboard key yardstick
#android.emulator_keyboard_key_yardstick = 

# (str) The Android emulator keyboard key measure
#android.emulator_keyboard_key_measure = 

# (str) The Android emulator keyboard key gauge
#android.emulator_keyboard_key_gauge = 

# (str) The Android emulator keyboard key scale
#android.emulator_keyboard_key_scale = 

# (str) The Android emulator keyboard key standard
#android.emulator_keyboard_key_standard = 

# (str) The Android emulator keyboard key specification
#android.emulator_keyboard_key_specification = 

# (str) The Android emulator keyboard key requirement
#android.emulator_keyboard_key_requirement = 

# (str) The Android emulator keyboard key prerequisite
#android.emulator_keyboard_key_prerequisite = 

# (str) The Android emulator keyboard key condition
#android.emulator_keyboard_key_condition = 

# (str) The Android emulator keyboard key stipulation
#android.emulator_keyboard_key_stipulation = 

# (str) The Android emulator keyboard key provision
#android.emulator_keyboard_key_provision = 

# (str) The Android emulator keyboard key term
#android.emulator_keyboard_key_term = 

# (str) The Android emulator keyboard key clause
#android.emulator_keyboard_key_clause = 

# (str) The Android emulator keyboard key article
#android.emulator_keyboard_key_article = 

# (str) The Android emulator keyboard key section
#android.emulator_keyboard_key_section = 

# (str) The Android emulator keyboard key paragraph
#android.emulator_keyboard_key_paragraph = 

# (str) The Android emulator keyboard key subsection
#android.emulator_keyboard_key_subsection = 

# (str) The Android emulator keyboard key subdivision
#android.emulator_keyboard_key_subdivision = 

# (str) The Android emulator keyboard key part
#android.emulator_keyboard_key_part = 

# (str) The Android emulator keyboard key portion
#android.emulator_keyboard_key_portion = 

# (str) The Android emulator keyboard key segment
#android.emulator_keyboard_key_segment = 

# (str) The Android emulator keyboard key section
#android.emulator_keyboard_key_section = 

# (str) The Android emulator keyboard key division
#android.emulator_keyboard_key_division = 

# (str) The Android emulator keyboard key component
#android.emulator_keyboard_key_component = 

# (str) The Android emulator keyboard key constituent
#android.emulator_keyboard_key_constituent = 

# (str) The Android emulator keyboard key element
#android.emulator_keyboard_key_element = 

# (str) The Android emulator keyboard key factor
#android.emulator_keyboard_key_factor = 

# (str) The Android emulator keyboard key feature
#android.emulator_keyboard_key_feature = 

# (str) The Android emulator keyboard key characteristic
#android.emulator_keyboard_key_characteristic = 

# (str) The Android emulator keyboard key attribute
#android.emulator_keyboard_key_attribute = 

# (str) The Android emulator keyboard key property
#android.emulator_keyboard_key_property = 

# (str) The Android emulator keyboard key quality
#android.emulator_keyboard_key_quality = 

# (str) The Android emulator keyboard key trait
#android.emulator_keyboard_key_trait = 

# (str) The Android emulator keyboard key aspect
#android.emulator_keyboard_key_aspect = 

# (str) The Android emulator keyboard key facet
#android.emulator_keyboard_key_facet = 

# (str) The Android emulator keyboard key dimension
#android.emulator_keyboard_key_dimension = 

# (str) The Android emulator keyboard key side
#android.emulator_keyboard_key_side = 

# (str) The Android emulator keyboard key angle
#android.emulator_keyboard_key_angle = 

# (str) The Android emulator keyboard key perspective
#android.emulator_keyboard_key_perspective = 

# (str) The Android emulator keyboard key viewpoint
#android.emulator_keyboard_key_viewpoint = 

# (str) The Android emulator keyboard key standpoint
#android.emulator_keyboard_key_standpoint = 

# (str) The Android emulator keyboard key position
#android.emulator_keyboard_key_position = 

# (str) The Android emulator keyboard key stance
#android.emulator_keyboard_key_stance = 

# (str) The Android emulator keyboard key attitude
#android.emulator_keyboard_key_attitude = 

# (str) The Android emulator keyboard key approach
#android.emulator_keyboard_key_approach = 

# (str) The Android emulator keyboard key outlook
#android.emulator_keyboard_key_outlook = 

# (str) The Android emulator keyboard key opinion
#android.emulator_keyboard_key_opinion = 

# (str) The Android emulator keyboard key view
#android.emulator_keyboard_key_view = 

# (str) The Android emulator keyboard key belief
#android.emulator_keyboard_key_belief = 

# (str) The Android emulator keyboard key conviction
#android.emulator_keyboard_key_conviction = 

# (str) The Android emulator keyboard key creed
#android.emulator_keyboard_key_creed = 

# (str) The Android emulator keyboard key doctrine
#android.emulator_keyboard_key_doctrine = 

# (str) The Android emulator keyboard key dogma
#android.emulator_keyboard_key_dogma = 

# (str) The Android emulator keyboard key tenet
#android.emulator_keyboard_key_tenet = 

# (str) The Android emulator keyboard key principle
#android.emulator_keyboard_key_principle = 

# (str) The Android emulator keyboard key rule
#android.emulator_keyboard_key_rule = 

# (str) The Android emulator keyboard key law
#android.emulator_keyboard_key_law = 

# (str) The Android emulator keyboard key precept
#android.emulator_keyboard_key_precept = 

# (str) The Android emulator keyboard key canon
#android.emulator_keyboard_key_canon = 

# (str) The Android emulator keyboard key maxim
#android.emulator_keyboard_key_maxim = 

# (str) The Android emulator keyboard key axiom
#android.emulator_keyboard_key_axiom = 

# (str) The Android emulator keyboard key postulate
#android.emulator_keyboard_key_postulate = 

# (str) The Android emulator keyboard key assumption
#android.emulator_keyboard_key_assumption = 

# (str) The Android emulator keyboard key presumption
#android.emulator_keyboard_key_presumption = 

# (str) The Android emulator keyboard key supposition
#android.emulator_keyboard_key_supposition = 

# (str) The Android emulator keyboard key hypothesis
#android.emulator_keyboard_key_hypothesis = 

# (str) The Android emulator keyboard key theory
#android.emulator_keyboard_key_theory = 

# (str) The Android emulator keyboard key thesis
#android.emulator_keyboard_key_thesis = 

# (str) The Android emulator keyboard key proposition
#android.emulator_keyboard_key_proposition = 

# (str) The Android emulator keyboard key statement
#android.emulator_keyboard_key_statement = 

# (str) The Android emulator keyboard key assertion
#android.emulator_keyboard_key_assertion = 

# (str) The Android emulator keyboard key claim
#android.emulator_keyboard_key_claim = 

# (str) The Android emulator keyboard key allegation
#android.emulator_keyboard_key_allegation = 

# (str) The Android emulator keyboard key contention
#android.emulator_keyboard_key_contention = 

# (str) The Android emulator keyboard key argument
#android.emulator_keyboard_key_argument = 

# (str) The Android emulator keyboard key reasoning
#android.emulator_keyboard_key_reasoning = 

# (str) The Android emulator keyboard key rationale
#android.emulator_keyboard_key_rationale = 

# (str) The Android emulator keyboard key justification
#android.emulator_keyboard_key_justification = 

# (str) The Android emulator keyboard key explanation
#android.emulator_keyboard_key_explanation = 

# (str) The Android emulator keyboard key interpretation
#android.emulator_keyboard_key_interpretation = 

# (str) The Android emulator keyboard key explication
#android.emulator_keyboard_key_explication = 

# (str) The Android emulator keyboard key exposition
#android.emulator_keyboard_key_exposition = 

# (str) The Android emulator keyboard key elucidation
#android.emulator_keyboard_key_elucidation = 

# (str) The Android emulator keyboard key clarification
#android.emulator_keyboard_key_clarification = 

# (str) The Android emulator keyboard key illustration
#android.emulator_keyboard_key_illustration = 

# (str) The Android emulator keyboard key exemplification
#android.emulator_keyboard_key_exemplification = 

# (str) The Android emulator keyboard key demonstration
#android.emulator_keyboard_key_demonstration = 

# (str) The Android emulator keyboard key proof
#android.emulator_keyboard_key_proof = 

# (str) The Android emulator keyboard key evidence
#android.emulator_keyboard_key_evidence = 

# (str) The Android emulator keyboard key testimony
#android.emulator_keyboard_key_testimony = 

# (str) The Android emulator keyboard key witness
#android.emulator_keyboard_key_witness = 

# (str) The Android emulator keyboard key confirmation
#android.emulator_keyboard_key_confirmation = 

# (str) The Android emulator keyboard key corroboration
#android.emulator_keyboard_key_corroboration = 

# (str) The Android emulator keyboard key validation
#android.emulator_keyboard_key_validation = 

# (str) The Android emulator keyboard key verification
#android.emulator_keyboard_key_verification = 

# (str) The Android emulator keyboard key authentication
#android.emulator_keyboard_key_authentication = 

# (str) The Android emulator keyboard key certification
#android.emulator_keyboard_key_certification = 

# (str) The Android emulator keyboard key accreditation
#android.emulator_keyboard_key_accreditation = 

# (str) The Android emulator keyboard key approval
#android.emulator_keyboard_key_approval = 

# (str) The Android emulator keyboard key endorsement
#android.emulator_keyboard_key_endorsement = 

# (str) The Android emulator keyboard key sanction
#android.emulator_keyboard_key_sanction = 

# (str) The Android emulator keyboard key permission
#android.emulator_keyboard_key_permission = 

# (str) The Android emulator keyboard key authorization
#android.emulator_keyboard_key_authorization = 

# (str) The Android emulator keyboard key license
#android.emulator_keyboard_key_license = 

# (str) The Android emulator keyboard key permit
#android.emulator_keyboard_key_permit = 

# (str) The Android emulator keyboard key warrant
#android.emulator_keyboard_key_warrant = 

# (str) The Android emulator keyboard key guarantee
#android.emulator_keyboard_key_guarantee = 

# (str) The Android emulator keyboard key warranty
#android.emulator_keyboard_key_warranty = 

# (str) The Android emulator keyboard key assurance
#android.emulator_keyboard_key_assurance = 

# (str) The Android emulator keyboard key pledge
#android.emulator_keyboard_key_pledge = 

# (str) The Android emulator keyboard key promise
#android.emulator_keyboard_key_promise = 

# (str) The Android emulator keyboard key commitment
#android.emulator_keyboard_key_commitment = 

# (str) The Android emulator keyboard key obligation
#android.emulator_keyboard_key_obligation = 

# (str) The Android emulator keyboard key duty
#android.emulator_keyboard_key_duty = 

# (str) The Android emulator keyboard key responsibility
#android.emulator_keyboard_key_responsibility = 

# (str) The Android emulator keyboard key liability
#android.emulator_keyboard_key_liability = 

# (str) The Android emulator keyboard key accountability
#android.emulator_keyboard_key_accountability = 

# (str) The Android emulator keyboard key answerability
#android.emulator_keyboard_key_answerability = 

# (str) The Android emulator keyboard key culpability
#android.emulator_keyboard_key_culpability = 

# (str) The Android emulator keyboard key guilt
#android.emulator_keyboard_key_guilt = 

# (str) The Android emulator keyboard key blame
#android.emulator_keyboard_key_blame = 

# (str) The Android emulator keyboard key fault
#android.emulator_keyboard_key_fault = 

# (str) The Android emulator keyboard key error
#android.emulator_keyboard_key_error = 

# (str) The Android emulator keyboard key mistake
#android.emulator_keyboard_key_mistake = 

# (str) The Android emulator keyboard key slip
#android.emulator_keyboard_key_slip = 

# (str) The Android emulator keyboard key lapse
#android.emulator_keyboard_key_lapse = 

# (str) The Android emulator keyboard key oversight
#android.emulator_keyboard_key_oversight = 

# (str) The Android emulator keyboard key omission
#android.emulator_keyboard_key_omission = 

# (str) The Android emulator keyboard key neglect
#android.emulator_keyboard_key_neglect = 

# (str) The Android emulator keyboard key disregard
#android.emulator_keyboard_key_disregard = 

# (str) The Android emulator keyboard key disregard
#android.emulator_keyboard_key_disregard = 

# (str) The Android emulator keyboard key disregard
#android.emulator_keyboard_key_disregard = 

# (ios) The path to the Python source code
#ios.source_dir = 

# (ios) The path to the Python requirements
#ios.requirements = 

# (ios) The path to the Python include directory
#ios.include_dir = 

# (ios) The path to the Python library directory
#ios.library_dir = 

# (ios) The path to the Python binary directory
#ios.binary_dir = 

# (ios) The path to the Python data directory
#ios.data_dir = 

# (ios) The path to the Python documentation directory
#ios.doc_dir = 

# (ios) The path to the Python test directory
#ios.test_dir = 

# (ios) The path to the Python example directory
#ios.example_dir = 

# (ios) The path to the Python demo directory
#ios.demo_dir = 

# (ios) The path to the Python tutorial directory
#ios.tutorial_dir = 

# (ios) The path to the Python guide directory
#ios.guide_dir = 

# (ios) The path to the Python manual directory
#ios.manual_dir = 

# (ios) The path to the Python reference directory
#ios.reference_dir = 

# (ios) The path to the Python specification directory
#ios.specification_dir = 

# (ios) The path to the Python standard directory
#ios.standard_dir = 

# (ios) The path to the Python norm directory
#ios.norm_dir = 

# (ios) The path to the Python criterion directory
#ios.criterion_dir = 

# (ios) The path to the Python benchmark directory
#ios.benchmark_dir = 

# (ios) The path to the Python measure directory
#ios.measure_dir = 

# (ios) The path to the Python metric directory
#ios.metric_dir = 

# (ios) The path to the Python indicator directory
#ios.indicator_dir = 

# (ios) The path to the Python index directory
#ios.index_dir = 

# (ios) The path to the Python statistic directory
#ios.statistic_dir = 

# (ios) The path to the Python data directory
#ios.data_dir = 

# (ios) The path to the Python information directory
#ios.information_dir = 

# (ios) The path to the Python knowledge directory
#ios.knowledge_dir = 

# (ios) The path to the Python wisdom directory
#ios.wisdom_dir = 

# (ios) The path to the Python insight directory
#ios.insight_dir = 

# (ios) The path to the Python understanding directory
#ios.understanding_dir = 

# (ios) The path to the Python comprehension directory
#ios.comprehension_dir = 

# (ios) The path to the Python awareness directory
#ios.awareness_dir = 

# (ios) The path to the Python consciousness directory
#ios.consciousness_dir = 

# (ios) The path to the Python perception directory
#ios.perception_dir = 

# (ios) The path to the Python cognition directory
#ios.cognition_dir = 

# (ios) The path to the Python thought directory
#ios.thought_dir = 

# (ios) The path to the Python thinking directory
#ios.thinking_dir = 

# (ios) The path to the Python reasoning directory
#ios.reasoning_dir = 

# (ios) The path to the Python logic directory
#ios.logic_dir = 

# (ios) The path to the Python analysis directory
#ios.analysis_dir = 

# (ios) The path to the Python synthesis directory
#ios.synthesis_dir = 

# (ios) The path to the Python evaluation directory
#ios.evaluation_dir = 

# (ios) The path to the Python assessment directory
#ios.assessment_dir = 

# (ios) The path to the Python appraisal directory
#ios.appraisal_dir = 

# (ios) The path to the Python judgment directory
#ios.judgment_dir = 

# (ios) The path to the Python decision directory
#ios.decision_dir = 

# (ios) The path to the Python choice directory
#ios.choice_dir = 

# (ios) The path to the Python option directory
#ios.option_dir = 

# (ios) The path to the Python selection directory
#ios.selection_dir = 

# (ios) The path to the Python alternative directory
#ios.alternative_dir = 

# (ios) The path to the Python possibility directory
#ios.possibility_dir = 

# (ios) The path to the Python probability directory
#ios.probability_dir = 

# (ios) The path to the Python chance directory
#ios.chance_dir = 

# (ios) The path to the Python likelihood directory
#ios.likelihood_dir = 

# (ios) The path to the Python risk directory
#ios.risk_dir = 

# (ios) The path to the Python uncertainty directory
#ios.uncertainty_dir = 

# (ios) The path to the Python ambiguity directory
#ios.ambiguity_dir = 

# (ios) The path to the Python vagueness directory
#ios.vagueness_dir = 

# (ios) The path to the Python imprecision directory
#ios.imprecision_dir = 

# (ios) The path to the Python inaccuracy directory
#ios.inaccuracy_dir = 

# (ios) The path to the Python error directory
#ios.error_dir = 

# (ios) The path to the Python mistake directory
#ios.mistake_dir = 

# (ios) The path to the Python fault directory
#ios.fault_dir = 

# (ios) The path to the Python defect directory
#ios.defect_dir = 

# (ios) The path to the Python flaw directory
#ios.flaw_dir = 

# (ios) The path to the Python bug directory
#ios.bug_dir = 

# (ios) The path to the Python issue directory
#ios.issue_dir = 

# (ios) The path to the Python problem directory
#ios.problem_dir = 

# (ios) The path to the Python challenge directory
#ios.challenge_dir = 

# (ios) The path to the Python difficulty directory
#ios.difficulty_dir = 

# (ios) The path to the Python obstacle directory
#ios.obstacle_dir = 

# (ios) The path to the Python barrier directory
#ios.barrier_dir = 

# (ios) The path to the Python hurdle directory
#ios.hurdle_dir = 

# (ios) The path to the Python impediment directory
#ios.impediment_dir = 

# (ios) The path to the Python obstruction directory
#ios.obstruction_dir = 

# (ios) The path to the Python blockage directory
#ios.blockage_dir = 

# (ios) The path to the Python bottleneck directory
#ios.bottleneck_dir = 

# (ios) The path to the Python constraint directory
#ios.constraint_dir = 

# (ios) The path to the Python limitation directory
#ios.limitation_dir = 

# (ios) The path to the Python restriction directory
#ios.restriction_dir = 

# (ios) The path to the Python confinement directory
#ios.confinement_dir = 

# (ios) The path to the Python bound directory
#ios.bound_dir = 

# (ios) The path to the Python limit directory
#ios.limit_dir = 

# (ios) The path to the Python boundary directory
#ios.boundary_dir = 

# (ios) The path to the Python border directory
#ios.border_dir = 

# (ios) The path to the Python edge directory
#ios.edge_dir = 

# (ios) The path to the Python margin directory
#ios.margin_dir = 

# (ios) The path to the Python fringe directory
#ios.fringe_dir = 

# (ios) The path to the Python periphery directory
#ios.periphery_dir = 

# (ios) The path to the Python outskirts directory
#ios.outskirts_dir = 

# (ios) The path to the Python vicinity directory
#ios.vicinity_dir = 

# (ios) The path to the Python neighborhood directory
#ios.neighborhood_dir = 

# (ios) The path to the Python surroundings directory
#ios.surroundings_dir = 

# (ios) The path to the Python environment directory
#ios.environment_dir = 

# (ios) The path to the Python context directory
#ios.context_dir = 

# (ios) The path to the Python setting directory
#ios.setting_dir = 

# (ios) The path to the Python background directory
#ios.background_dir = 

# (ios) The path to the Python backdrop directory
#ios.backdrop_dir = 

# (ios) The path to the Python scene directory
#ios.scene_dir = 

# (ios) The path to the Python scenery directory
#ios.scenery_dir = 

# (ios) The path to the Python landscape directory
#ios.landscape_dir = 

# (ios) The path to the Python seascape directory
#ios.seascape_dir = 

# (ios) The path to the Python cityscape directory
#ios.cityscape_dir = 

# (ios) The path to the Python townscape directory
#ios.townscape_dir = 

# (ios) The path to the Python view directory
#ios.view_dir = 

# (ios) The path to the Python sight directory
#ios.sight_dir = 

# (ios) The path to the Python spectacle directory
#ios.spectacle_dir = 

# (ios) The path to the Python display directory
#ios.display_dir = 

# (ios) The path to the Python show directory
#ios.show_dir = 

# (ios) The path to the Python exhibition directory
#ios.exhibition_dir = 

# (ios) The path to the Python presentation directory
#ios.presentation_dir = 

# (ios) The path to the Python demonstration directory
#ios.demonstration_dir = 

# (ios) The path to the Python illustration directory
#ios.illustration_dir = 

# (ios) The path to the Python example directory
#ios.example_dir = 

# (ios) The path to the Python instance directory
#ios.instance_dir = 

# (ios) The path to the Python case directory
#ios.case_dir = 

# (ios) The path to the Python specimen directory
#ios.specimen_dir = 

# (ios) The path to the Python sample directory
#ios.sample_dir = 

# (ios) The path to the Python model directory
#ios.model_dir = 

# (ios) The path to the Python pattern directory
#ios.pattern_dir = 

# (ios) The path to the Python template directory
#ios.template_dir = 

# (ios) The path to the Python prototype directory
#ios.prototype_dir = 

# (ios) The path to the Python archetype directory
#ios.archetype_dir = 

# (ios) The path to the Python paradigm directory
#ios.paradigm_dir = 

# (str) Path to the Python source code (relative to the app dir)
#ios.source_dir = src

# (str) Path to the Python requirements file (relative to the app dir)
#ios.requirements = requirements.txt

# (str) The iOS code signing identity
#ios.codesign.identity = 

# (str) The iOS code signing provisioning profile
#ios.codesign.provisioning_profile = 

# (str) The iOS deployment target
#ios.deployment_target = 12.0

# (str) The iOS bundle identifier
#ios.bundle_identifier = org.lab.ninhydrintest

# (str) The iOS bundle name
#ios.bundle_name = NinhydrinTest

# (str) The iOS bundle version
#ios.bundle_version = 1.0.0

# (str) The iOS bundle short version
#ios.bundle_short_version = 1.0

# (str) The iOS minimum OS version
#ios.minimum_os_version = 12.0

# (str) The iOS device family
#ios.device_family = iPhone,iPad

# (str) The iOS orientation
#ios.orientation = Portrait

# (bool) Whether to enable bitcode
#ios.enable_bitcode = True

# (bool) Whether to enable ARC
#ios.enable_arc = True

# (bool) Whether to enable visibility hiding
#ios.enable_visibility_hiding = True

# (bool) Whether to enable static analyzer
#ios.enable_static_analyzer = True

# (bool) Whether to enable testability
#ios.enable_testability = True

# (bool) Whether to enable app sandbox
#ios.enable_app_sandbox = True

# (bool) Whether to enable iCloud
#ios.enable_icloud = False

# (bool) Whether to enable Apple Pay
#ios.enable_apple_pay = False

# (bool) Whether to enable HealthKit
#ios.enable_healthkit = False

# (bool) Whether to enable HomeKit
#ios.enable_homekit = False

# (bool) Whether to enable SiriKit
#ios.enable_sirikit = False

# (bool) Whether to enable CallKit
#ios.enable_callkit = False

# (bool) Whether to enable Message UI
#ios.enable_message_ui = False

# (bool) Whether to enable MapKit
#ios.enable_mapkit = False

# (bool) Whether to enable Core Location
#ios.enable_core_location = True

# (bool) Whether to enable Core Motion
#ios.enable_core_motion = False

# (bool) Whether to enable Core Bluetooth
#ios.enable_core_bluetooth = False

# (bool) Whether to enable Core NFC
#ios.enable_core_nfc = False

# (bool) Whether to enable Core ML
#ios.enable_core_ml = False

# (bool) Whether to enable ARKit
#ios.enable_arkit = False

# (bool) Whether to enable Vision
#ios.enable_vision = False

# (bool) Whether to enable Natural Language
#ios.enable_natural_language = False

# (bool) Whether to enable Speech
#ios.enable_speech = False

# (bool) Whether to enable Translate
#ios.enable_translate = False

# (bool) Whether to enable Photos
#ios.enable_photos = True

# (bool) Whether to enable Photo Library
#ios.enable_photo_library = True

# (bool) Whether to enable Camera
#ios.enable_camera = True

# (bool) Whether to enable Microphone
#ios.enable_microphone = False

# (bool) Whether to enable Contacts
#ios.enable_contacts = False

# (bool) Whether to enable Calendar
#ios.enable_calendar = False

# (bool) Whether to enable Reminders
#ios.enable_reminders = False

# (bool) Whether to enable Notes
#ios.enable_notes = False

# (bool) Whether to enable Mail
#ios.enable_mail = False

# (bool) Whether to enable Messages
#ios.enable_messages = False

# (bool) Whether to enable Phone
#ios.enable_phone = False

# (bool) Whether to enable Safari
#ios.enable_safari = False

# (bool) Whether to enable WebKit
#ios.enable_webkit = False

# (bool) Whether to enable Network
#ios.enable_network = True

# (bool) Whether to enable Local Network
#ios.enable_local_network = True

# (bool) Whether to enable Background App Refresh
#ios.enable_background_app_refresh = False

# (bool) Whether to enable Background Fetch
#ios.enable_background_fetch = False

# (bool) Whether to enable Remote Notifications
#ios.enable_remote_notifications = False

# (bool) Whether to enable Local Notifications
#ios.enable_local_notifications = False

# (bool) Whether to enable Push Notifications
#ios.enable_push_notifications = False

# (bool) Whether to enable Silent Notifications
#ios.enable_silent_notifications = False

# (bool) Whether to enable VoIP Notifications
#ios.enable_voip_notifications = False

# (bool) Whether to enable Complications
#ios.enable_complications = False

# (bool) Whether to enable Watch Connectivity
#ios.enable_watch_connectivity = False

# (bool) Whether to enable Handoff
#ios.enable_handoff = False

# (bool) Whether to enable App Groups
#ios.enable_app_groups = False

# (bool) Whether to enable Keychain Sharing
#ios.enable_keychain_sharing = False

# (bool) Whether to enable Associated Domains
#ios.enable_associated_domains = False

# (bool) Whether to enable Universal Links
#ios.enable_universal_links = False

# (bool) Whether to enable App Links
#ios.enable_app_links = False

# (bool) Whether to enable Deep Linking
#ios.enable_deep_linking = False

# (bool) Whether to enable URL Schemes
#ios.enable_url_schemes = False

# (bool) Whether to enable Custom URL Schemes
#ios.enable_custom_url_schemes = False

# (bool) Whether to enable HTTP
#ios.enable_http = True

# (bool) Whether to enable HTTPS
#ios.enable_https = True

# (bool) Whether to enable ATS
#ios.enable_ats = True

# (bool) Whether to enable App Transport Security
#ios.enable_app_transport_security = True

# (bool) Whether to enable Allow Arbitrary Loads
#ios.enable_allow_arbitrary_loads = False

# (bool) Whether to enable Allow Arbitrary Loads in Web Content
#ios.enable_allow_arbitrary_loads_in_web_content = False

# (bool) Whether to enable Exception Domains
#ios.enable_exception_domains = False

# (str) The iOS exception domains
#ios.exception_domains = 

# (bool) Whether to enable Includes Subdomains
#ios.enable_includes_subdomains = False

# (bool) Whether to enable Requires Secure Transport
#ios.enable_requires_secure_transport = True

# (bool) Whether to enable Minimum TLS Version
#ios.enable_minimum_tls_version = True

# (str) The iOS minimum TLS version
#ios.minimum_tls_version = TLSv1.2

# (bool) Whether to enable Forward Secrecy
#ios.enable_forward_secrecy = True

# (bool) Whether to enable Certificate Transparency
#ios.enable_certificate_transparency = True

# (bool) Whether to enable OCSP
#ios.enable_ocsp = True

# (bool) Whether to enable CRL
#ios.enable_crl = True

# (bool) Whether to enable Revocation Checking
#ios.enable_revocation_checking = True

# (bool) Whether to enable Pinned Certificates
#ios.enable_pinned_certificates = False

# (str) The iOS pinned certificates
#ios.pinned_certificates = 

# (bool) Whether to enable Public Key Pinning
#ios.enable_public_key_pinning = False

# (str) The iOS public key pins
#ios.public_key_pins = 

# (bool) Whether to enable HPKP
#ios.enable_hpkp = False

# (str) The iOS HPKP pins
#ios.hpkp_pins = 

# (bool) Whether to enable Expect CT
#ios.enable_expect_ct = False

# (str) The iOS expect CT max age
#ios.expect_ct_max_age = 

# (bool) Whether to enable Expect CT Enforce
#ios.enable_expect_ct_enforce = False

# (bool) Whether to enable Expect CT Report
#ios.enable_expect_ct_report = False

# (str) The iOS expect CT report URI
#ios.expect_ct_report_uri = 

# (bool) Whether to enable Content Security Policy
#ios.enable_content_security_policy = False

# (str) The iOS content security policy
#ios.content_security_policy = 

# (bool) Whether to enable CSP Report Only
#ios.enable_csp_report_only = False

# (str) The iOS csp report URI
#ios.csp_report_uri = 

# (bool) Whether to enable Referrer Policy
#ios.enable_referrer_policy = False

# (str) The iOS referrer policy
#ios.referrer_policy = 

# (bool) Whether to enable Permissions Policy
#ios.enable_permissions_policy = False

# (str) The iOS permissions policy
#ios.permissions_policy = 

# (bool) Whether to enable Feature Policy
#ios.enable_feature_policy = False

# (str) The iOS feature policy
#ios.feature_policy = 

# (bool) Whether to enable Cross Origin Policy
#ios.enable_cross_origin_policy = False

# (str) The iOS cross origin policy
#ios.cross_origin_policy = 

# (bool) Whether to enable Cross Origin Embedder Policy
#ios.enable_cross_origin_embedder_policy = False

# (str) The iOS cross origin embedder policy
#ios.cross_origin_embedder_policy = 

# (bool) Whether to enable Cross Origin Opener Policy
#ios.enable_cross_origin_opener_policy = False

# (str) The iOS cross origin opener policy
#ios.cross_origin_opener_policy = 

# (bool) Whether to enable Cross Origin Resource Policy
#ios.enable_cross_origin_resource_policy = False

# (str) The iOS cross origin resource policy
#ios.cross_origin_resource_policy = 

# (bool) Whether to enable Server Timing
#ios.enable_server_timing = False

# (str) The iOS server timing
#ios.server_timing = 

# (bool) Whether to enable Timing Allow Origin
#ios.enable_timing_allow_origin = False

# (str) The iOS timing allow origin
#ios.timing_allow_origin = 

# (bool) Whether to enable Navigation Timing
#ios.enable_navigation_timing = False

# (str) The iOS navigation timing
#ios.navigation_timing = 

# (bool) Whether to enable Resource Timing
#ios.enable_resource_timing = False

# (str) The iOS resource timing
#ios.resource_timing = 

# (bool) Whether to enable User Timing
#ios.enable_user_timing = False

# (str) The iOS user timing
#ios.user_timing = 

# (bool) Whether to enable Paint Timing
#ios.enable_paint_timing = False

# (str) The iOS paint timing
#ios.paint_timing = 

# (bool) Whether to enable Element Timing
#ios.enable_element_timing = False

# (str) The iOS element timing
#ios.element_timing = 

# (bool) Whether to enable Largest Contentful Paint
#ios.enable_largest_contentful_paint = False

# (str) The iOS largest contentful paint
#ios.largest_contentful_paint = 

# (bool) Whether to enable First Input Delay
#ios.enable_first_input_delay = False

# (str) The iOS first input delay
#ios.first_input_delay = 

# (bool) Whether to enable Cumulative Layout Shift
#ios.enable_cumulative_layout_shift = False

# (str) The iOS cumulative layout shift
#ios.cumulative_layout_shift = 

# (bool) Whether to enable First Contentful Paint
#ios.enable_first_contentful_paint = False

# (str) The iOS first contentful paint
#ios.first_contentful_paint = 

# (bool) Whether to enable Time to First Byte
#ios.enable_time_to_first_byte = False

# (str) The iOS time to first byte
#ios.time_to_first_byte = 

# (bool) Whether to enable First Meaningful Paint
#ios.enable_first_meaningful_paint = False

# (str) The iOS first meaningful paint
#ios.first_meaningful_paint = 

# (bool) Whether to enable Speed Index
#ios.enable_speed_index = False

# (str) The iOS speed index
#ios.speed_index = 

# (bool) Whether to enable Total Blocking Time
#ios.enable_total_blocking_time = False

# (str) The iOS total blocking time
#ios.total_blocking_time = 

# (bool) Whether to enable Performance Score
#ios.enable_performance_score = False

# (str) The iOS performance score
#ios.performance_score = 

# (bool) Whether to enable Accessibility Score
#ios.enable_accessibility_score = False

# (str) The iOS accessibility score
#ios.accessibility_score = 

# (bool) Whether to enable Best Practices Score
#ios.enable_best_practices_score = False

# (str) The iOS best practices score
#ios.best_practices_score = 

# (bool) Whether to enable SEO Score
#ios.enable_seo_score = False

# (str) The iOS seo score
#ios.seo_score = 

# (bool) Whether to enable PWA Score
#ios.enable_pwa_score = False

# (str) The iOS pwa score
#ios.pwa_score = 

# (bool) Whether to enable Progressive Web App
#ios.enable_progressive_web_app = False

# (bool) Whether to enable Service Worker
#ios.enable_service_worker = False

# (str) The iOS service worker
#ios.service_worker = 

# (bool) Whether to enable Web App Manifest
#ios.enable_web_app_manifest = False

# (str) The iOS web app manifest
#ios.web_app_manifest = 

# (bool) Whether to enable Install Prompt
#ios.enable_install_prompt = False

# (str) The iOS install prompt
#ios.install_prompt = 

# (bool) Whether to enable Add to Home Screen
#ios.enable_add_to_home_screen = False

# (str) The iOS add to home screen
#ios.add_to_home_screen = 

# (bool) Whether to enable Standalone Mode
#ios.enable_standalone_mode = False

# (str) The iOS standalone mode
#ios.standalone_mode = 

# (bool) Whether to enable Fullscreen Mode
#ios.enable_fullscreen_mode = False

# (str) The iOS fullscreen mode
#ios.fullscreen_mode = 

# (bool) Whether to enable Minimal UI Mode
#ios.enable_minimal_ui_mode = False

# (str) The iOS minimal UI mode
#ios.minimal_ui_mode = 

# (bool) Whether to enable Browser Mode
#ios.enable_browser_mode = False

# (str) The iOS browser mode
#ios.browser_mode = 

# (bool) Whether to enable Display Mode
#ios.enable_display_mode = False

# (str) The iOS display mode
#ios.display_mode = 

# (bool) Whether to enable Orientation Mode
#ios.enable_orientation_mode = False

# (str) The iOS orientation mode
#ios.orientation_mode = 

# (bool) Whether to enable Theme Color
#ios.enable_theme_color = False

# (str) The iOS theme color
#ios.theme_color = 

# (bool) Whether to enable Background Color
#ios.enable_background_color = False

# (str) The iOS background color
#ios.background_color = 

# (bool) Whether to enable Start URL
#ios.enable_start_url = False

# (str) The iOS start URL
#ios.start_url = 

# (bool) Whether to enable Scope
#ios.enable_scope = False

# (str) The iOS scope
#ios.scope = 

# (bool) Whether to enable Short Name
#ios.enable_short_name = False

# (str) The iOS short name
#ios.short_name = 

# (bool) Whether to enable Name
#ios.enable_name = False

# (str) The iOS name
#ios.name = 

# (bool) Whether to enable Description
#ios.enable_description = False

# (str) The iOS description
#ios.description = 

# (bool) Whether to enable Icons
#ios.enable_icons = False

# (str) The iOS icons
#ios.icons = 

# (bool) Whether to enable Screenshots
#ios.enable_screenshots = False

# (str) The iOS screenshots
#ios.screenshots = 

# (bool) Whether to enable Categories
#ios.enable_categories = False

# (str) The iOS categories
#ios.categories = 

# (bool) Whether to enable IARC Rating
#ios.enable_iarc_rating = False

# (str) The iOS iarc rating
#ios.iarc_rating = 

# (bool) Whether to enable Related Applications
#ios.enable_related_applications = False

# (str) The iOS related applications
#ios.related_applications = 

# (bool) Whether to enable Prefer Related Applications
#ios.enable_prefer_related_applications = False

# (str) The iOS prefer related applications
#ios.prefer_related_applications = 

# (bool) Whether to enable Share Target
#ios.enable_share_target = False

# (str) The iOS share target
#ios.share_target = 

# (bool) Whether to enable Protocol Handler
#ios.enable_protocol_handler = False

# (str) The iOS protocol handler
#ios.protocol_handler = 

# (bool) Whether to enable File Handler
#ios.enable_file_handler = False

# (str) The iOS file handler
#ios.file_handler = 

# (bool) Whether to enable Launch Handler
#ios.enable_launch_handler = False

# (str) The iOS launch handler
#ios.launch_handler = 

# (bool) Whether to enable Window Controls Overlay
#ios.enable_window_controls_overlay = False

# (str) The iOS window controls overlay
#ios.window_controls_overlay = 

# (bool) Whether to enable File System Access
#ios.enable_file_system_access = False

# (str) The iOS file system access
#ios.file_system_access = 

# (bool) Whether to enable Contact Picker
#ios.enable_contact_picker = False

# (str) The iOS contact picker
#ios.contact_picker = 

# (bool) Whether to enable File Picker
#ios.enable_file_picker = False

# (str) The iOS file picker
#ios.file_picker = 

# (bool) Whether to enable Directory Picker
#ios.enable_directory_picker = False

# (str) The iOS directory picker
#ios.directory_picker = 

# (bool) Whether to enable Font Access
#ios.enable_font_access = False

# (str) The iOS font access
#ios.font_access = 

# (bool) Whether to enable Idle Detection
#ios.enable_idle_detection = False

# (str) The iOS idle detection
#ios.idle_detection = 

# (bool) Whether to enable Periodic Background Sync
#ios.enable_periodic_background_sync = False

# (str) The iOS periodic background sync
#ios.periodic_background_sync = 

# (bool) Whether to enable Background Sync
#ios.enable_background_sync = False

# (str) The iOS background sync
#ios.background_sync = 

# (bool) Whether to enable Push Manager
#ios.enable_push_manager = False

# (str) The iOS push manager
#ios.push_manager = 

# (bool) Whether to enable Notifications
#ios.enable_notifications = False

# (str) The iOS notifications
#ios.notifications = 

# (bool) Whether to enable Badging
#ios.enable_badging = False

# (str) The iOS badging
#ios.badging = 

# (bool) Whether to enable Shortcut Manager
#ios.enable_shortcut_manager = False

# (str) The iOS shortcut manager
#ios.shortcut_manager = 

# (bool) Whether to enable Web Share
#ios.enable_web_share = False

# (str) The iOS web share
#ios.web_share = 

# (bool) Whether to enable Web Share Target
#ios.enable_web_share_target = False

# (str) The iOS web share target
#ios.web_share_target = 

# (bool) Whether to enable Web Share Target Files
#ios.enable_web_share_target_files = False

# (str) The iOS web share target files
#ios.web_share_target_files = 

# (bool) Whether to enable Web Share Target URL
#ios.enable_web_share_target_url = False

# (str) The iOS web share target URL
#ios.web_share_target_url = 

# (bool) Whether to enable Web Share Target Method
#ios.enable_web_share_target_method = False

# (str) The iOS web share target method
#ios.web_share_target_method = 

# (bool) Whether to enable Web Share Target Action
#ios.enable_web_share_target_action = False

# (str) The iOS web share target action
#ios.web_share_target_action = 

# (bool) Whether to enable Web Share Target Title
#ios.enable_web_share_target_title = False

# (str) The iOS web share target title
#ios.web_share_target_title = 

# (bool) Whether to enable Web Share Target Text
#ios.enable_web_share_target_text = False

# (str) The iOS web share target text
#ios.web_share_target_text = 

# (bool) Whether to enable Web Share Target URL
#ios.enable_web_share_target_url = False

# (str) The iOS web share target URL
#ios.web_share_target_url = 

# (bool) Whether to enable Web Share Target Files
#ios.enable_web_share_target_files = False

# (str) The iOS web share target files
#ios.web_share_target_files = 

# (bool) Whether to enable Web Share Target MIME Type
#ios.enable_web_share_target_mime_type = False

# (str) The iOS web share target MIME type
#ios.web_share_target_mime_type = 

# (bool) Whether to enable Web Share Target Accept
#ios.enable_web_share_target_accept = False

# (str) The iOS web share target accept
#ios.web_share_target_accept = 

# (bool) Whether to enable Web Share Target Enctype
#ios.enable_web_share_target_enctype = False

# (str) The iOS web share target enctype
#ios.web_share_target_enctype = 

# (bool) Whether to enable Web Share Target Params
#ios.enable_web_share_target_params = False

# (str) The iOS web share target params
#ios.web_share_target_params = 

# (bool) Whether to enable Web Share Target Title
#ios.enable_web_share_target_title = False

# (str) The iOS web share target title
#ios.web_share_target_title = 

# (bool) Whether to enable Web Share Target Text
#ios.enable_web_share_target_text = False

# (str) The iOS web share target text
#ios.web_share_target_text = 

# (bool) Whether to enable Web Share Target URL
#ios.enable_web_share_target_url = False

# (str) The iOS web share target URL
#ios.web_share_target_url = 

# (bool) Whether to enable Web Share Target Files
#ios.enable_web_share_target_files = False

# (str) The iOS web share target files
#ios.web_share_target_files = 

# (bool) Whether to enable Web Share Target MIME Type
#ios.enable_web_share_target_mime_type = False

# (str) The iOS web share target MIME type
#ios.web_share_target_mime_type = 

# (bool) Whether to enable Web Share Target Accept
#ios.enable_web_share_target_accept = False

# (str) The iOS web share target accept
#ios.web_share_target_accept = 

# (bool) Whether to enable Web Share Target Enctype
#ios.enable_web_share_target_enctype = False

# (str) The iOS web share target enctype
#ios.web_share_target_enctype = 

# (bool) Whether to enable Web Share Target Params
#ios.enable_web_share_target_params = False

# (str) The iOS web share target params
#ios.web_share_target_params = 

# (bool) Whether to enable Web Share Target Title
#ios.enable_web_share_target_title = False

# (str) The iOS web share target title
#ios.web_share_target_title = 

# (bool) Whether to enable Web Share Target Text
#ios.enable_web_share_target_text = False

# (str) The iOS web share target text
#ios.web_share_target_text = 

# (bool) Whether to enable Web Share Target URL
#ios.enable_web_share_target_url = False

# (str) The iOS web share target URL
#ios.web_share_target_url = 

# (bool) Whether to enable Web Share Target Files
#ios.enable_web_share_target_files = False

# (str) The iOS web share target files
#ios.web_share_target_files = 

# (bool) Whether to enable Web Share Target MIME Type
#ios.enable_web_share_target_mime_type = False

# (str) The iOS web share target MIME type
#ios.web_share_target_mime_type = 

# (bool) Whether to enable Web Share Target Accept
#ios.enable_web_share_target_accept = False

# (str) The iOS web share target accept
#ios.web_share_target_accept = 

# (bool) Whether to enable Web Share Target Enctype
#ios.enable_web_share_target_enctype = False

# (str) The iOS web share target enctype
#ios.web_share_target_enctype = 

# (bool) Whether to enable Web Share Target Params
#ios.enable_web_share_target_params = False

# (str) The iOS web share target params
#ios.web_share_target_params = 

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
bin_dir = ./bin
