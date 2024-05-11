import os
import dotenv

dotenv.load_dotenv( )

### Get Environment Variables 
DRIVER = os.getenv('PROJECT_DRIVER')
SERVER = os.getenv('PROJECT_SERVER')
DATABASE = os.getenv('PROJECT_DATABASE')
USERNAME = os.getenv('PROJECT_USERNAME')
PASSWORD = os.getenv('PROJECT_PASSWORD')