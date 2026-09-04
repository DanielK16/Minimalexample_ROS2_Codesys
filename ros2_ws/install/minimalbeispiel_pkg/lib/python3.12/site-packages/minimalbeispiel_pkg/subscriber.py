import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

import asyncio
import logging
from asyncua import Client, ua  # <-- ua hier hinzugefügt

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.latest_pose = None  

        # Create Publisher
        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        # Create Subscription
        self.subscription = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.pose_callback,
            10)

    # topic werte der msg in variable zwischenspeichern
    def pose_callback(self, msg):
        self.latest_pose = msg

    def publish_twist(self, linear_x, angular_z):
        twist_msg = Twist()
        twist_msg.linear.x = float(linear_x)
        twist_msg.angular.z = float(angular_z)
        self.publisher.publish(twist_msg)

class SubscriptionHandler:
    def __init__(self,ros_node, target_nodes):
        self.ros_node = ros_node
        self.target_nodes = target_nodes
        self.current_linear_x = 0.0
        self.current_angular_z = 0.0

    def datachange_notification(self, node, val, data):
        if node == self.target_nodes["linear_x"]:
            self.current_linear_x = float(val)
        elif node == self.target_nodes["angular_z"]:
            self.current_angular_z = float(val)
        
        

async def async_main(args=None):
    # OPC UA Verbindungsaufbau
    ipaddress = "172.25.170.32"
    port = "4840"
    opc_url = f"opc.tcp://{ipaddress}:{port}"

    ros_node = MinimalSubscriber()

    async with Client(opc_url) as client:
        print(f"OPC Client {opc_url} verbunden")
        
        # 1. OPC-Node holen (hier einheitlicher Name: opc_target_nodes)
        opc_target_nodes = {

            "x_pose": client.get_node("ns=5;s=AQAAAKbhKnGK9zM6uvotdobvJ2ac8zBxx/c1Zp3vJSW28y9njK04S5nsM3Hp"),

            "y_pose": client.get_node("ns=5;s=AQAAAKbhKnGK9zM6uvotdobvJ2ac8zBxx/c1Zp3vJSW28y9njK05S5nsM3Hp"),

            "theta_pose": client.get_node("ns=5;s=AQAAAKbhKnGK9zM6uvotdobvJ2ac8zBxx/c1Zp3vJSW28y9njK00fIz3IUuZ7DNx6Q=="),

            "linear_x": client.get_node("ns=5;s=AQAAAKbhKnGK9zM6uvotdobvJ2ac8zBxx/c1Zp3vJSW24C1wtvUleMfvKXqM4jJLkYM="),

            "angular_z": client.get_node("ns=5;s=AQAAAKbhKnGK9zM6uvotdobvJ2ac8zBxx/c1Zp3vJSW24C1wtvUleMfiLnOc7yFmtvlA")
        }
                            
        handler = SubscriptionHandler(ros_node, opc_target_nodes)
        sub = await client.create_subscription(100,handler)
        await sub.subscribe_data_change([opc_target_nodes["linear_x"], opc_target_nodes["angular_z"]])

        try:
            while rclpy.ok():
                rclpy.spin_once(ros_node, timeout_sec=0.0)
                ros_node.publish_twist(handler.current_linear_x,handler.current_angular_z)
                
                if ros_node.latest_pose is not None:
                    # Hier den gleichen Variablennamen (opc_target_nodes) nutzen
                    await opc_target_nodes["x_pose"].write_value(ua.Variant(float(ros_node.latest_pose.x), ua.VariantType.Float))
                    await opc_target_nodes["y_pose"].write_value(ua.Variant(float(ros_node.latest_pose.y), ua.VariantType.Float))
                    await opc_target_nodes["theta_pose"].write_value(ua.Variant(float(ros_node.latest_pose.theta), ua.VariantType.Float))
                    
                await asyncio.sleep(0.01)
                
        except KeyboardInterrupt:
            pass
        finally:
            ros_node.destroy_node()

def main(args=None):
    rclpy.init(args=args)
    try:
        asyncio.run(async_main(args))
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()