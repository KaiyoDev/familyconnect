import React from 'react'
import { Link } from 'react-router-dom'
import { Button } from '@/components/ui/basic'
import { Users, BookOpen, Heart, Sparkles } from 'lucide-react'

export default function Pub01Landing() {
  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60 sticky top-0 z-50">
        <div className="container mx-auto px-4 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg bg-primary flex items-center justify-center">
              <span className="text-white font-bold text-sm">FC</span>
            </div>
            <span className="font-semibold text-lg">FamilyConnect</span>
          </div>
          <div className="flex items-center gap-3">
            <Link to="/login">
              <Button variant="ghost">Đăng nhập</Button>
            </Link>
            <Link to="/register">
              <Button>Khởi tạo</Button>
            </Link>
          </div>
        </div>
      </header>

      {/* Hero */}
      <section className="py-20 lg:py-32">
        <div className="container mx-auto px-4 text-center">
          <h1 className="text-4xl lg:text-6xl font-bold text-neutral-900 mb-6 leading-tight">
            Kết nối gia đình<br />
            <span className="text-primary">qua mọi thế hệ</span>
          </h1>
          <p className="text-xl text-neutral-600 mb-10 max-w-2xl mx-auto">
            FamilyConnect – nền tảng số kết nối các thành viên gia đình, lưu giữ di sản và xây dựng câu chuyện gia tộc qua trí tuệ nhân tạo.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/register">
              <Button size="lg" className="px-8">
                Bắt đầu ngay
              </Button>
            </Link>
            <Link to="/login">
              <Button size="lg" variant="outline" className="px-8">
                Tìm hiểu thêm
              </Button>
            </Link>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-20 bg-neutral-50">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold text-center mb-12">Tính năng nổi bật</h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            <FeatureCard
              icon={Users}
              title="Gia phả số"
              description="Xây dựng và quản lý cây gia phả đa thế hệ trực quan, dễ dàng thêm thành viên và mối quan hệ."
            />
            <FeatureCard
              icon={BookOpen}
              title="Lưu trữ di sản"
              description="Ghi lại câu chuyện gia đình, tư liệu lịch sử và thư viện ảnh qua nhiều thế hệ."
            />
            <FeatureCard
              icon={Heart}
              title="Kết nối cộng đồng"
              description="Chia sẻ sự kiện, tin tức và tương tác với các thành viên trong gia đình."
            />
            <FeatureCard
              icon={Sparkles}
              title="Trợ lý AI"
              description="Trợ lý AI hỗ trợ tra cứu quan hệ, gợi ý sự kiện và tóm tắt tài liệu gia tộc."
            />
          </div>
        </div>
      </section>

      {/* How it works */}
      <section className="py-20">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold text-center mb-12">Hoạt động như thế nào?</h2>
          <div className="grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
            <Step number="01" title="Tạo gia đình" description="Đăng ký tài khoản và tạo gia đình dòng họ của bạn." />
            <Step number="02" title="Thêm thành viên" description="Thêm các thành viên và thiết lập mối quan hệ gia phả." />
            <Step number="03" title="Kết nối & chia sẻ" description="Chia sẻ sự kiện, lưu trữ di sản và trò chuyện với AI." />
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-20 bg-primary">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl font-bold text-white mb-6">Bắt đầu hành trình kết nối gia đình</h2>
          <p className="text-primary-light text-lg mb-8 max-w-xl mx-auto">
            Tham gia cùng hàng nghìn gia đình đã sử dụng FamilyConnect để gắn kết các thế hệ.
          </p>
          <Link to="/register">
            <Button size="lg" variant="secondary" className="px-8 bg-white text-primary hover:bg-neutral-100">
              Đăng ký miễn phí
            </Button>
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 bg-neutral-900 text-neutral-400">
        <div className="container mx-auto px-4">
          <div className="grid md:grid-cols-3 gap-8">
            <div>
              <div className="flex items-center gap-2 mb-4">
                <div className="w-8 h-8 rounded-lg bg-primary flex items-center justify-center">
                  <span className="text-white font-bold text-sm">FC</span>
                </div>
                <span className="font-semibold text-lg text-white">FamilyConnect</span>
              </div>
              <p className="text-sm">Nền tảng kết nối gia đình số tích hợp trí tuệ nhân tạo.</p>
            </div>
            <div>
              <h3 className="font-semibold text-white mb-4">Liên kết</h3>
              <ul className="space-y-2 text-sm">
                <li><a href="#" className="hover:text-white">Về chúng tôi</a></li>
                <li><a href="#" className="hover:text-white">Tính năng</a></li>
                <li><a href="#" className="hover:text-white">Hướng dẫn</a></li>
                <li><a href="#" className="hover:text-white">Hỗ trợ</a></li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold text-white mb-4">Pháp lý</h3>
              <ul className="space-y-2 text-sm">
                <li><a href="#" className="hover:text-white">Điều khoản sử dụng</a></li>
                <li><a href="#" className="hover:text-white">Chính sách bảo mật</a></li>
              </ul>
            </div>
          </div>
          <div className="mt-8 pt-8 border-t border-neutral-800 text-center text-sm">
            © 2026 FamilyConnect. Bảo lưu mọi quyền.
          </div>
        </div>
      </footer>
    </div>
  )
}

function FeatureCard({ icon: Icon, title, description }: { 
  icon: React.ElementType; 
  title: string; 
  description: string 
}) {
  return (
    <div className="bg-background p-6 rounded-[10px] border border-border shadow-sm">
      <div className="w-12 h-12 rounded-lg bg-primary-light flex items-center justify-center mb-4">
        <Icon className="h-6 w-6 text-primary" />
      </div>
      <h3 className="font-semibold text-lg mb-2">{title}</h3>
      <p className="text-neutral-600 text-sm">{description}</p>
    </div>
  )
}

function Step({ number, title, description }: { number: string; title: string; description: string }) {
  return (
    <div className="text-center">
      <div className="w-16 h-16 rounded-full bg-primary text-white text-xl font-bold flex items-center justify-center mx-auto mb-4">
        {number}
      </div>
      <h3 className="font-semibold text-lg mb-2">{title}</h3>
      <p className="text-neutral-600 text-sm">{description}</p>
    </div>
  )
}
