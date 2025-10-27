import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class SmartphoneNode(Node): # [node name] got
    def __init__(self):
        super().__init__("smartphone") # node name to call after package(normally set to the same as .py file name)
        self.subscriber_ = self.create_subscription(
            # pub and sub must share the same MSG_TYPE=String and TOPIC="robot_news" to get communication
            String, "robot_news", self.callback_robot_news, 10) 
        self.get_logger().info("Smartphone has been started.")

    def callback_robot_news(self, msg: String):
        # decide what to do with the msg
        self.get_logger().info(msg.data)
             

def main(args=None):
    rclpy.init(args=args)
    node = SmartphoneNode() # [node name] got
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()