
import rclpy
from rclpy.node import Node
from ar_interface.msg import CubicTrajCoeffs
from std_msgs.msg import Float64
import numpy as np

class PlotCubicTraj(Node):
    def __init__(self):
        super().__init__('plot_cubic_traj')

        # publishers for position, velocity and acceleration
        self.pub_position = self.create_publisher(Float64, 'position_trajectory', 10)
        self.pub_velocity = self.create_publisher(Float64, 'velocity_trajectory', 10)
        self.pub_acceleration = self.create_publisher(Float64, 'acceleration_trajectory', 10)

        # Initialise empty arrays and index for trajectory data
        self.index = 0
        self.position = []        
        self.velocity = []
        self.acceleration = []
        # Create a new timer for each trajectory
        self.timer = None

        # subscriber
        self.sub = self.create_subscription(CubicTrajCoeffs, 'cubic_traj_coeffs', self.coeffs_callback, 10)

    def coeffs_callback(self, msg):
        # Extract polynomial coefficients and timeframe from message
        a0 = msg.a0
        a1 = msg.a1
        a2 = msg.a2
        a3 = msg.a3
        t0 = msg.t0
        tf = msg.tf

        # Generate 100 evenly spaced time points between t0 and tf
        time = np.linspace(t0, tf, 100)


        # Compute position, velocity and acceleration arrays using derivative rules
        # p(t) = a0 + a1*t + a2*t^2 + a3*t^3
        self.position = a0 + a1*time + a2*(time**2) + a3*(time**3)
        # p'(t) = v(t) = a1 + 2*a2*t + 3*a3*t^2
        self.velocity = a1 + 2*a2*time + 3*a3*(time**2)
        # p''(t) = a(t) = 2*a2 + 6*a3*t
        self.acceleration = 2*a2 + 6*a3*time

        # Resets index value back to 0 to publish new trajectories
        self.index = 0
        self.get_logger().info(f'new trajectory received: t0={t0} tf={tf:.2f}')

        # if self.timer is not None:
        #     self.timer.cancel()
        # Timer for each point, published every tf/100 seconds
        period = 0.02
        self.timer = self.create_timer(period, self.publish_point)

    def publish_point(self):
        # Publishes one datapoint from each array per time tick
        if self.index < 100:
            msg = Float64()

            msg.data = float(self.position[self.index])
            self.pub_position.publish(msg)

            msg.data = float(self.velocity[self.index])
            self.pub_velocity.publish(msg)

            msg.data = float(self.acceleration[self.index])
            self.pub_acceleration.publish(msg)

            self.index = self.index + 1


# boilerplate code
def main(args=None):
    rclpy.init(args=args)
    node = PlotCubicTraj()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()