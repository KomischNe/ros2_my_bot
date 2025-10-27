import rclpy
from rclpy.node import Node
# this is dev_zrf branch

class MyNode(Node):

    def __init__(self):
        super().__init__("node_camera_drive")
        self.get_logger().info("Camera Drive node started.")


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
