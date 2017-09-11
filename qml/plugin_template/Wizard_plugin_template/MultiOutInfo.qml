import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3


ListModel{
    id: multi_out_info
    ListElement{
        label:'outDataset 1 '
        placeholder: 'integer'
        ptype: 3
        option1: ''
        option2: ''
        option3: ''
        option4: ''
        option5: '' 
        n: 1        
    }
    ListElement{
        label:'Space of out datasets '
        placeholder: ''
        ptype: 1
        option1: 'Same as input'
        option2: 'tomo_raw'
        option3: 'tomo'
        option4: 'volume'
        n: 2        
    }   


    ListElement{
        label:'Patterns/pattern?? of out dataset '
        placeholder: ''
        ptype: 1
        option1: 'pattern'
        option2: 'SINOGRAM'
        option3: 'PROJECTION'
        option4: 'TIMESERIES'
        n: 3       
    }   
    ListElement{
        label:'Has the shape of the data changed? '
        placeholder: ''
        ptype: 1
        option1: 'Yes'
        option2: 'No'
        option3: ''
        option4: ''
        n: 4        
    }       
    
    ListElement{
        label:'outDataset 2 '
        placeholder: 'integer'
        ptype: 3
        option1: ''
        option2: ''
        option3: ''
        option4: ''
        option5: '' 
        n: 5      
    }
    ListElement{
        label:'Space of out dataset 2 '
        placeholder: ''
        ptype: 1
        option1: 'Same as input'
        option2: 'tomo_raw'
        option3: 'tomo'
        option4: 'volume'
        n: 6        
    }   


    ListElement{
        label:'Patterns/pattern?? of out dataset '
        placeholder: ''
        ptype: 1
        option1: 'pattern'
        option2: 'SINOGRAM'
        option3: 'PROJECTION'
        option4: 'TIMESERIES'
        n: 7        
    }   
    ListElement{
        label:'Has the shape of the data changed? '
        placeholder: ''
        ptype: 1
        option1: 'Yes'
        option2: 'No'
        option3: ''
        option4: ''
        n: 8       
    }       
    
}
    