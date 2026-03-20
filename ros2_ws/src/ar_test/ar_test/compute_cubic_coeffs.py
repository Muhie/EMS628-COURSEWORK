#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# import the custom service this has to be specified in the CMAKE file
from ar_interface.srv import ComputeCubicTraj

class ComputeCubicCoeffs(Node):
    def __init__(self):
        super().__init__('compute_cubic_coeffs')
        
        # create a service 
        self.srv = self.create_service(ComputeCubicTraj, 'compute_cubic_traj', self.compute_cubic_traj_callback)
        self.get_logger().info('computing cubic coefficients node started')

    def compute_cubic_traj_callback(self, request, response):
        """
        Calculates the coefficients of a cubic polynomial trajectory.
        """

        # output request to the terminal
        self.get_logger().info(f'received request: p0={request.p0:.2f} pf={request.pf:.2f} v0={request.v0:.2f} vf={request.vf:.2f} t0={request.t0:.2f} tf={request.tf:.2f}')
        
        # get the requests 
        p0 = request.p0
        pf = request.pf
        v0 = request.v0
        vf = request.vf
        t0 = request.t0
        tf = request.tf
        
        
        dt = tf - t0
        
        a0 = p0
        a1 = v0
        a2 = (3 * (pf - p0) - (2 * v0 + vf) * dt) / (dt**2)
        a3 = (-2 * (pf - p0) + (v0 +vf) * dt) / (dt ** 3)
        
        response.a0 = a0
        response.a1 = a1
        response.a2 = a2
        response.a3 = a3
        
        self.get_logger().info(f'Computed Coeffs: a0={a0:.2f}, a1={a1:.2f}, a2={a2:.2f}, a3={a3:.2f}')
        
        return response
    
# boilerplate code
def main(args=None):
    rclpy.init(args=args)
    compute_cubic_coeffs = ComputeCubicCoeffs()
    rclpy.spin(compute_cubic_coeffs)
    compute_cubic_coeffs.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
