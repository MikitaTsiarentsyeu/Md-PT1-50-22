import React, {useEffect, useState} from 'react';
import Navbar from '../elements/Navbar';
function Testing() {
  const [count, setCount] = useState(1)
  useEffect(()=>{
    console.log('Use effect test')
  }, [])
  return (<>
  <Navbar />
    <div>Testing</div>
    </>
  )
}

export default Testing