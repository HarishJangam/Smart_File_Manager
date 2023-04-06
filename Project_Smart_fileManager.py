import os
import shutil
import time
import helpers
from helpers import get_folders_list,create_folder,rename_folder,delete_folder,list_folder,search_file,sort_files
from helpers import take_input,size_of_each_folder,search,file_options



def main():
    while 1 :
        print("@@@@@@@@@@@ WELCOME TO SMART FILE MANAGER @@@@@@@@@@@@@")
        n=take_input(prompt="Enter your Option: ",input_class="int",options=[
            """
            1.get all folders
            2.create folder
            3.delete folder
            4.rename folder
            5.list_folder
            6.search file
            7.sort files
            8.size of each folders
            0.exit
            """
        ])
        if n==0:
            break
        elif n==1 :
            directory=take_input(prompt="ENTER YOUR PATH OR C:/ | D:/ : ")
            list=[]
            list=get_folders_list(directory)
            for f in list:
                print(f)
        elif n==2 :
            print("for creating folder enter path,name of folder")
            path=take_input(prompt="path :")
            name=take_input(prompt="name:")
            create_folder(path,name)
        elif n==3:
           
            path=take_input(prompt="enter path :",input_class="str")
            delete_folder(path)
        elif n==4:
            print("enter path, name :")
            path=take_input(prompt="path :")
            name=take_input(prompt="name :")
            rename_folder(path,name)
        elif n==5 :
            # print("ENTER PATH :")
            path=take_input(prompt="ENTER PATH :")
            list=list_folder(path)
            for l in list:
                print(l)
        elif n==6 :
            # directory=take_input(prompt="enter director :")
            name=take_input(prompt="ENTER NAME OF FILE :")
            list=search_file(name,False,True,None)
            for file in list:
                print(file)
            if len(list)!=0:
                f=input("enter file name")
                file_options(f)
            
        elif n==7:
            directory=take_input(prompt="enter directory :")
            name=take_input(prompt="enter sort by name or size :")
            list=sort_files(name,directory)
            for file in list:
                print(file)
        elif n==8:
            directory=input("enter directory : ")
            size_of_each_folder(directory)
            
            
     
if __name__=="__main__":
    start_time=time.time()
    os.chdir(os.getcwd())
    print("please wait....")
    search("C:/") 
    search("D:")
    end_time=time.time()
    total_time=end_time-start_time
    print(total_time)
    try:
        main()
    except Exception  as e:
        print(e)
    
    
    # print("total time take : {:.2f}".format(total_time))       




""""
1. pending:
    - 
2. Modify:

"""

"""
1. All prints, user outs should happen through main()/ Every function should not print anything. return value/None
"""