import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Badge } from '@/components/ui/basic'
import { Plus, Link2, ChevronRight, Info } from 'lucide-react'
import { useNavigate } from 'react-router-dom'

interface Member {
  id: string
  name: string
  gender: 'MALE' | 'FEMALE'
  birthYear?: number
  photo_url?: string
  parents?: string[]
  children?: string[]
}

export default function Gen01GenealogyTree() {
  const navigate = useNavigate()
  const [selectedMember, setSelectedMember] = useState<string | null>(null)
  
  const familyData = {
    founder: {
      id: '1',
      name: 'Nguyễn Văn Tổ',
      gender: 'MALE' as const,
      birthYear: 1920,
      deathYear: 1995,
    },
    children: [
      {
        id: '2',
        name: 'Nguyễn Văn Cha',
        gender: 'MALE' as const,
        birthYear: 1945,
        spouse: { id: '3', name: 'Trần Thị Mẹ', gender: 'FEMALE' as const, birthYear: 1950 },
        children: [
          { id: '4', name: 'Nguyễn Văn Con 1', gender: 'MALE' as const, birthYear: 1970 },
          { id: '5', name: 'Nguyễn Thị Con 2', gender: 'FEMALE' as const, birthYear: 1975 },
          { id: '6', name: 'Nguyễn Văn Con 3', gender: 'MALE' as const, birthYear: 1980 },
        ],
      },
      {
        id: '7',
        name: 'Nguyễn Thị Chị',
        gender: 'FEMALE' as const,
        birthYear: 1948,
        children: [],
      },
    ],
  }

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Cây gia phả</h1>
            <p className="text-neutral-600">Gia đình Nguyễn Văn</p>
          </div>
          <div className="flex gap-2">
            <Button variant="outline">
              <Link2 className="h-4 w-4 mr-2" />
              Đồ thị
            </Button>
            <Button onClick={() => navigate('/genealogy/add-member')}>
              <Plus className="h-4 w-4 mr-2" />
              Thêm thành viên
            </Button>
          </div>
        </div>

        <Card>
          <CardHeader><CardTitle>Cây gia phả</CardTitle></CardHeader>
          <CardContent>
            <div className="bg-neutral-50 rounded-lg p-8 min-h-[400px] flex items-center justify-center">
              <div className="text-center">
                <div className="w-20 h-20 rounded-full bg-accent-light border-2 border-accent flex items-center justify-center mx-auto mb-4">
                  <span className="text-2xl font-bold text-neutral-700">{familyData.founder.name.split(' ').pop()?.[0]}</span>
                </div>
                <p className="font-semibold text-lg">{familyData.founder.name}</p>
                <p className="text-sm text-muted-foreground">Ông tổ • {familyData.founder.birthYear}</p>
                <div className="mt-8 flex justify-center gap-12">
                  {familyData.children.map((child) => (
                    <div key={child.id} className="text-center">
                      <div className={`w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-2 ${
                        child.gender === 'MALE' ? 'bg-primary/10 border-2 border-primary' : 'bg-pink/10 border-2 border-pink'
                      }`}>
                        <span className="font-medium">{child.name.split(' ').pop()?.[0]}</span>
                      </div>
                      <p className="text-sm">{child.name}</p>
                      {child.children && child.children.length > 0 && (
                        <div className="mt-4 flex gap-4 justify-center">
                          {child.children.slice(0, 3).map((gc) => (
                            <div key={gc.id} className={`w-12 h-12 rounded-full flex items-center justify-center ${
                              gc.gender === 'MALE' ? 'bg-primary/10 border border-primary' : 'bg-pink/10 border border-pink'
                            }`}>
                              <span className="text-xs">{gc.name.split(' ').pop()?.[0]}</span>
                            </div>
                          ))}
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        <div className="flex gap-4 text-sm">
          <div className="flex items-center gap-2"><div className="w-4 h-4 rounded border-2 border-primary bg-primary/10" /><span>Nam</span></div>
          <div className="flex items-center gap-2"><div className="w-4 h-4 rounded border-2 border-pink bg-pink/10" /><span>Nữ</span></div>
          <div className="flex items-center gap-2"><div className="w-4 h-4 rounded border-2 border-accent bg-accent-light" /><span>Ông tổ</span></div>
        </div>
      </div>
    </Layout>
  )
}
