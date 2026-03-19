import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/muhie/Documents/cw/EMS628-COURSEWORK/ros2_ws/install/ar_test'
