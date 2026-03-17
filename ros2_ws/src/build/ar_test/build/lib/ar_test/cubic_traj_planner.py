#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# import the custom messages
from ar_interface.msg import CubicTrajParams
from ar_interface.msg import CubicTrajCoeffs

# import the custom service
from ar_interface.srv import ComputeCubicTraj

class CubicTrajPlanner(Node):
    def __init__(self):
        super().__init__('cubic_traj_planner')
        
        # subscribe to the to the cubic params topic
        self.subscription = self.create_subscription(
            CubicTrajParams,
            'cubic_traj_params',
            self.params_callback,
            10)
            
        # create for the cubic traj topic
        self.publisher_ = self.create_publisher(CubicTrajCoeffs, 'cubic_traj_coeffs', 10)
        
        # client for the compute cubic traj  service
        self.client = self.create_client(ComputeCubicTraj, 'compute_cubic_traj')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available')
            
        self.get_logger().info("cubic traj planner node started.")

    def params_callback(self, msg):
        """a method used  to parse the parameters """

        self.get_logger().info(f'received params: p0={msg.p0:.2f} pf={msg.pf:.2f} v0={msg.v0:.2f} vf={msg.vf:.2f} t0={msg.t0:.2f} tf={msg.tf:.2f}')
        
        # get the service request ready
        request = ComputeCubicTraj.Request()
        request.p0 = msg.p0
        request.pf = msg.pf
        request.v0 = msg.v0
        request.vf = msg.vf
        request.t0 = msg.t0
        request.tf = msg.tf
        
        # call the service using the async method
        future = self.client.call_async(request)
        future.add_done_callback(lambda future: self.service_response_callback(future, msg.t0, msg.tf))

    def service_response_callback(self, future, t0, tf):
        response = future.result()
        # publish the coefficients
        msg = CubicTrajCoeffs()
        msg.a0 = response.a0
        msg.a1 = response.a1
        msg.a2 = response.a2
        msg.a3 = response.a3
        msg.t0 = t0
        msg.tf = tf
        
        self.publisher_.publish(msg)
        self.get_logger().info(f'published coeffs: a0={msg.a0:.2f} a1={msg.a1:.2f} a2={msg.a2:.2f} a3={msg.a3:.2f}')


# boilerplate code
def main(args=None):
    rclpy.init(args=args)
    node = CubicTrajPlanner()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()