#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 10:12:15 2017

@author: jdn93577
"""

import sys
import PyQt5.QtWidgets as pw
import PyQt5.QtGui as pg
import shutil 



class PluginTemplateCreator(pw.QWidget):
    
    def __init__(self):
        super(PluginTemplateCreator, self).__init__()
        self.dictionary = None
        self._setup_dictionary()
        self.initUI()
        
    def _setup_dictionary(self):
        self.dictionary = {}
        self.dictionary['mod'] = {'label':'plugin template name', 'edit': None, 'position':1}
        self.dictionary['user_name']= {'label':'Your name:',  'edit': None,'position':2}
        self.dictionary['e_mail'] = {'label':'Your e-mail:', 'edit': None, 'position':3}
        self.dictionary['pre_processing_selection']={'label':'preProcessingSelection','edit': None,'position':4}
        self.dictionary['process']={'label':'process:', 'edit': None,'position':5}
        self.dictionary['post_processing_selection']={'label':'postProcessingSelection', 'edit': None,'position':6}        
        self.dictionary['number_of_inputs']={'label':'No. of input data sets:', 'edit': None,'position':7}
        self.dictionary['number_of_outputs']={'label':'No. of output data sets:', 'edit': None,'position':8}        
        
    def createTextBox(self,entry):
        #entry['edit'] = pw.QLineEdit()# when textBox is edited it will add th entry to the detup_dictionary
        pg.grid.addWidget(pw.QLabel(entry['label'] ), entry['position'], 0)
        pg.grid.addWidget(pw.QLineEdit(entry['edit']), entry['position'], 1)     
        
      
    def createDropdown(self,entry):
        entry['edit'] = pw.QComboBox()        
        entry['edit'].addItems(['pass','process'])
        pg.grid.addWidget(pw.QLabel(entry['label']),entry['position'],0)
        pg.grid.addWidget(entry['edit'],entry['position'],1)
    

        
    def initUI(self):# constructor deals with the layout of the GUI
        
        pw.QToolTip.setFont(pg.QFont('SansSerif', 10))
        
        pg.grid = pw.QGridLayout() 
        pg.grid.setSpacing(10)
        
        self.createTextBox( self.dictionary['mod'])     
        self.dictionary['mod']['edit'].setToolTip('Input the name of the module you want to create.\n It must be of the form: plugin_template.py,\n i.e all lowercase and underscores instead of spaces with .py at the end')
        
        self.createTextBox(self.dictionary['user_name'])
      
        self.createTextBox(self.dictionary['e_mail'])
     
        self.createDropdown(self.dictionary['pre_processing_selection'])
       
        self.createDropdown(self.dictionary['process'])
        
        self.createDropdown(self.dictionary['post_processing_selection'])
       
        self.createTextBox(self.dictionary['number_of_inputs'])

        self.createTextBox(self.dictionary['number_of_outputs'])
        
        
        qbtn = pw.QPushButton('Create plugin template', self)       
        qbtn.clicked.connect(self.CreateModule)
        qbtn.setToolTip('This is a creates a plugin template as a .py file ')	
  
        pg.grid.addWidget(qbtn, 9,0)
        
        self.setLayout(pg.grid)
        
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Create plugin template')    
        self.show() 
        
      
    # This function deals with writing the plugin template, using the input from the user 
    def CreateModule(self): 
        modname = self.dictionary['mod']['edit'].text()
        modname = modname if len(modname.split('.py')) > 1 else modname + '.py'  
        
        print(self.dictionary)
        
        with open(modname, 'a+') as f:
             shutil.copyfile('intro.py',modname)
             # still need to see if i can add to a specific line so can add name and email 
             f.write('\n\n    def pre_process(self):\n       ')
             f.write(self.dictionary['pre_processing_selection']['edit'].currentText())
             
             f.write('\n\n    def process_frames(self,data):\n       ')
             f.write(self.dictionary['process']['edit'].currentText())
             
             f.write('\n\n    def post_process(self):\n       ')
             f.write(self.dictionary['post_processing_selection']['edit'].currentText())
             
             f.write('\n\n    def setup(self):\n       pass')
             f.write('\n\n    def nInput_datasets(self):\n       return ')
             
             f.write( self.dictionary['number_of_inputs']['edit'].text())
             f.write('\n\n    def nOutput_datasets(self):\n       return ')
             
             f.write( self.dictionary['number_of_outputs']['edit'].text())  
             f.write("\n\n    def get_max_frames(self):\n       return 'multiple'")
             shutil.copyfile('intro.py',modname)

        f.close


# creates the GUI window, with specifications given above 
        
if __name__ == '__main__':
    
    app = pw.QApplication(sys.argv)
    ex = PluginTemplateCreator()
    sys.exit(app.exec_())
    
