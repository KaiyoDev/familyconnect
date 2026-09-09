import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Badge } from '@/components/ui/basic'
import { FileText, Upload, Check, X, Eye } from 'lucide-react'
import { useNavigate } from 'react-router-dom'

interface Document {
  id: string
  title: string
  type: 'CERTIFICATE' | 'LETTER' | 'PHOTO' | 'VIDEO' | 'OTHER'
  status: 'PENDING' | 'APPROVED' | 'REJECTED'
  uploader: string
  date: string
}

export default function Her02HistoricalDocs() {
  const navigate = useNavigate()
  const [documents, setDocuments] = useState<Document[]>([
    { id: '1', title: 'Sắc phong năm 1920', type: 'CERTIFICATE', status: 'APPROVED', uploader: 'Nguyễn Văn A', date: '2026-09-05' },
    { id: '2', title: 'Thư mời họp mặt 2025', type: 'LETTER', status: 'PENDING', uploader: 'Trần Thị B', date: '2026-09-03' },
    { id: '3', title: 'Ảnh gia đình 1990', type: 'PHOTO', status: 'APPROVED', uploader: 'Lê Văn C', date: '2026-09-01' },
  ])

  const handleApprove = (docId: string) => {
    setDocuments(documents.map(d => d.id === docId ? { ...d, status: 'APPROVED' } : d))
  }

  const handleReject = (docId: string) => {
    setDocuments(documents.map(d => d.id === docId ? { ...d, status: 'REJECTED' } : d))
  }

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Tư liệu lịch sử</h1>
            <p className="text-neutral-600">Quản lý và phê duyệt tư liệu gia tộc</p>
          </div>
          <Button>
            <Upload className="h-4 w-4 mr-2" />
            Tải lên tư liệu
          </Button>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-3 gap-4">
          <StatCard label="Đã duyệt" value={documents.filter(d => d.status === 'APPROVED').length} color="text-success" />
          <StatCard label="Chờ duyệt" value={documents.filter(d => d.status === 'PENDING').length} color="text-warning" />
          <StatCard label="Từ chối" value={documents.filter(d => d.status === 'REJECTED').length} color="text-destructive" />
        </div>

        {/* Documents List */}
        <div className="space-y-3">
          {documents.map((doc) => (
            <DocCard key={doc.id} doc={doc} onApprove={handleApprove} onReject={handleReject} />
          ))}
        </div>
      </div>
    </Layout>
  )
}

function StatCard({ label, value, color }: { label: string; value: number; color: string }) {
  return (
    <Card>
      <CardContent className="p-4 text-center">
        <p className={`text-3xl font-bold ${color}`}>{value}</p>
        <p className="text-sm text-muted-foreground">{label}</p>
      </CardContent>
    </Card>
  )
}

function DocCard({ doc, onApprove, onReject }: { doc: Document; onApprove: (id: string) => void; onReject: (id: string) => void }) {
  const typeIcons = {
    CERTIFICATE: '📜',
    LETTER: '✉️',
    PHOTO: '🖼️',
    VIDEO: '🎬',
    OTHER: '📄',
  }

  return (
    <Card>
      <CardContent className="p-4 flex items-center gap-4">
        <div className="text-3xl">{typeIcons[doc.type]}</div>
        <div className="flex-1">
          <div className="flex items-center gap-2">
            <p className="font-medium">{doc.title}</p>
            <Badge variant={doc.status === 'APPROVED' ? 'success' : doc.status === 'PENDING' ? 'warning' : 'destructive'}>
              {doc.status === 'APPROVED' ? 'Đã duyệt' : doc.status === 'PENDING' ? 'Chờ duyệt' : 'Từ chối'}
            </Badge>
          </div>
          <p className="text-sm text-muted-foreground">
            {doc.type} • Bởi {doc.uploader} • {doc.date}
          </p>
        </div>
        <div className="flex gap-2">
          {doc.status === 'PENDING' && (
            <>
              <Button variant="ghost" size="icon" onClick={() => onApprove(doc.id)}>
                <Check className="h-4 w-4 text-success" />
              </Button>
              <Button variant="ghost" size="icon" onClick={() => onReject(doc.id)}>
                <X className="h-4 w-4 text-destructive" />
              </Button>
            </>
          )}
          <Button variant="ghost" size="icon">
            <Eye className="h-4 w-4" />
          </Button>
        </div>
      </CardContent>
    </Card>
  )
}
