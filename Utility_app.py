import shutil
import psutil
import os
import socket
import subprocess

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

def check_system_health():
    if not check_disk_usage("C:/") or not check_cpu_usage():
        print("ERROR: System health check failed!")
    else:
        print("System health is OK.")

def list_available_networks():
    try:
        nw = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
        decoded_nw = nw.decode('utf-8', errors='ignore')
        print(decoded_nw)
    except Exception as e:
        print(f"Error retrieving network information: {e}")


def start_server():
    s = socket.socket()
    port = 56789
    s.bind(('', port))
    print(f"Socket bound to port {port}")
    s.listen(5)
    print('Server is listening on port', port)
    while True:
        c, addr = s.accept()
        print('Got connection from', addr)
        message = 'Thank you for connecting'
        c.send(message.encode())
        c.close()

def start_client():
    s = socket.socket()
    port = 56789
    s.connect(('127.0.0.1', port))
    print(s.recv(1024).decode())
    s.close()

def get_file_path():
    file_path = os.path.abspath("check_health.py")
    print(f"Absolute path of check_health.py: {file_path}")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Check System Health")
        print("2. List Available Networks")
        print("3. Start Server")
        print("4. Start Client")
        print("5. Get File Path")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            check_system_health()
        elif choice == '2':
            list_available_networks()
        elif choice == '3':
            start_server()
        elif choice == '4':
            start_client()
        elif choice == '5':
            get_file_path()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
