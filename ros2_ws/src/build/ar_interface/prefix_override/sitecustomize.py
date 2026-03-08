import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/muhie/Desktop/Coursework/EMS628-COURSEWORK/ros2_ws/src/install/ar_interface'
