import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.2


Screen {

    title: 'Review'
    hasNextButton: false
    hasCreateButton : true


     Pg5Model {
        id: pg5_model
    }


    TableView {
        anchors.fill: parent

        __verticalScrollBar.visible: false
        __horizontalScrollBar.visible: false              
        
        TableViewColumn{
            role : 'label'
            width: 300
        }
        TableViewColumn{
            role : 'input'
            width: 300
            //delegate: TextEdit {anchors.fill: parent}
        }              
      model: pg5_model
    }
 
    
              
     

}
     
    