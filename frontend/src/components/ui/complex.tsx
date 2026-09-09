import React, { useState } from 'react'
import { cn } from '@/lib/utils'

// Simplified complex components without the problematic ones

// Tabs
export const Tabs = ({ defaultValue, children }: { defaultValue: string; children: React.ReactNode }) => {
  const [activeTab, setActiveTab] = useState(defaultValue)
  return React.createElement('div', { className: 'w-full' },
    React.createElement(TabsContext.Provider, { value: { activeTab, setActiveTab } }, children)
  )
}

const TabsContext = React.createContext<{ activeTab: string; setActiveTab: (t: string) => void } | null>(null)

export const TabsList = ({ children, className }: { children: React.ReactNode; className?: string }) => (
  <div className={cn('inline-flex h-10 items-center justify-center rounded-md bg-muted p-1 text-muted-foreground', className)}>
    {children}
  </div>
)

export const TabsTrigger = ({ value, children, className }: { value: string; children: React.ReactNode; className?: string }) => {
  const ctx = React.useContext(TabsContext)
  if (!ctx) return null
  const isActive = ctx.activeTab === value
  return React.createElement('button', {
    className: cn('inline-flex items-center justify-center whitespace-nowrap rounded-sm px-3 py-1.5 text-sm font-medium ring-offset-background transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
      isActive && 'bg-background text-foreground shadow-sm', className),
    onClick: () => ctx.setActiveTab(value)
  }, children)
}

export const TabsContent = ({ value, children, className }: { value: string; children: React.ReactNode; className?: string }) => {
  const ctx = React.useContext(TabsContext)
  if (!ctx) return null
  if (ctx.activeTab !== value) return null
  return React.createElement('div', { className: cn('mt-2 ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2', className) }, children)
}

// Dialog
export const Dialog = ({ open, onOpenChange, children }: { open: boolean; onOpenChange: (o: boolean) => void; children: React.ReactNode }) => {
  if (!open) return null
  return React.createElement(React.Fragment, null,
    React.createElement('div', { className: 'fixed inset-0 z-50 flex items-center justify-center', onClick: () => onOpenChange(false) },
      React.createElement('div', { className: 'fixed inset-0 bg-black/40' }),
      React.createElement('div', { className: 'relative z-50 w-full max-w-lg mx-4' }, children)
    )
  )
}

export const DialogContent = ({ children, className }: { children: React.ReactNode; className?: string }) =>
  React.createElement('div', { className: cn('bg-background rounded-[12px] shadow-lg p-6', className) }, children)

export const DialogHeader = ({ children, className }: { children: React.ReactNode; className?: string }) =>
  React.createElement('div', { className: cn('flex flex-col space-y-1.5 text-center sm:text-left mb-4', className) }, children)

export const DialogTitle = ({ children, className }: { children: React.ReactNode; className?: string }) =>
  React.createElement('h2', { className: cn('text-lg font-semibold leading-none tracking-tight', className) }, children)

export const DialogDescription = ({ children, className }: { children: React.ReactNode; className?: string }) =>
  React.createElement('p', { className: cn('text-sm text-muted-foreground', className) }, children)

export const DialogFooter = ({ children, className }: { children: React.ReactNode; className?: string }) =>
  React.createElement('div', { className: cn('flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2', className) }, children)

// Sheet/Drawer
export const Sheet = ({ open, onOpenChange, side = 'right', children }: { open: boolean; onOpenChange: (o: boolean) => void; side?: 'left' | 'right' | 'top' | 'bottom'; children: React.ReactNode }) => {
  if (!open) return null
  const sides = { left: 'left-0 top-0 h-full w-80 border-r', right: 'right-0 top-0 h-full w-80 border-l', top: 'top-0 left-0 right-0 h-auto max-h-[80vh] border-b', bottom: 'bottom-0 left-0 right-0 h-auto max-h-[80vh] border-t' }
  return React.createElement(React.Fragment, null,
    React.createElement('div', { className: 'fixed inset-0 z-50' }),
    React.createElement('div', { className: cn('fixed bg-background shadow-lg', sides[side]) }, children)
  )
}

