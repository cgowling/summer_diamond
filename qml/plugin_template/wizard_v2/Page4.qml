import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.2


Screen {

    title: 'Out data'
  
    Pg4Model{
        id : pg4_model
    }
    
    Component {
        id: pg4_model_Delegate
            

        RowLayout {
            id: row
            width: parent.width
            height: 30                      
            spacing: 50
            
            Text { 
                  Layout.fillWidth: true
                  height: parent.height
                  verticalAlignment: Text.AlignVCenter
                  text:label
                  
            }                      
            
            
            ComboBox { 
                id: combo
                implicitWidth: 300
                height: parent.height
                visible : ptype ==1
                model: [option1 , option2, option3,option4]
                onCurrentIndexChanged: pluginInfo(label, combo.currentText)

            }
        }
    }        
    
    ListView {
        anchors.fill: parent
        model: pg4_model
        delegate: pg4_model_Delegate
    }
    

        
/*
    ListModel {
        id: mymodel2
    }

       
    function addElementsOut(n) {
        mymodel2.clear();
        for ( var i = 0; i < n; i++ ) {
            mymodel2.append({label: 'Out dataset ' + (i+1)});
        }
    }
    Component.onCompleted: (addElementsOut(2))   
*/    
}        