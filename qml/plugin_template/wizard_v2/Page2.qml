import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.2


Screen {

    title: 'Number of input and output datasets'
    //Component.onCompleted: console.log(handler.currentIndex) can get info from stack layout module l
  
    onNoDatasets :{
        console.log(value)
        elementNo = value;
    }
    
    Pg2Model {// list Model, contains content to fill component 
        id: pg2_model
    }
    
    Component {
        id: pg2_model_Delegate
        
        RowLayout {
            id: row
            width: parent.width
            height: 30                      
            spacing: 50
            
            Text { 
                  id: text 
                  Layout.fillWidth: true
                  height: parent.height
                  verticalAlignment: Text.AlignVCenter
                  text:label
                  
            }                      
            
            TextField {
                  id: textfield
                  implicitWidth: 300
                  height: parent.height
                  visible: ptype == 0  // will appear if want it to soecified in InInfo
                  placeholderText: placeholder
                  
                  onTextChanged: {
                      if( isInt(parseInt(textfield.text))== true){
                          noDatasets(parseInt(textfield.text));
                      } else{
                          warning.visible = true // pops up in middle of screen not window ?? 
                          void remove(0,1)// gets rid of it before you even see it                          
                      }   
                      pluginInfo(label,textfield.text)
    
                  }
            }
            ComboBox { 
                id: combo
                implicitWidth: 300
                height: parent.height
                visible : ptype ==1
                model:[option1,option2,option3]
                onCurrentIndexChanged: {
                    pluginInfo(label, combo.currentText)
                    if( combo.currentText == 'int'){
                        textfield.visible = true
                        combo.visible = false  
                    }
                }    
    
            }                      
            MessageDialog {
                id: warning
                title: 'Attention!'
                icon: StandardIcon.Warning
                text: 'Please input an integer'         
                standardButtons: StandardButton.Ok
                onAccepted : visible = false
            
            }
               
            function isInt(n){
                return n === +n && n === (n|0) && n != 0;
            }                  
        }
    }
    
    ListView {
        anchors.fill: parent
        model: pg2_model
        delegate: pg2_model_Delegate
    } 
   
}  
        








