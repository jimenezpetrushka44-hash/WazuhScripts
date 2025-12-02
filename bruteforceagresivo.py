import subprocess
import time

TARGET = "127.0.0.1"
USER = "ghost"
PASSWORD = "123456"

for i in range(20):
    cmd = ["net", "use", f"\\\\{TARGET}\\IPC$", f"/user:{USER}", PASSWORD]
    print(f"Attempt {i+1}")
    subprocess.run(cmd, shell=True)
    time.sleep(0.5)
print("Attack finished")