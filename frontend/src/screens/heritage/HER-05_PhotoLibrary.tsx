import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button } from '@/components/ui/basic'
import { Download, Trash2, Plus, Image as ImageIcon } from 'lucide-react'

export default function Her05PhotoLibrary() {
  const [photos, setPhotos] = useState([
    { id: '1', url: 'https://placehold.co/400x300', caption: 'Gia đình năm 1990', uploaded_by: 'Nguyễn Văn A', date: '2026-09-01' },
    { id: '2', url: 'https://placehold.co/400x300', caption: 'Ngày cưới bố mẹ', uploaded_by: 'Trần Thị B', date: '2026-08-28' },
    { id: '3', url: 'https://placehold.co/400x300', caption: 'Họp mặt Tết 2025', uploaded_by: 'Lê Văn C', date: '2026-08-25' },
    { id: '4', url: 'https://placehold.co/400x300', caption: 'Du lịch hè', uploaded_by: 'Phạm Thị D', date: '2026-08-20' },
  ])

  const [filter, setFilter] = useState('all')

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Thư viện ảnh gia đình</h1>
            <p className="text-neutral-600">{photos.length} ảnh</p>
          </div>
          <Button>
            <Plus className="h-4 w-4 mr-2" />
            Tải ảnh lên
          </Button>
        </div>

        {/* Filters */}
        <div className="flex gap-2">
          {['all', 'recent', 'favorites'].map((f) => (
            <button
              key={f}
              onClick={() => setFilter(f)}
              className={`px-4 py-2 rounded-full text-sm font-medium ${
                filter === f ? 'bg-primary text-white' : 'bg-background border border-border'
              }`}
            >
              {f === 'all' ? 'Tất cả' : f === 'recent' ? 'Mới nhất' : 'Yêu thích'}
            </button>
          ))}
        </div>

        {/* Photo Grid */}
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {photos.map((photo) => (
            <PhotoCard key={photo.id} photo={photo} />
          ))}
        </div>

        {photos.length === 0 && (
          <div className="text-center py-12">
            <ImageIcon className="h-12 w-12 text-muted-foreground mx-auto mb-4" />
            <p className="text-neutral-600">Chưa có ảnh nào</p>
          </div>
        )}
      </div>
    </Layout>
  )
}

function PhotoCard({ photo }: { photo: any }) {
  return (
    <div className="group relative aspect-square rounded-lg overflow-hidden bg-neutral-100">
      <img src={photo.url} alt={photo.caption} className="w-full h-full object-cover transition-transform group-hover:scale-105" />
      <div className="absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-colors flex items-center justify-center opacity-0 group-hover:opacity-100">
        <div className="flex gap-2">
          <Button variant="secondary" size="icon" className="h-8 w-8">
            <Download className="h-4 w-4" />
          </Button>
          <Button variant="danger" size="icon" className="h-8 w-8">
            <Trash2 className="h-4 w-4" />
          </Button>
        </div>
      </div>
      <div className="absolute bottom-0 left-0 right-0 p-2 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity">
        <p className="text-white text-xs truncate">{photo.caption}</p>
      </div>
    </div>
  )
}


