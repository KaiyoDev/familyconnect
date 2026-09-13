import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Input, Label } from '@/components/ui/basic'
import { Sparkles, ArrowRight } from 'lucide-react'
import { toast } from 'sonner'

export default function Gen03RelationshipLookup() {
  const [memberA, setMemberA] = useState('')
  const [memberB, setMemberB] = useState('')
  const [relationshipType, setRelationshipType] = useState('PARENT_CHILD')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState<string | null>(null)

  const handleLookup = async () => {
    if (!memberA || !memberB) {
      toast.error('Vui lòng chọn đầy đủ thành viên')
      return
    }
    setLoading(true)
    // Stub: in production this calls aiApi.lookupRelationship
    setTimeout(() => {
      setResult(`Mối quan hệ giữa ${memberA} và ${memberB}: Cha - Con (giả định)`)
      setLoading(false)
    }, 500)
  }

  const handleExplain = async () => {
    if (!memberA || !memberB) {
      toast.error('Vui lòng chọn đầy đủ thành viên')
      return
    }
    setLoading(true)
    // Stub: in production this calls aiApi.explainRelationship
    setTimeout(() => {
      setResult(`${memberA} là cha/mẹ của ${memberB} theo quan hệ ${relationshipType}. Đây là mối quan hệ trực tiếp trong gia phả.`)
      setLoading(false)
    }, 500)
  }

  return (
    <Layout>
      <div className="space-y-6 max-w-2xl mx-auto">
        <div>
          <h1 className="text-2xl font-bold text-neutral-900">Tra cứu quan hệ</h1>
          <p className="text-neutral-600">Tìm hiểu mối quan hệ giữa các thành viên trong gia đình</p>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Chọn thành viên</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid sm:grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label htmlFor="member-a">Thành viên 1</Label>
                <Input id="member-a" placeholder="Chọn thành viên..." value={memberA} onChange={(e) => setMemberA(e.target.value)} />
              </div>
              <div className="space-y-2">
                <Label htmlFor="member-b">Thành viên 2</Label>
                <Input id="member-b" placeholder="Chọn thành viên..." value={memberB} onChange={(e) => setMemberB(e.target.value)} />
              </div>
            </div>

            <div className="space-y-2">
              <Label>Kiểu quan hệ</Label>
              <select className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm" value={relationshipType} onChange={(e) => setRelationshipType(e.target.value)}>
                <option value="PARENT_CHILD">Cha - Con</option>
                <option value="MARRIAGE">Hôn nhân</option>
                <option value="SIBLING">Anh - Chị - Em</option>
              </select>
            </div>

            <div className="flex gap-3">
              <Button onClick={handleLookup} disabled={loading} className="flex-1">
                <ArrowRight className="h-4 w-4 mr-2" />
                Tra cứu
              </Button>
              <Button variant="outline" onClick={handleExplain} disabled={loading}>
                <Sparkles className="h-4 w-4 mr-2" />
                AI giải thích
              </Button>
            </div>
          </CardContent>
        </Card>

        {result && (
          <Card className="bg-primary/5 border-primary/20">
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Sparkles className="h-5 w-5 text-primary" />
                Kết quả
              </CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-neutral-700">{result}</p>
            </CardContent>
          </Card>
        )}

        <Card>
          <CardHeader>
            <CardTitle>Bảng xưng hô nhanh</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b">
                    <th className="text-left py-2 px-4">Quan hệ</th>
                    <th className="text-left py-2 px-4">Xưng hô</th>
                  </tr>
                </thead>
                <tbody>
                  <tr className="border-b"><td className="py-2 px-4">Cha → Con trai</td><td className="py-2 px-4">Cha gọi con: con, tên con | Con gọi cha: cha, bố</td></tr>
                  <tr className="border-b"><td className="py-2 px-4">Cha → Con gái</td><td className="py-2 px-4">Cha gọi con: con, tên con | Con gọi cha: cha, bố</td></tr>
                  <tr className="border-b"><td className="py-2 px-4">Anh trai → Em trai</td><td className="py-2 px-4">Anh gọi em: em, tên em | Em gọi anh: anh</td></tr>
                  <tr><td className="py-2 px-4">Anh trai → Em gái</td><td className="py-2 px-4">Anh gọi em: em, tên em | Em gọi anh: anh</td></tr>
                </tbody>
              </table>
            </div>
          </CardContent>
        </Card>
      </div>
    </Layout>
  )
}
