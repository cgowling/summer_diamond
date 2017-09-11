import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3


ApplicationWindow{
	id: root
	width: 500
	height:400
	
	signal createTemplate()

	ColumnLayout{
		id: frame
		anchors.fill: parent
		anchors.margins: 10
		
		LabelAndTextField{
				id: text1
		}
		LabelAndTextField{
				id:text2
		}
		LabelAndTextField{
				id:text3
		}
		Button {
		    id: butn1
		    text: "Create Template"
                    Layout.fillWidth: true
		    onClicked: {
				createTemplate()
		    }
		}	    			    		    
	}
}
