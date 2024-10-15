# Combined Utility App

## Overview

This application is a command-line tool that combines multiple functionalities into one script. It provides system health checks, networking utilities, a socket server/client communication interface, and a file path utility.

### Key Features:
1. **System Health Check**: Monitors disk space and CPU usage to ensure your system is healthy.
2. **Wi-Fi Network Finder**: Lists available Wi-Fi networks on your system.
3. **Socket Server**: Sets up a basic socket server that listens for connections.
4. **Socket Client**: Connects to the server and receives a message.
5. **File Path Utility**: Displays the absolute path of the `check_health.py` file.

---

## How to Use

### Prerequisites:
- Python 3.x installed on your system.
- The `psutil` package is required for system health checks. You can install it using:
  ```bash
  pip install psutil
  ```

### Running the App:

1. **Download the Script**: Make sure to download the `combined_app.py` script.
2. **Open Terminal**: Navigate to the directory where `combined_app.py` is located.
3. **Run the Application**:
   ```bash
   python combined_app.py
   ```

### Menu Options:
Once you run the script, you will be presented with the following menu options:

1. **Check System Health**:
   - This option checks the disk usage (on `C:/`) and CPU usage.
   - If disk space is lower than 20% or CPU usage exceeds 75%, it will display an error message.
   - Otherwise, it will confirm that your system health is OK.
  
2. **List Available Networks**:
   - This option uses the `netsh` command (Windows only) to list available Wi-Fi networks.
   - It displays the networks detected by your machine.

3. **Start Server**:
   - This option starts a socket server on port `56789`. 
   - It listens for client connections and sends a "Thank you for connecting" message when a client connects.
   
4. **Start Client**:
   - This option connects to the socket server at `127.0.0.1` on port `56789`.
   - It receives a message from the server and displays it in the terminal.

5. **Get File Path**:
   - This option displays the absolute path of the `check_health.py` file.

6. **Exit**:
   - This option exits the application.

---

## Example Usage

1. **Checking System Health**:
   ```bash
   python combined_app.py
   # Select option 1 to check disk and CPU usage
   ```

2. **Listing Available Networks**:
   ```bash
   python combined_app.py
   # Select option 2 to view available Wi-Fi networks
   ```

3. **Running the Server**:
   - Start the server using option 3.
   - In another terminal, run the client using option 4 to connect to the server.

---

## Additional Information

- **Port Configuration**: By default, the server listens on port `56789`. You can change this in the script if needed.
- **OS Compatibility**:
  - The `list_available_networks` function uses the `netsh` command, which is specific to Windows.
  - Other features like the server, client, and health checks should work on most operating systems.

Feel free to modify or extend the app for your needs!

---

 Troubleshooting

- Error when listing networks: This feature is Windows-specific. If you are running this on another operating system, the `list_available_networks` function will fail.
- Server/Client connection issues: Ensure no other services are using port `56789`, and confirm both server and client are running on the same machine or network.

