# CIS 4930
########### Contributors ###########
# Nipuna Weerapperuma
# Hannah Williams
# David Jaworski
# Carlos Morales-Diaz
# Spencer Bass

########### PyQT5 imports ###########
from PyQt5.QtGui import QFont, QPixmap, QTextCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QScrollArea, QVBoxLayout, \
    QSizePolicy, QTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, pyqtSignal
import configparser
from src.constants import CONFIG_FILE, assets

class UIHelpWindow(QWidget):
    def __init__(self, parent=None):
        super(UIHelpWindow, self).__init__(parent)
        self.setMinimumWidth(320)
        self.help_ui()

    def insertImageFunc(self, filepath, cursor):
        # grab image
        reader = QtGui.QImageReader(filepath)
        image = reader.read()

        # resize image
        resizedImage = image.scaled(400, 400, QtCore.Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # move the cursor
        cursor.movePosition(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)

        # add image
        cursor.insertImage(resizedImage)


    def help_ui(self):
        #self.mainLayout = QVBoxLayout()
        self.helpTextEditor = QTextEdit()
        self.helpTextEditor.setWindowTitle("Help")
        self.helpTextEditor.setMinimumSize(800,500)
        #self.mainLayout.addWidget(self.helpTextEditor)

        self.helpTextEditor.setReadOnly(True)

        self.helpTextEditor.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.document = self.helpTextEditor.document()
        self.cursor = QTextCursor(self.document)


        # Home Section
        self.helpTextEditor.setCurrentFont(QFont('Arial'))
        self.helpTextEditor.setFontUnderline(True)
        self.helpTextEditor.setFontPointSize(36)
        self.helpTextEditor.setText('Help')

        self.helpTextEditor.setCurrentFont(QFont('Arial'))
        self.helpTextEditor.setFontUnderline(False)
        self.helpTextEditor.setFontPointSize(10)

        self.helpTextEditor.append('\nWelcome to Lotus. This Help Page will introduce you to the main features of the Lotus Notes tool. \n\n')

        self.helpTextEditor.append('On the main hub screen, there are the three main options: (1) New Note, (2) Schedule, and (3) Previous Notes.\n')
        self.insertImageFunc(assets["help_lotus_home"], self.cursor)
        self.helpTextEditor.append('\n')

        # New Notes Section
        self.helpTextEditor.setCurrentFont(QFont('Arial'))
        self.helpTextEditor.setFontUnderline(True)
        self.helpTextEditor.setFontPointSize(24)
        self.helpTextEditor.append('New Notes')

        self.helpTextEditor.setCurrentFont(QFont('Arial'))
        self.helpTextEditor.setFontUnderline(False)
        self.helpTextEditor.setFontPointSize(10)
        self.helpTextEditor.append('\n')

        self.helpTextEditor.append(
            'By clicking on the New Notes button, a new window will appear which will contain a basic unscheduled note-taking window.\n')
        self.insertImageFunc(assets["help_new_notes_1"], self.cursor)
        self.helpTextEditor.append('\n')

        self.helpTextEditor.append('In the bottom taskbar, there are writing implements to choose from. '
                                   'By default, the pen icon on the far left is automatically selected.'
                                   'However, from left to right, the other options on that taskbar are eraser, highlighter, color wheel selector (for pen), undo, redo, clear all, and home.'
                                   'If a different option is selected, its icon will turn grey to visually signify the selection.\n')
        self.insertImageFunc(assets["help_new_notes_2"], self.cursor)
        self.helpTextEditor.append('\n')

        self.helpTextEditor.append('By clicking in the upper right of the canvas, you can type in a header. Once you finish one line in the header, you can click below that line to type another line. \n')
        self.insertImageFunc(assets["help_new_notes_3"], self.cursor)
        self.helpTextEditor.append('\n')

        self.helpTextEditor.append('The header is useful since it cannot be written over while taking notes. \n')
        self.insertImageFunc(assets["help_new_notes_4"], self.cursor)
        self.helpTextEditor.append('\n')

        self.helpTextEditor.append('Taking notes is as simple as drawing on your screen, either using a touchscreen or the mouse. '
                                   'Like mentioned above, you can also select a pen ink color by clicking the color wheel icon, which will pop up in a separate window. '
                                   'Your color choice is confirmed after clicked ok.'
                                   'You can also decrease or increase the pen tip size by pressing the "[" or "]" keys respectively. \n')
        self.insertImageFunc(assets["help_new_notes_5"], self.cursor)
        self.helpTextEditor.append('\n')
        self.insertImageFunc(assets["help_new_notes_6"], self.cursor)
        self.helpTextEditor.append('\n')

        self.helpTextEditor.append('Your notes can also be converted into a .txt text file by clicking under the OCR tab at the top of the window.'
                                   'This process, which is in beta, will only recognize very neatly drawn handwriting, so please use with this in mind. \n')
        self.insertImageFunc(assets["help_new_notes_7"], self.cursor)
        self.helpTextEditor.append('\n')

        self.helpTextEditor.append(
            'If not yet saved, Lotus will cue you to save your notes. The .txt file will be saved in the same directory as your notes image file. \n')
        self.insertImageFunc(assets["help_new_notes_8"], self.cursor)
        self.helpTextEditor.append('\n')
        self.insertImageFunc(assets["help_new_notes_9"], self.cursor)
        self.helpTextEditor.append('\n')

        self.helpTextEditor.append(
            'Lastly, a dialog box will appear which will display the text detected. \n')
        self.insertImageFunc(assets["help_new_notes_10"], self.cursor)
        self.helpTextEditor.append('\n')

        # Previous Notes Section
        self.helpTextEditor.setCurrentFont(QFont('Arial'))
        self.helpTextEditor.setFontUnderline(True)
        self.helpTextEditor.setFontPointSize(24)
        self.helpTextEditor.append('Previous Notes')

        self.helpTextEditor.setCurrentFont(QFont('Arial'))
        self.helpTextEditor.setFontUnderline(False)
        self.helpTextEditor.setFontPointSize(10)
        self.helpTextEditor.append('\n')

        self.helpTextEditor.append(
            'By clicking on the Previous Notes button, a new window will appear which will display all of the notes created by clicking the New Notes button and saving the canvas.\n')
        self.insertImageFunc(assets["help_previous_notes_1"], self.cursor)
        self.helpTextEditor.append('\n')

        self.helpTextEditor.append(
            'Clicking on the desired file will open it in a new notes window for you to edit further.\n')

        # Scheduled Notes Section
        self.helpTextEditor.setCurrentFont(QFont('Arial'))
        self.helpTextEditor.setFontUnderline(True)
        self.helpTextEditor.setFontPointSize(24)
        self.helpTextEditor.append('Scheduled Notes')

        self.helpTextEditor.setCurrentFont(QFont('Arial'))
        self.helpTextEditor.setFontUnderline(False)
        self.helpTextEditor.setFontPointSize(10)
        self.helpTextEditor.append('\n')

        self.helpTextEditor.append(
            'By clicking on the Schedule button, a new window will appear which allow the user to make scheduled notes. This is optimal for repeating events, such as classes.\n')
        #self.insertImageFunc(assets[" "], self.cursor)
        #self.helpTextEditor.append('\n')

        #self.helpTextEditor.append(
        #    'Clicking on the desired file will open it in a new notes window for you to edit further.\n')

        self.helpTextEditor.moveCursor(QtGui.QTextCursor.Start)
        self.helpTextEditor.show()
        #self.setLayout(self.mainLayout)