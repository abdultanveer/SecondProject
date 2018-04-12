import  webbrowser
import os
from string import digits


n=153
sum=0
while n>0:
    r=n%10
    sum+=r
    n=n/10
print (sum)


def rename_files():
    file_names = os.listdir(r"C:\Users\Ansari\Downloads\prank\prank")
    print(file_names)

    #print("abdul said\" hi how are you\"")
    os.chdir(r"C:\Users\Ansari\Downloads\prank\prank")
    current_working_directory = os.getcwd()
    print(current_working_directory)

    #os.rename("2chennai.jpg","chennai.jpg")
    for filename in file_names:
        os.rename(filename,filename.translate(str.maketrans('','',"0123456789")))
    new_files_list = os.listdir(r"C:\Users\Ansari\Downloads\prank\prank")
    print(new_files_list)

#rename_files()


# these are some good methods added by nairit

