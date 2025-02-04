import tkinter as tk
from tkinter import messagebox
import subprocess
import re

def scan_wifi():
    try:
        result = subprocess.run(['nmcli', '-t', '-f', 'SSID,SIGNAL,SECURITY', 'dev', 'wifi'], capture_output=True, text=True)
        networks = result.stdout.strip().split('\n')
        
        wifi_list.delete(0, tk.END)
        
        for net in networks:
            details = net.split(':')
            if len(details) >= 3:
                ssid, signal, security = details[0], details[1], details[2]
                wifi_list.insert(tk.END, f"SSID: {ssid}, Signal: {signal}%, Security: {security}")
                if 'WEP' in security:
                    messagebox.showwarning("Security Alert", f"{ssid} uses WEP, which is insecure!")
                elif 'NONE' in security:
                    messagebox.showwarning("Security Alert", f"{ssid} has no security! Use caution.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to scan networks: {e}")

# UI Setup
root = tk.Tk()
root.title("WiFi Security Scanner")
root.geometry("500x400")

tk.Label(root, text="Available WiFi Networks", font=("Arial", 14)).pack(pady=10)

wifi_list = tk.Listbox(root, width=60, height=15)
wifi_list.pack(pady=10)

scan_button = tk.Button(root, text="Scan WiFi", command=scan_wifi, font=("Arial", 12))
scan_button.pack(pady=10)

root.mainloop()
