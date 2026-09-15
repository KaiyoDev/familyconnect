import React, { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import { Button } from '@/components/ui/basic'
import { authApi } from '@/services/api'
import { toast } from 'sonner'

export default function Pub05ActivateAccount() {
  const { token } = useParams<{ token: string }>()
  const [loading, setLoading] = useState(true)
  const [activated, setActivated] = useState(false)
  const [error, setError] = useState(false)

  useEffect(() => {
    const activate = async () => {
      try {
        await authApi.verifyEmail({ token: token || '' })
        setActivated(true)
        toast.success('Kích hoạt tài khoản thành công!')
      } catch (error: any) {
        setError(true)
        toast.error('Liên kết kích hoạt không hợp lệ hoặc đã hết hạn')
      } finally {
        setLoading(false)
      }
    }
    activate()
  }, [token])

  if (loading) {
    return (
      <div className="min-h-screen bg-neutral-50 flex items-center justify-center">
        <div className="text-center">
          <div className="w-12 h-12 border-4 border-primary border-t-transparent rounded-full animate-spin mx-auto mb-4" />
          <p className="text-neutral-600">Đang kích hoạt...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-neutral-50 flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        <div className="bg-background rounded-[12px] border border-border shadow-sm p-8 text-center">
          {activated ? (
            <>
              <div className="w-16 h-16 rounded-full bg-success-bg flex items-center justify-center mx-auto mb-4">
                <svg className="w-8 h-8 text-success" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <h1 className="text-2xl font-bold text-neutral-900 mb-2">Kích hoạt thành công!</h1>
              <p className="text-neutral-600 mb-6">
                Tài khoản của bạn đã được kích hoạt. Bạn có thể đăng nhập để bắt đầu sử dụng.
              </p>
              <Link to="/login">
                <Button className="w-full">Đăng nhập ngay</Button>
              </Link>
            </>
          ) : (
            <>
              <div className="w-16 h-16 rounded-full bg-danger-bg flex items-center justify-center mx-auto mb-4">
                <svg className="w-8 h-8 text-danger" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
              </div>
              <h1 className="text-2xl font-bold text-neutral-900 mb-2">Không thể kích hoạt</h1>
              <p className="text-neutral-600 mb-6">
                Liên kết kích hoạt không hợp lệ hoặc đã hết hạn. Vui lòng đăng ký tài khoản mới.
              </p>
              <Link to="/register">
                <Button variant="outline" className="w-full">Đăng ký lại</Button>
              </Link>
            </>
          )}
        </div>
      </div>
    </div>
  )
}
