import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

'''
    Publisher1: wheels  Topic1: speed_monitor, type: float   Subscriber1: speed_controller
    Publisher2: speed_controller  Topic2: speed_correction, type: float   Subscriber2: wheels

    wheels generate speed, publish to speed monitor
'''

class WheelsNode(Node): # [node name] got
    def __init__(self):
        super().__init__("wheels") # node name to call
        self.speed_generator_ = 0.0

        self.publisher_ = self.create_publisher(Float32, "speed_monitor", 200) # topic tpye, topic name
        self.subscriber_ = self.create_subscription(Float32, "speed_correction", self.correction_callback, 200)

        self.timer_ = self.create_timer(0.05, self.publish_speed)
        self.speed_correction_ = 0.0

        self.get_logger().info("Speed UPPPPPPPPPPP")


    def correction_callback(self, corr:Float32):
        self.speed_correction_ = corr.data


    def publish_speed(self):
        self.speed_generator_ += 0.05 + self.speed_correction_

        msg = Float32()
        msg.data = self.speed_generator_
        self.publisher_.publish(msg)
        

def main(args=None):
    rclpy.init(args=args)
    node = WheelsNode() # [node name] got
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()