import { Routes, Route } from 'react-router-dom'
import './App.css'
import Layout from './components/Layout'
import HomePage from './pages/HomePage'
import ConfigPage from './pages/ConfigPage'
import WfmPage from './pages/WfmPage'
import CapturePage from './pages/CapturePage'
import HelpPage from './pages/HelpPage'
import DocumentationPage from './pages/DocumentationPage'
import LoginPage from './pages/LoginPage'
import LogoutPage from './pages/LogoutPage'
import NotFoundPage from './pages/NotFoundPage'

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<HomePage />} />
        <Route path="config" element={<ConfigPage />} />
        <Route path="wfm" element={<WfmPage />} />
        <Route path="capture" element={<CapturePage />} />
        <Route path="help" element={<HelpPage />} />
        <Route path="documentation" element={<DocumentationPage />} />
        <Route path="login" element={<LoginPage />} />
        <Route path="logout" element={<LogoutPage />} />
        <Route path="*" element={<NotFoundPage />} />
      </Route>
    </Routes>
  )
}

export default App