import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.2



Screen {
    
    title: 'User info'
    hasBackButton: false
       
                
    Pg1Model{
        id: pg1_model
    }
      
    Component{
        id: pg1_model_Delegate

        RowLayout{
            id: row
            width: parent.width
            height: 30                      
            spacing: 50
            
            Text { 
                id : textLabel
                  Layout.fillWidth: true
                  height: parent.height
                  verticalAlignment: Text.AlignVCenter
                  text: label
            }   
            TextField {
                  id: textInput
                  implicitWidth: 300
                  height: parent.height                    
                  placeholderText: placeholder 
                  onTextChanged: pluginInfo(label,textInput.text)
            }
       
        }
    }
            
    ListView {// this combines the model in Content with the info in component 
        anchors.fill: parent
        model: pg1_model
        delegate: pg1_model_Delegate                      
    }
    //Component.onCompleted: console.log(elementInfo) just showing the property from Screen can be acsessed here 
}                      