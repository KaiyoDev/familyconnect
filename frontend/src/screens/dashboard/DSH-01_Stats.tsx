import React from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button } from '@/components/ui/basic'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts'
import { TrendingUp, Users, Calendar, BookOpen } from 'lucide-react'

const demographicData = [
  { name: '0-18', value: 5 },
  { name: '19-30', value: 8 },
  { name: '31-50', value: 7 },
  { name: '51-70', value: 3 },
  { name: '70+', value: 1 },
]

const eventStats = [
  { month: 'T1', events: 2 },
  { month: 'T2', events: 1 },
  { month: 'T3', events: 3 },
  { month: 'T4', events: 2 },
  { month: 'T5', events: 1 },
  { month: 'T6', events: 4 },
]

const COLORS = ['#0D9488', '#F59E0B', '#DB2777', '#0284C7', '#16A34A']

export default function Dsh01Stats() {
  return (
    <Layout>
      <div className="space-y-6">
        <div>
          <h1 className="text-2xl font-bold text-neutral-900">Thống kê gia đình</h1>
          <p className="text-neutral-600">Tổng quan hoạt động và thành viên</p>
        </div>

        {/* Stats Cards */}
        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <StatCard icon={Users} label="Tổng thành viên" value="24" change="+2" />
          <StatCard icon={Calendar} label="Sự kiện năm" value="18" change="+5" />
          <StatCard icon={BookOpen} label="Tư liệu" value="156" change="+12" />
          <StatCard icon={TrendingUp} label="Bài viết" value="42" change="+8" />
        </div>

        {/* Charts */}
        <div className="grid lg:grid-cols-2 gap-6">
          <Card>
            <CardHeader>
              <CardTitle>Phân bố độ tuổi</CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={300}>
                <PieChart>
                  <Pie
                    data={demographicData}
                    cx="50%"
                    cy="50%"
                    innerRadius={60}
                    outerRadius={100}
                    paddingAngle={5}
                    dataKey="value"
                  >
                    {demographicData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
              <div className="grid grid-cols-2 gap-2 mt-4">
                {demographicData.map((item, idx) => (
                  <div key={item.name} className="flex items-center gap-2 text-sm">
                    <div className="w-3 h-3 rounded-full" style={{ backgroundColor: COLORS[idx] }} />
                    <span>{item.name}: {item.value}</span>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Sự kiện theo tháng</CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={eventStats}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="month" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="events" fill="#0D9488" radius={[4, 4, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </div>

        {/* Recent Activity */}
        <Card>
          <CardHeader>
            <CardTitle>Hoạt động gần đây</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {[
                { action: 'Thêm thành viên mới', detail: 'Nguyễn Văn E', time: '2 giờ trước' },
                { action: 'Tạo sự kiện', detail: 'Giỗ tổ họ Nguyễn', time: '1 ngày trước' },
                { action: 'Đăng bài viết', detail: 'Họp mặt gia đình', time: '2 ngày trước' },
              ].map((activity, idx) => (
                <div key={idx} className="flex items-center justify-between py-2 border-b border-border last:border-0">
                  <div>
                    <p className="font-medium">{activity.action}</p>
                    <p className="text-sm text-muted-foreground">{activity.detail}</p>
                  </div>
                  <span className="text-sm text-muted-foreground">{activity.time}</span>
                </div>
              ))}
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
  value: string; 
  change: string 
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
            <span className="text-xs text-success">{change}</span>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
