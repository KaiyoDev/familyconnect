import React, { useState } from 'react'
import { useNavigate, useSearchParams } from 'react-router-dom'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Input, Label } from '@/components/ui/basic'
import { memberApi } from '@/services/api'
import { toast } from 'sonner'
import { ArrowLeft } from 'lucide-react'

export default function Gen06SetRelationship() {
  const navigate = useNavigate()
  const [searchParams] = useSearchParams()
  const memberId = searchParams.get('memberId')
  
  const [formData, setFormData] = useState({
    relationshipType: 'PARENT_CHILD',
    targetMemberId: '',
    parentType: 'father',
  })
  const [loading, setLoading] = useState(false)

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    
    try {
      await memberApi.addRelationship('default-family-id', {
        member_a_id: memberId,
        member_b_id: formData.targetMemberId,
        relationship_type: formData.relationshipType,
        parent_type: formData.parentType,
      })
      toast.success('Thiết lập quan hệ thành công!')
      navigate('/genealogy')
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Thiết lập quan hệ thất bại')
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
            <h1 className="text-2xl font-bold text-neutral-900">Thiết lập quan hệ</h1>
            <p className="text-neutral-600">Kết nối thành viên với các thành viên khác</p>
          </div>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Chọn mối quan hệ</CardTitle>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="relationshipType">Loại quan hệ</Label>
                <select
                  id="relationshipType"
                  name="relationshipType"
                  className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm"
                  value={formData.relationshipType}
                  onChange={handleChange}
                >
                  <option value="PARENT_CHILD">Cha / Mẹ - Con</option>
                  <option value="MARRIAGE">Hôn nhân</option>
                  <option value="SIBLING">Anh / Chị / Em</option>
                </select>
              </div>

              {formData.relationshipType === 'PARENT_CHILD' && (
                <div className="space-y-2">
                  <Label htmlFor="parentType">Vai trò</Label>
                  <select
                    id="parentType"
                    name="parentType"
                    className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm"
                    value={formData.parentType}
                    onChange={handleChange}
                  >
                    <option value="father">Là cha</option>
                    <option value="mother">Là mẹ</option>
                    <option value="child">Là con</option>
                  </select>
                </div>
              )}

              <div className="space-y-2">
                <Label htmlFor="targetMemberId">Thành viên liên kết</Label>
                <Input
                  id="targetMemberId"
                  name="targetMemberId"
                  placeholder="Nhập ID hoặc tìm kiếm thành viên..."
                  value={formData.targetMemberId}
                  onChange={handleChange}
                  required
                />
              </div>

              <div className="pt-4">
                <Button type="submit" disabled={loading} className="w-full">
                  {loading ? 'Đang lưu...' : 'Lưu quan hệ'}
                </Button>
              </div>
            </form>
          </CardContent>
        </Card>

        {/* Relationship Guide */}
        <Card>
          <CardHeader>
            <CardTitle>Hướng dẫn thiết lập quan hệ</CardTitle>
          </CardHeader>
          <CardContent className="space-y-3 text-sm">
            <div className="flex items-start gap-3">
              <div className="w-6 h-6 rounded-full bg-primary/10 flex items-center justify-center flex-shrink-0 text-primary font-medium">1</div>
              <p>Chọn loại quan hệ phù hợp với mối quan hệ bạn muốn thiết lập.</p>
            </div>
            <div className="flex items-start gap-3">
              <div className="w-6 h-6 rounded-full bg-primary/10 flex items-center justify-center flex-shrink-0 text-primary font-medium">2</div>
              <p>Nhập ID hoặc tìm kiếm thành viên cần liên kết.</p>
            </div>
            <div className="flex items-start gap-3">
              <div className="w-6 h-6 rounded-full bg-primary/10 flex items-center justify-center flex-shrink-0 text-primary font-medium">3</div>
              <p>Nếu là quan hệ cha/con, chọn vai trò cụ thể (cha/mẹ/con).</p>
            </div>
            <div className="flex items-start gap-3">
              <div className="w-6 h-6 rounded-full bg-primary/10 flex items-center justify-center flex-shrink-0 text-primary font-medium">4</div>
              <p>Nhấn "Lưu quan hệ" để hoàn tất.</p>
            </div>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}
