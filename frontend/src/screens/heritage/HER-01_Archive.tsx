import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Badge } from '@/components/ui/basic'
import { Archive, FileText, BookOpen, Image as ImageIcon, Award } from 'lucide-react'
import { useNavigate } from 'react-router-dom'

export default function Her01Archive() {
  const navigate = useNavigate()
  
  const categories = [
    { id: 'documents', name: 'Tư liệu lịch sử', icon: FileText, count: 24, path: '/heritage/documents', color: 'bg-primary/10 text-primary' },
    { id: 'stories', name: 'Câu chuyện gia đình', icon: BookOpen, count: 18, path: '/heritage/stories', color: 'bg-accent/10 text-accent' },
    { id: 'photos', name: 'Thư viện ảnh', icon: ImageIcon, count: 156, path: '/heritage/photos', color: 'bg-info/10 text-info' },
    { id: 'outstanding', name: 'Thành viên tiêu biểu', icon: Award, count: 8, path: '/heritage/outstanding', color: 'bg-success/10 text-success' },
  ]

  return (
    <Layout>
      <div className="space-y-6">
        <div>
          <h1 className="text-2xl font-bold text-neutral-900">Kho lưu trữ di sản</h1>
          <p className="text-neutral-600">Lưu giữ và tôn vinh giá trị gia đình</p>
        </div>

        <div className="grid sm:grid-cols-2 gap-4">
          {categories.map((cat) => (
            <CategoryCard key={cat.id} category={cat} onClick={() => navigate(cat.path)} />
          ))}
        </div>

        {/* Recent uploads */}
        <Card>
          <CardHeader>
            <CardTitle>Tư liệu mới cập nhật</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {[
                { type: 'document', title: 'Sắc phong năm 1920', date: '2026-09-05' },
                { type: 'story', title: 'Câu chuyện ông nội', date: '2026-09-03' },
                { type: 'photo', title: 'Ảnh gia đình 1990', date: '2026-09-01' },
              ].map((item, idx) => (
                <div key={idx} className="flex items-center gap-3 p-3 bg-neutral-50 rounded-lg">
                  <div className="w-10 h-10 rounded-lg bg-primary/10 flex items-center justify-center">
                    <Archive className="h-5 w-5 text-primary" />
                  </div>
                  <div className="flex-1">
                    <p className="font-medium">{item.title}</p>
                    <p className="text-sm text-muted-foreground">
                      {item.type === 'document' ? 'Tư liệu' : item.type === 'story' ? 'Câu chuyện' : 'Ảnh'} • {item.date}
                    </p>
                  </div>
                  <Button variant="ghost" size="sm">Xem</Button>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}

function CategoryCard({ category, onClick }: { category: any; onClick: () => void }) {
  return (
    <Card className="cursor-pointer hover:border-primary/50 transition-colors" onClick={onClick}>
      <CardContent className="p-6">
        <div className="flex items-start gap-4">
          <div className={`w-14 h-14 rounded-xl ${category.color} flex items-center justify-center`}>
            <category.icon className="h-7 w-7" />
          </div>
          <div className="flex-1">
            <h3 className="font-semibold text-lg">{category.name}</h3>
            <p className="text-sm text-muted-foreground">{category.count} mục</p>
          </div>
          <ChevronRight className="h-5 w-5 text-muted-foreground" />
        </div>
      </CardContent>
    </Card>
  )
}

function ChevronRight(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m9 18 6-6-6-6"/></svg>
  )
}
