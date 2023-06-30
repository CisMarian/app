from flask_app import create_app
from app.localconfig import Config
import localconfig


config = Config()
application = create_app(localconfig.config)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
