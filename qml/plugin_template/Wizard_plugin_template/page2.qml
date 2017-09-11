import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3


Rectangle{
    id: page2Container 
    width: 600
    height: 400
    x:0
    color: 'steel blue'
    
    property bool morethan2: false

    Text{
        text: 'Number of input datasets'
        anchors{horizontalCenter: page2Container.horizontalCenter; top: page2Container.top}
    } 
            
    
    ColumnLayout {
          id: container
          anchors{fill: parent; margins: 20}
          
          NoInInfo{// list Model, contains content to fill component 
              id: no_in_info
          }
      
          Component {
              id: no_in_infoDelegate
              
              RowLayout {
                  id: row
                  width: parent.width
                  height: 30                      
                  spacing: 50
                  
                  Text { 
                        id: text 
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
                            
                            morethan2 = parseInt(textfield.text) >= 2;
                            //console.log(parseInt(textfield.text));
                            pluginInfo(n,label,textfield.text)
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
              model: no_in_info
              delegate: no_in_infoDelegate
          }
    }

    Button {
        id: butn21
        text: 'Next'
        anchors{bottom: page2Container.bottom; right: page2Container.right; margins: 10}
        onClicked: {
            if ( morethan2 ) {
                pageLoader.source = 'page2_5.qml'     
            } else {
                pageLoader.source = 'page3.qml'    
            } 
            butn21.z = -1
        }
    }    
    
    Button {
        id: butn22
        text: 'Back'
        onClicked:{
            pageLoader.source = "page1.qml"
            butn22.z = -1
        }    
        anchors{bottom: page2Container.bottom; left: page2Container.left; margins: 10}
    }          
}  
        
        








