import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.2

ApplicationWindow {

    id: mainWindow
    title: 'Savu plugin template auto-creation ' 

    width: 750
    height: 400
    

    signal pluginInfo( string attr, variant value)
    signal createTemplate()

    //Material.primary: Material.Indigo;
    //Material.accent: Material.Turquoise;

    Rectangle {
        id: top 
        width: 750
        height: 400

        StackLayout {
          id: handler
          anchors.fill : parent
          currentIndex : 0



          Page1 {
              id: page1
              onNextScreen : {
                  handler.currentIndex += 1;
              }
          }
          
          Page2 {
              id: page2
              onNextScreen : {
                  handler.currentIndex += 1;
              }              
              onPrevScreen : {
                  handler.currentIndex -= 1;
              }
    
          }
              
          Page3 {
              id: page3
              onNextScreen : {
                  handler.currentIndex += 1;
              }              
              onPrevScreen : {
                  handler.currentIndex -= 1;
              }

            
          }        
          Page4 {
              id: page4
              onNextScreen : {
                  handler.currentIndex += 1;
              }              
              onPrevScreen : {
                  handler.currentIndex -= 1;
              }
            
          } 
          Page5 {
              id: page5
              onNextScreen : {
                  handler.currentIndex += 1;
              }              
              onPrevScreen : {
                  handler.currentIndex -= 1;
              }
            
          } 
       }
    }
}                
