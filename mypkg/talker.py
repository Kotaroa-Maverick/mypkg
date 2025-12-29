import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import psutil

class CpuTalker(Node):
    def __init__(self):
        super().__init__('cpu_talker')
        self.pub = self.create_publisher(Float64, "cpu_usage", 10)
        self.create_timer(1.0, self.cb)

    def cb(self):
        msg = Float64()
        msg.data = psutil.cpu_percent(interval=None)
        self.pub.publish(msg)
        self.get_logger().info('Publishing CPU Usage: %f%%' % msg.data)

def main():
    rclpy.init()
    node = CpuTalker()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
