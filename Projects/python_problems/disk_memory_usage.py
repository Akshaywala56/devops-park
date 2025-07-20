# As a DevOps engineer, I prefer scripting lightweight monitoring in Python for basic checks. 
# I’d run this via a cronjob and alert manually or integrate with logs if needed

# Python Script to Monitor Disk Usage on a Server

import shutil
import os
import datetime

source_file =r"C:\\git\\devops-park\\Projects\\python_problems\\sample.log"
temp_folder = r"C:\git\devops-park\Projects\python_problems\temp_logs"

def check_disk_usage(path="/"):
    total,used,free =shutil.disk_usage(path)
    usage_percent = (used/total)*100
    print(f"Disk usage: {usage_percent:.2f}%")

    if usage_percent > 80:
        print("warning: Disk usage is above 80%")
    else:
        print("disk usage is under control")

def logs():
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    os.makedirs(temp_folder, exist_ok=True)
    shutil.copy(source_file,temp_folder)
    archive_name =f"log_backup_{timestamp}"
    shutil.make_archive(archive_name,'zip',temp_folder)
    # shutil.rmtree(temp_folder)
    # os.remove(source_file)
    print(f"✅ Backup completed: {archive_name}.zip")
# check_disk_usage()
logs()