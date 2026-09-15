import axios from 'axios'
import type { ApiResponse, ErrorResponse } from '../types'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      const refreshToken = localStorage.getItem('refresh_token')
      
      if (refreshToken) {
        try {
          const response = await axios.post(`${API_BASE_URL}/auth/refresh`, {
            refresh_token: refreshToken,
          })
          const { access_token, refresh_token: newRefreshToken } = response.data.data
          localStorage.setItem('access_token', access_token)
          if (newRefreshToken) localStorage.setItem('refresh_token', newRefreshToken)
          originalRequest.headers.Authorization = `Bearer ${access_token}`
          return api(originalRequest)
        } catch (refreshError) {
          localStorage.removeItem('access_token')
          localStorage.removeItem('refresh_token')
          window.location.href = '/login'
        }
      } else {
        window.location.href = '/login'
      }
    }
    return Promise.reject(error)
  }
)

export const authApi = {
  register: (data: { email: string; password: string; full_name: string }) =>
    api.post<ApiResponse<any>>('/auth/register', data),
  login: (data: { email: string; password: string }) =>
    api.post<ApiResponse<{ access_token: string; refresh_token: string; user: any }>>('/auth/login', data),
  logout: () => api.post('/auth/logout', {}),
  refresh: (refreshToken: string) =>
    api.post<ApiResponse<{ access_token: string; refresh_token: string }>>('/auth/refresh', { refresh_token: refreshToken }),
  verifyEmail: (data: { token: string }) =>
    api.post('/auth/verify-email', data),
  forgotPassword: (data: { email: string }) =>
    api.post('/auth/forgot-password', data),
  resetPassword: (data: { token: string; new_password: string }) =>
    api.post('/auth/reset-password', data),
}

export const userApi = {
  getMe: () => api.get<ApiResponse<any>>('/users/me'),
  updateMe: (data: Partial<any>) => api.put('/users/me', data),
  changePassword: (data: { current_password: string; new_password: string }) =>
    api.put('/users/me/password', data),
  uploadAvatar: (formData: FormData) =>
    api.post('/users/me/avatar', formData, { headers: { 'Content-Type': 'multipart/form-data' } }),
}

export const familyApi = {
  list: () => api.get<ApiResponse<any[]>>('/families'),
  create: (data: { name: string; description?: string }) => api.post<ApiResponse<any>>('/families', data),
  get: (familyId: string) => api.get<ApiResponse<any>>(`/families/${familyId}`),
  update: (familyId: string, data: Partial<any>) => api.put<ApiResponse<any>>(`/families/${familyId}`, data),
  delete: (familyId: string) => api.delete<ApiResponse<any>>(`/families/${familyId}`),
  transferOwnership: (familyId: string, data: { new_owner_id: string }) =>
    api.post<ApiResponse<any>>(`/families/${familyId}/transfer-ownership`, data),
  join: (data: { join_code: string }) => api.post<ApiResponse<any>>(`/families/join`, data),
}

export const memberApi = {
  list: (familyId: string, params?: { page?: number; page_size?: number }) =>
    api.get<ApiResponse<any[]>>(`/families/${familyId}/members`, { params }),
  create: (familyId: string, data: any) =>
    api.post<ApiResponse<any>>(`/families/${familyId}/members`, data),
  update: (familyId: string, memberId: string, data: any) =>
    api.put<ApiResponse<any>>(`/families/${familyId}/members/${memberId}`, data),
  delete: (familyId: string, memberId: string) =>
    api.delete<ApiResponse<any>>(`/families/${familyId}/members/${memberId}`),
  getTree: (familyId: string) => api.get<ApiResponse<any>>(`/families/${familyId}/tree`),
  addRelationship: (familyId: string, data: any) =>
    api.post<ApiResponse<any>>(`/families/${familyId}/relationships`, data),
  updateRelationship: (familyId: string, relationshipId: string, data: any) =>
    api.put<ApiResponse<any>>(`/families/${familyId}/relationships/${relationshipId}`, data),
  deleteRelationship: (familyId: string, relationshipId: string) =>
    api.delete<ApiResponse<any>>(`/families/${familyId}/relationships/${relationshipId}`),
  lookupRelationship: (familyId: string, data: { member_a_id: string; member_b_id: string }) =>
    api.post<ApiResponse<any>>(`/families/${familyId}/relationships/lookup`, data),
  explainRelationship: (familyId: string, data: any) =>
    api.post<ApiResponse<any>>(`/families/${familyId}/relationships/explain`, data),
}

export const branchApi = {
  list: (familyId: string) => api.get<ApiResponse<any[]>>(`/families/${familyId}/branches`),
  create: (familyId: string, data: { name: string; description?: string; parent_branch_id?: string }) =>
    api.post<ApiResponse<any>>(`/families/${familyId}/branches`, data),
  update: (familyId: string, branchId: string, data: Partial<any>) =>
    api.put<ApiResponse<any>>(`/families/${familyId}/branches/${branchId}`, data),
  delete: (familyId: string, branchId: string) =>
    api.delete<ApiResponse<any>>(`/families/${familyId}/branches/${branchId}`),
}

