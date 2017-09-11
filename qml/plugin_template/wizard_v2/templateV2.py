class Template:

      def write_template(self,plugin_info):

          modname = plugin_info["Plugin template name:"]
          modname = modname if len(modname.split('.py')) > 1 else modname + '.py'  
           
          with open(modname, 'a+') as f:
            
              with open('copyright.py') as input : 
                f.write(input.read())
                input.close
               
              f.write('"""\n.. module::')
              f.write(plugin_info["Plugin template name:"])
              f.write('\n   :platform: Unix\n   :synopsis:\n.. moduleauthor::')
              f.write (plugin_info["Your name:"])
              f.write(' <')
              f.write(plugin_info["Your e-mail:"])
              f.write('>\n\n"""\n')
                
              with open('imports.py') as input:
                f.write(input.read())
                input.close
               
              f.write('\nclass ')  
              f.write(plugin_info["Plugin class name:"]) 
              f.write('(Plugin, CpuPlugin):\n')
              
              with open('description.py') as input :
                f.write(input.read())
                input.close 
                        
              f.write('\n    def __init__(self):\n        super(')
              f.write(plugin_info["Plugin class name:"])
              f.write(', self).__init__("')
              f.write(plugin_info["Plugin class name:"])
              f.write('")\n\n')   
              
              with open('process_and_setup.py') as input :
                f.write(input.read())
                input.close           
              
              f.write("\n        if self.parameters['")
              f.write(plugin_info['Pattern 1'])
              f.write("']:\n            pattern = self.parameters['")
              f.write(plugin_info['Pattern 1'])
              f.write("']\n        else:\n            pattern = in_dataset[0].get_data_patterns().keys()[0]\n\n")
              
              with open('inout_setup.py') as input :
                f.write(input.read())
                input.close   
                
              f.write("\n\n    def nInput_datasets(self):\n        return ")  
              f.write(plugin_info['Number of in datasets '])
      
              f.write("\n\n    def nOutput_datasets(self):\n        return ")  
              f.write(plugin_info['Number of out datasets '])
                      
            
              
          f.close         

