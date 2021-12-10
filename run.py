from app import app
import os 

config_name = os.getenv('MYAPP_CONFIG')

if __name__ == "__main__":
    app.run(config_name)