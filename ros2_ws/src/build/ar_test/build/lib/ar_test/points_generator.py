#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
import random
from std_msgs.msg import Float32MultiArray
import math


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'topic', 10) # Create topic with a float data type
        timer_period = 10  # time for each message to be published
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0 # number of iterations

    def timer_callback(self):
        msg = Float32MultiArray()
        p0 = round(random.uniform(-10, 10), 2)
        pf = round(random.uniform(-10, 10), 2)
        v0 = round(random.uniform(-10, 10), 2)
        vf = round(random.uniform(-10, 10), 2)
        t0 = 0
        dt = round(random.uniform(4,8),2)
        tf = t0 + dt
        msg.data = [float(p0), float(pf), float(v0), float(vf), float(t0), float(tf)]
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing')
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


