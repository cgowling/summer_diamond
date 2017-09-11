import QtQuick 2.2
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3

ApplicationWindow {

    width: 640; height: 360
    title: "Create a plugin template"
    //signal  output()
    signal  create_template()

    ColumnLayout {
        id: mainLayout
        anchors.fill: parent
        anchors.margins: 10


        GroupBox {
            id: gridBox
            Layout.fillWidth: true

            GridLayout {
                id: gridLayout
                rows: 9
                flow: GridLayout.TopToBottom
                anchors.fill: parent


		Label { text: "Plugin template name:" }
                Label { text: "Your name:" }
                Label { text: "Your e-mail:" }
		Label { text: "Class name:" }
		Label { text: "Pre-processing:" }
		Label { text: "Filters:" }
		Label { text: "Post-processing:" }
		Label { text: "No. of inputs:" }
		Label { text: "No. of outputs:" }


                TextField {
	            placeholderText: "Must be of the form: plugin_template"
                    Layout.fillWidth: true
		    text: displayText
		    onEditingFinished: updateOutput(1,text);	
		}
                TextField { Layout.fillWidth: true}
                TextField { Layout.fillWidth: true}
		TextField { 	            
		    placeholderText: "Must be of the form: pluginTemplate"
                    Layout.fillWidth: true
		}
		ComboBox {
                    Layout.fillWidth: true
		    model: [ "Pass", "process" ]
		    //text: currentText

		}
		ComboBox {
                    Layout.fillWidth: true
		    model: [ "on", "off" ]
		}
		ComboBox {
                    Layout.fillWidth: true
		    model: [ "Pass", "process" ]
		}
		TextField {Layout.fillWidth: true }
		TextField { Layout.fillWidth: true}
		
		//function updateOutput(i,text):
			//output(i,text)
		
		//onEditingFinished: updateOutput(text);
            }
        }
        GroupBox {
            id: rowBox
            //title: "Row layout"
            Layout.fillWidth: true

            RowLayout {
                id: rowLayout
                anchors.fill: parent


		Button {
		    text: "Create Template"
                    Layout.fillWidth: true
	     	    onClicked : {
				create_template()
		    }
 		    			    		    
		}
            }
        }
    }
}
