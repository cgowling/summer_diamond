import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3

ApplicationWindow {

    id: mainWindow

    width: 750
    height: 400
    
    signal communicating() 
    signal pluginInfo(int idx, string attr, variant value)
    signal createTemplate()
    //onPluginInfo: console.log(attr,value)  
 
    //Material.primary: Material.Indigo;
    //Material.accent: Material.Turquoise;
    
    Rectangle {
        id: top 
        width: 550
        height: 400
        x:150 
                 
        Loader {
            id: pageLoader
            source: 'page1.qml'
        }
    }
}                