// Dropdown Menu
export const DropdownMenu = ({ trigger, children }: { trigger: React.ReactNode; children: React.ReactNode }) => {
  const [open, setOpen] = useState(false)
  return React.createElement('div', { className: 'relative' },
    React.createElement('div', { onClick: () => setOpen(!open) }, trigger),
    open && React.createElement(React.Fragment, null,
      React.createElement('div', { className: 'fixed inset-0 z-10', onClick: () => setOpen(false) }),
      React.createElement('div', { className: 'absolute right-0 z-20 mt-2 w-56 rounded-md border bg-popover p-1 text-popover-foreground shadow-md' }, children)
    )
  )
}

export const DropdownMenuItem = ({ children, onClick, className }: { children: React.ReactNode; onClick?: () => void; className?: string }) =>
  React.createElement('button', { className: cn('relative flex w-full cursor-pointer select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none transition-colors hover:bg-accent hover:text-accent-foreground', className), onClick }, children)

// Select (simplified)
export const Select = ({ value, onValueChange, children, placeholder }: { value?: string; onValueChange?: (v: string) => void; children: React.ReactNode; placeholder?: string }) => {
  const [open, setOpen] = useState(false)
  return React.createElement('div', { className: 'relative' },
    React.createElement('button', {
      className: 'flex h-10 w-full items-center justify-between rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50',
      onClick: () => setOpen(!open)
    }, React.createElement('span', { className: value ? '' : 'text-muted-foreground' }, value || placeholder),
      React.createElement('svg', { className: 'h-4 w-4 opacity-50', xmlns: 'http://www.w3.org/2000/svg', width: '24', height: '24', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', strokeWidth: '2', strokeLinecap: 'round', strokeLinejoin: 'round' },
        React.createElement('path', { d: 'm6 9 6 6 6-6' })
      )
    ),
    open && React.createElement(React.Fragment, null,
      React.createElement('div', { className: 'fixed inset-0 z-10', onClick: () => setOpen(false) }),
      React.createElement('div', { className: 'absolute z-20 mt-1 w-full min-w-[8rem] overflow-hidden rounded-md border bg-popover text-popover-foreground shadow-md' },
        React.createElement('div', { className: 'p-1' }, children)
      )
    )
  )
}

export const SelectTrigger = ({ children, className }: { children: React.ReactNode; className?: string }) =>
  React.createElement('button', { className: cn('flex h-10 w-full items-center justify-between rounded-md border border-input bg-background px-3 py-2 text-sm', className) }, children)

export const SelectValue = ({ placeholder }: { placeholder?: string }) => null

export const SelectContent = ({ children }: { children: React.ReactNode }) =>
  React.createElement('div', { className: 'absolute z-20 mt-1 w-full min-w-[8rem] overflow-hidden rounded-md border bg-popover text-popover-foreground shadow-md' },
    React.createElement('div', { className: 'p-1' }, children)
  )

export const SelectItem = ({ value, children, onClick }: { value: string; children: React.ReactNode; onClick?: () => void }) =>
  React.createElement('button', {
    className: 'relative flex w-full cursor-pointer select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none hover:bg-accent hover:text-accent-foreground',
    onClick
  }, children)

// Checkbox
export const Checkbox = ({ checked, onCheckedChange, className }: { checked?: boolean; onCheckedChange?: (c: boolean) => void; className?: string }) =>
  React.createElement('button', {
    className: cn('peer h-4 w-4 shrink-0 rounded-sm border border-primary ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=checked]:text-primary-foreground', className),
    'data-state': checked ? 'checked' : 'unchecked',
    onClick: () => onCheckedChange?.(!checked)
  }, checked && React.createElement('svg', { className: 'h-3 w-3', xmlns: 'http://www.w3.org/2000/svg', width: '24', height: '24', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', strokeWidth: '2', strokeLinecap: 'round', strokeLinejoin: 'round' },
    React.createElement('polyline', { points: '20 6 9 17 4 12' })
  ))

// Radio Group
export const RadioGroup = ({ value, onValueChange, children, className }: { value?: string; onValueChange?: (v: string) => void; children: React.ReactNode; className?: string }) =>
  React.createElement('div', { className: cn('grid gap-2', className) }, children)

export const RadioGroupItem = ({ value, checked, onCheckedChange }: { value: string; checked?: boolean; onCheckedChange?: (v: string) => void }) =>
  React.createElement('button', {
    className: 'aspect-square h-4 w-4 rounded-full border border-primary text-primary ring-offset-background focus:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50',
    'data-state': checked ? 'checked' : 'unchecked',
    onClick: () => onCheckedChange?.(value)
  }, checked && React.createElement('span', { className: 'flex h-full w-full items-center justify-center' }, React.createElement('span', { className: 'h-2 w-2 rounded-full bg-current' })))

// Table
export const Table = ({ children, className }: { children: React.ReactNode; className?: string }) =>
  React.createElement('div', { className: cn('relative w-full overflow-auto', className) },
    React.createElement('table', { className: cn('w-full caption-bottom text-sm', className) }, children)
  )

export const TableHeader = ({ children, className }: { children: React.ReactNode; className?: string }) =>
  React.createElement('thead', { className: cn('[&_tr]:border-b', className) }, children)

export const TableBody = ({ children, className }: { children: React.ReactNode; className?: string }) =>
  React.createElement('tbody', { className: cn('[&_tr:last-child]:border-0', className) }, children)

export const TableRow = ({ children, className }: { children: React.ReactNode; className?: string }) =>
  React.createElement('tr', { className: cn('border-b border-border transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted', className) }, children)

export const TableHead = ({ children, className }: { children: React.ReactNode; className?: string }) =>
  React.createElement('th', { className: cn('h-10 px-2 text-left align-middle font-medium text-muted-foreground [&:has([role=checkbox])]:pr-0', className) }, children)

export const TableCell = ({ children, className }: { children: React.ReactNode; className?: string }) =>
  React.createElement('td', { className: cn('p-2 align-middle [&:has([role=checkbox])]:pr-0', className) }, children)

// Progress
export const ProgressBar = ({ value, max = 100, className }: { value: number; max?: number; className?: string }) =>
  React.createElement('div', { className: cn('h-2 w-full overflow-hidden rounded-full bg-secondary', className) },
    React.createElement('div', { className: 'h-full w-full flex-1 bg-primary transition-all', style: { width: `${(value / max) * 100}%` } })
  )

// Toast
export const Toast = ({ title, description, type = 'info', onClose }: { title: string; description?: string; type?: 'success' | 'error' | 'warning' | 'info'; onClose?: () => void }) => {
  const types: Record<string, string> = {
    success: 'bg-success-bg text-success border-success',
    error: 'bg-danger-bg text-danger border-danger',
    warning: 'bg-warning-bg text-warning border-warning',
    info: 'bg-info-bg text-info border-info',
  }
  return React.createElement('div', { className: cn('rounded-md border px-4 py-3 shadow-sm', types[type]) },
    React.createElement('div', { className: 'flex items-start justify-between' },
      React.createElement('div', null,
        title && React.createElement('p', { className: 'font-medium' }, title),
        description && React.createElement('p', { className: 'text-sm opacity-90' }, description)
      ),
      onClose && React.createElement('button', { onClick: onClose, className: 'ml-4 opacity-50 hover:opacity-100' },
        React.createElement('svg', { className: 'h-4 w-4', xmlns: 'http://www.w3.org/2000/svg', width: '24', height: '24', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', strokeWidth: '2', strokeLinecap: 'round', strokeLinejoin: 'round' },
          React.createElement('path', { d: 'M18 6 6 18' }),
          React.createElement('path', { d: 'm6 6 12 12' })
        )
      )
    )
  )
}
