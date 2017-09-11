import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3

ApplicationWindow {

    width: 1000
    height: 800

      Rectangle {
          width: 200; height: 200
      
          Content{
              id: content
          }
      
          Component {
              id: contentDelegate
              Row {
                  spacing: 10
                  Text { text: label }
                  TextField { }
              }
          }
      
          ListView {
              anchors.fill: parent
              model: content
              delegate: contentDelegate
          }
      }
}