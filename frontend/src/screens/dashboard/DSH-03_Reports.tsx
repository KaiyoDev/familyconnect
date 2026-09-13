import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Input, Label } from '@/components/ui/basic'
import { Download, FileText, Plus } from 'lucide-react'

export default function Dsh03Reports() {
  const [reportType, setReportType] = useState('genealogy')
  const [year, setYear] = useState('2026')

  const reportTypes = [
    { id: 'genealogy', name: 'Gia phả', description: 'Xuất cây gia phả toàn bộ' },
    { id: 'members', name: 'Thành viên', description: 'Danh sách thành viên chi tiết' },
    { id: 'events', name: 'Sự kiện', description: 'Báo cáo sự kiện trong năm' },
    { id: 'heritage', name: 'Di sản', description: 'Kho lưu trữ tư liệu' },
  ]

  return (
    <Layout>
      <div className="space-y-6">
        <div>
          <h1 className="text-2xl font-bold text-neutral-900">Tạo & Xuất báo cáo</h1>
          <p className="text-neutral-600">Xuất dữ liệu gia đình theo mẫu có sẵn</p>
        </div>

        {/* Report Type Selection */}
        <Card>
          <CardHeader>
            <CardTitle>Chọn loại báo cáo</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid sm:grid-cols-2 gap-4">
              {reportTypes.map((type) => (
                <button
                  key={type.id}
                  onClick={() => setReportType(type.id)}
                  className={`p-4 rounded-lg border-2 text-left transition-colors ${
                    reportType === type.id ? 'border-primary bg-primary/5' : 'border-border hover:border-primary/50'
                  }`}
                >
                  <FileText className="h-6 w-6 text-primary mb-2" />
                  <p className="font-medium">{type.name}</p>
                  <p className="text-sm text-muted-foreground">{type.description}</p>
                </button>
              ))}
            </div>
          </CardContent>
        </Card>

        {/* Export Options */}
        <Card>
          <CardHeader>
            <CardTitle>Tùy chọn xuất</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid sm:grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label>Năm</Label>
                <select
                  className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm"
                  value={year}
                  onChange={(e) => setYear(e.target.value)}
                >
                  <option value="2026">2026</option>
                  <option value="2025">2025</option>
                  <option value="2024">2024</option>
                  <option value="all">Tất cả</option>
                </select>
              </div>
              <div className="space-y-2">
                <Label>Định dạng</Label>
                <select className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm">
                  <option value="pdf">PDF</option>
                  <option value="excel">Excel</option>
                  <option value="image">Ảnh (PNG)</option>
                </select>
              </div>
            </div>
            <Button className="w-full sm:w-auto" onClick={() => alert('Đang tạo báo cáo...')}>
              <Download className="h-4 w-4 mr-2" />
              Xuất báo cáo
            </Button>
          </CardContent>
        </Card>

        {/* Previous Reports */}
        <Card>
          <CardHeader>
            <CardTitle>Báo cáo đã xuất</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {[
                { name: 'Gia phả họ Nguyễn - 2026', date: '09/09/2026', size: '2.4 MB' },
                { name: 'Danh sách thành viên', date: '01/09/2026', size: '156 KB' },
              ].map((report, idx) => (
                <div key={idx} className="flex items-center justify-between p-3 bg-neutral-50 rounded-lg">
                  <div className="flex items-center gap-3">
                    <FileText className="h-5 w-5 text-primary" />
                    <div>
                      <p className="font-medium">{report.name}</p>
                      <p className="text-sm text-muted-foreground">{report.date} • {report.size}</p>
                    </div>
                  </div>
                  <Button variant="outline" size="sm">
                    <Download className="h-4 w-4 mr-2" />
                    Tải xuống
                  </Button>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}
