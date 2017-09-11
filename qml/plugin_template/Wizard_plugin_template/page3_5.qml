import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3


Rectangle{
    id: page3_5Container 
    width: 600
    height: 400
    x:0
    color: 'steel blue'
    
    Text{
        text: 'Output dataset(s) info'
        anchors{horizontalCenter: page3_5Container.horizontalCenter; top: page3_5Container.top}
    }      
    
    ColumnLayout {
          id: container
          anchors{fill: parent; margins: 20}
          
          MultiOutInfo{// list Model, contains content to fill component 
              id: multi_out_info
          }
      
          Component {
              id: multi_out_infoDelegate
              
              RowLayout {
                  id: row
                  width: parent.width
                  height: 30                      
                  spacing: 50
                  
                  Text { 
                        Layout.fillWidth: true
                        height: parent.height
                        verticalAlignment: Text.AlignVCenter
                        text:label
                        
                  }                      
                  
                  TextField {
                        id: textfield
                        implicitWidth: 300
                        height: parent.height
                        visible: ptype == 0  // will appear if want it to soecified in InInfo
                        placeholderText: placeholder
                        onTextChanged: pluginInfo(n,label,text)
                  }
                  
                  ComboBox { 
                      id: combo
                      implicitWidth: 300
                      height: parent.height
                      visible: ptype ==1 
                      model: [option1 , option2, option3,option4]
                      onCurrentIndexChanged: pluginInfo(currentIndex, label, currentText)

                  }
              }
          }
      
          ListView {
              anchors.fill: parent
              model: multi_out_info
              delegate: multi_out_infoDelegate
          }
    }

    Button {
        id: butn351
        anchors{bottom: page3_5Container.bottom ; right: page3_5Container.right ; margins: 10}
        text: 'Next'
        onClicked: {
            pageLoader.source = "page4.qml"
            butn351.z = -1
        }
    }    
    
    Button {
        id: butn352
        anchors{bottom: page3_5Container.bottom ; left: page3_5Container.right ; margins: 10}
        text: 'Back'
        onClicked:{
            pageLoader.source = "page3.qml"
            butn352.z = -1
        }    
        

    }          
} 