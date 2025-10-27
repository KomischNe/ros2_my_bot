import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStationNode(Node): 
    def __init__(self):
        super().__init__("robot_news_station") 
        self.counter_ = 0
        self.robot_name_ = "C3PO"
        self.publisher_ = self.create_publisher(String, "robot_news", 10) # topic name
        self.timer_ = self.create_timer(1.0, self.publish_news)
        self.get_logger().info("Robot News Station has been published.")
    
    def publish_news(self):
        msg = String()
        msg.data = self.robot_name_ + " has been published for " + str(self.counter_) + " sec"
        self.publisher_.publish(msg)
        self.counter_ += 1
    
             

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()