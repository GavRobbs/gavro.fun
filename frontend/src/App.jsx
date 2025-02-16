import { useEffect, useState } from 'react'
import './index.css'
import ReactleLogo from "./assets/reactle.png"
import FaceInvadersLogo from "./assets/faceinvaders.png"
import HomoClickymusLogo from "./assets/homoclickymus.png"
import GemDropLogo from "./assets/gemdrop.png"
import W2PLogo from "./assets/w2pn.png";
import EmbargoLogo from "./assets/embargo.png"
import Entry from './components/Entry'


function App() {

  const [gameList, setGameList] = useState([]);

  const apiUrl = import.meta.env.VITE_API_URL;

  useEffect(() => {

    fetch(`${apiUrl}/games/`, {
      method: "GET",
      headers: {
        "Content-Type" : "application/json"
      }
    })
    .then(response => response.json())
    .then(data => {
      setGameList(data);
      console.log(data);
    });
  }, []);

  return (
    <>
      <header>
        <img src="https://gavrofunspace.nyc3.digitaloceanspaces.com/static/imgs/gavinfunlogo.png" />
        <h2>Play My Projects</h2>
      </header>
      <main>
        <div className="app-holder">
          {
            gameList.map((game, i) => {

              return <Entry key={i} logo={game.image} title={game.name} link={game.url} mobile_friendly={game.mobile_friendly}/>

            })
          }
        </div>
      </main>
      <footer>
        <p>© 2025 Gavin Robinson</p>
        <div className="footer-buttons">
          <a href="https://blog.gavro.fun/about/">About Me</a>
          <a href="https://blog.gavro.fun">Read My Blog</a>
        </div>
      </footer>
    </>
  )
}

export default App
