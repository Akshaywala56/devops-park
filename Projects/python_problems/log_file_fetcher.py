# A simple Python script to parse log files and extract lines with specific log levels like ERROR, DEBUG, and Warning.  
# Uses regex with word boundaries to avoid partial matches.  
# Handles file read errors gracefully.  
# Great for basic log analysis and DevOps tasks.

import re
log_file_path = r"C:\git\devops-park\Projects\python_problems\sample.log"
pattern = r"\b(ERROR|DEBUG|Warning)\b"
error_lines =[]
 
try:
    with open(log_file_path,'r') as f:
        for line in f:
            if re.search(pattern,line):
                print(line.strip())
except FileNotFoundError:
    print(f"Error: log file '{log_file_path}' not found.")
except Exception as e:
    print(f"An error occured while reading the file :{e}")