import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3



Rectangle {id:testHelp
    width: 100
    height: 62
    x:30
    color:"pink"
    property int helpIndex:-1
    signal handlerLoader(string name, int index)
    MouseArea {
        anchors.fill:parent
        onClicked:handlerLoader("Page1.qml",helpIndex)
    }
}
