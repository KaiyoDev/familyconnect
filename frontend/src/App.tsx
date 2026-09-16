import { useState } from 'react'
import { BrowserRouter, Routes, Route, Navigate, useNavigate, useSearchParams } from 'react-router-dom'
import Pub01Landing from './screens/public/PUB-01_Landing'
import Pub02Login from './screens/public/PUB-02_Login'
import Pub03Register from './screens/public/PUB-03_Register'
import Pub04ForgotPassword from './screens/public/PUB-04_ForgotPassword'
import Pub05ActivateAccount from './screens/public/PUB-05_ActivateAccount'
import Shl02Dashboard from './screens/app-shell/SHL-02_Dashboard'
import Shl03Search from './screens/app-shell/SHL-03_Search'
import Gen01GenealogyTree from './screens/genealogy/GEN-01_GenealogyTree'
import Gen02RelationshipGraph from './screens/genealogy/GEN-02_RelationshipGraph'
import Gen03RelationshipLookup from './screens/genealogy/GEN-03_RelationshipLookup'
import Gen04MemberProfile from './screens/genealogy/GEN-04_MemberProfile'
import Gen05AddMember from './screens/genealogy/GEN-05_AddMember'
import Gen06SetRelationship from './screens/genealogy/GEN-06_SetRelationship'
import Fam01CreateFamily from './screens/family/FAM-01_CreateFamily'
import Fam02FamilyInfo from './screens/family/FAM-02_FamilyInfo'
import Fam03ManageBranch from './screens/family/FAM-03_ManageBranch'
import Fam04MemberList from './screens/family/FAM-04_MemberList'
import Fam05JoinRequest from './screens/family/FAM-05_JoinRequest'
import Com01Feed from './screens/community/COM-01_Feed'
import Com02PostDetail from './screens/community/COM-02_PostDetail'
import Com03CreatePost from './screens/community/COM-03_CreatePost'
import Com04News from './screens/community/COM-04_News'
import Com05Announcement from './screens/community/COM-05_Announcement'
import EvT01EventList from './screens/events/EVT-01_EventList'
import EvT02EventDetail from './screens/events/EVT-02_EventDetail'
import EvT03CreateEvent from './screens/events/EVT-03_CreateEvent'
import EvT04ManageParticipants from './screens/events/EVT-04_ManageParticipants'
import EvT05EventGallery from './screens/events/EVT-05_EventGallery'
import Dir01Directory from './screens/directory/DIR-01_Directory'
import Dir02MemberDetail from './screens/directory/DIR-02_MemberDetail'
import Dir03AdvancedSearch from './screens/directory/DIR-03_AdvancedSearch'
import Her01Archive from './screens/heritage/HER-01_Archive'
import Her02HistoricalDocs from './screens/heritage/HER-02_HistoricalDocs'
import Her03FamilyStories from './screens/heritage/HER-03_FamilyStories'
import Her04Outstanding from './screens/heritage/HER-04_Outstanding'
import Her05PhotoLibrary from './screens/heritage/HER-05_PhotoLibrary'
import Ai01AIAssistant from './screens/ai/AI-01_AIAssistant'
import Ai02SearchResults from './screens/ai/AI-02_SearchResults'
import Dsh01Stats from './screens/dashboard/DSH-01_Stats'
import Dsh02Demographics from './screens/dashboard/DSH-02_Demographics'
import Dsh03Reports from './screens/dashboard/DSH-03_Reports'
import Adm01AdminDashboard from './screens/admin/ADM-01_AdminDashboard'
import Adm02UserManagement from './screens/admin/ADM-02_UserManagement'
import Adm03Moderation from './screens/admin/ADM-03_Moderation'
import Adm04AuditLog from './screens/admin/ADM-04_AuditLog'
import Adm05Backup from './screens/admin/ADM-05_Backup'
import Adm06Settings from './screens/admin/ADM-06_Settings'
import Prf01Profile from './screens/profile/PRF-01_Profile'
import Prf02Notifications from './screens/profile/PRF-02_Notifications'
import Prf03ActivityHistory from './screens/profile/PRF-03_ActivityHistory'
import { useAuthStore } from './store/auth'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Public Routes */}
        <Route path="/" element={<Pub01Landing />} />
        <Route path="/login" element={<Pub02Login />} />
        <Route path="/register" element={<Pub03Register />} />
        <Route path="/forgot-password" element={<Pub04ForgotPassword />} />
        <Route path="/activate/:token" element={<Pub05ActivateAccount />} />
        
        {/* App Routes */}
        <Route path="/dashboard" element={<ProtectedRoute><Shl02Dashboard /></ProtectedRoute>} />
        <Route path="/search" element={<ProtectedRoute><Shl03Search /></ProtectedRoute>} />
        <Route path="/genealogy" element={<ProtectedRoute><Gen01GenealogyTree /></ProtectedRoute>} />
        <Route path="/genealogy/graph" element={<ProtectedRoute><Gen02RelationshipGraph /></ProtectedRoute>} />
        <Route path="/genealogy/lookup" element={<ProtectedRoute><Gen03RelationshipLookup /></ProtectedRoute>} />
        <Route path="/genealogy/member/:id" element={<ProtectedRoute><Gen04MemberProfile /></ProtectedRoute>} />
        <Route path="/genealogy/add-member" element={<ProtectedRoute><Gen05AddMember /></ProtectedRoute>} />
        <Route path="/genealogy/set-relationship" element={<ProtectedRoute><Gen06SetRelationship /></ProtectedRoute>} />
        <Route path="/family/create" element={<ProtectedRoute><Fam01CreateFamily /></ProtectedRoute>} />
        <Route path="/family/:id" element={<ProtectedRoute><Fam02FamilyInfo /></ProtectedRoute>} />
        <Route path="/family/:id/branches" element={<ProtectedRoute><Fam03ManageBranch /></ProtectedRoute>} />
        <Route path="/family/:id/members" element={<ProtectedRoute><Fam04MemberList /></ProtectedRoute>} />
        <Route path="/family/:id/join-requests" element={<ProtectedRoute><Fam05JoinRequest /></ProtectedRoute>} />
        <Route path="/community" element={<ProtectedRoute><Com01Feed /></ProtectedRoute>} />
        <Route path="/community/post/:id" element={<ProtectedRoute><Com02PostDetail /></ProtectedRoute>} />
        <Route path="/community/post/new" element={<ProtectedRoute><Com03CreatePost /></ProtectedRoute>} />
        <Route path="/community/news" element={<ProtectedRoute><Com04News /></ProtectedRoute>} />
        <Route path="/community/announcement/new" element={<ProtectedRoute><Com05Announcement /></ProtectedRoute>} />
        <Route path="/events" element={<ProtectedRoute><EvT01EventList /></ProtectedRoute>} />
        <Route path="/events/:id" element={<ProtectedRoute><EvT02EventDetail /></ProtectedRoute>} />
        <Route path="/events/new" element={<ProtectedRoute><EvT03CreateEvent /></ProtectedRoute>} />
        <Route path="/events/:id/participants" element={<ProtectedRoute><EvT04ManageParticipants /></ProtectedRoute>} />
        <Route path="/events/:id/gallery" element={<ProtectedRoute><EvT05EventGallery /></ProtectedRoute>} />
        <Route path="/directory" element={<ProtectedRoute><Dir01Directory /></ProtectedRoute>} />
        <Route path="/directory/:id" element={<ProtectedRoute><Dir02MemberDetail /></ProtectedRoute>} />
        <Route path="/directory/search" element={<ProtectedRoute><Dir03AdvancedSearch /></ProtectedRoute>} />
        <Route path="/heritage" element={<ProtectedRoute><Her01Archive /></ProtectedRoute>} />
        <Route path="/heritage/documents" element={<ProtectedRoute><Her02HistoricalDocs /></ProtectedRoute>} />
        <Route path="/heritage/stories" element={<ProtectedRoute><Her03FamilyStories /></ProtectedRoute>} />
        <Route path="/heritage/outstanding" element={<ProtectedRoute><Her04Outstanding /></ProtectedRoute>} />
        <Route path="/heritage/photos" element={<ProtectedRoute><Her05PhotoLibrary /></ProtectedRoute>} />
        <Route path="/ai/chat" element={<ProtectedRoute><Ai01AIAssistant /></ProtectedRoute>} />
        <Route path="/ai/search" element={<ProtectedRoute><Ai02SearchResults /></ProtectedRoute>} />
        <Route path="/dashboard/stats" element={<ProtectedRoute><Dsh01Stats /></ProtectedRoute>} />
        <Route path="/dashboard/demographics" element={<ProtectedRoute><Dsh02Demographics /></ProtectedRoute>} />
        <Route path="/dashboard/reports" element={<ProtectedRoute><Dsh03Reports /></ProtectedRoute>} />
        <Route path="/admin" element={<ProtectedRoute><Adm01AdminDashboard /></ProtectedRoute>} />
        <Route path="/admin/users" element={<ProtectedRoute><Adm02UserManagement /></ProtectedRoute>} />
        <Route path="/admin/moderation" element={<ProtectedRoute><Adm03Moderation /></ProtectedRoute>} />
        <Route path="/admin/audit-log" element={<ProtectedRoute><Adm04AuditLog /></ProtectedRoute>} />
        <Route path="/admin/backup" element={<ProtectedRoute><Adm05Backup /></ProtectedRoute>} />
        <Route path="/admin/settings" element={<ProtectedRoute><Adm06Settings /></ProtectedRoute>} />
        <Route path="/profile" element={<ProtectedRoute><Prf01Profile /></ProtectedRoute>} />
        <Route path="/profile/notifications" element={<ProtectedRoute><Prf02Notifications /></ProtectedRoute>} />
        <Route path="/profile/activity" element={<ProtectedRoute><Prf03ActivityHistory /></ProtectedRoute>} />
        
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  )
}

function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { isAuthenticated } = useAuthStore()
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />
  }
  return children
}
