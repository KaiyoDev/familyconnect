import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Input, Label } from '@/components/ui/basic'
import { Settings as SettingsIcon, Bell, Shield, Database, Cloud } from 'lucide-react'

export default function Adm06Settings() {
  const [settings, setSettings] = useState({
    siteName: 'FamilyConnect',
    maintenanceMode: false,
    registrationEnabled: true,
    aiEnabled: true,
    maxUploadSize: '10',
    backupFrequency: 'daily',
  })

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setSettings({ ...settings, [e.target.name]: e.target.value })
  }

  const handleToggle = (name: string) => {
    setSettings({ ...settings, [name]: !settings[name as keyof typeof settings] })
  }

  return (
    <Layout>
      <div className="space-y-6 max-w-2xl mx-auto">
        <div>
          <h1 className="text-2xl font-bold text-neutral-900">Cấu hình hệ thống</h1>
          <p className="text-neutral-600">Thiết lập các thông số vận hành</p>
        </div>

        {/* General Settings */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <SettingsIcon className="h-5 w-5" />
              Cài đặt chung
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <Label>Tên trang web</Label>
              <Input name="siteName" value={settings.siteName} onChange={handleChange} />
            </div>
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Chế độ bảo trì</p>
                <p className="text-sm text-muted-foreground">Tạm ngưng truy cập người dùng</p>
              </div>
              <button
                onClick={() => handleToggle('maintenanceMode')}
                className={`w-12 h-6 rounded-full transition-colors ${settings.maintenanceMode ? 'bg-primary' : 'bg-neutral-300'}`}
              >
                <div className={`w-5 h-5 rounded-full bg-white transition-transform ${settings.maintenanceMode ? 'translate-x-6' : 'translate-x-1'}`} />
              </button>
            </div>
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Cho phép đăng ký</p>
                <p className="text-sm text-muted-foreground">Người dùng mới có thể tạo tài khoản</p>
              </div>
              <button
                onClick={() => handleToggle('registrationEnabled')}
                className={`w-12 h-6 rounded-full transition-colors ${settings.registrationEnabled ? 'bg-primary' : 'bg-neutral-300'}`}
              >
                <div className={`w-5 h-5 rounded-full bg-white transition-transform ${settings.registrationEnabled ? 'translate-x-6' : 'translate-x-1'}`} />
              </button>
            </div>
          </CardContent>
        </Card>

        {/* AI Settings */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Cloud className="h-5 w-5" />
              Cài đặt AI
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Kích hoạt AI</p>
                <p className="text-sm text-muted-foreground">Bật/tắt các tính năng AI</p>
              </div>
              <button
                onClick={() => handleToggle('aiEnabled')}
                className={`w-12 h-6 rounded-full transition-colors ${settings.aiEnabled ? 'bg-primary' : 'bg-neutral-300'}`}
              >
                <div className={`w-5 h-5 rounded-full bg-white transition-transform ${settings.aiEnabled ? 'translate-x-6' : 'translate-x-1'}`} />
              </button>
            </div>
          </CardContent>
        </Card>

        {/* Storage Settings */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Database className="h-5 w-5" />
              Lưu trữ
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <Label>Kích thước tối đa upload (MB)</Label>
              <Input name="maxUploadSize" type="number" value={settings.maxUploadSize} onChange={handleChange} />
            </div>
            <div className="space-y-2">
              <Label>Tần suất backup tự động</Label>
              <select
                name="backupFrequency"
                className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm"
                value={settings.backupFrequency}
                onChange={handleChange}
              >
                <option value="hourly">Mỗi giờ</option>
                <option value="daily">Mỗi ngày</option>
                <option value="weekly">Mỗi tuần</option>
                <option value="monthly">Mỗi tháng</option>
              </select>
            </div>
          </CardContent>
        </Card>

        {/* Notifications */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Bell className="h-5 w-5" />
              Thông báo
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Thông báo email</p>
                <p className="text-sm text-muted-foreground">Gửi thông báo qua email</p>
              </div>
              <button className="w-12 h-6 rounded-full bg-primary">
                <div className="w-5 h-5 rounded-full bg-white translate-x-6" />
              </button>
            </div>
            <div className="flex items-center justify-between">
              <div>
                <p className="font-medium">Thông báo push</p>
                <p className="text-sm text-muted-foreground">Gửi thông báo trên trình duyệt</p>
              </div>
              <button className="w-12 h-6 rounded-full bg-neutral-300">
                <div className="w-5 h-5 rounded-full bg-white translate-x-1" />
              </button>
            </div>
          </CardContent>
        </Card>

        <div className="flex gap-3">
          <Button className="flex-1">Lưu cài đặt</Button>
          <Button variant="outline">Đặt lại mặc định</Button>
        </div>
      </div>
    </Layout>
  )
}
