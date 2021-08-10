import os

print("------------------------")
print("Your Hoster Name")
print("------------------------               Powered by PyPackager (github.com/Vodkarm/PyPackager)")
print("")
while(True):
    print("Do you want to install one (1) or more modules (2):")
    response = input()
    if response == "1":
        print("Which module do you want to install:")
        module = input()
        os.system('pip3 install '+ module +' -t ./')
        break
    elif response == "2":
        if os.path.exists("./requirements.txt") and os.path.isfile("./requirements.txt"):
            os.system('pip3 install -r requirements.txt -t ./')
            break
        else:
            print("The \"requirements.txt\" file does not exist or is not a file on your hosting.")
    else:
        print("Please enter a valid number (1 or 2)")
