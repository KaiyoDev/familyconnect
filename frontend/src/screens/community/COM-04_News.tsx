import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Badge } from '@/components/ui/basic'
import { Bell, Megaphone, Calendar } from 'lucide-react'

export default function Com04News() {
  const [news] = useState([
    { id: '1', title: 'Thông báo nghỉ lễ国庆节', content: 'Gia đình nghỉ phép từ 1/10 đến 7/10. Chúc mọi người có kỳ nghỉ vui vẻ!', date: '2026-09-28', type: 'announcement', read: false },
    { id: '2', title: 'Lịch họ tháng 10', content: 'Các sự kiện tháng 10: Giỗ tổ (10/10), Họp mặt (25/10). Vui lòng RSVP sớm.', date: '2026-09-25', type: 'news', read: true },
    { id: '3', title: 'Đóng góp quỹ gia đình', content: 'Mục tiêu quỹ năm 2026: 500 triệu VND. Hiện tại đạt 320 triệu. Mọi người cùng đóng góp nhé!', date: '2026-09-20', type: 'news', read: true },
  ])

  const [filter, setFilter] = useState<'all' | 'news' | 'announcement'>('all')

  const filteredNews = news.filter(n => filter === 'all' || n.type === filter)

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Tin tức gia đình</h1>
            <p className="text-neutral-600">Cập nhật thông tin và sự kiện</p>
          </div>
          <Button>
            <Megaphone className="h-4 w-4 mr-2" />
            Đăng thông báo
          </Button>
        </div>

        {/* Filters */}
        <div className="flex gap-2">
          {(['all', 'news', 'announcement'] as const).map((f) => (
            <button
              key={f}
              onClick={() => setFilter(f)}
              className={`px-4 py-2 rounded-full text-sm font-medium ${
                filter === f ? 'bg-primary text-white' : 'bg-background border border-border'
              }`}
            >
              {f === 'all' ? 'Tất cả' : f === 'news' ? 'Tin tức' : 'Thông báo'}
            </button>
          ))}
        </div>

        {/* News List */}
        <div className="space-y-4">
          {filteredNews.map((item) => (
            <NewsCard key={item.id} item={item} />
          ))}
        </div>

        {filteredNews.length === 0 && (
          <div className="text-center py-12">
            <Bell className="h-12 w-12 text-muted-foreground mx-auto mb-4" />
            <p className="text-neutral-600">Không có tin nào</p>
          </div>
        )}
      </div>
    </Layout>
  )
}

function NewsCard({ item }: { item: { id: string; title: string; content: string; date: string; type: string; read: boolean } }) {
  return (
    <Card className={!item.read ? 'border-primary/30 bg-primary/5' : ''}>
      <CardHeader className="flex flex-row items-center justify-between pb-2">
        <div className="flex items-center gap-2">
          <Badge variant={item.type === 'announcement' ? 'destructive' : 'info'}>
            {item.type === 'announcement' ? 'Thông báo' : 'Tin tức'}
          </Badge>
          {!item.read && <span className="w-2 h-2 rounded-full bg-primary" />}
        </div>
        <span className="text-sm text-muted-foreground">{new Date(item.date).toLocaleDateString('vi-VN')}</span>
      </CardHeader>
      <CardContent>
        <h3 className="font-semibold mb-2">{item.title}</h3>
        <p className="text-neutral-600 text-sm">{item.content}</p>
      </CardContent>
    </Card>
  )
}
