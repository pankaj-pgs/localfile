import os

ip_list = ['18.8.8.8']
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Request timed out" in response:
        print(f"DOWN {ip} Ping Unsuccessful")
    elif "Destination Host Unreachable" in response:
        print(f"DOWN {ip} Ping Unsuccessful")
    else:
        print(f"UP {ip} Ping successful")