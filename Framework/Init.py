from functions_and_classes.context import general

def init():
    str_message = ""
    try:
        # Your code logic here
        print("Initializing process...")
        print("first run")
        print(20/0)
        general.bol_systemException= False
        
    except Exception as e:
        print(f"An error occurred: {e}")        
        general.bol_systemException= True
    
        
    