import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


def main(args=None):
    rclpy.init(args=args)
    node = Node("add_two_ints_client_no_oop") # MODIFY NAME

    client = node.create_client(AddTwoInts, "add_two_ints") # service interface, name
    while not client.wait_for_service(1.0):
        node.get_logger().warn("Waiting for [Add Two Ints] server...")
    
    request = AddTwoInts.Request()  # fill the request
    request.a = 3
    request.b = 7

    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)
    response = future.result()

    node.get_logger().info(str(request.a) + "+" + str(request.b) + "=" + str(response.sum)) # do anything to the response

    rclpy.shutdown()

if __name__ == '__main__':
    main()