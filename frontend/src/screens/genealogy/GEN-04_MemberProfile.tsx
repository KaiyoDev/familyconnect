import React, { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button } from '@/components/ui/basic'
import { Badge } from '@/components/ui/basic'
import { 
  Edit, Trash2, Phone, Mail, Calendar, 
  MapPin, GraduationCap, Briefcase,
  ArrowLeft, User, Heart 
} from 'lucide-react'
import { memberApi } from '@/services/api'

export default function Gen04MemberProfile() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [member, setMember] = useState({
    id: id,
    name: 'Nguyễn Văn An',
    gender: 'MALE' as const,
    birthDate: '1990-05-15',
    deathDate: null,
    photoUrl: null,
    profession: 'Kỹ sư phần mềm',
    education: [
      { id: '1', degree: 'Cử nhân', school: 'ĐH Bách Khoa', field: 'Công nghệ thông tin', startYear: 2008, endYear: 2012 },
    ],
    relationships: [
      { type: 'father', name: 'Nguyễn Văn Cha' },
      { type: 'mother', name: 'Trần Thị Mẹ' },
      { type: 'spouse', name: 'Lê Thị Vợ' },
      { type: 'child', name: 'Nguyễn Văn Con' },
    ],
    family_id: 'default-family-id',
  })

  return (
    <Layout>
      <div className="space-y-6">
        {/* Back button */}
        <Button variant="ghost" onClick={() => navigate(-1)} className="pl-0">
          <ArrowLeft className="h-4 w-4 mr-2" />
          Quay lại
        </Button>

        {/* Header */}
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div className="flex items-center gap-4">
            <div className={`w-20 h-20 rounded-full flex items-center justify-center text-2xl font-bold ${
              member.gender === 'MALE' ? 'bg-primary/10 text-primary' : 'bg-pink/10 text-pink'
            }`}>
              {member.name.split(' ').pop()?.[0] || 'U'}
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-2xl font-bold text-neutral-900">{member.name}</h1>
                <Badge variant={member.gender === 'MALE' ? 'default' : 'secondary'}>
                  {member.gender === 'MALE' ? 'Nam' : 'Nữ'}
                </Badge>
              </div>
              <p className="text-neutral-600">
                {member.birthDate ? `Sinh ${new Date(member.birthDate).toLocaleDateString('vi-VN')}` : ''}
                {member.deathDate && ` - Mất ${new Date(member.deathDate).toLocaleDateString('vi-VN')}`}
              </p>
            </div>
          </div>
          <div className="flex gap-2">
            <Button variant="outline" onClick={() => navigate(`/genealogy/set-relationship?memberId=${id}`)}>
              <User className="h-4 w-4 mr-2" />
              Quan hệ
            </Button>
            <Button variant="outline">
              <Edit className="h-4 w-4 mr-2" />
              Sửa
            </Button>
            <Button variant="danger">
              <Trash2 className="h-4 w-4 mr-2" />
              Xóa
            </Button>
          </div>
        </div>

        <div className="grid lg:grid-cols-3 gap-6">
          {/* Main Info */}
          <div className="lg:col-span-2 space-y-6">
            {/* Personal Info */}
            <Card>
              <CardHeader>
                <CardTitle>Thông tin cá nhân</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="grid sm:grid-cols-2 gap-4">
                  <InfoItem icon={Calendar} label="Ngày sinh" value={member.birthDate ? new Date(member.birthDate).toLocaleDateString('vi-VN') : 'Chưa cập nhật'} />
                  <InfoItem icon={MapPin} label="Nơi sinh" value="Hà Nội" />
                  <InfoItem icon={Briefcase} label="Nghề nghiệp" value={member.profession || 'Chưa cập nhật'} />
                  <InfoItem icon={Mail} label="Email" value="nguyenvanan@example.com" />
                  <InfoItem icon={Phone} label="Điện thoại" value="0912 345 678" />
                </div>
              </CardContent>
            </Card>

            {/* Education */}
            <Card>
              <CardHeader>
                <CardTitle>Học vấn</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  {member.education.map((edu) => (
                    <div key={edu.id} className="flex items-start gap-3 p-3 bg-neutral-50 rounded-lg">
                      <GraduationCap className="h-5 w-5 text-primary mt-0.5 flex-shrink-0" />
                      <div>
                        <p className="font-medium">{edu.degree} - {edu.school}</p>
                        <p className="text-sm text-muted-foreground">{edu.field}</p>
                        <p className="text-xs text-muted-foreground">{edu.startYear} - {edu.endYear}</p>
                      </div>
                    </div>
                  ))}
                  <Button variant="outline" size="sm" className="ml-8">
                    <Plus className="h-4 w-4 mr-2" />
                    Thêm học vấn
                  </Button>
                </div>
              </CardContent>
            </Card>

            {/* Relationships */}
            <Card>
              <CardHeader>
                <CardTitle>Mối quan hệ gia đình</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid sm:grid-cols-2 gap-4">
                  {member.relationships.map((rel, idx) => (
                    <div key={idx} className="flex items-center gap-3 p-3 bg-neutral-50 rounded-lg">
                      <Heart className="h-5 w-5 text-primary" />
                      <div>
                        <p className="text-sm text-muted-foreground">{rel.type === 'father' ? 'Cha' : rel.type === 'mother' ? 'Mẹ' : rel.type === 'spouse' ? 'Vợ/chồng' : 'Con'}</p>
                        <p className="font-medium">{rel.name}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Sidebar */}
          <div className="space-y-6">
            {/* Quick Actions */}
            <Card>
              <CardHeader>
                <CardTitle>Thao tác nhanh</CardTitle>
              </CardHeader>
              <CardContent className="space-y-2">
                <Button variant="outline" className="w-full justify-start" onClick={() => navigate(`/genealogy/add-member?parent=${id}`)}>
                  <Plus className="h-4 w-4 mr-2" />
                  Thêm con
                </Button>
                <Button variant="outline" className="w-full justify-start">
                  <Plus className="h-4 w-4 mr-2" />
                  Thêm ảnh
                </Button>
                <Button variant="outline" className="w-full justify-start">
                  <Share2 className="h-4 w-4 mr-2" />
                  Chia sẻ hồ sơ
                </Button>
              </CardContent>
            </Card>

            {/* Family Tree Position */}
            <Card>
              <CardHeader>
                <CardTitle>Vị trí trong gia phả</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-center py-4">
                  <div className="w-16 h-16 rounded-full bg-primary/10 flex items-center justify-center mx-auto mb-3">
                    <span className="text-2xl font-bold text-primary">NA</span>
                  </div>
                  <p className="font-medium">Nguyễn Văn An</p>
                  <p className="text-sm text-muted-foreground">Thế hệ thứ 4</p>
                  <div className="mt-4 text-sm text-muted-foreground">
                    <p>Con của: Nguyễn Văn Cha</p>
                    <p>Anh/chị của: Nguyễn Thị Con 2</p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </Layout>
  )
}

function InfoItem({ icon: Icon, label, value }: { icon: React.ElementType; label: string; value: string }) {
  return (
    <div className="flex items-start gap-3">
      <Icon className="h-5 w-5 text-muted-foreground mt-0.5" />
      <div>
        <p className="text-sm text-muted-foreground">{label}</p>
        <p className="font-medium">{value}</p>
      </div>
    </div>
  )
}

function Plus(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14"/><path d="M12 5v14"/></svg>
  )
}

function Share2(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/></svg>
  )
}
