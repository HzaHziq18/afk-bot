import time
from mcstatus import MinecraftServer
import socket
import logging

# Set up logging for reconnection attempts
logging.basicConfig(filename="bot_log.txt", level=logging.INFO)

# Server details
server_ip = "katakana.aternos.me"
server_port = 33395

# Function to check server status
def check_server():
    server = MinecraftServer(server_ip, server_port)
    try:
        status = server.status()
        print(f"Server is online. Players online: {status.players.online}")
        logging.info(f"Server is online. Players online: {status.players.online}")
        return True
    except (socket.timeout, ConnectionRefusedError, OSError) as e:
        print(f"Failed to connect to server: {e}")
        logging.error(f"Failed to connect to server: {e}")
        return False

# Function to attempt reconnection
def reconnect():
    print("Attempting to reconnect...")
    logging.info("Attempting to reconnect...")
    connected = False
    while not connected:
        connected = check_server()
        if not connected:
            time.sleep(10)  # Wait 10 seconds before retrying
    print("Reconnected successfully!")
    logging.info("Reconnected successfully!")

# Keep the bot running indefinitely
def run_bot():
    while True:
        if not check_server():
            reconnect()
        time.sleep(60)  # Check server every 60 seconds

# Start the bot
if __name__ == "__main__":
    run_bot()
