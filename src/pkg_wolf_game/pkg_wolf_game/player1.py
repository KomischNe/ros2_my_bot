import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class Player1Node(Node): # MODIFY NAME

    def __init__(self):
        super().__init__("player1") # MODIFY NAME
        self.name = 'player1'
        self.state_ = 'alive'
        self.role_ = None
        self.ready_pub_ = self.create_publisher(String, "player_ready", 10) # topic name
        self.role_sub_ = self.create_subscription(String, 'assign_role', self.assign_role_callback, 10)
        self.get_logger().info(f"ready")
        self.create_timer(0.5, self.announce_ready)

    def announce_ready(self):
        msg = String()
        msg.data = self.name
        self.ready_pub_.publish(msg)

    def assign_role_callback(self, msg):
        player, role = msg.data.split(':')
        if player == self.name:
            self.role_ = role
            self.get_logger().info(f"Your role is: {self.role_}")
             

def main(args=None):
    rclpy.init(args=args)
    node = Player1Node() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()