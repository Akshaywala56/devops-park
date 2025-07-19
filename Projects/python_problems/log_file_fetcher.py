import re
log_file_path = "C:\git\devops-park\Projects\python_problems\sample.log"
error_lines =[]
 
try:
    with open(log_file_path,'r') as f:
        for line in f:
            word =["ERROR","DEBUG","Warning"]
            if re.search(rf"\b{word}\b",line):
                print(line)
            else:
                pass
except FileNotFoundError:
    print(f"Error: log file '{log_file_path}' not found.")
except Exception as e:
    print(f"An error occured while reading the file :{e}")