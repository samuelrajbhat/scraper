
import './App.css';
const user = {
  tag : 'Image',
  name : 'Samuel Raj Bhat',
  image_url : 'https://i.imgur.com/yXOvdOSs.jpg'

}
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <label>hello header</label>
      </header>
      <body className='App-body'>
        <h1>This is body part</h1>
        <h1>Hello</h1>
        <form method="get" id="myForm">
          <input type="button" value="Submit" onclick="readHeatwareItem()"></input>
        </form>
        <MyButton/>
        <ImageTag/>
      </body>
      <footer className='App-footer'>
        <p className='paragraph'>Hello I am learning react</p>
        <a href='.\sample.js'>click me</a>
      </footer>
    </div>
    
  );
}

function ImageTag(){
  return(
    <>    
    <h1>{user.tag}</h1>
        <img 
        src= {user.image_url} 
        alt = { 'Picture of '+user.name}
        />
    </>
  );
}
function MyButton(){
  return(
   <button>I'm a Button</button>
  );
}

export default App;
