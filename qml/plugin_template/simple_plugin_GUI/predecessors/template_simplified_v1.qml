import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3


ApplicationWindow{
	id: root
	width: 500
	height:400
	
	signal createTemplate()
	signal output(int idx,variant value)
    	

	ColumnLayout{
		anchors.fill: parent
		anchors.margins: 10

		FormStructure{}
        
		Button{
		    id: butn1
		    text: "Create Template"
                    Layout.fillWidth: true

		}	    			    		    
	
		///////////////////
		/// connections////
		///////////////////

		Connections{
			target: butn1
			onClicked: createTemplate()	
		}
	}
}




