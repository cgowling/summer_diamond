import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3


Rectangle{
    id: page3Container
    width: 600
    height: 400
    x:0   
    color: 'steel blue'    
    
    property bool morethan2: false   
    
    Text{
        text: 'Number of output datasets'
        anchors{horizontalCenter: page3Container.horizontalCenter; top: page3Container.top}
    }        
    
    ColumnLayout {
          anchors{fill: parent; margins: 20}
          
          NoOutInfo{
              id: no_out_info
          }
          Component {
              id: no_out_infoDelegate
              
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
                        
                        onTextChanged: {
                            pluginInfo(n,label,text)
                            morethan2 = parseInt(textfield.text) >= 2;
                        }
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
              model: no_out_info
              delegate: no_out_infoDelegate
          }
    }
          
    Button {
        id: butn31
        text: 'Next'
        onClicked:{
            if ( morethan2 ) {
                pageLoader.source = 'page3_5.qml'   //nextPage    
            } else {
                pageLoader.source = 'page4.qml'   //nextPage    
            }             

            butn31.z = -1
        }    
        anchors.bottom: page3Container.bottom
        anchors.right: page3Container.right
        anchors.margins: 10

    }         
    Button {
        id: butn32
        text: 'Back'
        onClicked:{
            pageLoader.source = "page2.qml"
            butn32.z = -1
        }    
        anchors.bottom: page3Container.bottom
        anchors.left: page3Container.left
        anchors.margins: 10

    }        
}     
    
    
