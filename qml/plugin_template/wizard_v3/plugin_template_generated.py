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
.. module::plugin_template_generated
   :platform: Unix
   :synopsis:
.. moduleauthor::Chloe Gowling <@diamond.ac.uk>

"""
from savu.plugins.plugin import Plugin
from savu.plugins.utils import register_plugin
from savu.plugins.driver.cpu_plugin import CpuPlugin


@register_plugin
class PluginTemplateGenerated(Plugin, CpuPlugin):
    """
    A plugin template # put your description in here 

    :param example: Example of a plugin parameter. Default: None.

    """
    def __init__(self):
        super(PluginTemplateGenerated, self).__init__("PluginTemplateGenerated")

    def pre_process(self):
        """ This method is called immediately after base_pre_process(). """
        pass  


    def process_frames(self, data):
        """
        This method is called after the plugin has been created by the
        pipeline framework and forms the main processing step

        :param data: A list of numpy arrays for each input dataset.
        :type data: list(np.array)
        """
        pass

    def post_process(self):
        """
        This method is called after the process function in the pipeline
        framework as a post-processing step. All processes will have finished
        performing the main processing at this stage.

        :param exp: An experiment object, holding input and output datasets
        :type exp: experiment class instance
        """
        pass

    def setup(self):
        """
        Initial setup of all datasets required as input and output to the
        plugin.  This method is called before the process method in the plugin
        chain.
        """
        in_dataset, out_dataset = self.get_datasets()
  
        out_dataset[0].create_dataset(in_dataset[0])
        out_dataset[1].create_dataset(in_dataset[1])

        in_pData, out_pData = self.get_plugin_datasets()

        in_pData[0].plugin_data_setup('SINOGRAM',SINOGRAM)
        out_pData[0].plugin_data_setup('SINOGRAM','multiple')

        in_pData[1].plugin_data_setup('PROJECTION',SINOGRAM)
        out_pData[1].plugin_data_setup('SINOGRAM','multiple')



    def nInput_datasets(self):
        return 2

    def nOutput_datasets(self):
        return 2