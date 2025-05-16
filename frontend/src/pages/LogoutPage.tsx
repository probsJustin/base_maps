import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'

const LogoutPage = () => {
  const { logout } = useAuth()
  const navigate = useNavigate()

  useEffect(() => {
    // Log the user out
    logout()
    // Redirect to home page after logout
    const timer = setTimeout(() => {
      navigate('/')
    }, 2000)

    return () => clearTimeout(timer)
  }, [logout, navigate])

  return (
    <div>
      <h2>Logging Out</h2>
      <p>You have been logged out. Redirecting to home page...</p>
    </div>
  )
}

export default LogoutPage