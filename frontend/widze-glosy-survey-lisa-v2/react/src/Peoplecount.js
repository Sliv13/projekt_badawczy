import React, { useState, useRef , useEffect} from 'react';

const Peoplecount= () =>{



let [peopleCounter, setCounter] = useState([]);
useEffect(() => {
    get_people_numberr()
    console.log("abc",peopleCounter)
  },[peopleCounter])
  let get_people_numberr = async ()=>
    {
      //console.log("number=",peopleCounterr)
      let response = await fetch(`/api/peopleCounter/`)
      console.log("done")
      let peopleCounterr= await response.text();
      let peopleCounters= parseInt(peopleCounterr);
      console.log("number=",peopleCounterr)
      setCounter(peopleCounterr);
      
    }
    if (peopleCounter[0] > 0){
      return (
        peopleCounter
    )
    }
    else{return 2}
    
}

export default Peoplecount
