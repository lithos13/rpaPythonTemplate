from functions_and_classes.sys_bussinesException import BusinessException


def process():
    try:
        # Your main process logic here
        print("Executing process...")
        # Example: raise BusinessException("A business error occurred")
        # Example: raise Exception("A system error occurred")
    except BusinessException as be:
        # Handle business exceptions
        print(f"Business exception caught: {be}")
    except Exception as e:
        # Handle system exceptions
        print(f"System exception caught: {e}")
    finally:
        # Cleanup or finalization code
        print("Process finished.")

