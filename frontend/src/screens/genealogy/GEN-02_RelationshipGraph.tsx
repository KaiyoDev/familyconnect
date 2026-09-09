import React from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button } from '@/components/ui/basic'
import { ZoomIn, ZoomOut, Maximize2, Download } from 'lucide-react'

export default function Gen02RelationshipGraph() {
  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Đồ thị quan hệ</h1>
            <p className="text-neutral-600">Xem quan hệ giữa các thành viên</p>
          </div>
          <div className="flex gap-2">
            <Button variant="outline" size="sm">
              <Download className="h-4 w-4 mr-2" />
              Xuất ảnh
            </Button>
          </div>
        </div>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle>Bảng đồ quan hệ gia đình</CardTitle>
            <div className="flex gap-2">
              <Button variant="outline" size="sm">
                <ZoomIn className="h-4 w-4" />
              </Button>
              <Button variant="outline" size="sm">
                <ZoomOut className="h-4 w-4" />
              </Button>
              <Button variant="outline" size="sm">
                <Maximize2 className="h-4 w-4" />
              </Button>
            </div>
          </CardHeader>
          <CardContent>
            <div className="bg-neutral-50 rounded-lg p-8 min-h-[600px] relative overflow-hidden">
              {/* SVG Graph */}
              <svg className="w-full h-[600px]" viewBox="0 0 800 600">
                {/* Connections */}
                <line x1="400" y1="100" x2="250" y2="250" stroke="#CBD5E1" strokeWidth="2" />
                <line x1="400" y1="100" x2="550" y2="250" stroke="#CBD5E1" strokeWidth="2" />
                <line x1="250" y1="250" x2="150" y2="400" stroke="#CBD5E1" strokeWidth="2" />
                <line x1="250" y1="250" x2="350" y2="400" stroke="#CBD5E1" strokeWidth="2" />
                <line x1="250" y1="250" x2="550" y2="400" stroke="#CBD5E1" strokeWidth="2" />
                
                {/* Founder */}
                <circle cx="400" cy="100" r="40" fill="#FEF3C7" stroke="#F59E0B" strokeWidth="2" />
                <text x="400" y="105" textAnchor="middle" className="text-sm font-medium fill-neutral-700">Nguyễn Văn Tổ</text>
                
                {/* Generation 2 */}
                <circle cx="250" cy="250" r="35" fill="#CCFBF1" stroke="#0D9488" strokeWidth="2" />
                <text x="250" y="255" textAnchor="middle" className="text-sm font-medium fill-neutral-700">Nguyễn Văn Cha</text>
                
                <circle cx="550" cy="250" r="35" fill="#FDF2F8" stroke="#DB2777" strokeWidth="2" />
                <text x="550" y="255" textAnchor="middle" className="text-sm font-medium fill-neutral-700">Nguyễn Thị Chị</text>
                
                {/* Generation 3 */}
                <circle cx="150" cy="400" r="30" fill="#CCFBF1" stroke="#0D9488" strokeWidth="2" />
                <text x="150" y="405" textAnchor="middle" className="text-sm font-medium fill-neutral-700">Con 1</text>
                
                <circle cx="350" cy="400" r="30" fill="#FDF2F8" stroke="#DB2777" strokeWidth="2" />
                <text x="350" y="405" textAnchor="middle" className="text-sm font-medium fill-neutral-700">Con 2</text>
                
                <circle cx="550" cy="400" r="30" fill="#CCFBF1" stroke="#0D9488" strokeWidth="2" />
                <text x="550" y="405" textAnchor="middle" className="text-sm font-medium fill-neutral-700">Con 3</text>
              </svg>
            </div>
          </CardContent>
        </Card>

        {/* Legend */}
        <div className="grid sm:grid-cols-3 gap-4">
          <LegendCard 
            color="bg-accent-light" 
            border="border-accent"
            title="Ông tổ"
            description="Người sáng lập dòng họ"
          />
          <LegendCard 
            color="bg-primary/10" 
            border="border-primary"
            title="Nam"
            description="Thành viên nam trong gia đình"
          />
          <LegendCard 
            color="bg-pink/10" 
            border="border-pink"
            title="Nữ"
            description="Thành viên nữ trong gia đình"
          />
        </div>
      </div>
    </Layout>
  )
}

function LegendCard({ color, border, title, description }: {
  color: string
  border: string
  title: string
  description: string
}) {
  return (
    <Card>
      <CardContent className="p-4 flex items-center gap-4">
        <div className={`w-12 h-12 rounded-full ${color} border-2 ${border} flex items-center justify-center`}>
          <span className="text-xs font-medium">●</span>
        </div>
        <div>
          <p className="font-medium">{title}</p>
          <p className="text-sm text-muted-foreground">{description}</p>
        </div>
      </CardContent>
    </Card>
  )
}
