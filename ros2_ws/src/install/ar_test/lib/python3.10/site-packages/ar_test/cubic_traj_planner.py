#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# Import the custom messages
from ar_interface.msg import CubicTrajParams
from ar_interface.msg import CubicTrajCoeffs

# Import the custom service
from ar_interface.srv import ComputeCubicTraj

class CubicTrajPlanner(Node):
    def __init__(self):
        super().__init__('cubic_traj_planner')
        
        # Subscribe to the 'cubic_traj_params' topic
        self.subscription = self.create_subscription(
            CubicTrajParams,
            'cubic_traj_params',
            self.params_callback,
            10)
            
        # Publisher for the 'cubic_traj_coeffs' topic
        self.publisher_ = self.create_publisher(CubicTrajCoeffs, 'cubic_traj_coeffs', 10)
        
        # Client for the compute_cubic_traj service
        self.client = self.create_client(ComputeCubicTraj, 'compute_cubic_traj')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('compute_cubic_traj service not available, waiting again...')
            
        self.get_logger().info("Cubic Traj Planner Node Started.")

    def params_callback(self, msg):
        self.get_logger().info(f'Received Params: p0={msg.p0:.2f}, pf={msg.pf:.2f}, v0={msg.v0:.2f}, vf={msg.vf:.2f}, t0={msg.t0:.2f}, tf={msg.tf:.2f}')
        
        # Prepare the service request
        request = ComputeCubicTraj.Request()
        request.p0 = msg.p0
        request.pf = msg.pf
        request.v0 = msg.v0
        request.vf = msg.vf
        request.t0 = msg.t0
        request.tf = msg.tf
        
        # Call the service asynchronously
        future = self.client.call_async(request)
        future.add_done_callback(lambda future: self.service_response_callback(future, msg.t0, msg.tf))

    def service_response_callback(self, future, t0, tf):
        try:
            response = future.result()
            # Publish the coefficients
            msg = CubicTrajCoeffs()
            msg.a0 = response.a0
            msg.a1 = response.a1
            msg.a2 = response.a2
            msg.a3 = response.a3
            msg.t0 = t0
            msg.tf = tf
            
            self.publisher_.publish(msg)
            self.get_logger().info(f'Published Coeffs: a0={msg.a0:.2f}, a1={msg.a1:.2f}, a2={msg.a2:.2f}, a3={msg.a3:.2f}')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')


def main(args=None):
    rclpy.init(args=args)
    node = CubicTrajPlanner()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()