import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Input } from '@/components/ui/basic'
import { aiApi } from '@/services/api'
import { toast } from 'sonner'
import { Search, Sparkles, FileText, Users, Calendar } from 'lucide-react'

export default function Ai02SearchResults() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<any[]>([])
  const [loading, setLoading] = useState(false)

  const handleSearch = async () => {
    if (!query.trim()) return
    
    setLoading(true)
    try {
      const response = await aiApi.search({ query })
      setResults(response.data.data.results || [])
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Tìm kiếm thất bại')
    } finally {
      setLoading(false)
    }
  }

  const suggestedQueries = [
    'Tra cứu quan hệ giữa Nguyễn Văn A và Nguyễn Văn B',
    'Tìm kiếm tư liệu về ông nội',
    'Sự kiện gia đình năm 2025',
  ]

  return (
    <Layout>
      <div className="space-y-6 max-w-3xl mx-auto">
        <div>
          <h1 className="text-2xl font-bold text-neutral-900">Tìm kiếm ngữ nghĩa</h1>
          <p className="text-neutral-600">Tìm kiếm thông tin trong kho dữ liệu gia đình bằng AI</p>
        </div>

        {/* Search Box */}
        <Card>
          <CardContent className="p-4">
            <div className="flex gap-2">
              <div className="relative flex-1">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-muted-foreground" />
                <Input
                  placeholder="Nhập câu hỏi hoặc từ khóa..."
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  className="pl-10 pr-4"
                  onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
                />
              </div>
              <Button onClick={handleSearch} disabled={loading}>
                {loading ? <Sparkles className="h-4 w-4 animate-spin" /> : <Search className="h-4 w-4" />}
                Tìm kiếm
              </Button>
            </div>
          </CardContent>
        </Card>

        {/* Suggested Queries */}
        {results.length === 0 && (
          <div>
            <h3 className="font-medium mb-3">Gợi ý tìm kiếm</h3>
            <div className="flex flex-wrap gap-2">
              {suggestedQueries.map((suggestion) => (
                <button
                  key={suggestion}
                  onClick={() => { setQuery(suggestion); handleSearch() }}
                  className="px-4 py-2 rounded-full border border-border text-sm hover:border-primary hover:text-primary transition-colors"
                >
                  {suggestion}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Results */}
        {results.length > 0 && (
          <div className="space-y-3">
            <h3 className="font-medium">Kết quả tìm kiếm ({results.length})</h3>
            {results.map((result, idx) => (
              <ResultCard key={idx} result={result} />
            ))}
          </div>
        )}

        {loading && (
          <div className="text-center py-12">
            <Sparkles className="h-12 w-12 text-primary animate-pulse mx-auto mb-4" />
            <p className="text-neutral-600">Đang tìm kiếm...</p>
          </div>
        )}
      </div>
    </Layout>
  )
}

function ResultCard({ result }: { result: any }) {
  const icons = {
    member: Users,
    document: FileText,
    event: Calendar,
  }
  const Icon = icons[result.type as keyof typeof icons] || FileText

  return (
    <Card className="cursor-pointer hover:border-primary/50 transition-colors">
      <CardContent className="p-4 flex gap-4">
        <div className="w-10 h-10 rounded-lg bg-primary/10 flex items-center justify-center flex-shrink-0">
          <Icon className="h-5 w-5 text-primary" />
        </div>
        <div className="flex-1">
          <p className="font-medium">{result.title}</p>
          <p className="text-sm text-muted-foreground mt-1">{result.content}</p>
          <div className="flex items-center gap-3 mt-2 text-xs text-muted-foreground">
            <span className="capitalize">{result.type}</span>
            {result.source && <span>• {result.source}</span>}
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
