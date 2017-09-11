import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3


ApplicationWindow {

    width: 500
    height: 800
    
    
        ColumnLayout {
              anchors.fill: parent
              anchors.margins: 10
              
              Content{
                  id: content
              }
          
              Component {
                  id: contentDelegate
                  RowLayout {
                      width: parent.width
                      height: 30                      
                      spacing: 50
                      Text { 
                            Layout.fillWidth: true
                            height: parent.height
                            verticalAlignment: Text.AlignVCenter
                            text: label
                        }                      
                      
                      TextField {
                            id: textinput
                            implicitWidth: 300
                            height: parent.height
                            visible: ptype == 0  // this means it will appear if want it to 
                            placeholderText: placeholder 
                            //text: input
                            //onEditingFinished:  
                      }
                      
                      ComboBox { // For int or floats
                          id: combo
                          implicitWidth: 300
                          height: parent.height
                          visible: ptype ==1
                          model: [option1 , option2]
                      }                      
                  }
              }
          
              ListView {
                  anchors.fill: parent
                  model: content
                  delegate: contentDelegate
              }
        Button{
            id: butn1
            text: "Create Template"
            Layout.fillWidth: true
            //onClicked:  createTemplate()

	   }        
        }
}              