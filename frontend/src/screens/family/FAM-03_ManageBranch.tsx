import React, { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Input, Label } from '@/components/ui/basic'
import { branchApi } from '@/services/api'
import { toast } from 'sonner'
import { Plus, Trash2, Edit2 } from 'lucide-react'

interface Branch {
  id: string
  name: string
  description?: string
  member_count: number
  parent_branch?: string
}

export default function Fam03ManageBranch() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [branches, setBranches] = useState<Branch[]>([
    { id: '1', name: 'Nhánh chính', member_count: 12, parent_branch: null },
    { id: '2', name: 'Nhánh Bắc', member_count: 6, parent_branch: '1' },
    { id: '3', name: 'Nhánh Nam', member_count: 6, parent_branch: '1' },
  ])
  const [showAddForm, setShowAddForm] = useState(false)
  const [newBranch, setNewBranch] = useState({ name: '', description: '', parent_branch_id: '' })

  const handleAddBranch = async () => {
    try {
      const response = await branchApi.create(id!, newBranch)
      setBranches([...branches, { ...newBranch, id: response.data.data.id, member_count: 0 }])
      setShowAddForm(false)
      toast.success('Thêm nhánh thành công!')
    } catch (error: any) {
      toast.error(error.response?.data?.detail || 'Thêm nhánh thất bại')
    }
  }

  const handleDeleteBranch = (branchId: string) => {
    setBranches(branches.filter(b => b.id !== branchId))
    toast.success('Đã xóa nhánh')
  }

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-neutral-900">Quản lý nhánh gia đình</h1>
            <p className="text-neutral-600">Tổ chức các chi nhánh trong gia đình</p>
          </div>
          <Button onClick={() => setShowAddForm(!showAddForm)}>
            <Plus className="h-4 w-4 mr-2" />
            Thêm nhánh
          </Button>
        </div>

        {showAddForm && (
          <Card className="border-primary">
            <CardHeader>
              <CardTitle>Thêm nhánh mới</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="space-y-2">
                <Label>Tên nhánh</Label>
                <Input
                  value={newBranch.name}
                  onChange={(e) => setNewBranch({ ...newBranch, name: e.target.value })}
                  placeholder="Nhánh Bắc, Nhánh Nam..."
                />
              </div>
              <div className="space-y-2">
                <Label>Mô tả</Label>
                <Input
                  value={newBranch.description}
                  onChange={(e) => setNewBranch({ ...newBranch, description: e.target.value })}
                  placeholder="Mô tả chi nhánh..."
                />
              </div>
              <div className="flex gap-2">
                <Button onClick={handleAddBranch}>Thêm</Button>
                <Button variant="outline" onClick={() => setShowAddForm(false)}>Hủy</Button>
              </div>
            </CardContent>
          </Card>
        )}

        {/* Branch Tree */}
        <div className="space-y-4">
          {branches.map((branch) => (
            <BranchCard
              key={branch.id}
              branch={branch}
              onDelete={handleDeleteBranch}
            />
          ))}
        </div>

        {/* Branch Children */}
        <div className="ml-8 space-y-3">
          {branches.filter(b => b.parent_branch).map((branch) => (
            <BranchCard
              key={branch.id}
              branch={branch}
              onDelete={handleDeleteBranch}
              isChild
            />
          ))}
        </div>
      </div>
    </Layout>
  )
}

function BranchCard({ branch, onDelete, isChild = false }: {
  branch: Branch
  onDelete: (id: string) => void
  isChild?: boolean
}) {
  return (
    <div className={`flex items-center gap-4 p-4 bg-background rounded-lg border ${isChild ? 'border-l-4 border-l-primary' : 'border-border'}`}>
      <div className="w-10 h-10 rounded-lg bg-primary/10 flex items-center justify-center flex-shrink-0">
        <span className="text-primary font-medium">{branch.name[0]}</span>
      </div>
      <div className="flex-1">
        <p className="font-medium">{branch.name}</p>
        <p className="text-sm text-muted-foreground">{branch.description || 'Không có mô tả'}</p>
      </div>
      <div className="flex items-center gap-2">
        <Badge variant="secondary">{branch.member_count} thành viên</Badge>
        <Button variant="ghost" size="icon">
          <Edit2 className="h-4 w-4" />
        </Button>
        <Button variant="ghost" size="icon" onClick={() => onDelete(branch.id)}>
          <Trash2 className="h-4 w-4 text-danger" />
        </Button>
      </div>
    </div>
  )
}

function Badge({ children, variant = 'default' }: { children: React.ReactNode; variant?: string }) {
  const variants: Record<string, string> = {
    default: 'bg-primary/10 text-primary',
    secondary: 'bg-neutral-100 text-neutral-700',
  }
  return (
    <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${variants[variant] || variants.default}`}>
      {children}
    </span>
  )
}
