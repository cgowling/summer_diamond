import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.2

import '.'// imports the directory 

Screen {

    title: 'Review'
    hasNextButton: false
    hasCreateButton : true

     
    ListModel {
        id: myModel    
    }


    TableView {
        anchors.fill: parent

        TableViewColumn{
            role : 'label'
            width: 300
        }
        TableViewColumn{
            role : 'input'
            title: "User input "
            width: 300
            //delegate: TextEdit {anchors.fill: parent}
        }              
        model: myModel
    }
 
    
    function updateModel() {

        myModel.clear();  // doesn't seem to be clearing !??
        for (var key in GModel.pluginInfo) {
            if (GModel.pluginInfo.hasOwnProperty(key)) {
                myModel.append({label: key, input: GModel.pluginInfo[key]});

            }
        }
    }
}
     
    