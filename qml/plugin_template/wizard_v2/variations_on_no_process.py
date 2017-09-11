"""
no process trying to map out different possibilties for no space change (i.e no mappings) 
"""


# Copyright 2014 Diamond Light Source Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. module::MODNAME
   :platform: Unix
   :synopsis: Plugin to test loading and saving without processing
.. moduleauthor:: USERNAME  USEREMAIL

"""
from savu.plugins.plugin import Plugin
from savu.plugins.utils import register_plugin
from savu.plugins.driver.cpu_plugin import CpuPlugin


@register_plugin
class PLUGINCLASSNAME(Plugin, CpuPlugin):
    """
    THE USER CAN WRITE THINGS IN HERE LATER
    The base class from which all plugins should inherit.
    :u*param pattern: Explicitly state the slicing pattern. Default: None.
    :param dummy: Dummy parameter for testing. Default: 10.
    """

    def __init__(self):
        super(PLUGINCLASSNAME, self).__init__("PLUGINCLASSNAME")
    
"""
    def get_plugin_pattern(self):
        return ''

"""    

    def process_frames(self, data):
        pass
 
    def setup(self):     
        """
        Initial setup of all datasets required as input and output to the
        plugin.  This method is called before the process method in the plugin
        chain.
        """
        in_dataset, out_dataset = self.get_datasets()
        out_dataset[0].create_dataset(in_dataset[0])
        in_pData, out_pData = self.get_plugin_datasets() # if space/ pattern hange this bit would be difff ??
        
        
"""
        in_meta_data = in_dataset[0].meta_data

"""        
        
"""
 options 

        if self.parameters['pattern']:
            pattern = self.parameters['pattern']
        else:
            pattern = in_dataset[0].get_data_patterns().keys()[0]
#

        if 'pattern' in self.parameters.keys():
            pattern = self.parameters['pattern']
        else:
            pattern = 'PROJECTION'
#
        plugin_pattern = self.get_plugin_pattern()
        
"""        
        in_pData[0].plugin_data_setup(pattern, self.get_max_frames())
        out_pData[0].plugin_data_setup(
                pattern, in_pData[0]._get_max_frames_process()        
  


      
    def get_max_frames(self):
        return 'USERMAXFRAME CHOICE'

    def nInput_datasets(self):
        return 'USERnIN CHOICE'

    def nOutput_datasets(self):
        return 'USERnOUT CHOICE' 
    