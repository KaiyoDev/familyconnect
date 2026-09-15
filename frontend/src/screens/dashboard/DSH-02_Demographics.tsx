import React from 'react'
import Layout from '@/components/Layout'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/basic'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, LineChart, Line } from 'recharts'

const ageData = [
  { age: '0-18', male: 3, female: 2 },
  { age: '19-30', male: 5, female: 3 },
  { age: '31-50', male: 4, female: 3 },
  { age: '51-70', male: 2, female: 1 },
  { age: '70+', male: 1, female: 0 },
]

const educationData = [
  { level: 'Tiểu học', count: 2 },
  { level: 'THCS', count: 3 },
  { level: 'THPT', count: 5 },
  { level: 'Cử nhân', count: 8 },
  { level: 'Thạc sĩ', count: 4 },
  { level: 'Tiến sĩ', count: 1 },
]

export default function Dsh02Demographics() {
  return (
    <Layout>
      <div className="space-y-6">
        <div>
          <h1 className="text-2xl font-bold text-neutral-900">Thống kê nhân khẩu</h1>
          <p className="text-neutral-600">Phân tích cấu trúc gia đình</p>
        </div>

        <div className="grid lg:grid-cols-2 gap-6">
          {/* Age Distribution */}
          <Card>
            <CardHeader>
              <CardTitle>Phân bố độ tuổi</CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={ageData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="age" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="male" fill="#0D9488" name="Nam" />
                  <Bar dataKey="female" fill="#DB2777" name="Nữ" />
                </BarChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>

          {/* Education Level */}
          <Card>
            <CardHeader>
              <CardTitle>Trình độ học vấn</CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={educationData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="level" />
                  <YAxis />
                  <Tooltip />
                  <Line type="monotone" dataKey="count" stroke="#0D9488" strokeWidth={2} />
                </LineChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>

          {/* Generation Count */}
          <Card>
            <CardHeader>
              <CardTitle>Số thế hệ</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="flex items-center justify-center py-8">
                <div className="text-center">
                  <div className="text-6xl font-bold text-primary mb-2">4</div>
                  <p className="text-neutral-600">thế hệ trong gia đình</p>
                </div>
              </div>
              <div className="space-y-2 mt-4">
                {['Thế hệ 1 (Ông bà)', 'Thế hệ 2 (Cha mẹ)', 'Thế hệ 3 (Con cháu)', 'Thế hệ 4 (Cháu chắt)'].map((gen, idx) => (
                  <div key={idx} className="flex items-center gap-3 p-2 bg-neutral-50 rounded-lg">
                    <div className="w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center text-sm font-medium">
                      {idx + 1}
                    </div>
                    <span className="text-sm">{gen}</span>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>

          {/* Family Size Trend */}
          <Card>
            <CardHeader>
              <CardTitle>Tăng trưởng gia đình</CardTitle>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={[
                  { year: '2020', members: 18 },
                  { year: '2021', members: 20 },
                  { year: '2022', members: 21 },
                  { year: '2023', members: 22 },
                  { year: '2024', members: 23 },
                  { year: '2025', members: 24 },
                ]}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="year" />
                  <YAxis />
                  <Tooltip />
                  <Line type="monotone" dataKey="members" stroke="#F59E0B" strokeWidth={2} />
                </LineChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </div>
      </div>
    </Layout>
  )
}
