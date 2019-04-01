import time
import os
import sched

schedule = sched.scheduler(time.time(),time.sleep())

def execute_command(cmd,inc):
    print("Execute the program")
    """
    Show the status of the computer in the terminal 
    """
    os.system(cmd)
    schedule.enter(inc,0,execute_command(),(cmd,inc))

def main(cmd,inc=60):
    schedule.enter(0,0,execute_command(),(cmd,inc))
    schedule.run()

if __name__ == '__main__':
    main("netstat -an", 60)

