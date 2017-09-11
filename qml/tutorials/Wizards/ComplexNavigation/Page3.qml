import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3



Rectangle {id:testPage3
    width: 100
    height: 62
    x:60
    color:"lightblue"
    Text{
        anchors.centerIn:parent
        text:"This page is loaded from \nwithin a component"
    }
}

