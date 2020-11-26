import os

CONFIG_FILE = os.path.join(os.path.abspath(os.path.dirname( __file__ )), 'data/config.ini')
SCHEDULE_FILE_PATH  = os.path.join(os.path.abspath(os.path.dirname( __file__ )), 'data/schedule.json')
SCHEDULED_NOTES_DIRECTORY = os.path.join(os.path.abspath(os.path.dirname( __file__ )), 'data/')
DIRECTORY_FILE = os.path.join(os.path.abspath(os.path.dirname( __file__ )), 'data/directories.txt')

########### Assets ###########
assets = {
    "logo": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/lotus.png'),
    "newNote": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/newNote.png'),
    "newNoteDarker": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/newNoteDarker.png'),
    "previousNotes": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/previousNotes.png'),
    "previousNotesDarker": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/previousNotesDarker.png'),
    "schedule": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/schedule.png'),
    "scheduleDarker": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/scheduleDarker.png'),
    "time_date" : os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/time_date.png'),
    "lato" : os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/Lato-Regular.ttf'),
    "logo_black" : os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/logo_black.png'),
    "settings" : os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/settings.png'),
    "pen" : os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/pen.png'),
    "eraser" : os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/eraser.png'),
    "highlighter" : os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/highlighter.png'),
    "undo" : os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/undo.png'),
    "redo" : os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/redo.png'),
    "clear" : os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/clear.png'),
    "home" : os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/home.png'),
    "color_wheel" : os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/color_wheel.png'),
    "color_indicator" : os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/color_indicator.png'),
    "help": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/help.png'),
    "help_lotus_home": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/help_lotus_home.jpg'),
    "help_new_notes_1": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/help_new_notes_1.jpg'),
    "help_new_notes_2": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/help_new_notes_2.jpg'),
    "help_new_notes_3": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/help_new_notes_3.jpg'),
    "help_new_notes_4": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/help_new_notes_4.jpg'),
    "help_new_notes_5": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/help_new_notes_5.jpg'),
    "help_new_notes_6": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/help_new_notes_6.jpg'),
    "help_new_notes_7": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/help_new_notes_7.jpg'),
    "help_new_notes_8": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/help_new_notes_8.jpg'),
    "help_new_notes_9": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/help_new_notes_9.jpg'),
    "help_new_notes_10": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/help_new_notes_10.jpg'),
    "help_previous_notes_1": os.path.join(os.path.abspath(os.path.dirname(__file__)), 'assets/help_previous_notes_1.jpg')

}