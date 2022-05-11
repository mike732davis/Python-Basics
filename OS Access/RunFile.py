import subprocess
from Audio import audio
print("Programs Available\n1.Notepad++\n2.MS Excel\n3.MS Word")
audio("Choose a program by entering its corresponding number")
choice=int(input("Choose a program to open that program:-\n"))
if (choice==1):    
    audio("Opening Notepad++")
    subprocess.Popen("D:\\New folder\\Notepad++\\notepad++.exe")
elif (choice==2):
    audio("Opening MS Excel")
    subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\Office16\\EXCEL.EXE")
elif (choice==3):
    audio("Opening MS Word")
    subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
else:
    audio("Sorry! Wrong Option selected. Please choose an option from 1 to 3")
    print("!!!!!!!ERROR!!!!!!!!!")
    