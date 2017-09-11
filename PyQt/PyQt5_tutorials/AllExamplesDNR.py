dul#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:12:11 2017

@author: jdn93577
"""
# tooltip and button 
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,QPushButton, QApplication)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont  

class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):# constructor
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget') # gives info when you hover over
        btn.resize(btn.sizeHint())# gives a recommended size for the button
        btn.move(50, 100)       
        

        
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 20)       
        
        self.statusBar().showMessage('Ready')
        
        
        self.setGeometry(300, 300, 300, 200)# this sets up window don't do for each button 
        self.setWindowTitle('Multiple Buttons')    
        self.show()    

        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

#%%
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
#NOTE seems to have window icon even if you dont do this  AMENDED has to be in right path !!!!

# This bit creates a window with an icon in the corner
# in object orientated programming style 

class Example(QWidget):
#the above creates a new class  which inherits from Qwidgets 
# => calls two CONSTRUCTORS, super returns parent object of Example, we then call the constructor see init     
    
    def __init__(self):
        super(Example, self).__init__()# init is a constructor NOTE: super requires argument if in Py 2
        
        self.initUI()# the initUI method creates the GUI
        
        
    def initUI(self):
        
        self.setGeometry(300, 300, 300, 220)#(x,y,w,h)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))# file is the image you want   NOT actually doing anything right now ??    
    
        self.show()
        

        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_()) 
#%%
# ASks the user if they are sure they want to exit 
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):
    
    def __init__(self):
        super(Example,self).__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('Message box')    
        self.show()
        
        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
#%%
# creates a text editor, has a drop down to quit or a quit button on the toolbar
#also a text editor widget 

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    
    def __init__(self):
        super(Example,self).__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit) # makes te central widget a text editor

        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar() # adds a status bar 

        menubar = self.menuBar() # this section is creating a drop dopwn menu 
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit') # sets a toolbar for frequently used actions 
        toolbar.addAction(exitAction)
        
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
  
#%%

# fix the buttons in eltion to the window so the scale with it

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        #creates two buttons 
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()# horizontal box layout
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox) # NOTE have added h layout to vertical 
        
        self.setLayout(vbox)# sets the main layout of the window  
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
#%%
# slider cahnging vaule 
#creates a slider 
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
    QVBoxLayout, QApplication)


class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        lcd = QLCDNumber(self) # gets number from slider ??
        sld = QSlider(Qt.Horizontal, self)# creates a horizontal slider 

        vbox = QVBoxLayout() # vertical box layout
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox) 
        sld.valueChanged.connect(lcd.display)# when slider value changes connect this to lcd display output 
        
        self.setGeometry(400, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
#%%
# asign event keys 
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()
        
        
    def keyPressEvent(self, e):# defines an eventy key 
        
        if e.key() == Qt.Key_Escape:# Key_Escape selcets key e.g could have F1 
            self.close()# closes window if escape key is pressed
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


    
#%% 
#Informing the user that an event was called
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):
    
    def __init__(self):
        super(Example,self).__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)
        
        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)
      
        btn1.clicked.connect(self.buttonClicked)# when the button is clicked it calls buttonClicked          
        btn2.clicked.connect(self.buttonClicked)
        
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()
        
        
    def buttonClicked(self):# the thing that has been clicked is passes here 
      
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed') #shows which button was pressed 
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

#%%
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

#QObject and pyqtSignal are teh new things here 

class Communicate(QObject): # Note communicate NOT Example 
    
    closeApp = pyqtSignal() # a signal is created 
    

class Example(QMainWindow):
    
    def __init__(self):
        super(Example,self).__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.c = Communicate()
        self.c.closeApp.connect(self.close)   # we are defining  a close window signal called closeApp which is connectedt to the close command
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()
        
        
    def mousePressEvent(self, event):
        
        self.c.closeApp.emit()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

#%%
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, 
    QInputDialog, QApplication)


class Example(QWidget):
    
    def __init__(self):
        super(Example,self).__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)# calls show dialog
        
        self.le = QLineEdit(self)# text edit box that will recieve info from the dialog box 
        self.le.move(130, 22)
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()
        
        
    def showDialog(self):
        
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        
        if ok:
            self.le.setText(str(text))
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
#%%
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, 
    QColorDialog, QApplication)
from PyQt5.QtGui import QColor


class Example(QWidget):
    
    def __init__(self):
        super(Example,self).__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        col = QColor(0, 0, 0) # sets initial colour to black

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" 
            % col.name())
        self.frm.setGeometry(130, 22, 100, 100)            
        
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()
        
        
    def showDialog(self):
      
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                % col.name())
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
#%%
#creates a font editing tool has a piece of text whixh the user can change the font. 
import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
    QSizePolicy, QLabel, QFontDialog, QApplication)


class Example(QWidget):
    
    def __init__(self):
        super(Example,self).__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)# creates dialog button 
        btn.setSizePolicy(QSizePolicy.Fixed,
            QSizePolicy.Fixed)
        
        btn.move(20, 20)# positions buttton

        vbox.addWidget(btn) # adds button to the  vbox layout

        btn.clicked.connect(self.showDialog)# sets up a response  if the button is clicked 
        
        self.lbl = QLabel('Knowledge only matters', self)# creates a label willl just appear in widget
        self.lbl.move(130, 20)# positions widet

        vbox.addWidget(self.lbl) # adds label to the vbox layout 
        self.setLayout(vbox)# creates layout     
        
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()
        
        
    def showDialog(self):

        font, ok = QFontDialog.getFont() # this calls the font editing window when ok is clicked then the font is set and selection window is clsed
        if ok:
            self.lbl.setFont(font)
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
#%%
#check box that chnges the title 
import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt


class Example(QWidget):
    
    def __init__(self):
        super(Example,self).__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        cb = QCheckBox('Show title', self)# creates a check box 
        cb.move(20, 20) #positions it 
        cb.toggle()# checks the box initially
        cb.stateChanged.connect(self.changeTitle)# concets the user defined changeTitle method to the state changed signal 
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()
        
        
    def changeTitle(self, state):
      
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
#%%
#creates a slider that changes the value of something  changes volume so changes picture label as gets louder
import sys
from PyQt5.QtWidgets import (QWidget, QSlider, 
    QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        sld = QSlider(Qt.Horizontal, self)#creates slider
        sld.setFocusPolicy(Qt.NoFocus) #??
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)#connects to the user defined changeValue
        
        self.label = QLabel(self)# creates a label widget with the following image 
        self.label.setPixmap(QPixmap('mute.png'))
        self.label.setGeometry(500, 10, 500, 100)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()
        
        
    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('vol.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('vol.png'))
        else:
            self.label.setPixmap(QPixmap('vol.png'))
            

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_()) 
#%%
#progess bar 
import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):
    
    def __init__(self):
        super(Example,self).__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.pbar = QProgressBar(self)# creates
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)# creates
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)# connects to user defined doAction

        self.timer = QBasicTimer()# creates a timer 
        self.step = 0# sets initial time
        
        self.setGeometry(300, 300, 280, 170)# ceates window 
        self.setWindowTitle('QProgressBar')
        self.show()
        
        
    def timerEvent(self, e):# what does the e mean ?? 
      
        if self.step >= 100: #when reaches 100% will say finished  
            self.timer.stop()
            self.btn.setText('Finished')# changes the text on the the button when finished 
            return
            
        self.step = self.step + 1 #adds a step on 
        self.pbar.setValue(self.step) # sets the progress bar vaue to the  timer 
        

    def doAction(self):
      
        if self.timer.isActive(): #not sure what this bt is doing 
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
#%% DROP DOWN MENU 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class combodemo(QWidget):
   def __init__(self, parent = None):
      super(combodemo, self).__init__(parent)
      
      layout = QHBoxLayout()
      self.cb = QComboBox()
      self.cb.addItem("pass")
      self.cb.addItem("C++")
      self.cb.addItems(["Java", "C#", "Python"])
      self.cb.currentIndexChanged.connect(self.selectionchange)
		
      layout.addWidget(self.cb)
      self.setLayout(layout)
      self.setWindowTitle("combo box demo")

   def selectionchange(self,i):
      print "Items in the list are :"
		
      for count in range(self.cb.count()):
         print self.cb.itemText(count)
      print "Current index",i,"selection changed ",self.cb.currentText()
		
def main():
   app = QApplication(sys.argv)
   ex = combodemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
