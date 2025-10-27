import rclpy
from rclpy.node import Node
# this is dev_zrf branch

class MyNode(Node):

    def __init__(self):
        super().__init__("node_camera_drive")
        self.counter_ = 0
        self.get_logger().info("Camera Drive node started.")
        self.create_timer(0.1, self.timer_callback)  # call function 'timer_callback' every 0.1 sec 

    def timer_callback(self):
        self.get_logger().info("Waiting " + str(self.counter_ / 10) + " sec")
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
