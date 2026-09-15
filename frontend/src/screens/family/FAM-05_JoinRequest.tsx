import React, { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Badge } from '@/components/ui/basic'
import { familyApi } from '@/services/api'
import { toast } from 'sonner'
import { Check, X, UserPlus } from 'lucide-react'

interface JoinRequest {
  id: string
  user_name: string
  user_email: string
  requested_at: string
  message?: string
}

export default function Fam05JoinRequest() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [requests, setRequests] = useState<JoinRequest[]>([
    { id: '1', user_name: 'Trần Văn Minh', user_email: 'minh@example.com', requested_at: '2026-09-08', message: 'Tôi là cháu ngoại muốn tìm hiểu về dòng họ.' },
    { id: '2', user_name: 'Lê Thị Hoa', user_email: 'hoa@example.com', requested_at: '2026-09-07', message: undefined },
  ])

  const handleApprove = async (requestId: string) => {
    try {
      await familyApi.update(id!, { action: 'approve_join_request', request_id: requestId })
      setRequests(requests.filter(r => r.id !== requestId))
      toast.success('Đã phê duyệt yêu cầu!')
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Phê duyệt thất bại')
    }
  }

  const handleReject = async (requestId: string) => {
    try {
      await familyApi.update(id!, { action: 'reject_join_request', request_id: requestId })
      setRequests(requests.filter(r => r.id !== requestId))
      toast.success('Đã từ chối yêu cầu!')
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Từ chối thất bại')
    }
  }

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Yêu cầu tham gia</h1>
            <p className="text-neutral-600">{requests.length} yêu cầu chờ xử lý</p>
          </div>
          <Button variant="outline" onClick={() => navigate(`/family/${id}`)}>
            Quay lại
          </Button>
        </div>

        {requests.length === 0 ? (
          <Card>
            <CardContent className="py-12 text-center">
              <UserPlus className="h-12 w-12 text-muted-foreground mx-auto mb-4" />
              <p className="text-neutral-600">Không có yêu cầu nào</p>
              <p className="text-sm text-muted-foreground">Tất cả yêu cầu đã được xử lý</p>
            </CardContent>
          </Card>
        ) : (
          <div className="space-y-4">
            {requests.map((request) => (
              <JoinRequestCard
                key={request.id}
                request={request}
                onApprove={() => handleApprove(request.id)}
                onReject={() => handleReject(request.id)}
              />
            ))}
          </div>
        )}
      </div>
    </Layout>
  )
}

function JoinRequestCard({ request, onApprove, onReject }: {
  request: JoinRequest
  onApprove: () => void
  onReject: () => void
}) {
  return (
    <Card>
      <CardHeader>
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-full bg-primary/10 flex items-center justify-center">
              <span className="font-medium text-primary">{request.user_name[0]}</span>
            </div>
            <div>
              <p className="font-medium">{request.user_name}</p>
              <p className="text-sm text-muted-foreground">{request.user_email}</p>
            </div>
          </div>
          <Badge variant="warning">Chờ duyệt</Badge>
        </div>
      </CardHeader>
      <CardContent>
        {request.message && (
          <p className="text-neutral-700 mb-4 p-3 bg-neutral-50 rounded-lg">
            "{request.message}"
          </p>
        )}
        <div className="flex items-center justify-between text-sm text-muted-foreground">
          <span>Yêu cầu từ {new Date(request.requested_at).toLocaleDateString('vi-VN')}</span>
          <div className="flex gap-2">
            <Button size="sm" variant="outline" onClick={onReject} className="border-danger text-danger hover:bg-danger-bg">
              <X className="h-4 w-4 mr-2" />
              Từ chối
            </Button>
            <Button size="sm" onClick={onApprove} className="bg-success text-white hover:bg-success/90">
              <Check className="h-4 w-4 mr-2" />
              Phê duyệt
            </Button>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
