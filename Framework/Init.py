from Functions_and_classes.sys_context import general
from Framework.closeApplications import closeApp
import pandas as pd
from decouple import config

def init():
    str_message = ""
    try:
        if general.int_numRetry == 0:
           print("first run")
           # load variables
           closeApp()
           # Init applications       
           general.bol_systemException= False
        
    except Exception as e:
        print(f"An error occurred: {e} - {general.str_messageError}")         
        general.bol_systemException= True
    
        
    