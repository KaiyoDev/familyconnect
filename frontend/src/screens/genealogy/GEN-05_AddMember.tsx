import React, { useState } from 'react'
import { useNavigate, useSearchParams } from 'react-router-dom'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Input, Label } from '@/components/ui/basic'
import { memberApi } from '@/services/api'
import { toast } from 'sonner'
import { ArrowLeft, Plus, X } from 'lucide-react'

export default function Gen05AddMember() {
  const navigate = useNavigate()
  const [searchParams] = useSearchParams()
  const parentMemberId = searchParams.get('parent')
  
  const [formData, setFormData] = useState({
    name: '',
    gender: 'MALE' as 'MALE' | 'FEMALE',
    birthDate: '',
    profession: '',
  })
  const [loading, setLoading] = useState(false)

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    try {
      await memberApi.create('default-family-id', { ...formData, parent_id: parentMemberId || undefined })
      toast.success('Thêm thành viên thành công!')
      navigate('/genealogy')
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Thêm thành viên thất bại')
    } finally {
      setLoading(false)
    }
  }

  return (
    <Layout>
      <div className="space-y-6 max-w-xl mx-auto">
        <div className="flex items-center gap-4">
          <Button variant="ghost" onClick={() => navigate(-1)} className="pl-0">
            <ArrowLeft className="h-4 w-4 mr-2" />
            Quay lại
          </Button>
          <h1 className="text-2xl font-bold">Thêm thành viên</h1>
        </div>

        <Card>
          <CardHeader><CardTitle>Thông tin cơ bản</CardTitle></CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-2">
                <Label>Họ và tên *</Label>
                <Input name="name" placeholder="Nguyễn Văn A" value={formData.name} onChange={handleChange} required />
              </div>
              <div className="space-y-2">
                <Label>Giới tính *</Label>
                <div className="flex gap-4">
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input type="radio" name="gender" value="MALE" checked={formData.gender === 'MALE'} onChange={() => setFormData({...formData, gender: 'MALE'})} />
                    Nam
                  </label>
                  <label className="flex items-center gap-2 cursor-pointer">
                    <input type="radio" name="gender" value="FEMALE" checked={formData.gender === 'FEMALE'} onChange={() => setFormData({...formData, gender: 'FEMALE'})} />
                    Nữ
                  </label>
                </div>
              </div>
              <div className="space-y-2">
                <Label>Ngày sinh</Label>
                <Input name="birthDate" type="date" value={formData.birthDate} onChange={handleChange} />
              </div>
              <div className="space-y-2">
                <Label>Nghề nghiệp</Label>
                <Input name="profession" placeholder="Kỹ sư, Giáo viên..." value={formData.profession} onChange={handleChange} />
              </div>
              <div className="flex gap-3 pt-4">
                <Button type="submit" disabled={loading} className="flex-1">
                  {loading ? 'Đang thêm...' : 'Thêm thành viên'}
                </Button>
                <Button type="button" variant="outline" onClick={() => navigate(-1)}>Hủy</Button>
              </div>
            </form>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}
