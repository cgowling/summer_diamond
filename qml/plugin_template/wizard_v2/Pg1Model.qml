import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3

ListModel{
    id: pg1_model  
    
    ListElement {
        label:"Plugin template name:"
        placeholder: "Must be of the form: plugin_name.py "
    }
    ListElement {
        label:"Plugin class name:"
        placeholder: "Must be of the form: PluginName "
    } 
    ListElement {
        label:"Your name:"
        placeholder: ""
    } 
    ListElement {
        label:"Your e-mail:"
        placeholder:""
    }     
    ListElement {
        label:"Plugin description:"
        placeholder: 'optional,may not have this option'
    }     
    
}