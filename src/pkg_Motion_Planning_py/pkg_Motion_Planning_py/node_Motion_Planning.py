import rclpy
from rclpy.node import Node


class MyNode(Node):

    def __init__(self):
        super().__init__("node_motion_plan")
        self.get_logger().info("Motion Planning node started.")


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()