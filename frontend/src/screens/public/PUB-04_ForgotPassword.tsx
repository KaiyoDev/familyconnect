import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import { Button, Input, Label } from '@/components/ui/basic'
import { authApi } from '@/services/api'
import { toast } from 'sonner'

export default function Pub04ForgotPassword() {
  const [email, setEmail] = useState('')
  const [loading, setLoading] = useState(false)
  const [sent, setSent] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    
    try {
      await authApi.forgotPassword({ email })
      setSent(true)
      toast.success('Đã gửi liên kết đặt lại mật khẩu!')
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Gửi yêu cầu thất bại')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-neutral-50 flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        <div className="text-center mb-8">
          <div className="w-12 h-12 rounded-xl bg-primary flex items-center justify-center mx-auto mb-4">
            <span className="text-white font-bold text-lg">FC</span>
          </div>
          <h1 className="text-2xl font-bold text-neutral-900">Quên mật khẩu</h1>
          <p className="text-neutral-600 mt-2">
            {sent ? 'Chúng tôi đã gửi liên kết đặt lại mật khẩu đến email của bạn.' : 'Nhập email để nhận liên kết đặt lại mật khẩu.'}
          </p>
        </div>

        <div className="bg-background rounded-[12px] border border-border shadow-sm p-6">
          {!sent ? (
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="email">Email</Label>
                <Input
                  id="email"
                  type="email"
                  placeholder="example@email.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </div>

              <Button type="submit" className="w-full" disabled={loading}>
                {loading ? 'Đang gửi...' : 'Gửi liên kết đặt lại'}
              </Button>
            </form>
          ) : (
            <div className="text-center py-4">
              <div className="w-16 h-16 rounded-full bg-success-bg flex items-center justify-center mx-auto mb-4">
                <svg className="w-8 h-8 text-success" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <p className="text-neutral-600 mb-4">
                Vui lòng kiểm tra email và làm theo hướng dẫn để đặt lại mật khẩu.
              </p>
            </div>
          )}

          <div className="mt-6 text-center">
            <Link to="/login" className="text-sm text-primary hover:underline">
              ← Quay lại đăng nhập
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}
