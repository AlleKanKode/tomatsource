# poetry add python-dotenv
from dotenv import dotenv_values, load_dotenv
import os


if __name__ == "__main__":
    
    '''
    Sætter OS environment variabler fra .env filen 
    '''
    #load_dotenv()
    #print(os.getenv("DEV_TOKEN"))

    config = dotenv_values("/.env")
    print (config)