export const postApi = {
  list: (familyId: string, params?: { page?: number; page_size?: number }) =>
    api.get<ApiResponse<any[]>>(`/families/${familyId}/posts`, { params }),
  create: (familyId: string, data: { content: string; media_urls?: string[]; visibility_scope?: string; branch_id?: string }) =>
    api.post<ApiResponse<any>>(`/families/${familyId}/posts`, data),
  get: (postId: string) => api.get<ApiResponse<any>>(`/posts/${postId}`),
  update: (postId: string, data: Partial<any>) => api.put<ApiResponse<any>>(`/posts/${postId}`, data),
  delete: (postId: string) => api.delete<ApiResponse<any>>(`/posts/${postId}`),
  addComment: (postId: string, data: { content: string }) =>
    api.post<ApiResponse<any>>(`/posts/${postId}/comments`, data),
  listComments: (postId: string, params?: { page?: number; page_size?: number }) =>
    api.get<ApiResponse<any[]>>(`/posts/${postId}/comments`, { params }),
  updateComment: (commentId: string, data: { content: string }) =>
    api.put<ApiResponse<any>>(`/comments/${commentId}`, data),
  deleteComment: (commentId: string) => api.delete<ApiResponse<any>>(`/comments/${commentId}`),
  react: (postId: string, data: { type: string }) =>
    api.post<ApiResponse<any>>(`/posts/${postId}/reactions`, data),
  removeReaction: (postId: string) => api.delete<ApiResponse<any>>(`/posts/${postId}/reactions`),
}

export const eventApi = {
  list: (familyId: string, params?: { page?: number; page_size?: number }) =>
    api.get<ApiResponse<any[]>>(`/families/${familyId}/events`, { params }),
  create: (familyId: string, data: any) =>
    api.post<ApiResponse<any>>(`/families/${familyId}/events`, data),
  get: (eventId: string) => api.get<ApiResponse<any>>(`/events/${eventId}`),
  update: (eventId: string, data: Partial<any>) => api.put<ApiResponse<any>>(`/events/${eventId}`, data),
  delete: (eventId: string) => api.delete<ApiResponse<any>>(`/events/${eventId}`),
  rsvp: (eventId: string, data: { status: string }) =>
    api.post<ApiResponse<any>>(`/events/${eventId}/rsvp`, data),
  listParticipants: (eventId: string) =>
    api.get<ApiResponse<any[]>>(`/events/${eventId}/participants`),
  sendReminder: (eventId: string) =>
    api.post<ApiResponse<any>>(`/events/${eventId}/remind`),
  uploadPhoto: (eventId: string, formData: FormData) =>
    api.post<ApiResponse<any>>(`/events/${eventId}/gallery`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }),
  listPhotos: (eventId: string) =>
    api.get<ApiResponse<any[]>>(`/events/${eventId}/gallery`),
  exportAttendees: (eventId: string) =>
    api.get<ApiResponse<any>>(`/events/${eventId}/export`, { responseType: 'blob' }),
}

export const heritageApi = {
  listDocuments: (familyId: string) =>
    api.get<ApiResponse<any[]>>(`/families/${familyId}/heritage/documents`),
  createDocument: (familyId: string, data: any) =>
    api.post<ApiResponse<any>>(`/families/${familyId}/heritage/documents`, data),
  updateDocument: (familyId: string, docId: string, data: any) =>
    api.put<ApiResponse<any>>(`/families/${familyId}/heritage/documents/${docId}`, data),
  deleteDocument: (familyId: string, docId: string) =>
    api.delete<ApiResponse<any>>(`/families/${familyId}/heritage/documents/${docId}`),
  approveDocument: (familyId: string, docId: string) =>
    api.post<ApiResponse<any>>(`/families/${familyId}/heritage/documents/${docId}/approve`),
  rejectDocument: (familyId: string, docId: string) =>
    api.post<ApiResponse<any>>(`/families/${familyId}/heritage/documents/${docId}/reject`),
  listStories: (familyId: string) =>
    api.get<ApiResponse<any[]>>(`/families/${familyId}/heritage/stories`),
  createStory: (familyId: string, data: { title: string; content: string; category?: string }) =>
    api.post<ApiResponse<any>>(`/families/${familyId}/heritage/stories`, data),
  updateStory: (familyId: string, storyId: string, data: any) =>
    api.put<ApiResponse<any>>(`/families/${familyId}/heritage/stories/${storyId}`, data),
  deleteStory: (familyId: string, storyId: string) =>
    api.delete<ApiResponse<any>>(`/families/${familyId}/heritage/stories/${storyId}`),
  listOutstanding: (familyId: string) =>
    api.get<ApiResponse<any[]>>(`/families/${familyId}/heritage/outstanding`),
  addOutstanding: (familyId: string, data: { member_id: string; title: string; description?: string }) =>
    api.post<ApiResponse<any>>(`/families/${familyId}/heritage/outstanding`, data),
  listPhotos: (familyId: string) =>
    api.get<ApiResponse<any[]>>(`/families/${familyId}/photos`),
}

