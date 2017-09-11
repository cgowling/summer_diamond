
import QtQuick 2.2
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Layouts 1.3


ApplicationWindow {
    color: "steelblue"
    width: 640; height: 360


    visible: true
    title: "Create a plugin template"

    ColumnLayout {
        id: mainLayout
        anchors.fill: parent
        //anchors.margins: margin


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
	            placeholderText: "Must be of the form plugin_template"
                    Layout.fillWidth: true
		}
                TextField { Layout.fillWidth: true}
                TextField { Layout.fillWidth: true}
		TextField { 	            
		    placeholderText: "Must be of the form pluginTemplate"
                    Layout.fillWidth: true
		}
		ComboBox {
                    Layout.fillWidth: true
		    model: [ "Pass", "process" ]
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
		    style: ButtonStyle {
			background: Rectangle {
			    implicitWidth: 300
			    implicitHeight: 25
			    border.width: control.activeFocus ? 2 : 1
			    border.color: "gray"
			    radius: 20
			    gradient: Gradient {
				GradientStop { position: 0 ; color: control.pressed ? "steelblue" : "white" }
				GradientStop { position: 1 ; color: control.pressed ? "#aaa" : "#ccc" }
			    }
			}
		    }
		}
            }
        }
    }
}
