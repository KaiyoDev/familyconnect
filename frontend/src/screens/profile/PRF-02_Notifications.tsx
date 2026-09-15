import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button } from '@/components/ui/basic'
import { Bell, Check, Trash2 } from 'lucide-react'

interface Notification {
  id: string
  type: 'POST_COMMENT' | 'EVENT_RSV' | 'MEMBER_REQUEST' | 'SYSTEM' | 'ANNOUNCEMENT'
  title: string
  message: string
  is_read: boolean
  time: string
}

const typeIcons: Record<string, string> = {
  POST_COMMENT: '💬',
  EVENT_RSV: '📅',
  MEMBER_REQUEST: '👤',
  SYSTEM: '⚙️',
  ANNOUNCEMENT: '📢',
}

export default function Prf02Notifications() {
  const [notifications, setNotifications] = useState<Notification[]>([
    { id: '1', type: 'POST_COMMENT', title: 'Bình luận mới', message: 'Trần Thị B đã bình luận vào bài viết của bạn', is_read: false, time: '5 phút trước' },
    { id: '2', type: 'EVENT_RSV', title: 'RSVP sự kiện', message: 'Lê Văn C đã xác nhận tham gia sự kiện "Giỗ tổ"', is_read: false, time: '1 giờ trước' },
    { id: '3', type: 'MEMBER_REQUEST', title: 'Yêu cầu tham gia', message: 'Phạm Văn D yêu cầu tham gia gia đình', is_read: true, time: '2 giờ trước' },
    { id: '4', type: 'ANNOUNCEMENT', title: 'Thông báo hệ thống', message: 'Gia đình đã có 25 thành viên', is_read: true, time: '1 ngày trước' },
  ])

  const markAsRead = (id: string) => {
    setNotifications(notifications.map(n => n.id === id ? { ...n, is_read: true } : n))
  }

  const markAllAsRead = () => {
    setNotifications(notifications.map(n => ({ ...n, is_read: true })))
  }

  const deleteNotification = (id: string) => {
    setNotifications(notifications.filter(n => n.id !== id))
  }

  const unreadCount = notifications.filter(n => !n.is_read).length

  return (
    <Layout>
      <div className="space-y-6 max-w-2xl mx-auto">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Thông báo</h1>
            <p className="text-neutral-600">{unreadCount} thông báo chưa đọc</p>
          </div>
          {unreadCount > 0 && (
            <Button variant="outline" size="sm" onClick={markAllAsRead}>
              <Check className="h-4 w-4 mr-2" />
              Đánh dấu đã đọc
            </Button>
          )}
        </div>

        <div className="space-y-3">
          {notifications.map((notif) => (
            <NotificationItem
              key={notif.id}
              notification={notif}
              onMarkRead={() => markAsRead(notif.id)}
              onDelete={() => deleteNotification(notif.id)}
            />
          ))}
        </div>

        {notifications.length === 0 && (
          <div className="text-center py-12">
            <Bell className="h-12 w-12 text-muted-foreground mx-auto mb-4" />
            <p className="text-neutral-600">Không có thông báo nào</p>
          </div>
        )}
      </div>
    </Layout>
  )
}

function NotificationItem({ notification, onMarkRead, onDelete }: {
  notification: Notification
  onMarkRead: () => void
  onDelete: () => void
}) {
  return (
    <div
      className={`flex items-start gap-3 p-4 rounded-lg border cursor-pointer transition-colors ${
        notification.is_read ? 'border-border bg-background' : 'border-primary/30 bg-primary/5'
      }`}
      onClick={onMarkRead}
    >
      <div className="text-2xl">{typeIcons[notification.type]}</div>
      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-2">
          <p className="font-medium">{notification.title}</p>
          {!notification.is_read && <span className="w-2 h-2 rounded-full bg-primary" />}
        </div>
        <p className="text-sm text-muted-foreground">{notification.message}</p>
        <p className="text-xs text-muted-foreground mt-1">{notification.time}</p>
      </div>
      <Button variant="ghost" size="icon" onClick={(e) => { e.stopPropagation(); onDelete(); }}>
        <Trash2 className="h-4 w-4 text-muted-foreground" />
      </Button>
    </div>
  )
}
