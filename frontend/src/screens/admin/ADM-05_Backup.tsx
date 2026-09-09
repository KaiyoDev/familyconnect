import React from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button } from '@/components/ui/basic'
import { Users, Calendar, BookOpen, TrendingUp, Download, FileText } from 'lucide-react'

export default function Adm05Backup() {
  const [backups] = React.useState([
    { id: '1', name: 'Backup tự động - 09/09/2026', size: '2.4 GB', date: '2026-09-09' },
    { id: '2', name: 'Backup thủ công - 01/09/2026', size: '2.3 GB', date: '2026-09-01' },
  ])

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Sao lưu & Phục hồi</h1>
            <p className="text-neutral-600">Quản lý bản sao lưu hệ thống</p>
          </div>
          <Button><Plus className="h-4 w-4 mr-2" />Tạo sao lưu mới</Button>
        </div>

        <div className="grid sm:grid-cols-3 gap-4">
          <StatCard label="Tổng dung lượng" value="7.0 GB" icon={Users} />
          <StatCard label="Số bản sao lưu" value={String(backups.length)} icon={Calendar} />
          <StatCard label="Lần backup cuối" value="09/09/2026" icon={Download} />
        </div>

        <Card>
          <CardHeader><CardTitle>Danh sách bản sao lưu</CardTitle></CardHeader>
          <CardContent>
            <div className="space-y-3">
              {backups.map(b => (
                <div key={b.id} className="flex items-center justify-between p-4 bg-neutral-50 rounded-lg">
                  <div className="flex items-center gap-4">
                    <div className="w-10 h-10 rounded-lg bg-primary/10 flex items-center justify-center">
                      <Database className="h-5 w-5 text-primary" />
                    </div>
                    <div>
                      <p className="font-medium">{b.name}</p>
                      <p className="text-sm text-muted-foreground">{b.size} • {b.date}</p>
                    </div>
                  </div>
                  <div className="flex gap-2">
                    <Button variant="outline" size="sm"><Download className="h-4 w-4 mr-2" />Tải xuống</Button>
                    <Button variant="outline" size="sm"><ArrowRightLeft className="h-4 w-4 mr-2" />Phục hồi</Button>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}

function StatCard({ label, value, icon: Icon }: { label: string; value: string; icon: React.ElementType }) {
  return (
    <Card>
      <CardContent className="p-4 flex items-center gap-4">
        <div className="w-12 h-12 rounded-lg bg-primary/10 flex items-center justify-center"><Icon className="h-6 w-6 text-primary" /></div>
        <div><p className="text-2xl font-bold">{value}</p><p className="text-sm text-muted-foreground">{label}</p></div>
      </CardContent>
    </Card>
  )
}

function Plus(props: React.SVGProps<SVGSVGElement>) {
  return <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14"/><path d="M12 5v14"/></svg>
}

function Database(props: React.SVGProps<SVGSVGElement>) {
  return <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/></svg>
}

function ArrowRightLeft(props: React.SVGProps<SVGSVGElement>) {
  return <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m16 3 4 4-4 4"/><path d="M20 7H4"/><path d="m8 21-4-4 4-4"/><path d="M4 17h16"/></svg>
}
