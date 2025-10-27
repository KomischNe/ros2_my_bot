import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import matplotlib.pyplot as plt
from collections import deque
import threading
import time

class SPeedPlotterNode(Node): # [node name] got
    def __init__(self):
        super().__init__("speed_plotter") # node name to call

        self.subscriber_ = self.create_subscription(Float32, "speed_monitor", self.speed_callback, 200)
        self.get_logger().info("Speed Plotter started.")

        # store last 500 samples
        self.data = deque(maxlen=500)
        self.timestamps = deque(maxlen=500)
        self.start_time = time.time()

        # run matplotlib in seqarate thread
        thread = threading.Thread(target=self.plot_thread)
        thread.daemon = True
        thread.start()

    def speed_callback(self, msg:Float32):
        self.data.append(msg.data)
        self.timestamps.append(time.time() - self.start_time)

    def plot_thread(self):
        plt.ion()
        fig, ax = plt.subplots()
        line, = ax.plot([], [], 'b-', label='Speed')
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Speed')
        ax.set_ylim(0, 6)
        ax.grid(True)
        ax.legend()

        while rclpy.ok():
            if self.data:
                line.set_xdata(list(self.timestamps))
                line.set_ydata(list(self.data))
                ax.set_xlim(max(0, self.timestamps[-1] - 10), self.timestamps[-1] + 1)
                plt.pause(0.05)


        

def main(args=None):
    rclpy.init(args=args)
    node = SPeedPlotterNode() # [node name] got
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()