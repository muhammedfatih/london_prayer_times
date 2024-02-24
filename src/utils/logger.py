# src/utils/logger.py
import os
from datetime import datetime

def log(string_to_write):
    log_path = "logs/output.txt"
    
    with open(log_path, 'a') as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{current_time} - {string_to_write}\n"
        file.write(log_entry)
        print(log_entry)
