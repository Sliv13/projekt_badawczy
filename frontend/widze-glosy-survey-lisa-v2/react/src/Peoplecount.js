import React, { useState, useRef , useEffect} from 'react';
import SpeechSection from './components/SpeechSection';
import MusicSection from './components/MusicSection';
var Peoplecount= ({updatedQuestions,updatedQuestions1}) =>{
 

let [peopleCounter, setCounter] = useState([]);
useEffect(() => {
  get_people_numberr()
  console.log("abc",peopleCounter)
},[peopleCounter])
  let get_people_numberr = async ()=>
    {
      //console.log("number=",peopleCounterr)
      
      let response = await fetch(`/api/peopleCounter/`)
      console.log("done",response)
      let peopleCounterr= await response.text();
      let peopleCounters= parseInt(peopleCounterr);
      console.log("3number=",peopleCounters)
      setCounter(peopleCounters);
      
    }
    console.log("1ulumulu counter=",peopleCounter)
    if (peopleCounter > 0){
      {console.log(updatedQuestions)}
      return (
      <section id="Peoplecount">  
      
      <SpeechSection questions = {updatedQuestions} peopleCounter={2}/>
      <SpeechSection questions = {updatedQuestions[1]} peopleCounter={peopleCounter}/>
      <SpeechSection questions = {updatedQuestions[2]} peopleCounter={peopleCounter}/>
      <SpeechSection questions = {updatedQuestions[3]} peopleCounter={peopleCounter}/>
      <SpeechSection questions = {updatedQuestions[4]} peopleCounter={peopleCounter}/>
      <SpeechSection questions = {updatedQuestions[5]} peopleCounter={peopleCounter}/>
      {/*ŚPIEW - KOLORY */}
       <MusicSection questions = {updatedQuestions[6]} peopleCounter={peopleCounter}/>
      <MusicSection questions = {updatedQuestions[7]} peopleCounter={peopleCounter}/>
      <MusicSection questions = {updatedQuestions[8]} peopleCounter={peopleCounter}/>
      <MusicSection questions = {updatedQuestions[9]} peopleCounter={peopleCounter}/>
      <MusicSection questions = {updatedQuestions[10]} peopleCounter={peopleCounter}/>
      </section>
    )
    }
    else{
      {console.log(updatedQuestions)}
      <> 
      <SpeechSection questions = {updatedQuestions} peopleCounter={2}/>
      <SpeechSection questions = {updatedQuestions} peopleCounter={2}/>
      <SpeechSection questions = {updatedQuestions} peopleCounter={2}/>
      <SpeechSection questions = {updatedQuestions} peopleCounter={2}/>
      <SpeechSection questions = {updatedQuestions} peopleCounter={2}/>
      <SpeechSection questions = {updatedQuestions} peopleCounter={2}/>
      {/*ŚPIEW - KOLORY */}
       <MusicSection questions = {updatedQuestions} peopleCounter={2}/>
      <MusicSection questions = {updatedQuestions} peopleCounter={2}/>
      <MusicSection questions = {updatedQuestions} peopleCounter={2}/>
      <MusicSection questions = {updatedQuestions} peopleCounter={2}/>
      <MusicSection questions = {updatedQuestions} peopleCounter={2}/>
      </>
    }
    
}

export default Peoplecount
