import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3


ListModel{
    id: pg4_model
    
    ListElement{
        label: "Out dataset 1"
        placeholder: ''
        ptype: 3
        option1: ''
        option2: ''
        option3: ''
        option4: ''
        n: 1           
        
    }

    ListElement{
        label:"Space of out datasets "
        placeholder: ''
        ptype: 1
        option1: 'Same as input'
        option2: 'tomo_raw'
        option3: 'tomo'
        option4: 'volume'
        n: 2    
    }   


    ListElement{
        label:"Pattern of out dataset "
        placeholder: ''
        ptype: 1
        option1: 'pattern'
        option2: 'SINOGRAM'
        option3: 'PROJECTION'
        option4: 'TIMESERIES'
        n: 3    
    }   
    ListElement{
        label:"Has the shape of the data changed? "
        placeholder: ''
        ptype: 1
        option1: 'Yes'
        option2: 'No'
        option3: ''
        option4: ''
        n: 4    
    }       
    
}