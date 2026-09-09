import React from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Search, Filter, X } from 'lucide-react'
import { Button, Input } from '@/components/ui/basic'

export default function Shl03Search() {
  const [query, setQuery] = React.useState('')
  const [results, setResults] = React.useState<any[]>([])
  const [activeFilter, setActiveFilter] = React.useState<string | null>(null)

  const filters = [
    { id: 'all', label: 'Tất cả' },
    { id: 'members', label: 'Thành viên' },
    { id: 'events', label: 'Sự kiện' },
    { id: 'docs', label: 'Tư liệu' },
    { id: 'stories', label: 'Câu chuyện' },
  ]

  const handleSearch = (value: string) => {
    setQuery(value)
    // Simulate search results
    if (value.length > 2) {
      setResults([
        { id: 1, type: 'member', title: 'Nguyễn Văn A', subtitle: 'Ông tổ dòng họ' },
        { id: 2, type: 'event', title: 'Giỗ tổ họ Nguyễn', subtitle: '10/11/2026' },
        { id: 3, type: 'doc', title: 'Sắc phong năm 1920', subtitle: 'Tư liệu lịch sử' },
      ])
    } else {
      setResults([])
    }
  }

  return (
    <Layout>
      <div className="space-y-6 max-w-3xl mx-auto">
        <div>
          <h1 className="text-2xl font-bold text-neutral-900 mb-4">Tìm kiếm</h1>
          
          {/* Search Input */}
          <div className="relative">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-muted-foreground" />
            <Input
              type="text"
              placeholder="Tìm kiếm thành viên, sự kiện, tư liệu..."
              className="pl-10 pr-4 py-6 text-base rounded-xl"
              value={query}
              onChange={(e) => handleSearch(e.target.value)}
            />
          </div>

          {/* Filters */}
          <div className="flex flex-wrap gap-2 mt-4">
            {filters.map((filter) => (
              <button
                key={filter.id}
                onClick={() => setActiveFilter(activeFilter === filter.id ? null : filter.id)}
                className={`px-4 py-2 rounded-full text-sm font-medium transition-colors ${
                  activeFilter === filter.id
                    ? 'bg-primary text-primary-foreground'
                    : 'bg-background border border-border hover:border-primary'
                }`}
              >
                {filter.label}
              </button>
            ))}
          </div>
        </div>

        {/* Results */}
        {results.length > 0 && (
          <div className="space-y-3">
            <h2 className="text-sm font-medium text-muted-foreground">
              Tìm thấy {results.length} kết quả
            </h2>
            {results.map((result) => (
              <Card key={result.id} className="cursor-pointer hover:border-primary/50 transition-colors">
                <CardContent className="p-4 flex items-center gap-4">
                  <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${
                    result.type === 'member' ? 'bg-primary/10' :
                    result.type === 'event' ? 'bg-accent/10' :
                    'bg-info/10'
                  }`}>
                    {result.type === 'member' ? (
                      <span className="text-primary font-medium">NV</span>
                    ) : result.type === 'event' ? (
                      <Calendar className="h-5 w-5 text-accent" />
                    ) : (
                      <BookOpen className="h-5 w-5 text-info" />
                    )}
                  </div>
                  <div className="flex-1">
                    <p className="font-medium">{result.title}</p>
                    <p className="text-sm text-muted-foreground">{result.subtitle}</p>
                  </div>
                  <ArrowRight className="h-5 w-5 text-muted-foreground" />
                </CardContent>
              </Card>
            ))}
          </div>
        )}

        {/* Empty State */}
        {query.length > 0 && results.length === 0 && (
          <div className="text-center py-12">
            <Search className="h-12 w-12 text-muted-foreground mx-auto mb-4" />
            <p className="text-neutral-600">Không tìm thấy kết quả nào</p>
            <p className="text-sm text-muted-foreground mt-1">Thử tìm kiếm với từ khóa khác</p>
          </div>
        )}

        {/* Recent Searches */}
        {query.length === 0 && (
          <div>
            <h2 className="text-lg font-semibold mb-4">Tìm kiếm gần đây</h2>
            <div className="space-y-2">
              {['Nguyễn Văn An', 'Giỗ tổ', 'Sắc phong'].map((term) => (
                <button
                  key={term}
                  onClick={() => handleSearch(term)}
                  className="w-full flex items-center gap-3 p-3 rounded-lg hover:bg-accent transition-colors text-left"
                >
                  <Search className="h-4 w-4 text-muted-foreground" />
                  <span>{term}</span>
                  <X className="h-4 w-4 ml-auto text-muted-foreground hover:text-foreground" />
                </button>
              ))}
            </div>
          </div>
        )}
      </div>
    </Layout>
  )
}

function Calendar(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/></svg>
  )
}

function BookOpen(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
  )
}

function ArrowRight(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg {...props} xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
  )
}
