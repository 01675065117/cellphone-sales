import './App.css';
import { useState, useEffect } from 'react'
import axios from "axios"
function App() {
  const [customers, setCustomers] =  useState([])
  useEffect(() => {
    async function getAllCustomers(){
      try {
        const customers = await axios.get("http://127.0.0.1:8000/cellphone/customer/")
        console.log(customers.data)
        setCustomers(customers.data)
      } catch (error) {
        console.log(error)
      }
    }
    getAllCustomers()
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <h1>Connect ReactJS to Django</h1>
        {
          customers.map((customer, i)=>{
            return (
              <h2>{customer.id} {customer.full_name}</h2>
            )
          })
        }
      </header>
    </div>
  );
}

export default App;
