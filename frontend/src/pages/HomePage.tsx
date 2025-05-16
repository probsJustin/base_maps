import { useAuth } from '../context/AuthContext'

const HomePage = () => {
  const { isAuthenticated } = useAuth()
  
  return (
    <div>
      <h2>Home Page</h2>
      <p>Hello, World!</p>
      {isAuthenticated ? (
        <p>Welcome back! You are logged in.</p>
      ) : (
        <p>Please log in to access all features.</p>
      )}
    </div>
  )
}

export default HomePage