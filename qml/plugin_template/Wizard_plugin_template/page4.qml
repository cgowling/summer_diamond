import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3


Rectangle{
    id: page4Container
    width: 600
    height: 400
    x:0   
    color: 'steel blue'

    
    Text{
        text: 'Review'
        anchors{horizontalCenter: page4Container.horizontalCenter; top: page4Container.top}
    }          
    ColumnLayout {
          anchors{fill: parent; margins: 20;bottomMargin: 40}


          CollectedInfo {// this is the list Model
              id: collected_info
          }
      

          TableView {
              anchors.fill: parent
              //width: page4Container.parent.width

              __verticalScrollBar.visible: false
              __horizontalScrollBar.visible: false              
              
              TableViewColumn{
                  role : 'label'
                  width: 300
              }
              TableViewColumn{
                  role : 'input'
                  width: 300
                  //delegate: TextEdit {anchors.fill: parent}
              }              
            model: collected_info
          }
       
    }
              
    Button {
        id: butn41
        activeFocusOnPress: true
        text: "Create template"
        onClicked: createTemplate()
        anchors.bottom: page4Container.bottom
        anchors.right: page4Container.right
        anchors.margins: 10

    }         
    Button {
        id: butn42
        text: 'Back'
        onClicked:{
            pageLoader.source = "page3.qml"
            butn42.z = -1
        }    
        anchors.bottom: page4Container.bottom
        anchors.left: page4Container.left
        anchors.margins: 10

    }   
}
     
    