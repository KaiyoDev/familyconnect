import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Input, Label } from '@/components/ui/basic'
import { familyApi } from '@/services/api'
import { toast } from 'sonner'
import { ArrowLeft } from 'lucide-react'

export default function Fam01CreateFamily() {
  const navigate = useNavigate()
  const [formData, setFormData] = useState({
    name: '',
    description: '',
  })
  const [loading, setLoading] = useState(false)

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    
    try {
      const response = await familyApi.create(formData)
      toast.success('Tạo gia đình thành công!')
      navigate(`/family/${response.data.data.id}`)
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Tạo gia đình thất bại')
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
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Tạo gia đình mới</h1>
            <p className="text-neutral-600">Khởi tạo dòng họ của bạn</p>
          </div>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Thông tin gia đình</CardTitle>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="name">Tên gia đình / Dòng họ *</Label>
                <Input
                  id="name"
                  name="name"
                  placeholder="Ví dụ: Họ Nguyễn Văn"
                  value={formData.name}
                  onChange={handleChange}
                  required
                />
                <p className="text-sm text-muted-foreground">Tên sẽ hiển thị trong danh sách gia đình và trên cây gia phả.</p>
              </div>

              <div className="space-y-2">
                <Label htmlFor="description">Mô tả (tùy chọn)</Label>
                <textarea
                  id="description"
                  name="description"
                  className="flex min-h-[100px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm"
                  placeholder="Giới thiệu về dòng họ, nguồn gốc..."
                  value={formData.description}
                  onChange={handleChange}
                />
              </div>

              <div className="pt-4">
                <Button type="submit" disabled={loading} className="w-full">
                  {loading ? 'Đang tạo...' : 'Tạo gia đình'}
                </Button>
              </div>
            </form>
          </CardContent>
        </Card>

        <div className="bg-accent-light rounded-lg p-4">
          <h3 className="font-medium mb-2">Thông tin cần biết</h3>
          <ul className="text-sm text-neutral-700 space-y-1">
            <li>• Bạn sẽ là chủ sở hữu (Owner) của gia đình</li>
            <li>• Mã gia tộc sẽ được tạo tự động để mời thành viên</li>
            <li>• Có thể thêm thành viên sau khi tạo gia đình</li>
          </ul>
        </div>
      </div>
    </Layout>
  )
}
