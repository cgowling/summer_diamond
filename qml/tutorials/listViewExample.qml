import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
ApplicationWindow {

    width: 500
    height: 600
    Rectangle {
        id: rect
        width: 200; height: 200
    
        FruitModel{
            id: fruitModel
            
        }
    
        Component {
            id: fruitDelegate
            RowLayout {
              spacing: 3

              Text { text: name }
              Text { text: '$' + cost }
              Text {text:input}
              
              MouseArea {
                  anchors.fill: parent
                  onClicked: fruitModel.setProperty(2, "input","trial")
              }
    
            }
        }
    
        ListView {
            anchors.fill: parent
            model: fruitModel
            delegate: fruitDelegate
        }
    }
}
