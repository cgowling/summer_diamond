import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3



Rectangle {id:test1
    width: 100
    height: 62
    color:"red"
    // switchPage1 value is logically controlled somewhere in the code
    property bool switchPage1:true   // false
    property int page1Index:2
    signal handlerLoader(string name, int index)
    MouseArea {
        anchors.fill:parent
        onClicked:{if (switchPage1==true)
                      handlerLoader("Page2.qml",page1Index);
                   else handlerLoader("Help.qml",0);
        }
    }
}
