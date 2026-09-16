import React, { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import Layout from '@/components/Layout'
import { Card, CardContent } from '@/components/ui/basic'
import { Button } from '@/components/ui/basic'
import { ArrowLeft, Heart, MessageCircle, Share2, Send } from 'lucide-react'
import { postApi } from '@/services/api'
import { toast } from 'sonner'

interface Comment {
  id: string
  post_id: string
  author_id: string
  content: string
  created_at: string
  updated_at: string
  author?: { id: string; name: string; avatar_url?: string }
}

export default function Com02PostDetail() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [liked, setLiked] = useState(false)
  const [likeCount, setLikeCount] = useState(12)
  const [commentText, setCommentText] = useState('')
  const isPersistedPostId = Boolean(id && /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(id))
  const [comments, setComments] = useState<Comment[]>(() => isPersistedPostId ? [] : [
    {
      id: 'demo-comment-1',
      post_id: id!,
      author_id: 'user2',
      content: 'Thật vui! Mình sẽ về đầy đủ ạ!',
      created_at: '2026-09-09T11:00:00Z',
      updated_at: '2026-09-09T11:00:00Z',
      author: { id: 'user2', name: 'Trần Thị B' },
    },
    {
      id: 'demo-comment-2',
      post_id: id!,
      author_id: 'user3',
      content: 'Gia đình sum họp thật hạnh phúc',
      created_at: '2026-09-09T12:00:00Z',
      updated_at: '2026-09-09T12:00:00Z',
      author: { id: 'user3', name: 'Lê Văn C' },
    },
  ])

  const getErrorMessage = (error: any, fallback: string) => {
    const detail = error?.response?.data?.detail
    if (Array.isArray(detail)) {
      return detail
        .map((item) => typeof item === 'string' ? item : item?.msg)
        .filter(Boolean)
        .join(', ') || fallback
    }
    return typeof detail === 'string' ? detail : fallback
  }

  React.useEffect(() => {
    if (!isPersistedPostId) return
    postApi.listComments(id)
      .then((response) => setComments(response.data.items ?? []))
      .catch((error) => toast.error(getErrorMessage(error, 'Không tải được bình luận')))
  }, [id, isPersistedPostId])

  const handleComment = async () => {
    if (!commentText.trim()) return
    if (!isPersistedPostId) {
      const now = new Date().toISOString()
      setComments((current) => [...current, {
        id: `demo-comment-${Date.now()}`,
        post_id: id!,
        author_id: 'current-user',
        content: commentText.trim(),
        created_at: now,
        updated_at: now,
        author: { id: 'current-user', name: 'Bạn' },
      }])
      setCommentText('')
      toast.success('Đã thêm bình luận demo')
      return
    }
    try {
      const response = await postApi.addComment(id!, { content: commentText.trim() })
      const comment = response.data.data ?? response.data
      setComments((current) => [...current, comment])
      setCommentText('')
      toast.success('Đã thêm bình luận')
    } catch (error: any) {
      toast.error(getErrorMessage(error, 'Thêm bình luận thất bại'))
    }
  }

  return (
    <Layout>
      <div className="space-y-6 max-w-2xl mx-auto">
        <Button variant="ghost" onClick={() => navigate(-1)} className="pl-0">
          <ArrowLeft className="h-4 w-4 mr-2" />Quay lại
        </Button>
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-3 mb-3">
              <div className="w-10 h-10 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold">NA</div>
              <div><p className="font-medium">Nguyễn Văn A</p><p className="text-xs text-muted-foreground">{new Date().toLocaleString('vi-VN')}</p></div>
            </div>
            <p className="text-neutral-800 mb-3">Hôm nay gia đình mình tổ chức giỗ tổ họ Nguyễn. Mọi người cùng về tham dự đầy đủ nhé!</p>
            <div className="flex items-center gap-6 pt-3 border-t">
              <button onClick={() => { setLiked(!liked); setLikeCount(p => liked ? p - 1 : p + 1); }} className={`flex items-center gap-2 text-sm ${liked ? 'text-danger' : 'text-muted-foreground'}`}>
                <Heart className={`h-5 w-5 ${liked ? 'fill-current' : ''}`} />{likeCount} Thích
              </button>
              <button className="flex items-center gap-2 text-sm text-muted-foreground"><MessageCircle className="h-5 w-5" />{comments.length} Bình luận</button>
              <button className="flex items-center gap-2 text-sm text-muted-foreground ml-auto"><Share2 className="h-5 w-5" />Chia sẻ</button>
            </div>
          </CardContent>
        </Card>
        <div className="space-y-3">
          <h3 className="font-medium">{comments.length} bình luận</h3>
          {comments.map(c => (
            <div key={c.id} className="flex gap-3">
              <div className="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center text-xs font-medium">{c.author?.name?.[0] || 'U'}</div>
              <div className="flex-1 bg-neutral-50 rounded-lg p-3">
                <div className="flex items-center justify-between mb-1"><span className="font-medium text-sm">{c.author?.name}</span><span className="text-xs text-muted-foreground">{new Date(c.created_at).toLocaleString('vi-VN')}</span></div>
                <p className="text-sm text-neutral-700">{c.content}</p>
              </div>
            </div>
          ))}
        </div>
        <div className="flex gap-3">
          <div className="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center text-xs font-medium">NA</div>
          <div className="flex-1 flex gap-2">
            <input type="text" placeholder="Viết bình luận..." className="input flex-1" value={commentText} onChange={e => setCommentText(e.target.value)} onKeyDown={e => e.key === 'Enter' && handleComment()} />
            <Button onClick={handleComment} disabled={!commentText.trim()}><Send className="h-4 w-4" /></Button>
          </div>
        </div>
      </div>
    </Layout>
  )
}
