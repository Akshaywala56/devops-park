# as a devops engineer in ec2 instance linux server the logs are cretaed rapidly and it is 2-3 GB per day.
# if this is the case then disk usage will be full after sometime so what will you do?

# what they are checking 
# whether you know the disk usage management?
# did you know the log rotation or not?
# can you able to write the pyhton script or not for log archival?

import os 
log_file = "C:\\git\\devops-park\\Projects\\python_problems\\big_data.log"


def size_check():
    size_in_mb =os.path.getsize(log_file)/(1024*1024)
    print(f"log file size in mb: ",size_in_mb)

if __name__ == '__main__':
    size_check()

