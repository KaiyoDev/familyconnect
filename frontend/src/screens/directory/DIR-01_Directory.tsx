import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Input, Badge } from '@/components/ui/basic'
import { Search, Filter, User } from 'lucide-react'
import { useNavigate } from 'react-router-dom'

interface Member {
  id: string
  name: string
  gender: 'MALE' | 'FEMALE'
  branch: string
  profession?: string
  photo_url?: string
}

export default function Dir01Directory() {
  const navigate = useNavigate()
  const [searchTerm, setSearchTerm] = useState('')
  const [members] = useState<Member[]>([
    { id: '1', name: 'Nguyễn Văn A', gender: 'MALE', branch: 'Nhánh chính', profession: 'Giám đốc' },
    { id: '2', name: 'Trần Thị B', gender: 'FEMALE', branch: 'Nhánh chính', profession: 'Giáo viên' },
    { id: '3', name: 'Nguyễn Văn C', gender: 'MALE', branch: 'Nhánh Bắc', profession: 'Kỹ sư' },
    { id: '4', name: 'Nguyễn Thị D', gender: 'FEMALE', branch: 'Nhánh Nam' },
    { id: '5', name: 'Lê Văn E', gender: 'MALE', branch: 'Nhánh chính', profession: 'Bác sĩ' },
  ])

  const filteredMembers = members.filter(m =>
    m.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    m.branch.toLowerCase().includes(searchTerm.toLowerCase())
  )

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Danh bạ gia đình</h1>
            <p className="text-neutral-600">{members.length} thành viên</p>
          </div>
        </div>

        {/* Search */}
        <div className="relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-muted-foreground" />
          <Input
            placeholder="Tìm kiếm theo tên, nhánh..."
            className="pl-10 pr-4 py-6 text-base rounded-xl"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>

        {/* Members Grid */}
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {filteredMembers.map((member) => (
            <MemberCard key={member.id} member={member} onClick={() => navigate(`/directory/${member.id}`)} />
          ))}
        </div>

        {filteredMembers.length === 0 && (
          <div className="text-center py-12">
            <User className="h-12 w-12 text-muted-foreground mx-auto mb-4" />
            <p className="text-neutral-600">Không tìm thấy thành viên nào</p>
          </div>
        )}
      </div>
    </Layout>
  )
}

function MemberCard({ member, onClick }: { member: Member; onClick: () => void }) {
  return (
    <Card className="cursor-pointer hover:border-primary/50 transition-colors" onClick={onClick}>
      <CardContent className="p-4 flex items-center gap-4">
        <div className={`w-12 h-12 rounded-full flex items-center justify-center text-lg font-medium ${
          member.gender === 'MALE' ? 'bg-primary/10 text-primary' : 'bg-pink/10 text-pink'
        }`}>
          {member.name.split(' ').pop()?.[0] || 'U'}
        </div>
        <div className="flex-1 min-w-0">
          <p className="font-medium truncate">{member.name}</p>
          <p className="text-sm text-muted-foreground">{member.branch}</p>
          {member.profession && (
            <p className="text-xs text-muted-foreground">{member.profession}</p>
          )}
        </div>
      </CardContent>
    </Card>
  )
}
