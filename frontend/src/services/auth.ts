import api from './api'

interface LoginCredentials {
  username: string
  password: string
}

interface AuthResponse {
  access_token: string
  token_type: string
  user: {
    id: string
    username: string
    email: string
  }
}

export const login = async (credentials: LoginCredentials): Promise<AuthResponse> => {
  const response = await api.post<AuthResponse>('/api/auth/login', credentials)
  if (response.data.access_token) {
    localStorage.setItem('token', response.data.access_token)
  }
  return response.data
}

export const logout = (): void => {
  localStorage.removeItem('token')
}

export const getCurrentUser = async (): Promise<AuthResponse['user'] | null> => {
  try {
    const response = await api.get<AuthResponse['user']>('/api/auth/me')
    return response.data
  } catch (error) {
    console.error('Error getting current user:', error)
    return null
  }
}