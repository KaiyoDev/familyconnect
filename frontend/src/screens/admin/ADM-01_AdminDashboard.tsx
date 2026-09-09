import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Badge } from '@/components/ui/basic'
import { Users, Shield, FileText, Database, Settings, Plus } from 'lucide-react'
import { useNavigate } from 'react-router-dom'

export default function Adm01AdminDashboard() {
  const navigate = useNavigate()
  const [stats] = useState({
    totalUsers: 1250,
    activeUsers: 342,
    families: 89,
    pendingModeration: 12,
    systemStatus: 'operational' as 'operational' | 'degraded' | 'down',
  })

  const quickActions = [
    { icon: Users, label: 'Quản lý người dùng', path: '/admin/users' },
    { icon: Shield, label: 'Kiểm duyệt', path: '/admin/moderation', badge: stats.pendingModeration },
    { icon: FileText, label: 'Nhật ký kiểm toán', path: '/admin/audit-log' },
    { icon: Database, label: 'Sao lưu & phục hồi', path: '/admin/backup' },
    { icon: Settings, label: 'Cấu hình hệ thống', path: '/admin/settings' },
  ]

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Admin Dashboard</h1>
            <p className="text-neutral-600">Quản trị hệ thống FamilyConnect</p>
          </div>
          <Badge variant={stats.systemStatus === 'operational' ? 'success' : 'warning'}>
            {stats.systemStatus === 'operational' ? 'Hoạt động bình thường' : 'Có vấn đề'}
          </Badge>
        </div>

        {/* Stats */}
        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <StatCard label="Tổng người dùng" value={stats.totalUsers} icon={Users} />
          <StatCard label="Người dùng hoạt động" value={stats.activeUsers} icon={Users} />
          <StatCard label="Gia đình" value={stats.families} icon={Users} />
          <StatCard label="Cần kiểm duyệt" value={stats.pendingModeration} icon={Shield} variant="warning" />
        </div>

        {/* Quick Actions */}
        <div>
          <h2 className="text-lg font-semibold mb-4">Thao tác nhanh</h2>
          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {quickActions.map((action) => (
              <button
                key={action.label}
                onClick={() => navigate(action.path)}
                className="flex items-center gap-4 p-4 bg-background rounded-lg border border-border hover:border-primary/50 transition-colors text-left"
              >
                <div className="w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center">
                  <action.icon className="h-6 w-6 text-primary" />
                </div>
                <div className="flex-1">
                  <p className="font-medium">{action.label}</p>
                </div>
                {action.badge && (
                  <Badge variant="destructive">{action.badge}</Badge>
                )}
              </button>
            ))}
          </div>
        </div>

        {/* Recent Activity */}
        <Card>
          <CardHeader>
            <CardTitle>Hoạt động gần đây</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {[
                { action: 'Người dùng mới đăng ký', user: 'tranthib@example.com', time: '5 phút trước' },
                { action: 'Gia đình mới được tạo', user: 'Họ Lê - TP HCM', time: '1 giờ trước' },
                { action: 'Nội dung bị báo cáo', user: 'Bài viết #1234', time: '2 giờ trước' },
                { action: 'Backup tự động', user: 'Hệ thống', time: '6 giờ trước' },
              ].map((activity, idx) => (
                <div key={idx} className="flex items-center justify-between py-2 border-b border-border last:border-0">
                  <div>
                    <p className="font-medium">{activity.action}</p>
                    <p className="text-sm text-muted-foreground">{activity.user}</p>
                  </div>
                  <span className="text-sm text-muted-foreground">{activity.time}</span>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}

function StatCard({ label, value, icon: Icon, variant = 'default' }: {
  label: string
  value: number
  icon: React.ElementType
  variant?: string
}) {
  const colors = {
    default: 'bg-primary/10 text-primary',
    warning: 'bg-warning/10 text-warning',
  }
  
  return (
    <Card>
      <CardContent className="p-4 flex items-center gap-4">
        <div className={`w-12 h-12 rounded-lg ${colors[variant as keyof typeof colors]} flex items-center justify-center`}>
          <Icon className="h-6 w-6" />
        </div>
        <div>
          <p className="text-2xl font-bold">{value.toLocaleString()}</p>
          <p className="text-sm text-muted-foreground">{label}</p>
        </div>
      </CardContent>
    </Card>
  )
}
