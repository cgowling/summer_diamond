import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.2


Screen {

    title: 'Input data'
    
    onElementNoChanged : console.log('pg3')

    Component {
        id: multi_in_infoDelegate
        
        RowLayout {
            id: row
            width: parent.width
            height: 30                      
            spacing: 50
            
            Text { 
                  Layout.fillWidth: true
                  height: parent.height
                  verticalAlignment: Text.AlignVCenter
                  text: label
                  
            }                      
            
            ComboBox { 
                id: combo
                implicitWidth: 300
                height: parent.height
                visible : ptype == 1 
                model: ['pass as parameter', 'SINOGRAM', 'PROJECTION', 'TIMESERIES']
                onCurrentIndexChanged: pluginInfo( label, combo.currentText)
            }
            Button { 
                id : helpButton
                text: '?'
                visible : ptype == 1
                onClicked: help.visible = true 
                
            }
            
            MessageDialog {
                id: help
                title: 'Help'
                icon: StandardIcon.Question
                text: 'Plese input the Space of the input dataset, if determined at runtime selcet pass parameter.'         
                standardButtons: StandardButton.Ok
                onAccepted : visible = false
            
            }            
        }
    }

    ListView {
        anchors.fill: parent
        model: mymodel
        delegate: multi_in_infoDelegate
    }
        

    ListModel {
        id: mymodel
    }

       
    function addElements(n) {
        mymodel.clear();
        for ( var i = 0; i < n; i++ ) {
            mymodel.append({label: 'In dataset' + (i+1), ptype: 0});
            mymodel.append({label:'Pattern '+ (i+1), ptype: 1});
        }
    }
    Component.onCompleted: addElements(2)  //elementinfo          
    //Component.onCompleted: (addElements(handler.elementinfo))  //elementinfo   
}        
   