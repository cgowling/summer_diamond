import Qt 4.7

Rectangle {
    signal messageRequired;

    function updateMessage(text) {
        messageText.text = text
    }

    anchors.fill: parent; color: "blue"

    Text {
        id: messageText
        anchors.centerIn: parent; color: "white"
    }

    MouseArea {
        anchors.fill: parent
        onClicked: messageRequired()
    }
}
