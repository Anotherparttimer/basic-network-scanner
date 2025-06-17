import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True, shell=True)
print(result.stdout)
check = True


type = input("enter 'tracert' or 'ping'")
# make a sep path for "tracert" feature 
address= input("enter an IP address: ")
print("select a flag t , c , n ")
flag = input("enter a choice: ")

while(check==True):
    if address == "null" and check==True:
         print("enter number")
    else:

       
        res = subprocess.call([type,'-'+flag,'5', address], shell=True)
        if res == 0 :
            print("ping to ", address,"OK")
        elif res == 2:
            print("no response from", address)
        else:
            print("ping to ",address,"failed ")
    
    check= False