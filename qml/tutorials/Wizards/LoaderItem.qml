import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3



ApplicationWindow {


    width: 500
    height: 600

    Loader { id: top }
  
    Rectangle {
      Component.onCompleted: {
        top.source = "Page.qml"
      }
    }
  
    Text {
      anchors.centerIn: parent
      text: "Hello World"
   
      MouseArea {
        anchors.fill: parent
        onClicked: {
          top.item.color="blue"
        }
      }
    }
  
}        