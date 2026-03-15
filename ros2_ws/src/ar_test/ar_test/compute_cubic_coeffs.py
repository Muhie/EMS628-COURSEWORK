#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# import the custom service this has to be specified in the CMAKE file
from ar_interface.srv import ComputeCubicTraj

class ComputeCubicCoeffs(Node):
    def __init__(self):
        super().__init__('compute_cubic_coeffs')
        
        # create a service server
        self.srv = self.create_service(ComputeCubicTraj, 'compute_cubic_traj', self.compute_cubic_traj_callback)
        self.get_logger().info('TEST')

    def compute_cubic_traj_callback(self, request, response):
        """
        Calculates the coefficients of a cubic polynomial trajectory.
        """
        self.get_logger().info(f'Received Request: p0={request.p0:.2f}, pf={request.pf:.2f}, v0={request.v0:.2f}, vf={request.vf:.2f}, t0={request.t0:.2f}, tf={request.tf:.2f}')
        
        # Extract inputs
        p0 = request.p0
        pf = request.pf
        v0 = request.v0
        vf = request.vf
        t0 = request.t0
        tf = request.tf
        
        # We assume t0 = 0. If it wasn't, we'd shift the time dt = tf - t0
        dt = tf - t0
        
        if dt <= 0:
            self.get_logger().error("Error: tf must be greater than t0")
            return response

        # Simplification for t0 = 0 (or operating on delta t)
        a0 = p0
        a1 = v0
        
        # Solving the matrix equation for a2 and a3
        # [dt^2   dt^3 ] [a2] = [pf - p0 - v0*dt]
        # [2*dt 3*dt^2 ] [a3] = [vf - v0        ]
        
        b1 = pf - p0 - v0*dt
        b2 = vf - v0
        
        det = (dt**2) * (3*dt**2) - (dt**3) * (2*dt)  # 3*dt^4 - 2*dt^4 = dt^4
        
        if det == 0:
            self.get_logger().error("Determinant is zero, cannot solve.")
            return response
            
        a2 = ( (3*dt**2)*b1 - (dt**3)*b2 ) / det
        a3 = ( -(2*dt)*b1 + (dt**2)*b2 ) / det
        
        response.a0 = a0
        response.a1 = a1
        response.a2 = a2
        response.a3 = a3
        
        self.get_logger().info(f'Computed Coeffs: a0={a0:.2f}, a1={a1:.2f}, a2={a2:.2f}, a3={a3:.2f}')
        
        return response

def main(args=None):
    rclpy.init(args=args)
    compute_cubic_coeffs = ComputeCubicCoeffs()
    try:
        rclpy.spin(compute_cubic_coeffs)
    except KeyboardInterrupt:
        pass
    finally:
        compute_cubic_coeffs.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
