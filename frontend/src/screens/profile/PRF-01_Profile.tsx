import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Input, Label } from '@/components/ui/basic'
import { userApi } from '@/services/api'
import { toast } from 'sonner'
import { Camera, Mail, User, Shield } from 'lucide-react'

export default function Prf01Profile() {
  const [formData, setFormData] = useState({
    full_name: 'Nguyễn Văn A',
    email: 'nguyenvana@example.com',
    phone: '0912 345 678',
    address: 'Hà Nội',
    bio: 'Thành viên gia đình Nguyễn Văn',
  })
  const [loading, setLoading] = useState(false)

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    
    try {
      await userApi.updateMe(formData)
      toast.success('Cập nhật hồ sơ thành công!')
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Cập nhật thất bại')
    } finally {
      setLoading(false)
    }
  }

  return (
    <Layout>
      <div className="space-y-6 max-w-2xl mx-auto">
        <div>
          <h1 className="text-2xl font-bold text-neutral-900">Hồ sơ cá nhân</h1>
          <p className="text-neutral-600">Quản lý thông tin tài khoản</p>
        </div>

        {/* Avatar */}
        <Card>
          <CardContent className="p-6 flex items-center gap-6">
            <div className="relative">
              <div className="w-24 h-24 rounded-full bg-primary/10 flex items-center justify-center text-3xl font-bold text-primary">
                NA
              </div>
              <label className="absolute bottom-0 right-0 w-8 h-8 rounded-full bg-primary flex items-center justify-center cursor-pointer">
                <Camera className="h-4 w-4 text-white" />
                <input type="file" accept="image/*" className="hidden" />
              </label>
            </div>
            <div>
              <h2 className="text-xl font-bold">{formData.full_name}</h2>
              <p className="text-muted-foreground">{formData.email}</p>
              <Button variant="outline" size="sm" className="mt-3">
                Đổi ảnh đại diện
              </Button>
            </div>
          </CardContent>
        </Card>

        {/* Personal Info */}
        <Card>
          <CardHeader>
            <CardTitle>Thông tin cá nhân</CardTitle>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="grid sm:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label htmlFor="full_name">Họ và tên</Label>
                  <div className="relative">
                    <User className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
                    <Input
                      id="full_name"
                      name="full_name"
                      className="pl-9"
                      value={formData.full_name}
                      onChange={handleChange}
                    />
                  </div>
                </div>
                <div className="space-y-2">
                  <Label htmlFor="email">Email</Label>
                  <div className="relative">
                    <Mail className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
                    <Input
                      id="email"
                      name="email"
                      type="email"
                      className="pl-9"
                      value={formData.email}
                      onChange={handleChange}
                    />
                  </div>
                </div>
              </div>

              <div className="grid sm:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label htmlFor="phone">Điện thoại</Label>
                  <Input
                    id="phone"
                    name="phone"
                    value={formData.phone}
                    onChange={handleChange}
                  />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="address">Địa chỉ</Label>
                  <Input
                    id="address"
                    name="address"
                    value={formData.address}
                    onChange={handleChange}
                  />
                </div>
              </div>

              <div className="space-y-2">
                <Label htmlFor="bio">Giới thiệu</Label>
                <textarea
                  id="bio"
                  name="bio"
                  className="flex min-h-[100px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm"
                  value={formData.bio}
                  onChange={handleChange}
                />
              </div>

              <Button type="submit" disabled={loading}>
                {loading ? 'Đang lưu...' : 'Lưu thay đổi'}
              </Button>
            </form>
          </CardContent>
        </Card>

        {/* Security */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Shield className="h-5 w-5" />
              Bảo mật
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Đổi mật khẩu</p>
                <p className="text-sm text-muted-foreground">Cập nhật mật khẩu định kỳ</p>
              </div>
              <Button variant="outline">Đổi mật khẩu</Button>
            </div>
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Xác thực 2 yếu tố</p>
                <p className="text-sm text-muted-foreground">Bật xác thực 2FA để bảo vệ tài khoản</p>
              </div>
              <Button variant="outline">Bật 2FA</Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}
