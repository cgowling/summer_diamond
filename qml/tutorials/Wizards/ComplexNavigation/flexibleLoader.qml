import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3



ApplicationWindow {
    id: mainWindow

    width: 500
    height: 500


    Item {id:top
        width:300
        height:200
        Loader{id:window}
        signal handlerLoader(string name, int index)
        Loader {
            id:pageLoader
            source:"Page1.qml"
        }
        Connections {
            target:pageLoader.item
            onHandlerLoader:{pageLoader.source=name;
                if(index===2)
                    window.source="NewWindow.qml";
            }
        }
    }
 
}          