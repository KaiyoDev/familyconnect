import React, { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Badge } from '@/components/ui/basic'
import { 
  ArrowLeft, Calendar, MapPin, Users, Clock, 
  CheckCircle, XCircle, HelpCircle, Share2, Download 
} from 'lucide-react'

export default function EvT02EventDetail() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [rsvpStatus, setRsvpStatus] = useState<'none' | 'attending' | 'interested' | 'declined'>('none')

  const event = {
    id,
    title: 'Giỗ tổ họ Nguyễn',
    description: 'Lễ giỗ tổ dòng họ Nguyễn năm 2026. Chương trình bao gồm: làm lễ tưởng niệm, dâng hoa, họp mặt gia đình và bữa cơm thân mật.',
    start_time: '2026-10-10T09:00:00Z',
    end_time: '2026-10-10T12:00:00Z',
    location: 'Nhà thờ họ - 123 Đường Lê Lợi, Hà Nội',
    organizer: 'Nguyễn Văn A',
    participant_count: 18,
    max_participants: 50,
    image_url: null,
  }

  const participants = [
    { id: '1', name: 'Nguyễn Văn A', status: 'attending', avatar: 'NA' },
    { id: '2', name: 'Trần Thị B', status: 'attending', avatar: 'TB' },
    { id: '3', name: 'Lê Văn C', status: 'interested', avatar: 'LC' },
  ]

  const startDate = new Date(event.start_time)
  const endDate = event.end_time ? new Date(event.end_time) : startDate

  const handleRsvp = (status: 'attending' | 'interested' | 'declined') => {
    setRsvpStatus(status)
  }

  return (
    <Layout>
      <div className="space-y-6 max-w-3xl mx-auto">
        <Button variant="ghost" onClick={() => navigate(-1)} className="pl-0">
          <ArrowLeft className="h-4 w-4 mr-2" />
          Quay lại
        </Button>

        {/* Header */}
        <div className="flex items-start justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">{event.title}</h1>
            <p className="text-neutral-600 mt-1">{event.description}</p>
          </div>
          <div className="flex gap-2">
            <Button variant="outline" size="icon">
              <Share2 className="h-4 w-4" />
            </Button>
            <Button variant="outline" size="icon">
              <Download className="h-4 w-4" />
            </Button>
          </div>
        </div>

        {/* Event Details */}
        <Card>
          <CardHeader>
            <CardTitle>Thông tin sự kiện</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid sm:grid-cols-2 gap-4">
              <InfoItem icon={Calendar} label="Ngày bắt đầu" value={startDate.toLocaleDateString('vi-VN')} />
              <InfoItem icon={Clock} label="Thời gian" value={`${startDate.toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' })} - ${endDate.toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' })}`} />
              <InfoItem icon={MapPin} label="Địa điểm" value={event.location} />
              <InfoItem icon={Users} label="Người tổ chức" value={event.organizer} />
            </div>
          </CardContent>
        </Card>

        {/* RSVP Section */}
        <Card>
          <CardHeader>
            <CardTitle>Tham dự sự kiện</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-3 gap-3 mb-4">
              <RSVPButton
                status="attending"
                label="Có tham dự"
                icon={CheckCircle}
                color="text-success"
                bgColor="bg-success/10"
                selected={rsvpStatus === 'attending'}
                onClick={() => handleRsvp('attending')}
              />
              <RSVPButton
                status="interested"
                label="Quan tâm"
                icon={HelpCircle}
                color="text-warning"
                bgColor="bg-warning/10"
                selected={rsvpStatus === 'interested'}
                onClick={() => handleRsvp('interested')}
              />
              <RSVPButton
                status="declined"
                label="Không tham dự"
                icon={XCircle}
                color="text-destructive"
                bgColor="bg-destructive/10"
                selected={rsvpStatus === 'declined'}
                onClick={() => handleRsvp('declined')}
              />
            </div>
            <Button className="w-full" onClick={() => navigate(`/events/${id}/participants`)}>
              Xem danh sách tham gia ({event.participant_count})
            </Button>
          </CardContent>
        </Card>

        {/* Participants */}
        <Card>
          <CardHeader>
            <CardTitle>Thành viên tham gia</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {participants.map((p) => (
                <div key={p.id} className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center text-sm font-medium text-primary">
                    {p.avatar}
                  </div>
                  <span className="flex-1">{p.name}</span>
                  <Badge variant={p.status === 'attending' ? 'success' : 'warning'}>
                    {p.status === 'attending' ? 'Sẽ tham dự' : 'Quan tâm'}
                  </Badge>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

        {/* Actions */}
        <div className="flex gap-3">
          <Button variant="outline" className="flex-1" onClick={() => navigate(`/events/${id}/gallery`)}>
            Thư viện ảnh
          </Button>
          <Button variant="danger" className="flex-1">
            Hủy sự kiện
          </Button>
        </div>
      </div>
    </Layout>
  )
}

function InfoItem({ icon: Icon, label, value }: { icon: React.ElementType; label: string; value: string }) {
  return (
    <div className="flex items-start gap-3">
      <Icon className="h-5 w-5 text-primary mt-0.5" />
      <div>
        <p className="text-sm text-muted-foreground">{label}</p>
        <p className="font-medium">{value}</p>
      </div>
    </div>
  )
}

function RSVPButton({ status, label, icon: Icon, color, bgColor, selected, onClick }: {
  status: string
  label: string
  icon: React.ElementType
  color: string
  bgColor: string
  selected: boolean
  onClick: () => void
}) {
  return (
    <button
      onClick={onClick}
      className={`p-3 rounded-lg border-2 transition-all ${
        selected ? 'border-primary bg-primary/10' : 'border-border hover:border-primary/50'
      }`}
    >
      <Icon className={`h-6 w-6 mx-auto mb-2 ${color}`} />
      <span className="text-sm font-medium">{label}</span>
    </button>
  )
}
