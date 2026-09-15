import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Badge } from '@/components/ui/basic'
import { BookOpen, Plus, Edit, Trash2 } from 'lucide-react'
import { useNavigate } from 'react-router-dom'

interface Story {
  id: string
  title: string
  content: string
  category: string
  author: string
  date: string
  status: 'PENDING' | 'APPROVED' | 'REJECTED'
}

export default function Her03FamilyStories() {
  const navigate = useNavigate()
  const [stories] = useState<Story[]>([
    { id: '1', title: 'Câu chuyện ông nội', content: 'Ông nội tôi từng là một người thầy...', category: 'Kỷ niệm', author: 'Nguyễn Văn A', date: '2026-09-05', status: 'APPROVED' },
    { id: '2', title: 'Ngày lập nghiệp', content: 'Năm 1975, gia đình tôi di cư...', category: 'Lịch sử', author: 'Trần Thị B', date: '2026-09-03', status: 'PENDING' },
  ])

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Câu chuyện gia đình</h1>
            <p className="text-neutral-600">{stories.length} câu chuyện</p>
          </div>
          <Button>
            <Plus className="h-4 w-4 mr-2" />
            Viết câu chuyện
          </Button>
        </div>

        {/* Stories Grid */}
        <div className="grid md:grid-cols-2 gap-4">
          {stories.map((story) => (
            <StoryCard key={story.id} story={story} />
          ))}
        </div>
      </div>
    </Layout>
  )
}

function StoryCard({ story }: { story: Story }) {
  return (
    <Card className="cursor-pointer hover:border-primary/50 transition-colors">
      <CardHeader>
        <div className="flex items-start justify-between">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <Badge variant="secondary">{story.category}</Badge>
              {story.status === 'PENDING' && <Badge variant="warning">Chờ duyệt</Badge>}
            </div>
            <CardTitle>{story.title}</CardTitle>
          </div>
          <div className="flex gap-1">
            <Button variant="ghost" size="icon">
              <Edit className="h-4 w-4" />
            </Button>
            <Button variant="ghost" size="icon">
              <Trash2 className="h-4 w-4 text-destructive" />
            </Button>
          </div>
        </div>
      </CardHeader>
      <CardContent>
        <p className="text-neutral-600 line-clamp-3">{story.content}</p>
        <div className="flex items-center justify-between mt-4 text-sm text-muted-foreground">
          <span>Bởi {story.author}</span>
          <span>{new Date(story.date).toLocaleDateString('vi-VN')}</span>
        </div>
      </CardContent>
    </Card>
  )
}
