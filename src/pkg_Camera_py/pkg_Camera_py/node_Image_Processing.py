import rclpy
from rclpy.node import Node


class MyNode(Node): # MODIFY NAME

    def __init__(self):
        super().__init__("node_image_processing") # MODIFY NAME
        self.get_logger().info("Image Processing node started.")
             

def main(args=None):
    rclpy.init(args=args)
    node = MyNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()