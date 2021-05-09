import sys

from my_robot_interfaces.srv import InterPol
import rclpy
from rclpy.node import Node


class JintControlSrv(Node):

    def __init__(self):
        super().__init__('JintControlSrv')
        self.cli = self.create_client(InterPol, 'interpol')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.req = InterPol.Request()

    def send_request(self):
        self.req.shoulder = float(sys.argv[1])
        self.req.elbow = float(sys.argv[2])
        self.req.wrist = float(sys.argv[3])
        self.req.time = float(sys.argv[4])
        self.req.velocity = str(sys.argv[5])
        self.future = self.cli.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    minimal_client = JintControlSrv()
    minimal_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
            try:
                response = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:

                if response.success == True:
                    minimal_client.get_logger().info(
                        'Succes  %s' %
                        (response.description))
                else:
                    minimal_client.get_logger().info(
                        'Operation failed!  %s' %
                        (response.description))
            break

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()