import React, { useState, useRef , useEffect} from 'react';
import SpeechSection from './components/SpeechSection';
import MusicSection from './components/MusicSection';
var Peoplecount= () =>{
 

let [peopleCounter, setCounter] = useState(1);
useEffect(() => {
  
  console.log("abc",peopleCounter)
},[peopleCounter])
  let get_people_numberr = async ()=>
    {
      //console.log("number=",peopleCounterr)
      
      let response = await fetch(`/api/pc/`)
      console.log("done",response)
      let peopleCounterr= await response.text();
      let peopleCounters= parseInt(peopleCounterr);
      console.log("3number=",peopleCounters)
      setCounter(peopleCounters);
      
    }
    
    get_people_numberr()
    return (
     peopleCounter
    )
    
}

export default Peoplecount
