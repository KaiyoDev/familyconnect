import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Input, Label } from '@/components/ui/basic'
import { toast } from 'sonner'
import { ArrowLeft, Bell } from 'lucide-react'

export default function Com05Announcement() {
  const navigate = useNavigate()
  const [formData, setFormData] = useState({ title: '', content: '', type: 'announcement' })
  const [loading, setLoading] = useState(false)

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setTimeout(() => {
      toast.success('Đăng thông báo thành công!')
      navigate('/community/news')
      setLoading(false)
    }, 500)
  }

  return (
    <Layout>
      <div className="space-y-6 max-w-2xl mx-auto">
        <div className="flex items-center gap-4">
          <Button variant="ghost" onClick={() => navigate(-1)} className="pl-0"><ArrowLeft className="h-4 w-4 mr-2" />Quay lại</Button>
          <h1 className="text-2xl font-bold">Đăng thông báo</h1>
        </div>
        <Card>
          <CardHeader><CardTitle>Thông tin thông báo</CardTitle></CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-2">
                <Label>Loại</Label>
                <select name="type" className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm" value={formData.type} onChange={handleChange}>
                  <option value="announcement">Thông báo</option>
                  <option value="news">Tin tức</option>
                </select>
              </div>
              <div className="space-y-2">
                <Label>Tiêu đề *</Label>
                <Input name="title" placeholder="Nhập tiêu đề..." value={formData.title} onChange={handleChange} required />
              </div>
              <div className="space-y-2">
                <Label>Nội dung *</Label>
                <textarea name="content" className="flex min-h-[120px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm" placeholder="Nhập nội dung..." value={formData.content} onChange={handleChange} required />
              </div>
              <div className="flex gap-3 pt-4">
                <Button type="submit" disabled={loading} className="flex-1">{loading ? 'Đang đăng...' : 'Đăng thông báo'}</Button>
                <Button type="button" variant="outline" onClick={() => navigate(-1)}>Hủy</Button>
              </div>
            </form>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}
