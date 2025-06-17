import subprocess
import socket


print("hello")

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)

for ping in range (1,10):
    address = "127.0.0." + str(ping)
    res = subprocess.call(['ping','-n','3', address])
    if res == 0 :
        print("ping to ", address,"OK")
    elif res == 2:
        print("no response from", address)
    else:
        print("ping to ",address,"failed ")

