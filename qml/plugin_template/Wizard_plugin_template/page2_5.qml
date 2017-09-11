import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3


Rectangle{
    id: page2_5Container 
    width: 600
    height: 400
    x:0
    color: 'steel blue'
    
    Text{
        text: 'Input dataset(s) info'
        anchors{horizontalCenter: page2_5Container.horizontalCenter; top: page2_5Container.top}
    }     
    
    ColumnLayout {
          id: container
          anchors{fill: parent; margins: 20}
          
          /*MultiInInfo {// list Model, contains content to fill component 
              id: multi_in_info
          }*/
                 
      
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
                  
                  TextField {
                        id: textfield
                        implicitWidth: 300
                        height: parent.height
                        visible: ptype == 0  // will appear if want it to soecified in InInfo
                        placeholderText: placeholder
                        onTextChanged: (n,label,text)
                  }
                  
                  ComboBox { 
                      id: combo
                      implicitWidth: 300
                      height: parent.height
                      visible: ptype == 1 
                      model: ['pattern', 'sinogram', 'projection', 'option4']
                      onCurrentIndexChanged: pluginInfo(currentIndex, label, currentText)

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
    }

    Button {
        id: butn251
        anchors{bottom: page2_5Container.bottom ; right: page2_5Container.right ; margins: 10}
        text: 'Next'
        
        onClicked: {
            pageLoader.source = "page3.qml"
            butn251.z = -1
        }
    }    
    
    Button {
        id: butn252
        anchors{bottom: page2_5Container.bottom ; left: page2_5Container.right ; margins: 10}
        text: 'Back'
        onClicked:{
            pageLoader.source = "page2.qml"
            butn252.z = -1
        }    
    }
        
    function addElements(n) {
        mymodel.clear();
        for ( var i = 0; i < n; i++ ) {
            mymodel.append({label: 'Label' + n, ptype: 1});
        }
    }
        
    Component.onCompleted: {
        addElements(5);
    }
}  