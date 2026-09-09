import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Input, Label } from '@/components/ui/basic'
import { postApi } from '@/services/api'
import { toast } from 'sonner'
import { ArrowLeft, Image as ImageIcon, Smile, Tag, X } from 'lucide-react'

export default function Com03CreatePost() {
  const navigate = useNavigate()
  const [content, setContent] = useState('')
  const [mediaUrls, setMediaUrls] = useState<string[]>([])
  const [visibility, setVisibility] = useState('FAMILY')
  const [loading, setLoading] = useState(false)
  const [imagePreview, setImagePreview] = useState<string | null>(null)

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file) {
      const reader = new FileReader()
      reader.onloadend = () => {
        setImagePreview(reader.result as string)
        setMediaUrls([...mediaUrls, reader.result as string])
      }
      reader.readAsDataURL(file)
    }
  }

  const handleRemoveImage = (index: number) => {
    setMediaUrls(mediaUrls.filter((_, i) => i !== index))
    if (index === 0) setImagePreview(null)
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!content.trim()) {
      toast.error('Vui lòng nhập nội dung bài viết')
      return
    }
    
    setLoading(true)
    try {
      await postApi.create('default-family-id', {
        content,
        media_urls: mediaUrls,
        visibility_scope: visibility,
      })
      toast.success('Đăng bài thành công!')
      navigate('/community')
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Đăng bài thất bại')
    } finally {
      setLoading(false)
    }
  }

  return (
    <Layout>
      <div className="space-y-6 max-w-2xl mx-auto">
        <div className="flex items-center gap-4">
          <Button variant="ghost" onClick={() => navigate(-1)} className="pl-0">
            <ArrowLeft className="h-4 w-4 mr-2" />
            Quay lại
          </Button>
          <h1 className="text-2xl font-bold text-neutral-900">Đăng bài viết</h1>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Tạo bài viết mới</CardTitle>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-2">
                <Label>Nội dung</Label>
                <textarea
                  className="flex min-h-[150px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm"
                  placeholder="Chia sẻ điều gì đó với gia đình..."
                  value={content}
                  onChange={(e) => setContent(e.target.value)}
                  required
                />
              </div>

              {/* Image Upload */}
              <div className="space-y-2">
                <Label>Ảnh (tùy chọn)</Label>
                <div className="flex flex-wrap gap-3">
                  {mediaUrls.map((url, idx) => (
                    <div key={idx} className="relative w-24 h-24 rounded-lg overflow-hidden">
                      <img src={url} alt="Preview" className="w-full h-full object-cover" />
                      <button
                        type="button"
                        onClick={() => handleRemoveImage(idx)}
                        className="absolute top-1 right-1 w-5 h-5 rounded-full bg-black/50 text-white flex items-center justify-center"
                      >
                        <X className="h-3 w-3" />
                      </button>
                    </div>
                  ))}
                  <label className="w-24 h-24 rounded-lg border-2 border-dashed border-neutral-300 flex flex-col items-center justify-center cursor-pointer hover:border-primary transition-colors">
                    <ImageIcon className="h-6 w-6 text-muted-foreground" />
                    <span className="text-xs text-muted-foreground mt-1">Thêm ảnh</span>
                    <input type="file" accept="image/*" className="hidden" onChange={handleImageChange} />
                  </label>
                </div>
              </div>

              {/* Visibility */}
              <div className="space-y-2">
                <Label>Phạm vi hiển thị</Label>
                <select
                  className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm"
                  value={visibility}
                  onChange={(e) => setVisibility(e.target.value)}
                >
                  <option value="FAMILY">Toàn gia đình</option>
                  <option value="BRANCH">Theo nhánh</option>
                  <option value="PUBLIC">Công khai</option>
                </select>
              </div>

              <div className="flex gap-3 pt-4">
                <Button type="submit" disabled={loading} className="flex-1">
                  {loading ? 'Đang đăng...' : 'Đăng bài'}
                </Button>
                <Button type="button" variant="outline" onClick={() => navigate(-1)}>
                  Hủy
                </Button>
              </div>
            </form>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}
