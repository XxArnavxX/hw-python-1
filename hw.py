import os
import shutil

Input = input("Input folder name: ")
Output = input("Output folder name: ")

Input = Input + '/'
Output = Output + '/'

listOfFiles = os.listdir(Input)
print(listOfFiles)

for file in listOfFiles:
    shutil.move((Input + file), Output)