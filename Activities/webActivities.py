# Import for the Web Bot
from botcity.web import WebBot
# Import webdriver_manager to automatically download the WebDriver binary
from webdriver_manager.chrome import ChromeDriverManager
# Import default_options to set the options for the WebDriver
from botcity.web.browsers.chrome import default_options
from decouple import config
import os

# This is the path to the Chrome profile you want to use-----
# you should go to the profile path in google chrome, copy it and create another folder in C:\BotCity\[project folder]\profile_chrome
profile_full_path = config('PROFILE_PATH')  

if not isinstance(profile_full_path, str):
    raise TypeError(f"PROFILE_PATH debe ser una cadena de texto, pero se obtuvo: {type(profile_full_path)}")
profile_directory_name = os.path.basename(profile_full_path)
user_data_dir_path = os.path.dirname(profile_full_path) 

print(f"Ruta completa del perfil: {profile_full_path}")
print(f"Directorio de datos de usuario (user_data_dir): {user_data_dir_path}")
print(f"Nombre del directorio del perfil (profile-directory): {profile_directory_name}")

def_options = default_options(
    headless=False,
    user_data_dir=user_data_dir_path  # Correcto: la ruta a "User Data"
)

# Agregar los argumentos
def_options.add_argument(f"--profile-directory={profile_directory_name}")
def_options.add_argument('--disable-gpu')
def_options.add_argument("--no-sandbox")
def_options.add_argument("--disable-dev-shm-usage")


# Initialize the WebBot instance
webbot             = WebBot()
# assigning the default options to the webbot instance
webbot.options     = def_options
print(f"WebBot options: {profile_full_path}")
# Configure whether or not to run on headless mode
webbot.driver_path = ChromeDriverManager().install()

#------------------------------------------------------------


# Open the browser and navigate to the URL
# This function opens the browser and navigates to the specified URL
def open_browser(url):
   webbot.browse(url)
   # Wait 3 seconds before closing
   webbot.wait(3000)  
   # Finish and clean up the Web Browser
   # You MUST invoke the stop_browser to avoid
   # leaving instances of the webdriver open
   #webbot.stop_browser()    
   return webbot

       
def wait_and_click(selector, by, wait_time=1000):
    try:
        element = webbot.find_element(selector=selector, by=by)
        if element:
            webbot.wait_for_element_visibility(element=element, visible=True, waiting_time=100000)
            webbot.wait(wait_time)
            element.click()
            return element
        else:
            return None
    except:
        return None

def wait_and_sendKeys(selector, by, wait_time=2000, value=None):
    try:
        element = webbot.find_element(selector=selector, by=by)
        if element:
            webbot.wait_for_element_visibility(element=element, visible=True, waiting_time=100000)
            webbot.wait(wait_time)
            element.clear()    
            element.send_keys(value)
            return element
        else:
            return None
    except:
        return None

     