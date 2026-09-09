import React from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle, Button, Badge } from '@/components/ui/basic'
import { Search, Filter, Plus } from 'lucide-react'
import { useNavigate } from 'react-router-dom'

interface User {
  id: string
  email: string
  full_name: string
  system_role: 'ADMIN' | 'USER' | 'GUEST'
  family_count: number
  status: 'ACTIVE' | 'SUSPENDED'
  created_at: string
}

export default function Adm02UserManagement() {
  const navigate = useNavigate()
  const [searchTerm, setSearchTerm] = React.useState('')
  const [users] = React.useState<User[]>([
    { id: '1', email: 'nguyenvana@example.com', full_name: 'Nguyen Van A', system_role: 'USER', family_count: 1, status: 'ACTIVE', created_at: '2026-01-15' },
    { id: '2', email: 'tranthib@example.com', full_name: 'Tran Thi B', system_role: 'USER', family_count: 1, status: 'ACTIVE', created_at: '2026-02-20' },
    { id: '3', email: 'levanc@example.com', full_name: 'Le Van C', system_role: 'ADMIN', family_count: 2, status: 'ACTIVE', created_at: '2025-12-01' },
  ])

  const filtered = users.filter(u =>
    u.full_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    u.email.toLowerCase().includes(searchTerm.toLowerCase())
  )

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Quản lý người dùng</h1>
            <p className="text-neutral-600">{users.length} users</p>
          </div>
          <Button><Plus className="h-4 w-4 mr-2" />Thêm người dùng</Button>
        </div>

        <Card>
          <CardContent className="p-4">
            <div className="flex gap-4">
              <div className="relative flex-1">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
                <input placeholder="Tìm kiếm..." className="input pl-9" value={searchTerm} onChange={e => setSearchTerm(e.target.value)} />
              </div>
              <Button variant="outline" size="icon"><Filter className="h-4 w-4" /></Button>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-0">
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b bg-neutral-50">
                    <th className="text-left py-3 px-4 font-medium">Tên</th>
                    <th className="text-left py-3 px-4 font-medium">Email</th>
                    <th className="text-left py-3 px-4 font-medium">Vai trò</th>
                    <th className="text-left py-3 px-4 font-medium">Gia đình</th>
                    <th className="text-left py-3 px-4 font-medium">Trạng thái</th>
                    <th className="text-left py-3 px-4 font-medium">Hành động</th>
                  </tr>
                </thead>
                <tbody>
                  {filtered.map(u => (
                    <tr key={u.id} className="border-b hover:bg-neutral-50">
                      <td className="py-3 px-4 font-medium">{u.full_name}</td>
                      <td className="py-3 px-4 text-muted-foreground">{u.email}</td>
                      <td className="py-3 px-4"><Badge variant={u.system_role === 'ADMIN' ? 'default' : 'secondary'}>{u.system_role}</Badge></td>
                      <td className="py-3 px-4">{u.family_count}</td>
                      <td className="py-3 px-4"><Badge variant={u.status === 'ACTIVE' ? 'success' : 'destructive'}>{u.status === 'ACTIVE' ? 'Hoạt động' : 'Đã khóa'}</Badge></td>
                      <td className="py-3 px-4">
                        <Button variant="ghost" size="sm">Sửa</Button>
                      </td>
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
