#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 10:42:02 2017

@author: jdn93577
"""

class SpaceDict(object): # may need to inherit from somewhere
    
      def __init__(self):
        super(SpaceDict,self).__init__()
        
     
      def spaces_setup(self):
        spaces= {}
        spaces['tomo_raw']= {# checked once
                             'inheritance': None,
                             'axis_labels': 'detector_x, detector_y,rotation_angle',
                             'meta_data'  : 'dark, flat, angles',
                             'patterns'   : 'PROJECTION, SINOGRAM', # maybe want a dict here so can acces these individually 
                             'plugins'    : 'distortion_correction, dezing, correction',
                             'mappings'   : 'tomo' # have to do mapping to get to tomo as meta_data is different  
                             # what is definition of mapping tomo_raw to tommo seems v. diff to tomo to volume, 
                             # do we want to be able to map to all other spaces?
                             # use cases will tell us which spaces will need to map to where
                             }                          
        
        spaces['tomo']= {# checked once
                             'inheritance': None,
                             'axis_labels': 'detector_x, detector_y,rotation_angle',
                             'meta_data'  : 'angles' ,
                             'patterns'   : 'PROJECTION, SINOGRAM' ,
                             'plugins'    : None,
                             'mappings'   : 'volume'
                             }      
        
        spaces['volume']= {
                             'inheritance': None,
                             'axis_labels': 'volume_x, volume_y, rotation_angle',
                             'meta_data'  : None ,
                             'patterns'   :'VOLUME',
                             'plugins'    : None,
                             'mappings'   : None
                             }
            
        spaces['time_volume']= {
                             'inheritance': 'volume',
                             'axis_labels': 'scan',# inherits: volume_x, volume_y, rotation_angle,
                             'meta_data'  : None ,
                             'patterns'   :'TIMESERIES' ,# inherits: VOLUME
                             'plugins'    : None,
                             'mappings'   : None
                             }
        
        spaces['energy_time_volume']= {
                             'inheritance': 'time_volume',
                             'axis_labels': 'energy', # inherits: volume_x, volume_y, rotation_angle,
                             'meta_data'  : None ,
                             'patterns'   : None, # inherits: 'VOLUME, TIMESERIES' 
                             'plugins'    : None,
                             'mappings'   : None
                             }        
        
        
        spaces['time_tomo_raw']={ 
                             'inheritance': 'tomo_raw',
                             'axis_labels': 'scan', # inherits: detector_x, detector_y,rotation_angle,
                             'meta_data'  : None , # inherits: 'dark, flat , angles '
                             'patterns'   :'TIMESERIES', # inherits: PROJECTIONS, SINOGRAMS,
                             'plugins'    : None,
                             'mappings'   : None
                             }        

        spaces['time_tomo']= {
                             'inheritance': 'tomo',
                             'axis_labels': 'scan',#inherits: detector_x, detector_y,rotation_angle
                             'meta_data'  : None , # inherits 'angles'
                             'patterns'   :'TIMESERIES' , # inherits: PROJECTIONS, SINOGRAMS,
                             'plugins'    : None,
                             'mappings'   : None
                             }            
                             
        spaces['energy_tomo_raw']={ 
                             'inheritance': 'tomo_raw',
                             'axis_labels': 'energy', # inherits: detector_x, detector_y,rotation_angle,
                             'meta_data'  :  None,# inherits:'dark, flat, angles'
                             'patterns'   : None, # inherits: 'PROJECTIONS, SINOGRAMS
                             'plugins'    : None,
                             'mappings'   : None
                             }

        spaces['energy_tomo']= {
                             'inheritance': 'tomo',
                             'axis_labels': 'energy', # inherits: 'detector_x, detector_y,rotation_angle,
                             'meta_data'  : None ,# inherits: 'angles'
                             'patterns'   : None , #inherits: 'PROJECTIONS, SINOGRAMS'
                             'plugins'    : None,
                             'mappings'   : None
                             }
        spaces['energy_time_tomo_raw']= {
                             'inheritance':'time_tomo_raw',
                             'axis_labels':'energy', # inherits: detector_x, detector_y,rotation_angle, scan,
                             'meta_data'  : None , # imherits 'dark, flat, angles'
                             'patterns'   : None, # inherits 'PROJECTIONS, SINOGRAMS, TIMESERIES' 
                             'plugins'    : None,
                             'mappings'   : None
                             }
        
        spaces['energy_time_tomo']= {
                             'inheritance': 'time_tomo',
                             'axis_labels': 'energy', # inherits: detector_x, detector_y,rotation_angle, scan,
                             'meta_data'  : None , # inherits: 'angles'
                             'patterns'   : None ,# inherits: 'PROJECTIONS, SINOGRAMS, TIMESERIES'
                             'plugins'    : None,
                             'mappings'   : None
                             }
        
























