import { useEffect, useState } from 'react'



import { BrowserRouter as Router, Route, Link } from "react-router-dom";

function App() {
const [chores, setChores] = useState([]);

  useEffect
  

  return (
    <>
      <Router>
15       <div>
16         <nav>
17           <ul>
18             <li>
19               <Link to="/">Home</Link>
20             </li>
21             <li>
                  <Link to="/Chores">Chores</Link>
                  </li>
27           </ul>
28         </nav>
29 
30         <Route path="/" exact component={Index} />
31         <Route path="/products/:id" component={Product} />
32       </div>
33     </Router>
    </>
  )
}

export default App
