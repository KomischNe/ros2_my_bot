import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
import random




class GameMasterNode(Node): # MODIFY NAME

    def __init__(self):
        super().__init__("game_master") # MODIFY NAME
        self.players_ready_ = []
        self.roles_assigned_ = False
        self.roles_ = ['villager','villager','wolf','wolf','witch','perdictor']
        self.ready_sub_ = self.create_subscription(String, 'player_ready', self.player_ready_callback, 10) # topic name
        self.roles_pub_ = self.create_publisher(String, 'assign_role', 10)
        self.get_logger().info("WOLF GAME (6 players)")
        self.get_logger().info("2 villagers, 2 wolves, 1 witch, 1 predictor")
             
    def player_ready_callback(self, msg):
        player_name = msg.data
        if player_name not in self.players_ready_:
            self.players_ready_.append(player_name)
            self.get_logger().info(f"{player_name} is ready")
        # Assign roles when all 6 players are ready
        if len(self.players_ready_) == 6 and not self.roles_assigned_:
            self.assign_rloe()
            self.roles_assigned_ = True
            

    def assign_rloe(self):
        random.shuffle(self.roles_)
        for player, role in zip(self.players_ready_, self.roles_):
            msg = String()
            msg.data = f"{player}:{role}"
            self.roles_pub_.publish(msg)
        self.get_logger().info(f"All 6 players ready. Roles are assigned.")


def main(args=None):
    rclpy.init(args=args)
    node = GameMasterNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()