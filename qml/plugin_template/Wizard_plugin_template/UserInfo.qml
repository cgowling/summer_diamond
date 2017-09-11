import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3

ListModel{
    id:user_info 
    
    ListElement {
        label:"Plugin template name:"
        placeholder: "Must be of the form: plugin_name.py "
        n: 1 
    }
    ListElement {
        label:"Plugin class name:"
        placeholder: "Must be of the form: PluginName "
        n: 2
    } 
    ListElement {
        label:"Your name:"
        placeholder: ""
        n: 3
    } 
    ListElement {
        label:"Your e-mail:"
        placeholder:""
        n: 4
    }     
    ListElement {
        label:"Plugin description:"
        placeholder: 'optional'
        n: 5
    }     
    
}