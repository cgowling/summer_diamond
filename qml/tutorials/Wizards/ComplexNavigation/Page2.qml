import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3


Rectangle {id:testPage2
    width: 100
    height: 62
    x:30
    color:"yellow"
    property int page2Index:3
    signal handlerLoader(string name, int index)
    MouseArea {
        anchors.fill:parent
        onClicked:handlerLoader("Page3.qml",page2Index)
    }
}
