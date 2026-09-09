import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Badge } from '@/components/ui/basic'
import { Shield, Check, X, Eye } from 'lucide-react'
import { useNavigate } from 'react-router-dom'

interface ModerationItem {
  id: string
  type: 'post' | 'comment' | 'story' | 'document'
  author: string
  content: string
  reported_by: string
  reported_at: string
  status: 'pending' | 'approved' | 'removed'
}

export default function Adm03Moderation() {
  const navigate = useNavigate()
  const [items] = useState<ModerationItem[]>([
    { id: '1', type: 'post', author: 'Nguyễn Văn A', content: 'Nội dung bị báo cáo vi phạm...', reported_by: 'Trần Thị B', reported_at: '2026-09-09', status: 'pending' },
    { id: '2', type: 'comment', author: 'Lê Văn C', content: 'Bình luận không phù hợp...', reported_by: 'Phạm Thị D', reported_at: '2026-09-08', status: 'pending' },
  ])

  const handleAction = (id: string, action: 'approve' | 'remove') => {
    // Handle moderation action
    console.log(action, id)
  }

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Kiểm duyệt nội dung</h1>
            <p className="text-neutral-600">{items.filter(i => i.status === 'pending').length} mục đang chờ xử lý</p>
          </div>
        </div>

        <div className="space-y-4">
          {items.map((item) => (
            <ModerationCard key={item.id} item={item} onApprove={() => handleAction(item.id, 'approve')} onRemove={() => handleAction(item.id, 'remove')} />
          ))}
        </div>
      </div>
    </Layout>
  )
}

function ModerationCard({ item, onApprove, onRemove }: {
  item: ModerationItem
  onApprove: () => void
  onRemove: () => void
}) {
  const typeLabels = {
    post: 'Bài viết',
    comment: 'Bình luận',
    story: 'Câu chuyện',
    document: 'Tư liệu',
  }

  return (
    <Card>
      <CardHeader>
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Badge variant="secondary">{typeLabels[item.type]}</Badge>
            <span className="text-sm text-muted-foreground">Bởi {item.author}</span>
          </div>
          <Badge variant="warning">Chờ xử lý</Badge>
        </div>
      </CardHeader>
      <CardContent>
        <p className="bg-neutral-50 p-3 rounded-lg mb-4">{item.content}</p>
        <div className="flex items-center justify-between text-sm text-muted-foreground mb-4">
          <span>Báo cáo bởi: {item.reported_by}</span>
          <span>{new Date(item.reported_at).toLocaleDateString('vi-VN')}</span>
        </div>
        <div className="flex gap-2">
          <Button variant="outline" size="sm" onClick={onApprove}>
            <Check className="h-4 w-4 mr-2 text-success" />
            Phê duyệt
          </Button>
          <Button variant="outline" size="sm" className="border-danger text-danger hover:bg-danger-bg" onClick={onRemove}>
            <X className="h-4 w-4 mr-2" />
            Gỡ bỏ
          </Button>
          <Button variant="ghost" size="sm">
            <Eye className="h-4 w-4 mr-2" />
            Xem chi tiết
          </Button>
        </div>
      </CardContent>
    </Card>
  )
}
