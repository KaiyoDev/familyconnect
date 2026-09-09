import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Input, Label } from '@/components/ui/basic'
import { eventApi } from '@/services/api'
import { toast } from 'sonner'
import { ArrowLeft, Calendar, Clock, MapPin, Users } from 'lucide-react'

export default function EvT03CreateEvent() {
  const navigate = useNavigate()
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    start_date: '',
    start_time: '09:00',
    end_date: '',
    end_time: '12:00',
    location: '',
    max_participants: '',
  })
  const [loading, setLoading] = useState(false)

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    
    try {
      await eventApi.create('default-family-id', {
        ...formData,
        start_time: `${formData.start_date}T${formData.start_time}:00`,
        end_time: `${formData.end_date || formData.start_date}T${formData.end_time}:00`,
      })
      toast.success('Tạo sự kiện thành công!')
      navigate('/events')
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Tạo sự kiện thất bại')
    } finally {
      setLoading(false)
    }
  }

  return (
    <Layout>
      <div className="space-y-6 max-w-2xl mx-auto">
        <div className="flex items-center gap-4">
          <Button variant="ghost" onClick={() => navigate(-1)} className="pl-0">
            <ArrowLeft className="h-4 w-4 mr-2" />
            Quay lại
          </Button>
          <h1 className="text-2xl font-bold text-neutral-900">Tạo sự kiện mới</h1>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Thông tin sự kiện</CardTitle>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-2">
                <Label>Tên sự kiện *</Label>
                <Input
                  name="title"
                  placeholder="VD: Giỗ tổ họ Nguyễn"
                  value={formData.title}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="space-y-2">
                <Label>Mô tả</Label>
                <textarea
                  name="description"
                  className="flex min-h-[100px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm"
                  placeholder="Mô tả chi tiết về sự kiện..."
                  value={formData.description}
                  onChange={handleChange}
                />
              </div>

              <div className="grid sm:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label>Ngày bắt đầu *</Label>
                  <Input
                    name="start_date"
                    type="date"
                    value={formData.start_date}
                    onChange={handleChange}
                    required
                  />
                </div>
                <div className="space-y-2">
                  <Label>Giờ bắt đầu *</Label>
                  <Input
                    name="start_time"
                    type="time"
                    value={formData.start_time}
                    onChange={handleChange}
                    required
                  />
                </div>
              </div>

              <div className="grid sm:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label>Ngày kết thúc</Label>
                  <Input
                    name="end_date"
                    type="date"
                    value={formData.end_date}
                    onChange={handleChange}
                  />
                </div>
                <div className="space-y-2">
                  <Label>Giờ kết thúc</Label>
                  <Input
                    name="end_time"
                    type="time"
                    value={formData.end_time}
                    onChange={handleChange}
                  />
                </div>
              </div>

              <div className="space-y-2">
                <Label>Địa điểm *</Label>
                <Input
                  name="location"
                  placeholder="VD: Nhà thờ họ - Hà Nội"
                  value={formData.location}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="space-y-2">
                <Label>Số lượng tối đa</Label>
                <Input
                  name="max_participants"
                  type="number"
                  placeholder="Để trống nếu không giới hạn"
                  value={formData.max_participants}
                  onChange={handleChange}
                />
              </div>

              <div className="flex gap-3 pt-4">
                <Button type="submit" disabled={loading} className="flex-1">
                  {loading ? 'Đang tạo...' : 'Tạo sự kiện'}
                </Button>
                <Button type="button" variant="outline" onClick={() => navigate(-1)}>
                  Hủy
                </Button>
              </div>
            </form>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}
