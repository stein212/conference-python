import os

os.system("cd /home/opt/isls/isls/")
#os.system("flask run --host=192.168.70.15 --port=6000")
#os.system("cd ../../")

if os.system("python3 app.py") == 0:
    print("Ok")