import os
import json
#Need to Figure out Installation Problems With Module
#import binary2strings as b2s
def extractStringsLinuxWay(exeName):
    currentDir = os.path.dirname(os.path.realpath(exeName))
    os.chdir(currentDir)
    command = "strings " + exeName + " > output.txt"
    tempDict = {}
    commands = ""
    os.system(command)
    with open("output.txt") as tempFile:
        for x in tempFile:
            command += x
    
    out_file = open("output.json","w")
    tempDict[command] = 1
    json.dump(tempDict,out_file)
    out_file.close()


def main():
    executable = input("Enter .exe file: ")
    extractStringsLinuxWay(executable)


if __name__ == "__main__":
    main()