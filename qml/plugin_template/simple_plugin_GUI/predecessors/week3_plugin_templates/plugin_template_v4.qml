import QtQuick 2.2
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3

ApplicationWindow {

    width: 640; height: 360
    title: "Create a plugin template"
    signal  output(text)
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
                rows: 1
                flow: GridLayout.TopToBottom
                anchors.fill: parent



		Label { text: "Plugin template name:" }

                TextField {
	            placeholderText: "Must be of the form: plugin_template"
                    Layout.fillWidth: true
		    text: displayText		    
		    onEditingFinished: {
				output(text)	
		    }
		 }
		function updateOutput(i,text){
			output(i,text);
		}

            }
        }
        GroupBox {
            id: rowBox

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


