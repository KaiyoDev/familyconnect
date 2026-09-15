import React, { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Badge } from '@/components/ui/basic'
import { ArrowLeft, Check, X } from 'lucide-react'

export default function EvT04ManageParticipants() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [participants, setParticipants] = useState([
    { id: '1', name: 'Nguyễn Văn A', status: 'attending', avatar: 'NA' },
    { id: '2', name: 'Trần Thị B', status: 'attending', avatar: 'TB' },
    { id: '3', name: 'Lê Văn C', status: 'interested', avatar: 'LC' },
    { id: '4', name: 'Phạm Thị D', status: 'declined', avatar: 'PD' },
  ])

  const stats = {
    attending: participants.filter(p => p.status === 'attending').length,
    interested: participants.filter(p => p.status === 'interested').length,
    declined: participants.filter(p => p.status === 'declined').length,
  }

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-4">
            <Button variant="ghost" onClick={() => navigate(-1)} className="pl-0">
              <ArrowLeft className="h-4 w-4 mr-2" />
              Quay lại
            </Button>
            <div>
              <h1 className="text-2xl font-bold text-neutral-900">Quản lý người tham gia</h1>
              <p className="text-neutral-600">{participants.length} người đã phản hồi</p>
            </div>
          </div>
          <Button variant="outline">
            Xuất danh sách
          </Button>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-3 gap-4">
          <StatCard label="Tham dự" value={stats.attending} color="bg-success" />
          <StatCard label="Quan tâm" value={stats.interested} color="bg-warning" />
          <StatCard label="Không tham dự" value={stats.declined} color="bg-destructive" />
        </div>

        {/* Participants List */}
        <Card>
          <CardHeader>
            <CardTitle>Danh sách tham gia</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {participants.map((p) => (
                <ParticipantRow key={p.id} participant={p} />
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}

function StatCard({ label, value, color }: { label: string; value: number; color: string }) {
  return (
    <Card>
      <CardContent className="p-4 text-center">
        <div className={`w-12 h-12 rounded-full ${color} text-white flex items-center justify-center mx-auto mb-2 text-xl font-bold`}>
          {value}
        </div>
        <p className="text-sm text-muted-foreground">{label}</p>
      </CardContent>
    </Card>
  )
}

function ParticipantRow({ participant }: { participant: any }) {
  const statusConfig = {
    attending: { label: 'Tham dự', icon: Check, color: 'text-success' },
    interested: { label: 'Quan tâm', icon: null, color: 'text-warning' },
    declined: { label: 'Không tham dự', icon: X, color: 'text-destructive' },
  }
  const config = statusConfig[participant.status]
  const Icon = config.icon

  return (
    <div className="flex items-center gap-3 p-3 rounded-lg hover:bg-neutral-50">
      <div className="w-10 h-10 rounded-full bg-primary/10 flex items-center justify-center text-sm font-medium text-primary">
        {participant.avatar}
      </div>
      <span className="flex-1 font-medium">{participant.name}</span>
      <Badge variant={participant.status === 'attending' ? 'success' : participant.status === 'interested' ? 'warning' : 'destructive'}>
        {config.label}
      </Badge>
    </div>
  )
}
