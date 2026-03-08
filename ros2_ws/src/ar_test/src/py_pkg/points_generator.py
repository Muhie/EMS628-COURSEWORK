#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
import random

# from std_msgs.msg import 


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(float, 'topic', 10) # Create topic with a float data type
        timer_period = 10  # time for each message to be published
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0 # number of iterations

    def timer_callback(self):
        msg = list[float] # Create a message full of floating point numbers
        p0 = random.uniform(-10, 10)
        pf = random.uniform(-10, 10)
        v0 = random.uniform(-10, 10)
        vf = random.uniform(-10, 10)
        t0 = 0
        dt = random.uniform(4,8)
        tf = t0 + dt
        msg.data = [p0, pf, v0, vf, t0, tf]
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()