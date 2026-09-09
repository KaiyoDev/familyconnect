import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Badge } from '@/components/ui/basic'
import { FileText, Search, Download, Filter } from 'lucide-react'
import { useNavigate } from 'react-router-dom'

export default function Adm04AuditLog() {
  const navigate = useNavigate()
  const [logs] = useState([
    { id: '1', action: 'USER_LOGIN', user: 'nguyenvana@example.com', ip: '192.168.1.1', time: '2026-09-09T10:30:00Z', details: 'Đăng nhập thành công' },
    { id: '2', action: 'FAMILY_CREATE', user: 'tranthib@example.com', ip: '192.168.1.2', time: '2026-09-09T09:15:00Z', details: 'Tạo gia đình "Họ Trần"' },
    { id: '3', action: 'MEMBER_ADD', user: 'levanc@example.com', ip: '192.168.1.3', time: '2026-09-08T14:20:00Z', details: 'Thêm thành viên Nguyễn Văn E' },
    { id: '4', action: 'POST_DELETE', user: 'admin@example.com', ip: '192.168.1.4', time: '2026-09-08T11:00:00Z', details: 'Xóa bài viết vi phạm #1234' },
  ])

  const actionColors: Record<string, string> = {
    USER_LOGIN: 'bg-success/10 text-success',
    FAMILY_CREATE: 'bg-primary/10 text-primary',
    MEMBER_ADD: 'bg-info/10 text-info',
    POST_DELETE: 'bg-destructive/10 text-destructive',
  }

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Nhật ký kiểm toán</h1>
            <p className="text-neutral-600">Theo dõi mọi hoạt động trên hệ thống</p>
          </div>
          <Button variant="outline">
            <Download className="h-4 w-4 mr-2" />
            Xuất báo cáo
          </Button>
        </div>

        <Card>
          <CardContent className="p-4">
            <div className="flex gap-4">
              <div className="relative flex-1">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
                <input
                  type="text"
                  placeholder="Tìm kiếm theo hành động, người dùng..."
                  className="input pl-9 pr-4 w-full"
                />
              </div>
              <Button variant="outline" size="icon">
                <Filter className="h-4 w-4" />
              </Button>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-0">
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b bg-neutral-50">
                    <th className="text-left py-3 px-4 font-medium">Thời gian</th>
                    <th className="text-left py-3 px-4 font-medium">Hành động</th>
                    <th className="text-left py-3 px-4 font-medium">Người dùng</th>
                    <th className="text-left py-3 px-4 font-medium">IP</th>
                    <th className="text-left py-3 px-4 font-medium">Chi tiết</th>
                  </tr>
                </thead>
                <tbody>
                  {logs.map((log) => (
                    <tr key={log.id} className="border-b hover:bg-neutral-50">
                      <td className="py-3 px-4 text-muted-foreground">
                        {new Date(log.time).toLocaleString('vi-VN')}
                      </td>
                      <td className="py-3 px-4">
                        <span className={`px-2 py-1 rounded-full text-xs font-medium ${actionColors[log.action] || 'bg-neutral-100'}`}>
                          {log.action.replace(/_/g, ' ')}
                        </span>
                      </td>
                      <td className="py-3 px-4 font-medium">{log.user}</td>
                      <td className="py-3 px-4 text-muted-foreground font-mono text-xs">{log.ip}</td>
                      <td className="py-3 px-4 text-muted-foreground">{log.details}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}
