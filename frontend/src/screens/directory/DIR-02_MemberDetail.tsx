import React from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button } from '@/components/ui/basic'
import { ArrowLeft, Calendar, MapPin } from 'lucide-react'

export default function Dir02MemberDetail() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  
  const member = {
    id,
    name: 'Nguyễn Văn An',
    gender: 'MALE',
    birthDate: '1990-05-15',
    profession: 'Kỹ sư phần mềm',
    branch: 'Nhánh chính',
  }

  return (
    <Layout>
      <div className="space-y-6">
        <Button variant="ghost" onClick={() => navigate(-1)} className="pl-0">
          <ArrowLeft className="h-4 w-4 mr-2" />
          Quay lại
        </Button>
        
        <Card>
          <CardContent className="p-6 flex items-center gap-6">
            <div className={`w-20 h-20 rounded-full flex items-center justify-center text-3xl font-bold ${
              member.gender === 'MALE' ? 'bg-primary/10 text-primary' : 'bg-pink/10 text-pink'
            }`}>
              {member.name.split(' ').pop()?.[0] || 'U'}
            </div>
            <div>
              <h1 className="text-2xl font-bold">{member.name}</h1>
              <p className="text-neutral-600">{member.profession}</p>
              <div className="flex gap-4 mt-2 text-sm text-muted-foreground">
                <span className="flex items-center gap-1"><Calendar className="h-4 w-4" />{member.birthDate}</span>
                <span className="flex items-center gap-1"><MapPin className="h-4 w-4" />{member.branch}</span>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}
