import subprocess as cmd
import random
import string
import os

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
    title = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(titleVal)) + '.txt'
    f = open(title, "a")
    for i in range(lineVal):
        f.write(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(contentVal)))
        f.write('\n')
    f.close()   

def clean():
    filelist = [ f for f in os.listdir() if f.endswith(".txt") ]
    print(filelist)
    for f in filelist:
        os.remove(os.path.join( f))

generateFiles()
commit()
clean()

