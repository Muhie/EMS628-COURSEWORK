#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

# Import the custom message
from ar_interface.msg import CubicTrajCoeffs

class PlotCubicTraj(Node):
    def __init__(self):
        super().__init__('plot_cubic_traj')
        
        # Subscribe to the 'cubic_traj_coeffs' topic
        self.subscription = self.create_subscription(
            CubicTrajCoeffs,
            'cubic_traj_coeffs',
            self.coeffs_callback,
            10)
            
        # Publishers for position, velocity, and acceleration
        self.pos_pub = self.create_publisher(Float64, 'position_trajectory', 10)
        self.vel_pub = self.create_publisher(Float64, 'velocity_trajectory', 10)
        self.acc_pub = self.create_publisher(Float64, 'acceleration_trajectory', 10)
        
        # Simulation parameters
        self.a0 = 0.0
        self.a1 = 0.0
        self.a2 = 0.0
        self.a3 = 0.0
        self.t0 = 0.0
        self.tf = 0.0
        
        self.current_t = 0.0
        self.is_active = False
        
        # 50 Hz control loop for smooth plotting
        self.dt = 0.02 
        self.timer = self.create_timer(self.dt, self.timer_callback)
        
        self.get_logger().info("Plot Cubic Traj Node Started.")

    def coeffs_callback(self, msg):
        self.get_logger().info(f'Starting new trajectory simulation...')
        
        # Load the coefficients
        self.a0 = msg.a0
        self.a1 = msg.a1
        self.a2 = msg.a2
        self.a3 = msg.a3
        
        self.t0 = msg.t0
        self.tf = msg.tf
        
        # Reset the current time and activate simulation
        self.current_t = 0.0
        self.is_active = True

    def timer_callback(self):
        if not self.is_active:
            return
            
        # The equation for cubic polynomial is based on relative time (from 0 to tf-t0)
        # since t0 is always 0 based on coursework instructions point 1.
        # p(t) = a0 + a1*t + a2*t^2 + a3*t^3
        # v(t) = a1 + 2*a2*t + 3*a3*t^2
        # a(t) = 2*a2 + 6*a3*t
        
        t = self.current_t
        
        # Position
        pos_msg = Float64()
        pos_msg.data = self.a0 + self.a1*t + self.a2*(t**2) + self.a3*(t**3)
        self.pos_pub.publish(pos_msg)
        
        # Velocity
        vel_msg = Float64()
        vel_msg.data = self.a1 + 2*self.a2*t + 3*self.a3*(t**2)
        self.vel_pub.publish(vel_msg)
        
        # Acceleration
        acc_msg = Float64()
        acc_msg.data = 2*self.a2 + 6*self.a3*t
        self.acc_pub.publish(acc_msg)
        
        # Increment time
        self.current_t += self.dt
        
        # Stop simulation if we have reached the final time
        expected_duration = self.tf - self.t0
        if self.current_t > expected_duration:
            self.is_active = False
            self.get_logger().info('Trajectory finished.')

# boilerplate code
def main(args=None):
    rclpy.init(args=args)
    plot_cubic_traj = PlotCubicTraj()
    rclpy.spin(plot_cubic_traj)

    plot_cubic_traj.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
