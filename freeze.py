from click.decorators import password_option
from flask_frozen import Freezer
from PasswordReminder import app

freezer = Freezer(PasswordReminder)

if __name__ == '__main__':
    freezer.freeze()