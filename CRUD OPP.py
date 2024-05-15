import os 

def dirdisplay(dir):
    try:
        if os.path.exists(dir):
            contents = os.listdir(dir)
            count = 1
            for items in contents :
                print(f"{count}. {items}")
                count+= 1
    except FileNotFoundError:
        print(f"Error: File not found.")
    except PermissionError:
        print(f"Error: You don't have permission to rename the file.")
    except OSError as e:
        print(f"An error occurred: {e}")
        

def dir_itemlist(dir):
    try:
        if os.path.exists(dir):
            contents = os.listdir(dir)
            count = 1
            item_list = []
            for items in contents :
                item_list.append(items) 
                count+= 1
            
            return item_list 
    except FileNotFoundError:
        print(f"Error: File not found.")
    except PermissionError:
        print(f"Error: You don't have permission to rename the file.")
    except OSError as e:
        print(f"An error occurred: {e}")
        

          
def create_file(Dpath):
        try:
            filename  = input("""Lets create file
                        Enter the name of file :       
                """)
            file_path = os.path.join(Dpath , filename)
            if not os.path.exists(Dpath):
                print(f"Error: Directory '{Dpath}' does not exist.")
            with open(file_path,"w") as file:
                file.write("testing testing test")
                pass
                print(f"{filename} was created")
                dirdisplay(Dpath)
        except FileNotFoundError:
            print(f"Error: File '{Dpath}' not found.")
        except PermissionError:
            print(f"Error: You don't have permission to rename the file.")
        except OSError as e:
            print(f"An error occurred: {e}")
        
        

def delete_file(Dpath):
    try:
        if os.path.exists:
            os.remove(Dpath)
            print(f"File {Dpath} is removed")
            dirdisplay(Dpath)

        else:
            print(f"File {Dpath} Doesnt exist")
    except FileNotFoundError:
        print(f"Error: File '{Dpath}' not found.")
    except PermissionError:
        print(f"Error: You don't have permission to rename the file.")
    except OSError as e:
        print(f"An error occurred: {e}")
        

def Rename_file(Dpath):
    try:
        print(dirdisplay(Dpath))
        selected_file_index = int(input("Which file do you want to rename: "))
        file_names = dir_itemlist(Dpath)
        print(file_names)
        for old_filename in file_names:
            if file_names.index(old_filename) ==  selected_file_index-1:
                print(f"File selected for renaming is {old_filename}")
                    
        new_filename = input(f"Enter new name for {old_filename} : ")
        new_filepath  = os.path.join(Dpath,new_filename)
        old_filepath  = os.path.join(Dpath,old_filename)
        os.rename(old_filepath,new_filepath)
        print(f"File {old_filename} is now renamed {new_filename}")
        dirdisplay(Dpath)
    except FileNotFoundError:
        print(f"Error: File '{old_filepath}' not found.")
    except PermissionError:
        print(f"Error: You don't have permission to rename the file.")
    except OSError as e:
        print(f"An error occurred: {e}")
        

kill_me = 0
while kill_me == 0 :
    Dpath = "D:\practice file\\tester2"
    dirdisplay(Dpath)

    user_input =  input(
         ''' hello !!
1. Create a file
2. Delete a file
3. Rename a file
        
        Enter here :'''
    )

    match user_input:
         case "1" : create_file(Dpath) 
         case "2" : delete_file(Dpath)
         case "3" : Rename_file(Dpath)
    
    loop_end = input("do you want to continue operations? (y/n): " )

    if loop_end == "n":
         kill_me = 1
    elif loop_end == "y":
         kill_me = 0
    




    


