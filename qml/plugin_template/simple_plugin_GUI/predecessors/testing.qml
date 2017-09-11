import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3

ApplicationWindow {

    width: 1000
    height: 800

   // signal modified(int idx, string attr, variant value)
    signal createTemplate()

    // ==========================
    // Simple UI
    // ==========================

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10

        // Left column
        // A list view that renders one pluginDelegate
        // for each item in pluginModel
        

            
        GroupBox {
              width: parent.width
              
            
                ListView {
                    id: forms
                    Layout.fillWidth: true
                    Layout.fillHeight: true
        
                    model: content
                    delegate: paramDelegate
                    onContentHeightChanged: {
                        this.height = this.contentHeight;
                            }
                }
        }
        Button{
            id: butn1
            text: "Create Template"
            Layout.fillWidth: true
            onClicked:  createTemplate()

	   }
    }

    Content{
        id: content
    }
      

    Component {
        id: paramDelegate

        // It is going to be a row (horizontal layout)
        RowLayout {
            id: rowsss
            width: parent.width
            height: 30

            // First the name in a standard Label
            Text {
                Layout.fillWidth: true
                height: parent.height
                verticalAlignment: Text.AlignVCenter
                text: label
            }
            // Then either a TextField or a CombBox, depending on
            // whether it is string, int or float
            TextField { // For text
                id: text
                implicitWidth: 300
                height: parent.height
                //visible: ptype == 0  // this means it will appear if want it to 
                placeholderText: placeholder

              //  onEditingFinished: updateModel(text);
            }

           // ComboBox { // For int or floats
           //     id: combo
            //    implicitWidth: 300
            //    height: parent.height
            //    visible: ptype > 0
             //   value: ptype == 1? ivalue : fvalue// what is this doing ??? 
//
            //    onEditingFinished: updateModel(value)
           // }

            //function updateModel(value) {
              //  modified(i, label, value);
            //}
        }
    }
            
}
