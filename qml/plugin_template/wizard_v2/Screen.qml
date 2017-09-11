import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.2


Rectangle {
    id: root
    width: 750
    height: 400 
    color: 'steel blue'


    property int elementInfo :1
    property alias hasBackButton: backButton.visible
    property alias hasNextButton: nextButton.visible   
    property alias hasCreateButton: create.visible    
    property alias title: text.text
    property int elementNo : 1    

    default property alias children: columnlayout.data // all of the stuff from the pages is a child of column layout 
    
    signal nextScreen()
    signal prevScreen()
    signal noDatasets(int value)
    

        //elementInfo: value 
        //addElements(value) // this calls 
    
       
            
    
    Text{
        id: text// title asign in  page files
        text: ''
        anchors{horizontalCenter: root.horizontalCenter; top: root.top; margins: 10 }
    }
    
    ColumnLayout {
        id: columnlayout
        anchors{fill: parent; margins: 30}

    }
        
    Button {
        id: nextButton
        text: 'Next'
        onClicked: nextScreen()
        
        anchors{bottom: root.bottom; right: root.right; margins: 10}
    }         
    Button {
        id: backButton
        text: 'Back'
        onClicked:{
            prevScreen()
        }
        anchors{bottom: root.bottom; left: root.left; margins: 10}
    }       
    Button {
        id: create
        text: "Create template"
        onClicked: createTemplate()
        anchors{bottom: root.bottom; right: root.right; margins: 10}
        visible: false 
    }        
}