from flask_app import create_app
from app import localconfig


application = create_app(localconfig.Config())

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=7002)
