import React, { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button } from '@/components/ui/basic'
import { ArrowLeft, Upload, Image as ImageIcon, Download, Trash2 } from 'lucide-react'

export default function EvT05EventGallery() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [photos, setPhotos] = useState([
    { id: '1', url: 'https://placehold.co/400x300', caption: 'Ảnh giỗ tổ 2026', uploaded_by: 'Nguyễn Văn A' },
    { id: '2', url: 'https://placehold.co/400x300', caption: 'Khánh thành nhà thờ', uploaded_by: 'Trần Thị B' },
    { id: '3', url: 'https://placehold.co/400x300', caption: 'Gia đình sum họp', uploaded_by: 'Lê Văn C' },
  ])
  const [isUploading, setIsUploading] = useState(false)

  const handleUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files
    if (!files) return
    
    setIsUploading(true)
    // Simulate upload
    setTimeout(() => {
      const newPhotos = Array.from(files).map((file, idx) => ({
        id: String(Date.now() + idx),
        url: URL.createObjectURL(file),
        caption: '',
        uploaded_by: 'Current User',
      }))
      setPhotos([...photos, ...newPhotos])
      setIsUploading(false)
    }, 1000)
  }

  const handleDelete = (photoId: string) => {
    setPhotos(photos.filter(p => p.id !== photoId))
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
              <h1 className="text-2xl font-bold text-neutral-900">Thư viện ảnh sự kiện</h1>
              <p className="text-neutral-600">{photos.length} ảnh</p>
            </div>
          </div>
          <label className="cursor-pointer">
            <input type="file" multiple accept="image/*" className="hidden" onChange={handleUpload} />
            <Button disabled={isUploading}>
              <Upload className="h-4 w-4 mr-2" />
              {isUploading ? 'Đang tải lên...' : 'Tải ảnh lên'}
            </Button>
          </label>
        </div>

        {/* Upload Area */}
        <Card className="border-dashed border-2 border-primary/30 bg-primary/5">
          <CardContent className="py-12">
            <label className="cursor-pointer block text-center">
              <Upload className="h-12 w-12 text-primary mx-auto mb-4" />
              <p className="font-medium text-neutral-700">Kéo thả ảnh vào đây hoặc click để chọn</p>
              <p className="text-sm text-muted-foreground mt-1">Hỗ trợ: JPG, PNG, WEBP</p>
              <input type="file" multiple accept="image/*" className="hidden" onChange={handleUpload} />
            </label>
          </CardContent>
        </Card>

        {/* Gallery Grid */}
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {photos.map((photo) => (
            <div key={photo.id} className="relative group aspect-square rounded-lg overflow-hidden bg-neutral-100">
              <img src={photo.url} alt={photo.caption} className="w-full h-full object-cover" />
              <div className="absolute inset-0 bg-black/50 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-2">
                <Button variant="secondary" size="icon" className="h-8 w-8">
                  <Download className="h-4 w-4" />
                </Button>
                <Button variant="danger" size="icon" className="h-8 w-8" onClick={() => handleDelete(photo.id)}>
                  <Trash2 className="h-4 w-4" />
                </Button>
              </div>
              {photo.caption && (
                <div className="absolute bottom-0 left-0 right-0 p-2 bg-black/50 text-white text-xs">
                  {photo.caption}
                </div>
              )}
            </div>
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
