import './App.css';
import {React, Component} from 'react'
import axios from 'axios'

class App extends Component {
    constructor(props){
      super(props)
      this.state={
          button_label:'Fetch',
          data:''
      }
    }

  fetchClearWord=()=>{
    if (this.state.button_label === 'Fetch'){
      const config={
        headers:{
            "Content-Type":"application/json"
        }
      }
      axios.get('http://localhost:8000/api/get_company_name',config)
      .then((res)=>{
          this.setState({...this.state,button_label:'Clear',data:res.data.company_name})
      })
    }

    else{
      this.setState({...this.state,button_label:'Fetch',data:''})
    }

  }

  render(){
    const {data, button_label} = this.state
      return (
        <div className="App App-header">
          <h3>Just Testing</h3>
          <button onClick = {this.fetchClearWord}>{button_label}</button>
          <div className='fetch-word'>{data}</div>
        </div>
      )
   }
}

export default App;
