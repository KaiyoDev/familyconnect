import React, { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Badge } from '@/components/ui/basic'
import { 
  Users, Settings, Plus, ArrowLeft, Edit, 
  FileText, Share2 
} from 'lucide-react'

export default function Fam02FamilyInfo() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [family] = useState({
    id,
    name: 'Gia đình Nguyễn Văn',
    description: 'Dòng họ Nguyễn Văn - Hà Nội',
    joinCode: 'NV-2026-XYZ',
    owner: 'Nguyễn Văn A',
    members: 24,
    branches: 3,
    created_at: '2026-01-15',
  })

  const menuItems = [
    { icon: Users, label: 'Thành viên', path: `/family/${id}/members`, count: family.members },
    { icon: Plus, label: 'Nhánh gia đình', path: `/family/${id}/branches`, count: family.branches },
    { icon: FileText, label: 'Yêu cầu tham gia', path: `/family/${id}/join-requests`, badge: 2 },
    { icon: Settings, label: 'Cài đặt', path: '#' },
    { icon: Share2, label: 'Chia sẻ mã gia tộc', path: '#' },
  ]

  return (
    <Layout>
      <div className="space-y-6">
        {/* Header */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-4">
            <Button variant="ghost" onClick={() => navigate('/dashboard')} className="pl-0">
              <ArrowLeft className="h-4 w-4 mr-2" />
              Quay lại
            </Button>
            <div>
              <h1 className="text-2xl font-bold text-neutral-900">{family.name}</h1>
              <p className="text-neutral-600">{family.description}</p>
            </div>
          </div>
          <div className="flex gap-2">
            <Button variant="outline">
              <Edit className="h-4 w-4 mr-2" />
              Chỉnh sửa
            </Button>
            <Button onClick={() => navigate(`/family/${id}/members`)}>
              <Plus className="h-4 w-4 mr-2" />
              Thêm thành viên
            </Button>
          </div>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-3 gap-4">
          <StatCard label="Thành viên" value={family.members} icon={Users} />
          <StatCard label="Nhánh" value={family.branches} icon={Users} />
          <StatCard label="Tham gia" value="2" icon={Users} />
        </div>

        {/* Join Code */}
        <Card>
          <CardHeader>
            <CardTitle>Mã gia tộc</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex items-center gap-4">
              <div className="flex-1 p-4 bg-neutral-50 rounded-lg text-center">
                <p className="text-2xl font-mono font-bold text-primary">{family.joinCode}</p>
                <p className="text-sm text-muted-foreground mt-1">Chia sẻ mã này để mời thành viên tham gia</p>
              </div>
              <Button onClick={() => navigator.clipboard.writeText(family.joinCode)}>
                <Copy className="h-4 w-4 mr-2" />
                Sao chép
              </Button>
            </div>
          </CardContent>
        </Card>

        {/* Menu */}
        <div className="space-y-2">
          <h2 className="text-lg font-semibold">Quản lý</h2>
          {menuItems.map((item, idx) => (
            <button
              key={idx}
              onClick={() => item.path !== '#' && navigate(item.path)}
              className="w-full flex items-center gap-4 p-4 bg-background rounded-lg border border-border hover:border-primary/50 transition-colors text-left"
            >
              <div className="w-10 h-10 rounded-lg bg-primary/10 flex items-center justify-center">
                <item.icon className="h-5 w-5 text-primary" />
              </div>
              <span className="flex-1 font-medium">{item.label}</span>
              {item.count !== undefined && (
                <Badge variant="secondary">{item.count}</Badge>
              )}
              {item.badge && (
                <Badge variant="destructive">{item.badge}</Badge>
              )}
              <ChevronRight className="h-5 w-5 text-muted-foreground" />
            </button>
          ))}
        </div>

        {/* Danger Zone */}
        <Card className="border-danger/20">
          <CardHeader>
            <CardTitle className="text-danger">Vùng nguy hiểm</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Chuyển quyền sở hữu</p>
                <p className="text-sm text-muted-foreground">Chuyển quyền quản lý gia đình cho thành viên khác</p>
              </div>
              <Button variant="outline">Chuyển giao</Button>
            </div>
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium text-danger">Xóa gia đình</p>
                <p className="text-sm text-muted-foreground">Hành động này không thể hoàn tác</p>
              </div>
              <Button variant="danger">Xóa</Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}

function StatCard({ label, value, icon: Icon }: { label: string; value: string | number; icon: React.ElementType }) {
  return (
    <Card>
      <CardContent className="p-4 flex items-center gap-4">
        <div className="w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center">
          <Icon className="h-6 w-6 text-primary" />
        </div>
        <div>
          <p className="text-2xl font-bold">{value}</p>
          <p className="text-sm text-muted-foreground">{label}</p>
        </div>
      </CardContent>
    </Card>
  )
}

function Copy(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>
  )
}

function ChevronRight(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m9 18 6-6-6-6"/></svg>
  )
}
