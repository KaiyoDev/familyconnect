export interface User {
  id: string
  email: string
  full_name: string
  avatar_url?: string
  system_role: 'ADMIN' | 'USER' | 'GUEST'
  family_roles?: FamilyRole[]
  created_at: string
  updated_at: string
}

export interface FamilyRole {
  family_id: string
  role: 'FAMILY_OWNER' | 'BRANCH_ADMIN' | 'FAMILY_MEMBER'
  branch_id?: string
}

export interface Family {
  id: string
  name: string
  description?: string
  founder_id: string
  owner_id: string
  join_code: string
  created_at: string
  updated_at: string
  member_count?: number
}

export interface Member {
  id: string
  family_id: string
  user_id: string
  branch_id?: string
  name: string
  gender: 'MALE' | 'FEMALE' | 'OTHER'
  birth_date?: string
  death_date?: string
  photo_url?: string
  relationship?: string
  profession?: string
  education?: Education[]
  created_at: string
  updated_at: string
}

export interface Education {
  id: string
  degree: string
  school: string
  field_of_study?: string
  start_year?: number
  end_year?: number
}

export interface Branch {
  id: string
  family_id: string
  name: string
  description?: string
  parent_branch_id?: string
  created_at: string
  updated_at: string
}

export interface Post {
  id: string
  family_id: string
  author_id: string
  content: string
  media_urls?: string[]
  visibility_scope: 'FAMILY' | 'BRANCH' | 'PUBLIC'
  branch_id?: string
  like_count?: number
  comment_count?: number
  created_at: string
  updated_at: string
  author?: {
    id: string
    name: string
    avatar_url?: string
  }
}

export interface Comment {
  id: string
  post_id: string
  author_id: string
  content: string
  parent_comment_id?: string
  created_at: string
  updated_at: string
  author?: {
    id: string
    name: string
    avatar_url?: string
  }
}

export interface Reaction {
  id: string
  post_id: string
  user_id: string
  type: 'LIKE' | 'HEART' | 'HAHA' | 'WOW' | 'SAD' | 'ANGRY'
  created_at: string
}

export interface Event {
  id: string
  family_id: string
  title: string
  description?: string
  start_time: string
  end_time?: string
  location?: string
  organizer_id: string
  max_participants?: number
  image_url?: string
  created_at: string
  updated_at: string
  participant_count?: number
}

export interface EventParticipant {
  id: string
  event_id: string
  member_id: string
  status: 'ATTENDING' | 'INTERESTED' | 'DECLINED'
  created_at: string
  member?: {
    id: string
    name: string
    avatar_url?: string
  }
}

export interface HeritageDocument {
  id: string
  family_id: string
  title: string
  description?: string
  document_type: 'CERTIFICATE' | 'LETTER' | 'PHOTO' | 'VIDEO' | 'OTHER'
  file_url: string
  upload_status: 'PENDING' | 'APPROVED' | 'REJECTED'
  uploader_id: string
  created_at: string
  updated_at: string
}

export interface HeritageStory {
  id: string
  family_id: string
  title: string
  content: string
  author_id: string
  category?: string
  upload_status: 'PENDING' | 'APPROVED' | 'REJECTED'
  created_at: string
  updated_at: string
}

export interface AIConversation {
  id: string
  user_id: string
  title?: string
  created_at: string
  updated_at: string
}

export interface AIMessage {
  id: string
  conversation_id: string
  role: 'user' | 'assistant'
  content: string
  created_at: string
}

export interface Notification {
  id: string
  user_id: string
  type: 'POST_COMMENT' | 'EVENT_RSV' | 'MEMBER_REQUEST' | 'SYSTEM' | 'ANNOUNCEMENT'
  title: string
  message: string
  is_read: boolean
  link?: string
  created_at: string
}

export interface ApiResponse<T> {
  success: boolean
  data?: T
  message?: string
  timestamp: string
}

export interface PaginatedResponse<T> {
  success: boolean
  data: T[]
  pagination: {
    page: number
    page_size: number
    total_items: number
    total_pages: number
  }
  message?: string
  timestamp: string
}

export interface ErrorResponse {
  success: false
  error: {
    code: string
    message: string
    details?: Array<{ field: string; message: string }>
  }
  timestamp: string
}
