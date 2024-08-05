import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 12345)
client_socket.connect(server_address)

print("REVERSE ADDRESS RESOLUTION PROTOCOL")
print("------------------------------------")
print("RARP client side:")

while True:
    mac_address = input("Enter MAC address (or 'exit' to quit): ")
    if mac_address == 'exit':
        break
    client_socket.send(mac_address.encode('utf-8'))
    ip_address = client_socket.recv(1024).decode('utf-8')
    print(f"IP address for MAC address {mac_address}: {ip_address}")

client_socket.close()
# import socket
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = ('127.0.0.1', 12345)
# client_socket.connect(server_address)
# while True:
#     mac_address = input("Enter MAC address (or 'exit' to quit): ")
#     if mac_address == 'exit':
#         break
# client_socket.send(mac_address.encode('utf-8'))
# ip_address = client_socket.recv(1024).decode('utf-8')
# print(f"IP address for MAC address {mac_address}: {ip_address}")
# client_socket.close()