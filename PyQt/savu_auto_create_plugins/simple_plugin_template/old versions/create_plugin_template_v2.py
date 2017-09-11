#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 10:12:15 2017

@author: jdn93577
"""

import sys
import PyQt5.QtWidgets as pw
import PyQt5.QtGui as pg


class Example(pw.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.dictionary = None
        self._setup_dictionary()
        self.initUI()
        
    def _setup_dictionary(self):
        self.dictionary = {}
        self.dictionary['mod'] = {'label':'plugin template name', 'name': None, 'edit': None, 'position':1}
        self.dictionary['user_name']= {'label':'Your name:', 'name': None, 'edit': None,'position':2}
        self.dictionary['e_mail'] = {'label':'Your e-mail:','name': None, 'edit': None, 'position':3}
        self.dictionary['pre_processing_selection']={'label':'preProcessingSelection','name': None, 'edit': None,'position':4,'processType':'self.preProcessSelection'}
        self.dictionary['filter']={'label':'Filter frames:','name': None, 'edit': None,'position':5}
        self.dictionary['post_processing_selection']={'label':'postProcessingSelection','name': None, 'edit': None,'position':6,'processType':'postProcessSelection'}        
        self.dictionary['number_of_inputs']={'label':'No. of input data sets:','name': None, 'edit': None,'position':7}
        self.dictionary['number_of_outputs']={'label':'No. of output data sets:','name': None, 'edit': None,'position':8}        
        
    def createTextBox(self,entry):
        entry['name'] = pw.QLabel(entry['label'])
        entry['edit'] = pw.QLineEdit()
        pg.grid.addWidget(entry['name'] , entry['position'], 0)
        pg.grid.addWidget(entry['edit'], entry['position'], 1)     
        
      
    def createDropdown(self,entry):
        entry['name'] = pw.QLabel(entry['label'])
        entry['edit'] = pw.QComboBox()        
        entry['edit'].addItems(['passed','pass2'])
        print(str(entry['processType']))
        entry['edit'].currentIndexChanged.connect(self.entry['label'])        
        pg.grid.addWidget(entry['name'],entry['position'],0)
        pg.grid.addWidget(entry['edit'],entry['position'],1)
        
        
        
    def initUI(self):# constructor        
        
        pw.QToolTip.setFont(pg.QFont('SansSerif', 10))
        
        pg.grid = pw.QGridLayout() #creates an empty grid with spacing 10 (gaps) between boxes
        pg.grid.setSpacing(10)
        
        self.createTextBox( self.dictionary['mod'])     
        self.dictionary['mod']['edit'].setToolTip('Input the name of the module you want to create. It must be of the form: plugin_template.py, i.e all lowercase and underscores instead of spaces with .py at the end')
        
        
        self.createTextBox(self.dictionary['user_name'])
      
        self.createTextBox(self.dictionary['e_mail'])
     
        self.createDropdown(self.dictionary['pre_processing_selection'])
       
        self.createTextBox(self.dictionary['filter'])
        
        self.createDropdown(self.dictionary['post_processing-selection'])
       
        self.createTextBox(self.dictionary['number_of_inputs'])

        self.createTextBox(self.dictionary['number_of_outputs'])
        
        
        qbtn = pw.QPushButton('Create plugin template', self)       
        qbtn.clicked.connect(self.CreateModule)
        qbtn.setToolTip('This is a creates a plugin template as a .py file ')	
  
        pg.grid.addWidget(qbtn, 9,0)
        
        self.setLayout(pg.grid)
        
        
        self.setGeometry(300, 300, 300, 200)# this sets up window don't do for each button 
        self.setWindowTitle('Create plugin template')    
        self.show() 
        
        
        
    def preProcessSelection(self,i):
        print(self.dictionary['pre_processing_selection']['edit'].currentText())
        print('doing pre-processing')
        self.dictionary['pre_processing_selection']['edit'].currentText()
        

      
    def postProcessSelection(self,i):
        print(self.dictionary['post_processing_selection']['edit'].currentText())
        print('doing post')
        self.dictionary['post_processing_selection']['edit'].currentText()
        
    
    def CreateModule(self): 
        y = self.dictionary['mod']['edit'].text()
        y = y if len(y.split('.py')) > 1 else y + '.py'
        f = open(y, 'w+')# creates ablank .py file i.e a new module. in the folder that it is run in 
        # w+ means read and write 
        f.write('#Copyright 2014 Diamond Light Source Ltd.\n#Licensed under the Apache License, Version 2.0 (the "License");\n# you may not use this file except in compliance with the License.\n# You may obtain a copy of the License at\n#\n#     http://www.apache.org/licenses/LICENSE-2.0\n#\n# Unless required by applicable law or agreed to in writing, software\n# distributed under the License is distributed on an "AS IS" BASIS,\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n# See the License for the specific language governing permissions and\n# limitations under the License.\n# $Id: dezing_filter.py 467 2016-02-16 11:40:42Z kny48981 $')
        f.write("""... module:: plugin_template\n:platform: Unix\n:synopsis: A template to create a plugin\n.. moduleauthor:: Developer Name <email@address.ac.uk>\n""")
        
      

        
if __name__ == '__main__':
    
    app = pw.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    