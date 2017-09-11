import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3


RowLayout{
	id: textInput

	Label{
		id: testLabel
		text:"test label" 
	}
	TextField{	  
		id: testField          
		placeholderText: "Must be of the form:plugin_template"
                Layout.fillWidth: true
	}
}
