import os
import shutil
import json
import datetime


def take_input(prompt = "Enter value: ", input_class = "str", options : list = None):
    """Takes input from user and converts into appropriate date type.
    params:
        promt:
        input_class:
    return:
    
    """
    val = None
    if options:
        for i in range(0, len(options)):
            print(f"{i}: {options[i]}")
            
    for _ in range(0, 3):
        try:
            val = input(prompt)
            if input_class == "int":
                val = int(val)
            
            return val
        except Exception as e:
            print("Wrong Value entered. Please enter again:",e)
    
    return None

def log_data(err_msg: str, excp) -> int:
    now=datetime.datetime.now()
    date_time=now.strftime("%Y-%m-%d %H:%M:%S")
    log_fmt = [{
        "date":date_time,
        "err_msg": err_msg,
        "excp": excp
    }]
    with open("modify.json","a") as f:
        f.write(f"{log_fmt}\n")



def get_folders_list(directory=os.getcwd()):
    # files=[]
   
    # for root,dir,file in os.walk(directory):
    #     for name in dir:
    #         files.append(os.path.join(root,name))
    try:
        return os.listdir(directory)
    except Exception as e:
        log_data(f"entered wrong directory",e)



def create_folder(name: str, path: str = os.getcwd()): # option arguments should be after positional orguments
    try:
        os.makedirs(os.path.join(path,name))
    except Exception as e:
        log_data(f"Folder creation failed. {path}/{name}", e)


def delete_folder(path):
    try:
        shutil.rmtree(path)
    except Exception as e:
        log_data(f"Folder deletion failed.{path}",e)
        
        
        
def rename_folder(old_name: str, new_name: str,path1=os.getcwd()):
    try:
        os.rename(old_name,os.path.join(os.path.dirname(path1),new_name))
    except Exception as e:
        log_data(f"folder name not changed due to ",e)    
        
        
        
def list_folder(path, dir_only: bool = True, files_olny: bool = True, hidden: bool=False):
    try:
        return os.listdir(path)
    except Exception as e:
        # print(f"List of folders are not acceced ",e)  
        log_data(f"List of folders are not acceced ",e)  
    
    
skip=["Program Files (x86)","Windows","Program Files"]    
dict={}
def search(dir):
    for root,dir,file in os.walk(dir):
        if root[0]=='$':
            continue
        if root in skip or dir in skip:
            continue
        # print(dir)
        for f in file:
            try:
                size=round(os.path.getsize(os.path.join(root,f))//(1024))
                dict[f]=[os.path.join(root,f),size]
            except:
                continue
    return dict

      
def search_file(file_name:str, exact_match=False, pattren_match=True, Extention=None):
    files=[]

    
    if exact_match:
        if file_name in dict:
            files.append(dict[file_name])
    elif pattren_match:
        for key in dict.keys():
            source=key
            if file_name in source:
                files.append(dict[key])
    # elif Extention:
    #     if name.endswith(Extention):
    #         files.append(os.path.join(root,name))
    print(len(dict))
    return files


def file_options(file):
    print("""
          1.open file
          2.rename file
          3.delete file
          """)
    try:
        opt=int(input("enter ur option"))
        if opt==1:
            # file1=file[0]
            print(file)
            f=open(file,"r")
            content=f.read()
            print(content)
        # elif opt==2:
        #     rename(file)
        # elif opt==3:
        #     delete(file)
    except Exception as e:
            log_data(f"exception occure in file_options",e)

def sort_files(sort_by_filename = None,directory  = os.getcwd()):
    files=[]
    for root,dir,file in os.walk(directory):
        for name in file:
            files.append(os.path.join(root,name))
    
    if sort_by_filename == 'name':
        files.sort()
    elif sort_by_filename== 'size':
        files.sort(key=os.path.getsize)
    else:
        files.sort()

    return files

def size_of_each_folder(directory):
    
    for root,dir,file in os.walk(directory):
        size=0
        for name in file:
            size=size+os.path.getsize(os.path.join(root,name))
        print(root," : ",round(size/(1024*1024),2),"MB")          




