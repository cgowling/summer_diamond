import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3


Rectangle{
    id: page1Container // can't anchor fill parent nto exactly its parent surely a better way of sizing 
    width: 600 //want it tobe same size as rectangle in core
    height: 400
    x:0   
    color: 'steel blue'

    Text{
        text: 'User info'
        anchors{horizontalCenter: page1Container.horizontalCenter; top: page1Container.top}
    } 
        
    ColumnLayout {
        id: columnlayout
        anchors{fill: parent; margins: 20}
            
        UserInfo{
            id: user_info
        }
          
        Component{
            id: user_infoDelegate
            
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
                      onEditingFinished: pluginInfo(n,label,text)
                }
            }
        }
                
        ListView {// this combines the model in Content with the info in component 
            anchors.fill: parent
            model: user_info
            delegate: user_infoDelegate                      
        }
    } 
    Button {
        id: butn11
        anchors{bottom: page1Container.bottom;right: page1Container.right; margins: 10}
        text: 'Next'
        onClicked:{
            pageLoader.source = "page2.qml"
            butn11.z = -1
        }    

    }     
}                      