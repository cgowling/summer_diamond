#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 10:42:02 2017

@author: jdn93577
"""

import copy

class SpaceDict(): # may need to inherit from somewhere
     


    def __init__(self):
      self.space = {}


    def update_dict(self, entry, inheritance, axis_labels,n1,metadata,patterns,n2):
      self.space[entry] = copy.deepcopy(self.space[inheritance])
      self.space[entry]['inheritance'] = inheritance
      self.space[entry]['axis_labels'][n1]= axis_labels
      self.space[entry]['patterns'][n2] = patterns
      return self.space[entry]
        
    def get_dict(self):
        self.space= {}
        self.space['tomo_raw']= {# checked once
                             'inheritance': None,
                             'axis_labels': {'first':'detector_x','second':'detector_y','third':'rotation_angle'},
                             'meta_data'  : {'first':'dark','second': 'flat','third': 'angles'},
                             'patterns'   : {'first':'PROJECTION','second':' SINOGRAM'}, 
                             'plugins'    : 'distortion_correction, dezing, correction',
                             'mappings'   : 'tomo' # have to do mapping to get to tomo as meta_data is different            
                             # use cases will tell us which spaces will need to map to where
                             }                          
    
        self.space['tomo']= {# checked once
                             'inheritance': None,
                             'axis_labels': {'first':'detector_x','second':'detector_y','third':'rotation_angle'},
                             'meta_data'  : {'first':'angles'} ,
                             'patterns'   : {'first':'PROJECTION','second':' SINOGRAM'} ,
                             'plugins'    : None,
                             'mappings'   : 'volume'
                             }      
        
        self.space['volume']= {
                             'inheritance': None,
                             'axis_labels': {'first':'volume_x','second':'volume_y','third':'rotation_angle'},
                             'meta_data'  : None ,
                             'patterns'   :{'first':'VOLUME'},
                             'plugins'    : None,
                             'mappings'   : None
                             }
        
        self.update_dict('time_volume','volume','scan','fourth',None,'TIMESERIES','second')
            
        
        self.update_dict('energy_time_volume','time_volume','energy','fifth',None,None, None)
      

        self.update_dict('time_tomo_raw','tomo_raw','scan','fourth',None,'TIMESERIES','third')   

        
        self.update_dict('time_tomo','tomo','scan','fourth',None,'TIMESERIES','third')
        
        
        self.update_dict('energy_tomo_raw','tomo_raw','energy','fourth',None,None,None)

        
        self.update_dict('time_tomo','tomo','scan','fourth',None,'TIMESERIES','third')


        self.update_dict('energy_tomo','tomo','energy','fourth',None,None,None)
                  
           
        self.update_dict('energy_time_tomo','time_tomo','energy','fifth',None,None,None)
        
        
        self.update_dict('energy_time_tomo_raw','time_tomo_raw','energy','fifth',None,None,None)        


        return self.space
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        









