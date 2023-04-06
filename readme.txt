Usage:
 #small_
#small_file_manager
#it gives list of folders in a directory

# python ./run.py --log=expose

""""
1. code error: (Something went wrong. We are finxing it.)
2. input error: (Path not exists.)
"""

  
# def rename_folder(old_name: str, new_name: str):
#     try:
#         os.rename(path,os.path.join(os.path.dirname(path),name))
#     except:
#         print(f"from {path} to {name} changed successfully...")    
# linters         
# def size_of_each_folder(directory):
    
#     for root,dir,file in os.walk(directory):
#         size=0
#         for name in file:
#             size=size+os.path.getsize(os.path.join(root,name))
#         print(root," : ",round(size/(1024*1024),2),"MB")          


# def take_input(prompt = "Enter value: ", input_class = "str", options : list = None):
#     val = None
#     if options:
#         for i in range(0, len(options)):
#             print(f"{i}: {options[i]}")
            
#     for _ in range(0, 3):
#         try:
#             val = input(prompt)
#             if input_class == "int":
#                 val = int(val)
            
#             return val
#         except Exception as e:
#             print("Wrong Value entered. Please enter again:")
    
#     return None
            
        