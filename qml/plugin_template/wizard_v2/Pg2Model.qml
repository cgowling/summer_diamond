import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3


ListModel{
    id: pg2_model
    ListElement{
        label:"Number of in datasets "
        placeholder: 'Please input an integer'
        ptype: 0
        option1: ''
        option2: ''
        option3: ''        

    }
    ListElement{
        label:"Number of out datasets "
        placeholder: 'Please input an integer'
        ptype: 0 
        option1: ''
        option2: ''
        option3: ''
 
    }  
    ListElement{
        label: "Max frames"
        placeholder: 'Please input an integer'
        ptype: 1
        option1: 'single'
        option2: 'multiple'
        option3: 'int'
    
        
    }
}