import React, { useEffect } from 'react'
import { useNavigate } from '@tanstack/react-router'
import { useAuthStore } from '../store/auth'
import { 
  Home, Users, Calendar, Archive, User, Menu, Bell, Search, 
  ChevronDown, LogOut, Settings, Plus, Filter, MoreVertical 
} from 'lucide-react'
import { Button } from './ui/basic'
import { Avatar, Badge } from './ui/basic'

interface LayoutProps {
  children: React.ReactNode
}

export default function Layout({ children }: LayoutProps) {
  const navigate = useNavigate()
  const { user, isAuthenticated, logout } = useAuthStore()
  const [sidebarOpen, setSidebarOpen] = React.useState(true)
  const [mobileMenuOpen, setMobileMenuOpen] = React.useState(false)
  const [userMenuOpen, setUserMenuOpen] = React.useState(false)

  useEffect(() => {
    if (!isAuthenticated) {
      navigate({ to: '/login' })
    }
  }, [isAuthenticated, navigate])

  const handleLogout = () => {
    logout()
    navigate({ to: '/login' })
  }

  const navItems = [
    { icon: Home, label: 'Trang chủ', path: '/dashboard' },
    { icon: Users, label: 'Gia phả', path: '/genealogy' },
    { icon: Calendar, label: 'Sự kiện', path: '/events' },
    { icon: Archive, label: 'Di sản', path: '/heritage' },
    { icon: User, label: 'Cá nhân', path: '/profile' },
  ]

  return (
    <div className="min-h-screen bg-neutral-50">
      {/* Mobile Header */}
      <header className="lg:hidden fixed top-0 left-0 right-0 z-40 bg-background border-b border-border h-14 flex items-center justify-between px-4">
        <Button variant="ghost" size="icon" onClick={() => setMobileMenuOpen(true)}>
          <Menu className="h-5 w-5" />
        </Button>
        <span className="font-semibold text-primary">FamilyConnect</span>
        <div className="flex items-center gap-2">
          <Button variant="ghost" size="icon" onClick={() => navigate({ to: '/notifications' })}>
            <Bell className="h-5 w-5" />
          </Button>
          <Avatar src={user?.avatar_url} fallback={user?.full_name?.[0] || 'U'} size="sm" />
        </div>
      </header>

      {/* Desktop Sidebar */}
      <aside className={`hidden lg:flex fixed left-0 top-0 h-full bg-background border-r border-border flex-col ${sidebarOpen ? 'w-56' : 'w-16'}`}>
        <div className="p-4 flex items-center gap-3 border-b border-border">
          <div className="w-8 h-8 rounded-lg bg-primary flex items-center justify-center flex-shrink-0">
            <span className="text-white font-bold text-sm">FC</span>
          </div>
          {sidebarOpen && <span className="font-semibold text-lg">FamilyConnect</span>}
        </div>

        <nav className="flex-1 p-2 space-y-1">
          {navItems.map((item) => (
            <button
              key={item.path}
              onClick={() => navigate({ to: item.path })}
              className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-md transition-colors ${
                sidebarOpen ? 'justify-start' : 'justify-center'
              } hover:bg-accent text-muted-foreground hover:text-foreground`}
            >
              <item.icon className="h-5 w-5 flex-shrink-0" />
              {sidebarOpen && <span className="text-sm font-medium">{item.label}</span>}
            </button>
          ))}
        </nav>

        <div className="p-4 border-t border-border">
          <div className={`flex items-center gap-3 ${!sidebarOpen && 'justify-center'}`}>
            <Avatar src={user?.avatar_url} fallback={user?.full_name?.[0] || 'U'} size="sm" />
            {sidebarOpen && (
              <div className="flex-1 min-w-0">
                <p className="text-sm font-medium truncate">{user?.full_name}</p>
                <p className="text-xs text-muted-foreground truncate">{user?.email}</p>
              </div>
            )}
            {sidebarOpen && (
              <Button variant="ghost" size="icon" onClick={handleLogout}>
                <LogOut className="h-4 w-4" />
              </Button>
            )}
          </div>
        </div>
      </aside>

      {/* Mobile Menu Sheet */}
      {mobileMenuOpen && (
        <div className="fixed inset-0 z-50 lg:hidden">
          <div className="fixed inset-0 bg-black/40" onClick={() => setMobileMenuOpen(false)} />
          <div className="fixed inset-y-0 left-0 w-80 bg-background shadow-lg">
            <div className="p-4 border-b border-border flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="w-8 h-8 rounded-lg bg-primary flex items-center justify-center">
                  <span className="text-white font-bold text-sm">FC</span>
                </div>
                <span className="font-semibold">FamilyConnect</span>
              </div>
              <Button variant="ghost" size="icon" onClick={() => setMobileMenuOpen(false)}>
                <ChevronDown className="h-5 w-5 rotate-90" />
              </Button>
            </div>
            <nav className="p-4 space-y-2">
              {navItems.map((item) => (
                <button
                  key={item.path}
                  onClick={() => {
                    navigate({ to: item.path })
                    setMobileMenuOpen(false)
                  }}
                  className="w-full flex items-center gap-3 px-4 py-3 rounded-md hover:bg-accent"
                >
                  <item.icon className="h-5 w-5" />
                  <span className="font-medium">{item.label}</span>
                </button>
              ))}
            </nav>
            <div className="absolute bottom-0 left-0 right-0 p-4 border-t border-border">
              <div className="flex items-center gap-3">
                <Avatar src={user?.avatar_url} fallback={user?.full_name?.[0] || 'U'} />
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-medium truncate">{user?.full_name}</p>
                  <p className="text-xs text-muted-foreground truncate">{user?.email}</p>
                </div>
                <Button variant="ghost" size="icon" onClick={handleLogout}>
                  <LogOut className="h-5 w-5" />
                </Button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Main Content */}
      <main className={`pt-14 lg:pt-0 ${sidebarOpen ? 'lg:ml-56' : 'lg:ml-16'} transition-all`}>
        {/* Top Bar */}
        <div className="hidden lg:flex h-14 border-b border-border bg-background sticky top-0 z-30 items-center justify-between px-6">
          <div className="flex items-center gap-4 flex-1">
            <Button variant="ghost" size="icon" onClick={() => setSidebarOpen(!sidebarOpen)}>
              <Menu className="h-5 w-5" />
            </Button>
            <div className="relative max-w-md w-full">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
              <input
                type="text"
                placeholder="Tìm kiếm..."
                className="input pl-9 pr-4 py-2 w-full rounded-full text-sm"
              />
            </div>
          </div>
          <div className="flex items-center gap-3">
            <Button variant="ghost" size="icon" className="relative" onClick={() => navigate({ to: '/notifications' })}>
              <Bell className="h-5 w-5" />
              <Badge className="absolute -top-1 -right-1 h-4 w-4 p-0 flex items-center justify-center" variant="destructive">
                3
              </Badge>
            </Button>
            <Avatar src={user?.avatar_url} fallback={user?.full_name?.[0] || 'U'} />
          </div>
        </div>

        <div className="p-4 lg:p-6">
          {children}
        </div>
      </main>

      {/* Mobile Bottom Nav */}
      <nav className="lg:hidden fixed bottom-0 left-0 right-0 bg-background border-t border-border z-40">
        <div className="flex justify-around items-center h-16">
          {navItems.map((item) => (
            <button
              key={item.path}
              onClick={() => navigate({ to: item.path })}
              className="flex flex-col items-center justify-center w-full h-full gap-1 text-muted-foreground"
            >
              <item.icon className="h-5 w-5" />
              <span className="text-xs">{item.label}</span>
            </button>
          ))}
        </div>
      </nav>
    </div>
  )
}
