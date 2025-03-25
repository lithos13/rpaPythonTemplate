from functions_and_classes.sys_context import general
import pandas as pd

def init():
    str_message = ""
    try:
        # load variables
        # init applications

        print("Initializing process...")
        print("first run")
        
        general.bol_systemException= False
        
    except Exception as e:
        print(f"An error occurred: {e}")        
        general.bol_systemException= True
    
        
    