export const aiApi = {
  search: (data: { query: string; family_id?: string }) =>
    api.post<ApiResponse<any>>('/ai/search', data),
  chat: (conversationId: string, data: { message: string }) =>
    api.post<ApiResponse<any>>(`/ai/conversations/${conversationId}/chat`, data),
  listConversations: (params?: { page?: number; page_size?: number }) =>
    api.get<ApiResponse<any>>('/ai/conversations', { params }),
  getConversation: (conversationId: string) =>
    api.get<ApiResponse<any>>(`/ai/conversations/${conversationId}`),
  getMessages: (conversationId: string) =>
    api.get<ApiResponse<any[]>>(`/ai/conversations/${conversationId}/messages`),
  createConversation: (data: { title?: string }) =>
    api.post<ApiResponse<any>>('/ai/conversations', data),
  deleteConversation: (conversationId: string) =>
    api.delete<ApiResponse<any>>(`/ai/conversations/${conversationId}`),
  summarize: (data: { content: string; length?: string }) =>
    api.post<ApiResponse<any>>('/ai/summarize', data),
  suggest: (data: any) =>
    api.post<ApiResponse<any>>('/ai/suggest', data),
}

export const notificationApi = {
  list: (params?: { page?: number; page_size?: number }) =>
    api.get<ApiResponse<any[]>>(`/notifications`, { params }),
  markAsRead: (notificationId: string) =>
    api.put<ApiResponse<any>>(`/notifications/${notificationId}/read`),
  markAllAsRead: () =>
    api.put<ApiResponse<any>>('/notifications/read-all'),
  getSettings: () =>
    api.get<ApiResponse<any>>('/notifications/settings'),
  updateSettings: (data: any) =>
    api.put<ApiResponse<any>>( '/notifications/settings', data),
}

export const adminApi = {
  listUsers: (params?: { page?: number; page_size?: number }) =>
    api.get<ApiResponse<any>>('/admin/users', { params }),
  getUser: (userId: string) =>
    api.get<ApiResponse<any>>(`/admin/users/${userId}`),
  updateUser: (userId: string, data: any) =>
    api.put<ApiResponse<any>>(`/admin/users/${userId}`, data),
  suspendUser: (userId: string) =>
    api.post<ApiResponse<any>>(`/admin/users/${userId}/suspend`),
  activateUser: (userId: string) =>
    api.post<ApiResponse<any>>(`/admin/users/${userId}/activate`),
  listModeration: (params?: { page?: number; page_size?: number }) =>
    api.get<ApiResponse<any>>('/admin/moderation', { params }),
  approveContent: (itemId: string) =>
    api.post<ApiResponse<any>>(`/admin/moderation/${itemId}/approve`),
  removeContent: (itemId: string) =>
    api.post<ApiResponse<any>>(`/admin/moderation/${itemId}/remove`),
  getAuditLog: (params?: { page?: number; page_size?: number }) =>
    api.get<ApiResponse<any>>('/admin/audit-log', { params }),
  createBackup: () =>
    api.post<ApiResponse<any>>('/admin/backup'),
  listBackups: () =>
    api.get<ApiResponse<any>>('/admin/backups'),
  restoreBackup: (backupId: string) =>
    api.post<ApiResponse<any>>(`/admin/restore`, { backup_id: backupId }),
  getConfig: () =>
    api.get<ApiResponse<any>>('/admin/config'),
  updateConfig: (data: any) =>
    api.put<ApiResponse<any>>('/admin/config', data),
}

export const analyticsApi = {
  getStats: (familyId: string) =>
    api.get<ApiResponse<any>>(`/families/${familyId}/analytics`),
  getDemographics: (familyId: string) =>
    api.get<ApiResponse<any>>(`/families/${familyId}/analytics/demographics`),
  getEvents: (familyId: string) =>
    api.get<ApiResponse<any>>(`/families/${familyId}/analytics/events`),
  createReport: (familyId: string, data: any) =>
    api.post<ApiResponse<any>>(`/families/${familyId}/reports`, data),
  getReport: (familyId: string, reportId: string) =>
    api.get<ApiResponse<any>>(`/families/${familyId}/reports/${reportId}`),
  exportReport: (familyId: string, reportId: string) =>
    api.get<ApiResponse<any>>(`/families/${familyId}/reports/${reportId}/export`, {
      responseType: 'blob',
    }),
}

export default api
