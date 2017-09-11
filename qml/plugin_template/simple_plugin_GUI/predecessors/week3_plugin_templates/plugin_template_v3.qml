import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3

ApplicationWindow {

    width: 640; height: 360
    title: "Create a plugin template"
    signal  modified(idx, newtext)
    signal  create_template()

    ColumnLayout {
        id: mainLayout
        anchors.fill: parent
        anchors.margins: 10

        GroupBox{
		id: forms

		RowLayout {
			id: root
			width: parent.width
			height: 30

			Text {
				Layout.fillWidth: true
				height: parent.height
				verticalAlignment: Text.AlignVCenter
				text: "Plugin template name:"
			}


		        TextField {
				id:input
				placeholderText: "Must be of the form: plugin_template"             

				//text: displayText
				onEditingFinished: updateModel(1,displayText);	
			}

			function updateModel(i, text){
				modified(i, text);
                        }
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
}
