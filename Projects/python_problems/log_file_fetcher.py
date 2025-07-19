# 🔍 Log Filter Script (Python)

# A lightweight Python script to scan and extract specific log levels (`ERROR`, `DEBUG`, `Warning`) from any `.log` file.

# ## 🚀 Features
# - Filters log entries based on level
# - Supports regex word-boundary matching (no partial matches!)
# - Handles missing file errors gracefully
# - Easy to extend for other log levels

# ## 🛠️ Usage

# Update the file path:
# ```python
# log_file_path = r"C:\path\to\your\logfile.log"

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