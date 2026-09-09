import React from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button } from '@/components/ui/basic'
import { Award, Star } from 'lucide-react'

interface OutstandingMember {
  id: string
  name: string
  title: string
  description: string
  photo_url?: string
}

export default function Her04Outstanding() {
  const members: OutstandingMember[] = [
    { id: '1', name: 'Nguyễn Văn Tổ', title: 'Người sáng lập', description: 'Đức ngài đã khởi nghiệp và xây dựng nghiệp gia từ năm 1920.', photo_url: null },
    { id: '2', name: 'Nguyễn Văn Cha', title: 'Anh hùng lao động', description: 'Đã có nhiều đóng góp cho cộng đồng và dòng họ.', photo_url: null },
  ]

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Thành viên tiêu biểu</h1>
            <p className="text-neutral-600">{members.length} thành viên được vinh danh</p>
          </div>
          <Button>
            <Award className="h-4 w-4 mr-2" />
            Bổ sung thành viên
          </Button>
        </div>

        <div className="grid md:grid-cols-2 gap-6">
          {members.map((member) => (
            <OutstandingCard key={member.id} member={member} />
          ))}
        </div>
      </div>
    </Layout>
  )
}

function OutstandingCard({ member }: { member: OutstandingMember }) {
  return (
    <Card className="text-center">
      <CardContent className="p-6">
        <div className="w-20 h-20 rounded-full bg-accent-light border-2 border-accent flex items-center justify-center mx-auto mb-4">
          <Award className="h-10 w-10 text-accent" />
        </div>
        <h3 className="text-xl font-bold mb-1">{member.name}</h3>
        <Badge variant="accent" className="mb-3 inline-block">{member.title}</Badge>
        <p className="text-neutral-600">{member.description}</p>
        <div className="flex justify-center gap-1 mt-4">
          {[...Array(5)].map((_, i) => (
            <Star key={i} className="h-4 w-4 fill-accent text-accent" />
          ))}
        </div>
      </CardContent>
    </Card>
  )
}

function Badge({ children, variant = 'default', className = '' }: { children: React.ReactNode; variant?: string; className?: string }) {
  const variants: Record<string, string> = {
    default: 'bg-primary/10 text-primary',
    accent: 'bg-accent-light text-accent',
  }
  return (
    <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${variants[variant] || variants.default} ${className}`}>
      {children}
    </span>
  )
}
