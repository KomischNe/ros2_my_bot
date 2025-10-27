import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

'''
    Publisher1: wheels  Topic1: speed_monitor, type: float   Subscriber1: speed_controller
    Publisher2: speed_controller  Topic2: speed_correction, type: float   Subscriber2: wheels

    speed controller subscribe the speed monotor to get speed value
'''

class SpeedControllerNode(Node): # [node name] got
    def __init__(self):
        super().__init__("speed_controller") # node name to call
        self.subscriber_ = self.create_subscription(Float32, "speed_monitor", self.get_speed, 200)
        self.get_logger().info("Speed Monitor is on.")

    def get_speed(self, value:Float32):
        self.get_logger().info(f"{value.data:.2f}")

             

def main(args=None):
    rclpy.init(args=args)
    node = SpeedControllerNode() # [node name] got
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()