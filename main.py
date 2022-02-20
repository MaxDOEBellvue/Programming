import os


def main():
    directory = input("What directory would you like to access?: ")
    filename = input(
        "Please enter the name of the file that you would like to access: ")
    username = input("Please enter your name: ")
    useraddress = ("Please enter your address: ")
    usernumber = input("Please enter your phone number: ")

    if os.path.isdir(directory):
        writeFile = open(os.path.join(directory, filename), 'w')
        writeFile.write(username + ',' + useraddress + ',' + usernumber + '/n')
        writeFile.close()

        print("File contents:")
        readFile = open(os.paht.join(directory, filename), 'r')
        for line in readFile:
            print(line)
        readFile.close()
    else:
        print("That directory is not available")


main()
