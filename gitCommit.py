import subprocess as cmd
import random
import string
import os
import schedule
import time

def commit():
    adder = cmd.run("git add .", check=True, shell=True)
    messages = ['update the repository', 'added new files', 'commiting files', 'general maintence']
    message = random.choice(messages)
    adder = cmd.run("git commit -m \'" + message + "\' ", check=True, shell=True)
    adder = cmd.run("git push ", check=True, shell=True)

def generateFiles():
    titleVal = random.randint(1,10)
    contentVal = random.randint(100,1000)
    lineVal = random.randint(10,70)
    title = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(titleVal)) + '.cpp'
    f = open(title, "a")
    for i in range(lineVal):
        f.write(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(contentVal)))
        f.write('\n')
    f.close()   

def clean():
    filelist = [ f for f in os.listdir() if f.endswith(".cpp") ]
    # print(filelist)
    for f in filelist:
        os.remove(os.path.join( f))

def job():
    commitVal = random.randint(10,70)
    for i in range(commitVal):
        generateFiles()
        commit()
        clean()
        time.sleep(1)

schedule.every().monday.at("11:00").do(job)
schedule.every().tuesday.at("11:00").do(job)
schedule.every().wednesday.at("11:00").do(job)
schedule.every().thursday.at("11:00").do(job)
schedule.every().friday.at("11:00").do(job)
schedule.every().saturday.at("11:00").do(job)


while True: 
  
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    time.sleep(1) 
