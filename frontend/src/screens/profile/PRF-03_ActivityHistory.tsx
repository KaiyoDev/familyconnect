import React from 'react'
import Layout from '@/components/Layout'
import { Button, Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Download, FileText } from 'lucide-react'

interface Activity {
  id: string
  action: string
  target: string
  time: string
  icon: string
}

export default function Prf03ActivityHistory() {
  const activities: Activity[] = [
    { id: '1', action: 'Đăng nhập', target: '', time: '2026-09-09T10:30:00Z', icon: '🔐' },
    { id: '2', action: 'Đăng bài viết', target: 'Họp mặt gia đình', time: '2026-09-09T09:15:00Z', icon: '📝' },
    { id: '3', action: 'RSVP sự kiện', target: 'Giỗ tổ họ Nguyễn', time: '2026-09-08T14:20:00Z', icon: '📅' },
    { id: '4', action: 'Bình luận', target: 'Bài viết của Trần Thị B', time: '2026-09-08T11:00:00Z', icon: '💬' },
    { id: '5', action: 'Thêm thành viên', target: 'Nguyễn Văn E', time: '2026-09-07T16:45:00Z', icon: '👤' },
    { id: '6', action: 'Tải tư liệu', target: 'Sắc phong năm 1920', time: '2026-09-06T09:30:00Z', icon: '📄' },
  ]

  return (
    <Layout>
      <div className="space-y-6 max-w-2xl mx-auto">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Lịch sử hoạt động</h1>
            <p className="text-neutral-600">Theo dõi các hoạt động gần đây</p>
          </div>
          <Button variant="outline">
            <Download className="h-4 w-4 mr-2" />
            Xuất báo cáo
          </Button>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Hoạt động của bạn</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-0">
              {activities.map((activity, idx) => (
                <div key={activity.id} className="flex items-start gap-4 py-4">
                  <div className="w-10 h-10 rounded-full bg-neutral-100 flex items-center justify-center text-xl flex-shrink-0">
                    {activity.icon}
                  </div>
                  <div className="flex-1">
                    <p className="font-medium">
                      {activity.action}
                      {activity.target && <span className="text-muted-foreground"> — {activity.target}</span>}
                    </p>
                    <p className="text-sm text-muted-foreground">
                      {new Date(activity.time).toLocaleString('vi-VN')}
                    </p>
                  </div>
                  <FileText className="h-4 w-4 text-muted-foreground flex-shrink-0" />
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}
