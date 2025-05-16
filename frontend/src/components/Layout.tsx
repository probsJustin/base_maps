import { Outlet, NavLink } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'

const Layout = () => {
  const { isAuthenticated } = useAuth()

  return (
    <div>
      <header>
        <h1>Base Maps</h1>
        <nav className="nav-links">
          <NavLink to="/">Home</NavLink>
          {isAuthenticated ? (
            <>
              <NavLink to="/config">Config</NavLink>
              <NavLink to="/wfm">WFM</NavLink>
              <NavLink to="/capture">Capture</NavLink>
              <NavLink to="/logout">Logout</NavLink>
            </>
          ) : (
            <NavLink to="/login">Login</NavLink>
          )}
          <NavLink to="/help">Help</NavLink>
          <NavLink to="/documentation">Documentation</NavLink>
        </nav>
      </header>
      
      <main className="page-container">
        <Outlet />
      </main>
      
      <footer>
        <p>© 2023 Base Maps</p>
      </footer>
    </div>
  )
}

export default Layout