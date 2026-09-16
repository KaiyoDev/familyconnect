import React, { useState } from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { Button, Input } from '@/components/ui/basic'
import { aiApi } from '@/services/api'
import { toast } from 'sonner'
import { Sparkles, Send, Bot, User, Loader } from 'lucide-react'

interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  timestamp: string
}

export default function Ai01AIAssistant() {
  const [messages, setMessages] = useState<Message[]>([
    { id: '1', role: 'assistant', content: 'Chào bạn! Tôi là trợ lý AI của gia đình. Tôi có thể giúp bạn tra cứu quan hệ, tìm kiếm thông tin, hoặc giải thích các mối quan hệ trong gia phả. Bạn cần tôi giúp gì?', timestamp: new Date().toISOString() }
  ])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [conversations, setConversations] = useState([
    { id: '1', title: 'Hỏi về quan hệ gia đình', date: 'Hôm nay' },
    { id: '2', title: 'Tìm kiếm tư liệu', date: 'Hôm qua' },
  ])

  const handleSend = async () => {
    if (!input.trim()) return
    
    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: input,
      timestamp: new Date().toISOString(),
    }
    
    setMessages(prev => [...prev, userMessage])
    setInput('')
    setLoading(true)

    try {
      // Simulate AI response
      await new Promise(resolve => setTimeout(resolve, 1000))
      
      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: 'Đây là câu trả lời mẫu từ AI. Trong thực tế, đây sẽ là phản hồi từ API AI của bạn.',
        timestamp: new Date().toISOString(),
      }
      
      setMessages(prev => [...prev, assistantMessage])
    } catch (error) {
      toast.error('Có lỗi xảy ra')
    } finally {
      setLoading(false)
    }
  }

  return (
    <Layout>
      <div className="space-y-6 max-w-4xl mx-auto h-[calc(100vh-8rem)] flex">
        {/* Sidebar */}
        <div className="w-64 flex-shrink-0 space-y-4">
          <Button className="w-full" onClick={() => setMessages([])}>
            <Sparkles className="h-4 w-4 mr-2" />
            Hội thoại mới
          </Button>
          
          <div className="space-y-2">
            <h3 className="text-sm font-medium text-muted-foreground">Lịch sử</h3>
            {conversations.map((conv) => (
              <button
                key={conv.id}
                className="w-full text-left p-3 rounded-lg hover:bg-accent text-sm"
              >
                <p className="font-medium truncate">{conv.title}</p>
                <p className="text-xs text-muted-foreground">{conv.date}</p>
              </button>
            ))}
          </div>
        </div>

        {/* Chat Area */}
        <div className="flex-1 flex flex-col">
          <Card className="flex-1 flex flex-col">
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Bot className="h-5 w-5 text-primary" />
                Trợ lý AI Gia tộc
              </CardTitle>
            </CardHeader>
            <CardContent className="flex-1 overflow-y-auto space-y-4 pb-4">
              {messages.map((msg) => (
                <MessageBubble key={msg.id} message={msg} />
              ))}
              {loading && (
                <div className="flex items-center gap-2 text-muted-foreground">
                  <Loader className="h-4 w-4 animate-spin" />
                  <span>Đang suy nghĩ...</span>
                </div>
              )}
            </CardContent>
            
            <div className="p-4 border-t border-border">
              <div className="flex gap-2">
                <Input
                  placeholder="Nhập câu hỏi..."
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  onKeyDown={(e) => e.key === 'Enter' && handleSend()}
                  className="flex-1"
                />
                <Button onClick={handleSend} disabled={loading}>
                  <Send className="h-4 w-4" />
                </Button>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </Layout>
  )
}

function MessageBubble({ message }: { message: Message }) {
  const isUser = message.role === 'user'
  
  return (
    <div className={`flex gap-3 ${isUser ? 'flex-row-reverse' : ''}`}>
      <div className={`w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 ${
        isUser ? 'bg-primary text-white' : 'bg-accent text-accent-foreground'
      }`}>
        {isUser ? <User className="h-4 w-4" /> : <Bot className="h-4 w-4" />}
      </div>
      <div className={`max-w-[70%] rounded-lg p-3 ${
        isUser ? 'bg-primary text-white' : 'bg-neutral-100'
      }`}>
        <p className="text-sm whitespace-pre-wrap">{message.content}</p>
        <p className="text-xs opacity-75 mt-1">
          {new Date(message.timestamp).toLocaleTimeString('vi-VN')}
        </p>
      </div>
    </div>
  )
}
