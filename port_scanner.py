import socket

target = input("Enter target IP address: ")

print(f"\nScanning target {target}...\n")

for port in range(1, 101):   # scans ports 1 to 100
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is OPEN 🔓")
    
    s.close()

print("\nScan completed ✅")