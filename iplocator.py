import socket
import requests

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]



if __name__ == '__main__':
    ip_address = get_ip_address()


    with open("ip_and_location_info.txt", "w") as file:
        file.write("IP Address: " + ip_address + "\n")
        
        
    print("The IP address and location information have been saved to the file 'ip_and_location_info.txt'")
