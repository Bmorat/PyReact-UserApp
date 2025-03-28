import { useState, useEffect } from "react";

function Users({id,name,age}) {
  return (
    <article className="w-96 bg-gray-200 rounded-xl shadow-lg shadow-gray-700 mx-aut my-10 mt-10 p-10">
      <p className="text-2xl text-center">{name}</p>
      <h2>{id}</h2>
      <p>{age} </p>
      <div className="flex justify-center">
        <button className="bg-red-600 text-gray-200 w-40 font-semibold rounded-xl h-10 hover:bg-red-700 hover:text-gray-300  ">Delete</button>
      </div>
    </article>
  ) 
}

function App() {
  const [users, setUsers] = useState([]);

  const getUsers = async () => { 
    const allUsers = await fetch ('http://localhost:8000/api/v1/users')
    const userJson = await allUsers.json()
    setUsers(userJson)
  }

  useEffect(() => {
    getUsers()
  }, [])

  return (
    <main className="w-full min-h-screen bg-gray-200">   
    <h1 className="bg-green-500 text-blue-600 p-10 text-5xl">
      UsersApp! 
    </h1>
      <div>
      {users.length === 0 ? "Loading..." : users.map((user) => (
        <Users  
        id={user.id} 
        name={user.name} 
        age={user.age} />
      ))}
      </div>
      </main>
  );    
}
export default App;