import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.2

ApplicationWindow {

    id: mainWindow

    width: 750
    height: 400
       
   
    Rectangle {
        id: top 
        width:650
        height: 400
        x:100  
            
  
            MessageDialog {
                id: message
                title: 'Attention!'
                icon: StandardIcon.Warning
                text: 'Please input an integer'         
                standardButtons: StandardButton.Ok
                onAccepted : visible = false

            }        
            Button{
                id: help 
                text: 'Help'
                onClicked: message.visible = true
            } 
                     
    

    } 
}            