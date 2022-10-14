
    function  bi( year )  { 
    switch  (  (  ( year  %  4  ==  0 )  &&  ( year  %  100  !=  0 )  )  ||  ( year  %  400  ==  0 )  )  { 
        case  ( true ) :
              console . log ( "It's a leap" ) ; 
             break ; 
        case  ( false ) :
            console . log ( "Not a leap" ) ; 
            break ; 
    } 
}