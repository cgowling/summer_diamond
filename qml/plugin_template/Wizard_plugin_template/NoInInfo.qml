import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3


ListModel{
    id: in_info
    ListElement{
        label:'Number of in datasets '
        placeholder: 'integer'
        ptype: 0
        option1: ''
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
    
}