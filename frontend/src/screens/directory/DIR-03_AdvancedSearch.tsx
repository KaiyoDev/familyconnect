import React from 'react'
import Layout from '@/components/Layout'
import { Input } from '@/components/ui/basic'
import { Search } from 'lucide-react'

export default function Dir03AdvancedSearch() {
  return (
    <Layout>
      <div className="space-y-6 max-w-2xl mx-auto">
        <h1 className="text-2xl font-bold">Tìm kiếm nâng cao</h1>
        <div className="relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-muted-foreground" />
          <Input placeholder="Tìm kiếm theo tên, nghề nghiệp, địa chỉ..." className="pl-10 py-6 text-base" />
        </div>
      </div>
    </Layout>
  )
}
