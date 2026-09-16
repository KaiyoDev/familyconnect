import React, { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Input, Badge, Avatar } from '@/components/ui/basic'
import { memberApi } from '@/services/api'
import { Plus, Search, Filter, MoreVertical } from 'lucide-react'

interface Member {
  id: string
  name: string
  gender: 'MALE' | 'FEMALE'
  branch?: string
  role: 'OWNER' | 'ADMIN' | 'MEMBER'
  photo_url?: string
}

export default function Fam04MemberList() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [searchTerm, setSearchTerm] = useState('')
  const [filterRole, setFilterRole] = useState<string>('all')
  
  const [members, setMembers] = useState<Member[]>([
    { id: '1', name: 'Nguyễn Văn A', gender: 'MALE', branch: 'Nhánh chính', role: 'OWNER', photo_url: null },
    { id: '2', name: 'Trần Thị B', gender: 'FEMALE', branch: 'Nhánh chính', role: 'ADMIN', photo_url: null },
    { id: '3', name: 'Nguyễn Văn C', gender: 'MALE', branch: 'Nhánh Bắc', role: 'MEMBER', photo_url: null },
    { id: '4', name: 'Nguyễn Thị D', gender: 'FEMALE', branch: 'Nhánh Nam', role: 'MEMBER', photo_url: null },
  ])

  const filteredMembers = members.filter(m => {
    const matchesSearch = m.name.toLowerCase().includes(searchTerm.toLowerCase())
    const matchesRole = filterRole === 'all' || m.role.toLowerCase() === filterRole
    return matchesSearch && matchesRole
  })

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Danh sách thành viên</h1>
            <p className="text-neutral-600">{members.length} thành viên</p>
          </div>
          <Button onClick={() => navigate('/genealogy/add-member')}>
            <Plus className="h-4 w-4 mr-2" />
            Thêm thành viên
          </Button>
        </div>

        {/* Filters */}
        <Card>
          <CardContent className="p-4">
            <div className="flex flex-col sm:flex-row gap-4">
              <div className="relative flex-1">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
                <Input
                  placeholder="Tìm kiếm thành viên..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="pl-9"
                />
              </div>
              <div className="flex gap-2">
                <select
                  className="h-10 rounded-md border border-input bg-background px-3 py-2 text-sm"
                  value={filterRole}
                  onChange={(e) => setFilterRole(e.target.value)}
                >
                  <option value="all">Tất cả vai trò</option>
                  <option value="owner">Owner</option>
                  <option value="admin">Admin</option>
                  <option value="member">Member</option>
                </select>
                <Button variant="outline" size="icon">
                  <Filter className="h-4 w-4" />
                </Button>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Member List */}
        <div className="space-y-3">
          {filteredMembers.map((member) => (
            <MemberCard
              key={member.id}
              member={member}
              onClick={() => navigate(`/genealogy/member/${member.id}`)}
            />
          ))}
        </div>

        {filteredMembers.length === 0 && (
          <div className="text-center py-12">
            <Users className="h-12 w-12 text-muted-foreground mx-auto mb-4" />
            <p className="text-neutral-600">Không tìm thấy thành viên nào</p>
          </div>
        )}
      </div>
    </Layout>
  )
}

function MemberCard({ member, onClick }: { member: Member; onClick: () => void }) {
  const roleColors = {
    OWNER: 'bg-accent',
    ADMIN: 'bg-primary',
    MEMBER: 'bg-neutral-200',
  }

  const roleLabels = {
    OWNER: 'Chủ họ',
    ADMIN: 'Quản lý',
    MEMBER: 'Thành viên',
  }

  return (
    <div
      onClick={onClick}
      className="flex items-center gap-4 p-4 bg-background rounded-lg border border-border hover:border-primary/50 cursor-pointer transition-colors"
    >
      <Avatar src={member.photo_url} fallback={member.name.split(' ').pop()?.[0] || 'U'} />
      <div className="flex-1">
        <div className="flex items-center gap-2">
          <p className="font-medium">{member.name}</p>
          <span className={`px-2 py-0.5 rounded-full text-xs font-medium ${roleColors[member.role]}`}>
            {roleLabels[member.role]}
          </span>
        </div>
        <p className="text-sm text-muted-foreground">{member.branch || 'Không có nhánh'}</p>
      </div>
      <MoreVertical className="h-5 w-5 text-muted-foreground" />
    </div>
  )
}

function Users(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
  )
}
