import React from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { 
  Users, Calendar, BookOpen, MessageCircle, 
  TrendingUp, Plus, ArrowRight 
} from 'lucide-react'
import { Button } from '@/components/ui/basic'
import { useNavigate } from 'react-router-dom'

export default function Shl02Dashboard() {
  const navigate = useNavigate()
  
  const quickActions = [
    { icon: Plus, label: 'Thêm thành viên', path: '/genealogy/add-member', color: 'bg-primary' },
    { icon: Calendar, label: 'Tạo sự kiện', path: '/events/new', color: 'bg-accent' },
    { icon: MessageCircle, label: 'Đăng bài viết', path: '/community/post/new', color: 'bg-info' },
  ]

  const recentActivity = [
    { id: 1, type: 'member', action: 'đã thêm thành viên mới', time: '2 giờ trước', avatar: 'NT' },
    { id: 2, type: 'event', action: 'đã tạo sự kiện "Giỗ tổ họ Nguyễn"', time: '5 giờ trước', avatar: 'GC' },
    { id: 3, type: 'post', action: 'đã đăng bài viết mới', time: '1 ngày trước', avatar: 'MH' },
  ]

  return (
    <Layout>
      <div className="space-y-6">
        {/* Header */}
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Trang chủ</h1>
            <p className="text-neutral-600">Gia đình Nguyễn Văn</p>
          </div>
          <Button onClick={() => navigate('/family/create')}>
            <Plus className="h-4 w-4 mr-2" />
            Tạo gia đình
          </Button>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
          <StatCard icon={Users} label="Thành viên" value="24" change="+2" />
          <StatCard icon={Calendar} label="Sự kiện" value="8" change="tháng này" />
          <StatCard icon={BookOpen} label="Tư liệu" value="156" change="" />
          <StatCard icon={MessageCircle} label="Bài viết" value="42" change="+5" />
        </div>

        {/* Quick Actions */}
        <div>
          <h2 className="text-lg font-semibold mb-4">Thao tác nhanh</h2>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            {quickActions.map((action) => (
              <button
                key={action.label}
                onClick={() => navigate(action.path)}
                className="flex items-center gap-4 p-4 bg-background rounded-[10px] border border-border hover:border-primary/50 transition-colors text-left"
              >
                <div className={`w-12 h-12 rounded-lg ${action.color} flex items-center justify-center`}>
                  <action.icon className="h-6 w-6 text-white" />
                </div>
                <span className="font-medium">{action.label}</span>
                <ArrowRight className="h-5 w-5 ml-auto text-muted-foreground" />
              </button>
            ))}
          </div>
        </div>

        {/* Main Content Grid */}
        <div className="grid lg:grid-cols-3 gap-6">
          {/* Family Tree Preview */}
          <Card className="lg:col-span-2">
            <CardHeader className="flex flex-row items-center justify-between pb-2">
              <CardTitle>Cây gia phả</CardTitle>
              <Button variant="ghost" size="sm" onClick={() => navigate('/genealogy')}>
                Xem tất cả
              </Button>
            </CardHeader>
            <CardContent>
              <div className="bg-neutral-50 rounded-lg p-8 min-h-[300px] flex items-center justify-center">
                <div className="text-center">
                  <div className="w-20 h-20 rounded-full bg-primary-light flex items-center justify-center mx-auto mb-4">
                    <Users className="h-10 w-10 text-primary" />
                  </div>
                  <p className="font-medium mb-2">Nguyễn Văn A</p>
                  <p className="text-sm text-muted-foreground">Ông tổ dòng họ</p>
                  <div className="mt-6 flex justify-center gap-8">
                    <div className="text-center">
                      <div className="w-12 h-12 rounded-full bg-primary/20 flex items-center justify-center mx-auto mb-2">
                        <span className="text-sm font-medium">NT</span>
                      </div>
                      <p className="text-xs text-muted-foreground">Nguyễn Văn B</p>
                    </div>
                    <div className="text-center">
                      <div className="w-12 h-12 rounded-full bg-pink/20 flex items-center justify-center mx-auto mb-2">
                        <span className="text-sm font-medium">GH</span>
                      </div>
                      <p className="text-xs text-muted-foreground">Giữ Thị C</p>
                    </div>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Recent Activity */}
          <Card>
            <CardHeader>
              <CardTitle>Hoạt động gần đây</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {recentActivity.map((activity) => (
                  <div key={activity.id} className="flex items-start gap-3">
                    <div className="w-8 h-8 rounded-full bg-primary-light flex items-center justify-center flex-shrink-0">
                      <span className="text-xs font-medium text-primary">{activity.avatar}</span>
                    </div>
                    <div className="flex-1 min-w-0">
                      <p className="text-sm">
                        <span className="font-medium">{activity.action}</span>
                      </p>
                      <p className="text-xs text-muted-foreground">{activity.time}</p>
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Upcoming Events */}
        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle>Sự kiện sắp tới</CardTitle>
            <Button variant="ghost" size="sm" onClick={() => navigate('/events')}>
              Xem tất cả
            </Button>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              <EventItem 
                title="Giỗ tổ họ Nguyễn"
                date="10/11/2026"
                time="09:00"
                location="Nhà thờ họ"
                upcoming
              />
              <EventItem 
                title="Họp mặt cuối năm"
                date="31/12/2026"
                time="18:00"
                location="Nhà văn hóa"
              />
            </div>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}

function StatCard({ icon: Icon, label, value, change }: { 
  icon: React.ElementType; 
  label: string; 
  value: string | number;
  change: string;
}) {
  return (
    <Card>
      <CardContent className="p-4 flex items-center gap-4">
        <div className="w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center">
          <Icon className="h-6 w-6 text-primary" />
        </div>
        <div>
          <p className="text-2xl font-bold">{value}</p>
          <div className="flex items-center gap-2">
            <p className="text-sm text-muted-foreground">{label}</p>
            {change && (
              <span className="text-xs text-success flex items-center gap-0.5">
                <TrendingUp className="h-3 w-3" />
                {change}
              </span>
            )}
          </div>
        </div>
      </CardContent>
    </Card>
  )
}

function EventItem({ title, date, time, location, upcoming }: {
  title: string
  date: string
  time: string
  location: string
  upcoming?: boolean
}) {
  return (
    <div className={`flex items-center gap-4 p-3 rounded-lg ${upcoming ? 'bg-primary/5 border border-primary/20' : 'bg-neutral-50'}`}>
      <div className={`w-12 h-12 rounded-lg flex items-center justify-center flex-shrink-0 ${upcoming ? 'bg-primary' : 'bg-neutral-200'}`}>
        <Calendar className={`h-6 w-6 ${upcoming ? 'text-white' : 'text-neutral-600'}`} />
      </div>
      <div className="flex-1 min-w-0">
        <p className="font-medium truncate">{title}</p>
        <p className="text-sm text-muted-foreground">{date} · {time}</p>
        <p className="text-xs text-muted-foreground">{location}</p>
      </div>
      {upcoming && (
        <Button size="sm">RSVP</Button>
      )}
    </div>
  )
}


