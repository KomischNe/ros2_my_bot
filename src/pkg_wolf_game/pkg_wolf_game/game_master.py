import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
import random
import time



class GameMasterNode(Node): # MODIFY NAME

    def __init__(self):
        super().__init__("game_master") # MODIFY NAME
        self.players_ready_ = []
        self.player_states_ = {} 
        self.player_roles_ = {}    
        self.player_action_ = {} 
        self.wolf_action_ = {} 

        self.roles_assigned_ = False
        self.game_phase_ = "waiting"  # can be 'waiting', 'night', 'day', 'end'
        self.roles_ = ['villager','villager','villager','villager','wolf'] # ['villager','villager','wolf','wolf','witch','perdictor']
        self.ready_sub_ = self.create_subscription(String, 'player_ready', self.player_ready_callback, 10) # topic name
        self.roles_pub_ = self.create_publisher(String, 'assign_role', 10)
        # night actions
        self.night_start_pub_ = self.create_publisher(String, 'night_start', 10)
        self.wolf_action_sub_ = self.create_subscription(String, 'wolf_action', self.wolf_action_callback, 10)

        self.get_logger().info("WOLF GAME (5 players)")
        self.get_logger().info("4 villagers, 1 wolf")
             
    ### Step1: players ready
    def player_ready_callback(self, msg):
        player_name = msg.data
        if player_name not in self.players_ready_:
            self.players_ready_.append(player_name)
            self.get_logger().info(f"{player_name} is ready")
        # Assign roles when all 5 players are ready
        if len(self.players_ready_) == 5 and not self.roles_assigned_:
            self.assign_rloe()
            self.roles_assigned_ = True
            # start of night actions, this will also triggered only once HERE
            time.sleep(1)
            self.start_night_phase()
            

    def assign_rloe(self):
        random.shuffle(self.roles_)
        for player, role in zip(self.players_ready_, self.roles_):
            msg = String()
            msg.data = f"{player}:{role}"
            self.roles_pub_.publish(msg)
        
            # Store player states
            self.player_roles_[player] = role
            self.player_states_[player] = 'alive'

            # Initialize night action
            if role == "villager":
                self.player_action_[player] = "done"  # villagers have no night action
            else:
                self.player_action_[player] = None    # non-villagers need to act

        self.get_logger().info(f"All 5 players ready. Roles are assigned.")

    ### Step2: night actions
    def start_night_phase(self):
        self.game_phase_ = "night"
        # self.night_done_players_.clear()
        for i in range(30,0,-1):
            msg = String()
            msg.data = f"Night start in {i/10} s"
            self.night_start_pub_.publish(msg)
            self.get_logger().info(msg.data)
            time.sleep(0.1)
        
        msg = String()
        msg.data = "🌙 Night phase begins!"
        self.night_start_pub_.publish(msg)
        self.get_logger().info(msg.data)

    def wolf_action_callback(self, msg):
        voter, target = msg.data.split(':')[0], msg.data.split(':')[1].split(',')[0]

        # Record vote only if voter is a wolf and alive
        if self.player_roles_.get(voter) == "wolf" and self.player_states_.get(voter) == 'alive':
            # Store wolf vote
            self.wolf_action_[voter] = target
            # Mark wolf action as done
            self.player_action_[voter] = "done"
            # announce who is killed
            self.get_logger().info(f"Player{target} is killed.")

            # Mark target player as dead
            self.player_states_[f"player{target}"] = 'dead'
            
            # Check if all night actions are done
            self.night_done()


    def night_done(self):     
        if all(action is not None for action in self.player_action_.values()):   
            self.get_logger().info("🌞 Night actions complete. Starting day phase...")
            time.sleep(1)
            self.start_day_phase()
        


    ### Step3: day actions
    def start_day_phase(self):
        self.game_phase_ = "day"

        # List alive players
        alive_players = [player for player, state in self.player_states_.items() if state == 'alive']
        self.get_logger().info(f"🌞 Day phase begins! Alive players: {', '.join(alive_players)}")

        # Count alive wolves and humans
        alive_wolves = [p for p in alive_players if self.player_roles_[p] == "wolf"]
        alive_humans = [p for p in alive_players if self.player_roles_[p] != "wolf"]

        # Check game end conditions
        if len(alive_wolves) >= len(alive_humans):
            self.get_logger().info("🐺 Wolves win! Game over.")
            self.game_phase_ = "end"
            return
        elif len(alive_wolves) == 0:
            self.get_logger().info("🏠 Humans win! Game over.")
            self.game_phase_ = "end"
            return
        else:
            self.get_logger().info("Game continues...")

        self.get_logger().info("This is day action, gaming continues...")
        time.sleep(3)
        
        # Start next night
        self.start_night_phase()
        


def main(args=None):
    rclpy.init(args=args)
    node = GameMasterNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()