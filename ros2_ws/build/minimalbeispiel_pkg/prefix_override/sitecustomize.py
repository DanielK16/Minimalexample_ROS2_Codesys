import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/Minimalbeispiel_Codesys_ROS2/ros2_ws/install/minimalbeispiel_pkg'
