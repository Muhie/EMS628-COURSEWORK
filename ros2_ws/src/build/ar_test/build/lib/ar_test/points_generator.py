#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import random

# import the message that I made in the separate package
from ar_interface.msg import CubicTrajParams

class PointsGenerator(Node):
    def __init__(self):
        super().__init__('points_generator')
        
        # publish to the 'cubic_traj_params' topic
        self.publisher_ = self.create_publisher(CubicTrajParams, 'cubic_traj_params', 10)
        
        # create a timer that fires every 10 seconds
        timer_period = 10.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info("Points Generator Node Started.")

    def timer_callback(self):
        msg = CubicTrajParams()
        
        # positions and velocities should be within the -10 and 10 range
        msg.p0 = random.uniform(-10.0, 10.0)
        msg.pf = random.uniform(-10.0, 10.0)
        msg.v0 = random.uniform(-10.0, 10.0)
        msg.vf = random.uniform(-10.0, 10.0)
        
        # t0 should always be 0
        msg.t0 = 0.0
        
        # tf should be random float number between 4 and 8
        dt = random.uniform(4.0, 8.0)
        msg.tf = msg.t0 + dt
        
        # publish the message
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: p0={msg.p0:.2f}, pf={msg.pf:.2f}, v0={msg.v0:.2f}, vf={msg.vf:.2f}, t0={msg.t0:.2f}, tf={msg.tf:.2f}')


# boilerplate code
def main(args=None):
    rclpy.init(args=args)
    points_generator = PointsGenerator()

    rclpy.spin(points_generator)


    points_generator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
