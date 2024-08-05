import socket

mac_to_ip_mapping = {
    "BC-17-B8-7F-F2-B0": "10.1.74.155",
    "AA:BB:CC:DD:EE:FF": "192.168.1.3",
}

def get_ip_address(mac_address):
    return mac_to_ip_mapping.get(mac_address, "IP Not Found")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 12345)
server_socket.bind(server_address)
server_socket.listen(1)

print("REVERSE ADDRESS RESOLUTION PROTOCOL")
print("------------------------------------")
print("RARP server side:")
print("Server is ready to receive requests...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    while True:
        mac_address = client_socket.recv(1024).decode('utf-8')
        ip_address = get_ip_address(mac_address)
        client_socket.send(ip_address.encode('utf-8'))
# import socket
# mac_to_ip_mapping = {
# "BC-17-B8-7F-F2-B0": "10.1.74.155",
# "AA:BB:CC:DD:EE:FF": "192.168.1.3",
# }
# def get_ip_address(mac_address):
#         return mac_to_ip_mapping.get(mac_address, "IP Not Found")
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = ('127.0.0.1', 12345)
# server_socket.bind(server_address)
# server_socket.listen(1)
# print("Server is ready to receive requests...")
# while True:
#       client_socket, client_address = server_socket.accept()
# print(f"Connection from {client_address}")
# while True:
#     mac_address = client_socket.recv(1024).decode('utf-8')
# ip_address = get_ip_address(mac_address)
# client_socket.send(ip_address.encode('utf-8'))