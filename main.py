import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

log = logging.getLogger(__name__)


def main():
    log.info('Tutaj zdarzyło się coś')


if __name__ == "__main__":
    main()
    app.run()
