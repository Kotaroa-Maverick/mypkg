import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class CpuListener(Node):
    def __init__(self):
        super().__init__('cpu_listener')
        self.sub = self.create_subscription(Float64, "cpu_usage", self.cb, 10)

    def cb(self, msg):
        
        status = "NORMAL"
        if msg.data > 80.0:
            status = "HIGH LOAD!"
        
        self.get_logger().info('CPU Usage: %.1f%% [%s]' % (msg.data, status))

def main():
    rclpy.init()
    node = CpuListener()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

