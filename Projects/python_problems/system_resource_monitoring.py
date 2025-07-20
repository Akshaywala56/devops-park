import psutil
import time
import os
import datetime

os.makedirs("logs", exist_ok=True)
log_file = "logs/sys_monitor.log"

def monitor():
    while True:
        #CPU usage
        cpu_usage =psutil.cpu_percent(interval=1)
        print(f"CPU usage: ",cpu_usage)
        if cpu_usage > 90:
            print("ALERT: CPU usage is above 90%!")

        # Memory usage
        memory_usage =psutil.virtual_memory()
        print(f"Memory usage: ",memory_usage)
        if memory_usage.percent > 90:
            print("ALERT: Memory usage is above 90%!")

        # Disk usage
        Disk_usage = psutil.disk_usage('/')
        print(f"Disk usgae", Disk_usage)
        if Disk_usage.percent > 90:
            print("ALERT: Disk usage is above 90%!")

        # network usage
        Network_usage = psutil.net_io_counters()
        print(f"Bytes cent: {Network_usage.bytes_sent},bytes recived: {Network_usage.bytes_recv}")

        # adding seperator for redability
        print("-" * 50)

        with open(log_file, "a") as f:
            f.write(f"{datetime.datetime.now()} - CPU: {cpu_usage}%, MEM: {memory_usage}%, DISK: {Disk_usage}%\n")
        # for for few second before the next step
        time.sleep(5)

if __name__ == '__main__':
    monitor()


# I’ve used the psutil module in Python to build lightweight server monitoring scripts. 
# I monitor CPU, memory, disk, and network usage at regular intervals, 
# and add thresholds to alert if resource usage crosses limits. The script can also be extended to log results or send email/Slack alerts.