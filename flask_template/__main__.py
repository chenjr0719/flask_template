from flask_template import app
from flask_template import views
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--debug", default=False, action="store_true",
    )
    args = parser.parse_args()

    app.run(debug=args.debug)
