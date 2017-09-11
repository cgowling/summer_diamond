import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3


ListModel{
    id: multi_data_info
    ListElement{
        label:'Dataset 1 '
        placeholder: 'integer'
        ptype:3
        options: ''
        option2: ''
        option3: ''
        option4: ''
        option5: '' 
        n: 1        
    }

    ListElement{
        label:'Patterns/pattern?? of in datasets '
        placeholder: ''
        ptype: 1
        option1: 'pattern'
        option2: 'SINOGRAM'
        option3: 'PROJECTION'
        option4: 'TIMESERIES'
        n: 2        
    }    
    
    ListElement{
        label:'Dataset 2 '
        placeholder: 'integer'
        ptype: 3
        option1: ''
        option2: ''
        option3: ''
        option4: ''
        option5: '' 
        n: 3       
    }

    ListElement{
        label:'Patterns/pattern?? of in datasets '
        placeholder: ''
        ptype: 1
        option1: 'pattern'
        option2: 'SINOGRAM'
        option3: 'PROJECTION'
        option4: 'TIMESERIES'
        n: 4     
    }    
}    
    