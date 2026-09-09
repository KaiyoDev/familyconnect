import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Badge } from '@/components/ui/basic'
import { Calendar, MapPin, Users, Plus, Filter } from 'lucide-react'
import { useNavigate } from 'react-router-dom'

interface Event {
  id: string
  title: string
  description: string
  start_time: string
  end_time?: string
  location: string
  organizer: string
  participant_count: number
  image_url?: string
}

export default function EvT01EventList() {
  const navigate = useNavigate()
  const [events, setEvents] = useState<Event[]>([
    {
      id: '1',
      title: 'Giỗ tổ họ Nguyễn',
      description: 'Lễ giỗ tổ dòng họ Nguyễn năm 2026',
      start_time: '2026-10-10T09:00:00Z',
      end_time: '2026-10-10T12:00:00Z',
      location: 'Nhà thờ họ - Hà Nội',
      organizer: 'Nguyễn Văn A',
      participant_count: 18,
    },
    {
      id: '2',
      title: 'Họp mặt cuối năm',
      description: 'Tổng kết năm 2026 và đón Tết Nguyên Đán',
      start_time: '2026-12-31T18:00:00Z',
      location: 'Nhà văn hóa phường',
      organizer: 'Nguyễn Văn B',
      participant_count: 24,
    },
  ])
  const [filter, setFilter] = useState<'all' | 'upcoming' | 'past'>('upcoming')

  const filteredEvents = events.filter(e => {
    const date = new Date(e.start_time)
    const now = new Date()
    if (filter === 'upcoming') return date >= now
    if (filter === 'past') return date < now
    return true
  })

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Sự kiện gia đình</h1>
            <p className="text-neutral-600">Quản lý và tham gia sự kiện</p>
          </div>
          <Button onClick={() => navigate('/events/new')}>
            <Plus className="h-4 w-4 mr-2" />
            Tạo sự kiện
          </Button>
        </div>

        {/* Filters */}
        <div className="flex gap-2">
          {(['all', 'upcoming', 'past'] as const).map((f) => (
            <button
              key={f}
              onClick={() => setFilter(f)}
              className={`px-4 py-2 rounded-full text-sm font-medium ${
                filter === f ? 'bg-primary text-white' : 'bg-background border border-border'
              }`}
            >
              {f === 'all' ? 'Tất cả' : f === 'upcoming' ? 'Sắp tới' : 'Đã qua'}
            </button>
          ))}
        </div>

        {/* Events Grid */}
        <div className="grid md:grid-cols-2 gap-4">
          {filteredEvents.map((event) => (
            <EventCard key={event.id} event={event} onClick={() => navigate(`/events/${event.id}`)} />
          ))}
        </div>

        {filteredEvents.length === 0 && (
          <div className="text-center py-12">
            <Calendar className="h-12 w-12 text-muted-foreground mx-auto mb-4" />
            <p className="text-neutral-600">Không có sự kiện nào</p>
            <Button variant="outline" className="mt-4" onClick={() => navigate('/events/new')}>
              Tạo sự kiện đầu tiên
            </Button>
          </div>
        )}
      </div>
    </Layout>
  )
}

function EventCard({ event, onClick }: { event: Event; onClick: () => void }) {
  const startDate = new Date(event.start_time)
  const isPast = startDate < new Date()

  return (
    <Card className="cursor-pointer hover:border-primary/50 transition-colors" onClick={onClick}>
      <CardContent className="p-4">
        <div className="flex gap-4">
          <div className={`w-16 h-16 rounded-lg flex flex-col items-center justify-center flex-shrink-0 ${
            isPast ? 'bg-neutral-100' : 'bg-primary text-white'
          }`}>
            <span className="text-xs opacity-75">{startDate.toLocaleString('vi-VN', { month: 'short' }).toUpperCase()}</span>
            <span className="text-xl font-bold">{startDate.getDate()}</span>
          </div>
          <div className="flex-1 min-w-0">
            <div className="flex items-start justify-between">
              <h3 className="font-semibold truncate">{event.title}</h3>
              {isPast && <Badge variant="secondary">Đã qua</Badge>}
            </div>
            <p className="text-sm text-muted-foreground mt-1 line-clamp-2">{event.description}</p>
            <div className="flex items-center gap-4 mt-3 text-xs text-muted-foreground">
              <span className="flex items-center gap-1">
                <Calendar className="h-3 w-3" />
                {startDate.toLocaleDateString('vi-VN')}
              </span>
              <span className="flex items-center gap-1">
                <MapPin className="h-3 w-3" />
                {event.location}
              </span>
            </div>
            <div className="flex items-center justify-between mt-3">
              <span className="flex items-center gap-1 text-xs text-muted-foreground">
                <Users className="h-3 w-3" />
                {event.participant_count} tham gia
              </span>
              {!isPast && <Button size="sm">RSVP</Button>}
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
