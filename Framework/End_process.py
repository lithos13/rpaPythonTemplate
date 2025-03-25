from functions_and_classes.context import general

def end_process():
    if general.bol_systemException:
        print("System exception occurred. Process stopped.")
    else:   
        print("Process finished.")
    