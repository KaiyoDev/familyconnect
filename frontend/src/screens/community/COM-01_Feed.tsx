import React from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Avatar, Badge } from '@/components/ui/basic'
import { Heart, MessageCircle, Share2, Plus, ArrowRight } from 'lucide-react'
import { useNavigate } from 'react-router-dom'

interface Post {
  id: string
  author: { id: string; name: string; avatar_url?: string }
  content: string
  media_urls?: string[]
  like_count: number
  comment_count: number
  created_at: string
  updated_at?: string
}

export default function Com01Feed() {
  const navigate = useNavigate()
  const [posts] = React.useState<Post[]>([
    {
      id: '1',
      author: { id: 'user1', name: 'Nguyễn Văn A', avatar_url: undefined },
      content: 'Hôm nay gia đình mình tổ chức giỗ tổ họ Nguyễn. Mọi người cùng về tham dự đầy đủ nhé! 🎉',
      media_urls: [],
      like_count: 12,
      comment_count: 5,
      created_at: '2026-09-09T10:00:00Z',
    },
    {
      id: '2',
      author: { id: 'user2', name: 'Trần Thị B', avatar_url: undefined },
      content: 'Các cháu đã hoàn thành bài tập về nhà rồi ạ! 📚✨',
      media_urls: [],
      like_count: 8,
      comment_count: 2,
      created_at: '2026-09-08T15:30:00Z',
    },
  ])

  return (
    <Layout>
      <div className="space-y-6 max-w-2xl mx-auto">
        <div className="flex items-center justify-between">
          <h1 className="text-2xl font-bold">Bảng tin gia đình</h1>
          <Button onClick={() => navigate('/community/post/new')}>
            <Plus className="h-4 w-4 mr-2" />Đăng bài
          </Button>
        </div>

        <Card>
          <CardContent className="p-4">
            <div className="flex gap-3">
              <Avatar src={undefined} fallback="NA" />
              <input
                type="text"
                placeholder="Chia sẻ điều gì đó với gia đình..."
                className="flex-1 bg-neutral-100 rounded-full px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary/50"
                onClick={() => navigate('/community/post/new')}
              />
            </div>
          </CardContent>
        </Card>

        <div className="space-y-4">
          {posts.map((post) => (
            <PostCard key={post.id} post={post} onClick={() => navigate(`/community/post/${post.id}`)} />
          ))}
        </div>
      </div>
    </Layout>
  )
}

function PostCard({ post, onClick }: { post: Post; onClick: () => void }) {
  const [liked, setLiked] = React.useState(false)
  return (
    <Card className="cursor-pointer hover:border-primary/50" onClick={onClick}>
      <CardContent className="p-4">
        <div className="flex items-center gap-3 mb-3">
          <Avatar src={post.author.avatar_url} fallback={post.author.name[0]} />
          <div>
            <p className="font-medium">{post.author.name}</p>
            <p className="text-xs text-muted-foreground">{new Date(post.created_at).toLocaleDateString('vi-VN')}</p>
          </div>
        </div>
        <p className="text-neutral-800 mb-3">{post.content}</p>
        <div className="flex items-center gap-6 pt-3 border-t">
          <button onClick={(e) => { e.stopPropagation(); setLiked(!liked); }} className={`flex items-center gap-2 text-sm ${liked ? 'text-danger' : 'text-muted-foreground'}`}>
            <Heart className={`h-5 w-5 ${liked ? 'fill-current' : ''}`} />{post.like_count + (liked ? 1 : 0)}
          </button>
          <button className="flex items-center gap-2 text-sm text-muted-foreground"><MessageCircle className="h-5 w-5" />{post.comment_count}</button>
          <button className="flex items-center gap-2 text-sm text-muted-foreground ml-auto"><Share2 className="h-5 w-5" /></button>
        </div>
      </CardContent>
    </Card>
  )
}
