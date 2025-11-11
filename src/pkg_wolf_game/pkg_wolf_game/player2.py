import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class Player2Node(Node): # MODIFY NAME

    def __init__(self):
        super().__init__("player2") # MODIFY NAME
        self.name = 'player2'
        self.state_ = 'alive'
        self.role_ = None
        self.ready_pub_ = self.create_publisher(String, "player_ready", 10) # topic name
        self.role_sub_ = self.create_subscription(String, 'assign_role', self.assign_role_callback, 10)
        
        self.night_start_sub_ = self.create_subscription(String, 'night_start', self.night_start_callback, 10)
        self.wolf_action_pub_ = self.create_publisher(String, 'wolf_action', 10)

        self.dead_sub_ = self.create_subscription(String, 'dead', self.dead_callback, 10)

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

    def night_start_callback(self, msg):
        if self.state_ == 'dead':
            return  # ignore all night messages if dead
        """Respond to game master's announcements"""
        data = msg.data
        self.get_logger().info(data)

        ### night actions
        # role == villager
        if data == "🌙 Night phase begins!" and self.role_ == "villager" and self.state_ == "alive":
            self.get_logger().info("Wait for day time...")

        # role == wolf
        if data == "🌙 Night phase begins!" and self.role_ == "wolf" and self.state_ == "alive":
            self.wolf_action()
        


    def wolf_action(self):
        # Ask user input
        target = None
        while target not in range(1, 6):
            try:
                target = int(input("Enter player number to kill (1-5): ").strip())
                if target not in range(1, 6):
                    print("Invalid choice, try again.")
            except ValueError:
                print("Please enter a valid number between 1 and 5.")

        msg = String()
        msg.data = f"{self.name}:{target}, action:done"
        self.wolf_action_pub_.publish(msg)



    def dead_callback(self, msg):
        dead_players = [p.strip() for p in msg.data.split(',')]
        if self.name in dead_players:
            self.get_logger().info("💀 YOU'RE DEAD")
            self.state_ = 'dead'

             

def main(args=None):
    rclpy.init(args=args)
    node = Player2Node() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()