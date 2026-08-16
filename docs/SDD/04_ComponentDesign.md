# 04. Component Design

## 1. Introduction

### 1.1. Purpose

This document describes the component-level design of the FamilyConnect
system.

The purpose of this document is to define:

- The main domain classes and their responsibilities.
- The backend and frontend components.
- Dependencies between components.
- Runtime interactions represented by Sequence Diagrams.
- Design patterns used throughout the system.
- Traceability between Functional Requirements, Use Cases, Architecture
  Modules, Classes, Components, and Sequence Diagrams.

The Component Design is derived from the following input documents:

- System Architecture Design
- Database Design
- UI/UX Design
- Functional Requirements
- Use Case Specification
- Business Rules
- Glossary and Data Dictionary

---

### 1.2. Scope

The Component Design covers:

- Backend domain classes.
- Backend service classes.
- Backend repository classes.
- Frontend page components.
- Frontend shared components.
- Frontend service classes.
- Frontend state management.
- API Gateway.
- AI Service Layer.
- Database and Storage components.
- Cross-cutting concerns such as authentication, notifications,
  administration, and audit logging.

The following items are outside the detailed implementation scope:

- Source code implementation.
- Detailed database schema.
- Detailed UI/UX specifications.
- Detailed API specifications.
- Infrastructure deployment configuration.

---

### 1.3. Architectural Context

FamilyConnect follows a layered component architecture.

The main layers are:

1. Frontend Layer
2. API Access Layer
3. Backend Services Layer
4. AI Service Layer
5. Data & Storage Layer

The general dependency flow is:

Frontend
→ API Gateway
→ Backend Services
→ Database / Storage

AI requests follow:

API Gateway
→ AI Service
→ RAG Component
→ Embedding Component
→ LLM Integration

The RAG retrieval flow is:

AI Service
→ RAG Component
→ Embedding Component

RAG Component
→ Database

---

### 1.4. Design Objectives

The component architecture is designed to achieve the following objectives:

- Separation of concerns.
- Single responsibility for business components.
- Loose coupling between modules.
- Clear dependency boundaries.
- Reusable frontend components.
- Independent backend service responsibilities.
- Centralized API routing.
- Dedicated AI processing architecture.
- Maintainability and extensibility.
- Traceability from requirements to implementation design.

---

## 2. Class Diagram

### 2.1. Class Diagram Overview

The Class Diagram defines the main classes used by the FamilyConnect system.

The classes are divided into the following groups:

1. Backend Domain Classes
2. Backend Service Classes
3. Backend Repository Classes
4. Frontend Page Components
5. Frontend Shared Components
6. Frontend Service Classes
7. Frontend State Management Classes

The Class Diagram is represented by the existing PlantUML class diagrams
created for the FamilyConnect system.

---

### 2.2. Backend Domain Classes

The main backend domain classes are:

- User
- Family
- FamilyBranch
- FamilyMember
- Relationship
- Post
- Comment
- Reaction
- Event
- EventRSVP
- HeritageItem
- FamilyStory
- Notification
- AuditLog

These classes represent the main business entities of FamilyConnect.

---

### 2.3. User

The User class represents an authenticated system user.

Main attributes:

- id
- email
- phone
- password_hash
- full_name
- avatar_url
- date_of_birth
- role
- status
- created_at
- updated_at

Main responsibilities:

- Store account information.
- Store authentication-related information.
- Represent user roles and account status.

Related requirements:

- FR-US-*

---

### 2.4. Family

The Family class represents a family or family organization.

Main attributes:

- id
- name
- description
- region
- country
- owner_id
- status
- created_at

Main responsibilities:

- Store family information.
- Identify the family owner.
- Represent family status and metadata.

Related requirement:

- FR-FG-01

---

### 2.5. FamilyBranch

The FamilyBranch class represents a branch within a family.

Main attributes:

- id
- family_id
- name
- description
- leader_id
- created_at

Main responsibilities:

- Organize family members into branches.
- Store branch information.
- Identify branch leadership.

Related requirement:

- FR-FG-02

---

### 2.6. FamilyMember

The FamilyMember class represents a member of a family.

Main attributes:

- id
- user_id
- family_id
- branch_id
- generation
- display_name
- gender
- birth_date
- death_date
- photo_url
- status

Main responsibilities:

- Represent family membership.
- Store genealogy-related member information.
- Associate a user with a family.
- Store generation information.

Related requirement:

- FR-FG-03

---

### 2.7. Relationship

The Relationship class represents relationships between family members.

Main attributes:

- id
- from_member_id
- to_member_id
- type
- marriage_date
- divorce_date
- status

Relationship types include:

- PARENT_CHILD
- SPOUSE

Main responsibilities:

- Represent family relationships.
- Connect members within the genealogy tree.
- Store relationship status and relevant dates.

Related requirements:

- FR-FG-04
- FR-FG-05

---

### 2.8. Community Domain Classes

The Community domain contains:

- Post
- Comment
- Reaction

#### Post

Main attributes:

- id
- author_id
- family_id
- branch_id
- content
- media_urls
- visibility
- status
- created_at
- updated_at

#### Comment

Main attributes:

- id
- post_id
- author_id
- content
- created_at
- updated_at

#### Reaction

Main attributes:

- id
- post_id
- user_id
- type
- created_at

Responsibilities:

- Store community posts.
- Store comments.
- Store member reactions.
- Support community interactions.

Related requirements:

- FR-COM-01
- FR-COM-02

---

### 2.9. Event Domain Classes

The Event domain contains:

- Event
- EventRSVP

#### Event

Main attributes:

- id
- creator_id
- family_id
- name
- type
- start_time
- end_time
- location
- description
- cover_url
- status

#### EventRSVP

Main attributes:

- id
- event_id
- user_id
- status
- guest_count
- responded_at

Responsibilities:

- Create and manage events.
- Store event information.
- Store RSVP status.
- Store participant information.

Related requirements:

- FR-EVT-01
- FR-EVT-02

---

### 2.10. Heritage Domain Classes

The Heritage domain contains:

- HeritageItem
- FamilyStory

#### HeritageItem

Main attributes:

- id
- family_id
- title
- type
- era
- description
- file_url
- related_member_ids
- created_by

#### FamilyStory

Main attributes:

- id
- author_id
- family_id
- title
- content
- related_member_ids
- era
- status

Responsibilities:

- Store family heritage.
- Store historical information.
- Store family stories.
- Associate heritage information with family members.

Related requirements:

- FR-HER-01
- FR-HER-02

---

### 2.11. Notification

The Notification class represents system notifications.

Main attributes:

- id
- user_id
- type
- title
- content
- is_read
- created_at

Responsibilities:

- Store notifications.
- Track notification status.
- Associate notifications with users.

---

### 2.12. AuditLog

The AuditLog class records administrative and security-related actions.

Main attributes:

- id
- user_id
- action
- resource_type
- resource_id
- details
- timestamp

Responsibilities:

- Record administrative actions.
- Support auditing.
- Provide historical information for moderation and administration.

Related requirement:

- FR-ADM-03

---

### 2.13. Backend Service Classes

The backend Service Layer contains the following services:

- AuthService
- UserService
- FamilyService
- GenealogyService
- CommunityService
- EventService
- DirectoryService
- HeritageService
- AIService
- NotificationService
- AdminService

---

### 2.14. AuthService

Responsibilities:

- register()
- login()
- logout()
- refresh_token()
- verify_email()
- reset_password()

The AuthService coordinates authentication operations between frontend
requests, authentication logic, and persistence.

---

### 2.15. UserService

Responsibilities:

- get_profile()
- update_profile()
- change_password()

The UserService manages user profile-related operations.

---

### 2.16. FamilyService

Responsibilities:

- create_family()
- update_family()
- get_families_by_user()
- transfer_ownership()

The FamilyService manages family lifecycle operations.

---

### 2.17. GenealogyService

Responsibilities:

- add_member()
- add_relationship()
- get_tree()
- lookup_relationship()

The GenealogyService manages family members, relationships, and genealogy
tree operations.

---

### 2.18. CommunityService

Responsibilities:

- create_post()
- get_feed()
- add_comment()
- add_reaction()

The CommunityService manages posts and member interactions.

---

### 2.19. EventService

Responsibilities:

- create_event()
- rsvp()
- get_participants()
- send_reminders()

The EventService manages events and RSVP operations.

---

### 2.20. DirectoryService

Responsibilities:

- search_members()
- update_profession()
- update_education()

The DirectoryService provides member directory and search functionality.

---

### 2.21. HeritageService

Responsibilities:

- upload_document()
- create_story()
- get_archive()

The HeritageService manages family heritage and historical content.

---

### 2.22. AIService

Responsibilities:

- semantic_search()
- chat_assistant()
- explain_relationship()
- summarize_content()

The AIService coordinates AI-related operations and communicates with the
RAG and LLM layers.

---

### 2.23. NotificationService

Responsibilities:

- send_notification()
- send_email()
- get_notifications()

The NotificationService manages application notifications and email
notifications.

---

### 2.24. AdminService

Responsibilities:

- manage_users()
- moderate_content()
- get_audit_log()
- backup()
- restore()

The AdminService manages administration, moderation, and audit operations.

---

### 2.25. Backend Repository Classes

The repository layer contains:

- UserRepository
- FamilyRepository
- RelationshipRepository
- PostRepository
- EventRepository
- HeritageRepository
- NotificationRepository
- AuditLogRepository

Repositories provide data-access responsibilities and isolate business
services from direct persistence implementation.

---

### 2.26. Frontend Page Components

The main frontend pages are:

- LandingPage
- LoginPage
- RegisterPage
- DashboardPage
- FamilyListPage
- FamilyManagementPage
- GenealogyTreePage
- CommunityFeedPage
- PostDetailPage
- EventsListPage
- EventDetailPage
- MemberDirectoryPage
- MemberProfilePage
- HeritageArchivePage
- AIAssistantPage
- AdminDashboardPage

These components provide the main user-facing interfaces.

---

### 2.27. Frontend Shared Components

Reusable frontend components include:

- Header
- Sidebar
- PostCard
- MemberCard
- EventCard
- GenealogyTreeViewer
- AIChatWidget
- NotificationPanel
- Modal
- Form
- DataTable

These components reduce duplicated UI implementation and maintain visual
consistency.

---

### 2.28. Frontend Service Classes

The frontend service layer contains:

- ApiClient
- AuthService
- FamilyService
- CommunityService
- EventService
- AIService
- NotificationService

These services communicate with backend APIs through the API Gateway.

---

### 2.29. Frontend State Management

The main state management classes are:

- AuthStore
- FamilyStore
- UIStore

Responsibilities include:

- Authentication state.
- Current family state.
- Global UI state.
- Shared application data.

---

### 2.30. Class Relationships

The main domain relationships include:

- User owns Family.
- Family contains FamilyBranch.
- Family contains FamilyMember.
- FamilyBranch contains FamilyMember.
- User belongs to FamilyMember.
- FamilyMember connects to other FamilyMember objects through Relationship.
- User authors Post.
- Post contains Comment.
- Post contains Reaction.
- User creates Event.
- Event contains EventRSVP.
- Family contains HeritageItem.
- Family contains FamilyStory.
- User receives Notification.
- User performs AuditLog actions.

Service classes depend on corresponding domain classes and repositories.

---

## 3. Component Diagram

### 3.1. Component Architecture Overview

The FamilyConnect Component Diagram contains 21 major components.

The components are organized into five logical layers:

1. Frontend
2. API Access Layer
3. Backend Services
4. AI Service Layer
5. Data & Storage

---

### 3.2. Frontend Components

The Frontend layer contains:

1. Shell Component
2. Pages Component
3. Shared Components
4. Services Component
5. State Management Component

Responsibilities:

- Provide the application interface.
- Handle user interactions.
- Maintain frontend state.
- Communicate with backend APIs.

---

### 3.3. API Access Layer

The API Access Layer contains:

6. API Gateway

The API Gateway provides a centralized entry point for frontend requests.

Responsibilities:

- Request routing.
- API boundary management.
- Authentication-related routing.
- Backend response forwarding.

---

### 3.4. Backend Components

The Backend Services layer contains:

7. Auth Component
8. Family Management Component
9. Genealogy Component
10. Community Component
11. Event Component
12. Directory Component
13. Heritage Component
14. Notification Component
15. Admin Component

Each component has a clearly defined business responsibility.

---

### 3.5. AI Service Layer

The AI Service Layer contains:

16. AI Service Component
17. RAG Component
18. Embedding Component
19. LLM Integration Component

The AI flow is:

API Gateway
→ AI Service
→ RAG Component
→ Embedding Component
→ LLM Integration

The RAG retrieval flow is:

AI Service
→ RAG Component

RAG Component
→ Embedding Component

RAG Component
→ Database

---

### 3.6. Data & Storage Components

The Data & Storage layer contains:

20. Database Component
21. Storage Component

Database responsibilities:

- Persistent structured data.
- User data.
- Family data.
- Genealogy data.
- Community data.
- Event data.
- Heritage data.
- Notification data.
- Audit data.
- AI/RAG data.

Storage responsibilities:

- Images.
- Documents.
- Post media.
- Heritage files.
- Member photos.

---

### 3.7. Component Dependencies

The main frontend dependency flow is:

Pages
→ Services
→ API Gateway

The main backend dependency flow is:

API Gateway
→ Auth
→ Family Management
→ Genealogy
→ Community
→ Event
→ Directory
→ Heritage
→ Notification
→ Admin

Backend services depend on:

- Database
- Storage
- Notification where required

The AI dependency flow is:

AI Service
→ RAG
→ Embedding
→ LLM Integration

RAG also depends on:

- Database

---

### 3.8. Component Design Principles

The Component Diagram follows these principles:

- Each component has a clear responsibility.
- Components communicate through defined boundaries.
- Database access is separated from frontend components.
- API Gateway isolates frontend clients from backend implementation.
- AI processing is isolated in a dedicated layer.
- Storage is separated from structured database persistence.
- Circular dependencies should be avoided.

---

## 4. Sequence Diagrams

### 4.1. Sequence Diagram Overview

Ten main runtime flows are represented by Sequence Diagrams.

The diagrams correspond to the major Use Cases of FamilyConnect.

---

### 4.2. SD-01 - Login

Main flow:

User
→ LoginPage
→ AuthService
→ API Gateway
→ Auth Component
→ UserRepository
→ Database

The flow includes:

- Credential submission.
- User lookup.
- Password verification.
- Successful authentication.
- Invalid credential handling.
- Error response.

---

### 4.3. SD-02 - Register

Main flow:

User
→ RegisterPage
→ AuthService
→ API Gateway
→ Auth Component
→ UserRepository
→ Database

The flow includes:

- Registration data submission.
- Validation.
- Existing email detection.
- Password hashing.
- User creation.
- Registration success.
- Registration error handling.

---

### 4.4. SD-03 - Create Family

Main flow:

Family Owner
→ FamilyListPage
→ FamilyService
→ API Gateway
→ Family Management
→ FamilyRepository
→ Database

The flow also includes:

Family Management
→ AuditLogRepository
→ Database

The sequence handles:

- Family data validation.
- Family creation.
- Audit logging.
- Success response.
- Invalid family data handling.

---

### 4.5. SD-04 - Add Member & Relationship

Main flow:

Family Owner
→ GenealogyTreePage
→ GenealogyService
→ API Gateway
→ Genealogy Component

Member creation:

Genealogy Component
→ MemberRepository
→ Database

Relationship creation:

Genealogy Component
→ RelationshipRepository
→ Database

The sequence handles:

- Member validation.
- Member creation.
- Member ID retrieval.
- Relationship creation.
- Updated genealogy tree response.
- Invalid member data handling.

---

### 4.6. SD-05 - View Genealogy Tree

Main flow:

Member
→ GenealogyTreePage
→ GenealogyService
→ API Gateway
→ Genealogy Component
→ GenealogyRepository
→ Database

The Genealogy Component retrieves member and relationship information
required to construct the genealogy tree.

The sequence handles:

- Family tree request.
- Tree data retrieval.
- Tree construction.
- Successful tree rendering.
- Tree unavailable handling.

---

### 4.7. SD-06 - Create Post & Interact

Main flow:

Member
→ CommunityFeedPage
→ CommunityService
→ API Gateway
→ Community Component
→ PostRepository
→ Database

The interaction flow supports:

- Post creation.
- Comment.
- Reaction.
- Interaction persistence.
- Notification processing.
- Error handling.

The create-post lifecycle and interaction lifecycle are represented within
the same Sequence Diagram while maintaining separate activation periods.

---

### 4.8. SD-07 - Create Event & RSVP

Main flow:

Member
→ EventDetailPage
→ EventService
→ API Gateway
→ Event Component
→ EventRepository
→ Database

RSVP flow:

Member
→ EventDetailPage
→ EventService
→ API Gateway
→ Event Component
→ EventRepository
→ Database

The sequence handles:

- Event creation.
- Event validation.
- Event persistence.
- RSVP creation or update.
- RSVP notification.
- Success and error responses.

The create-event lifecycle and RSVP lifecycle are represented in the same
Sequence Diagram without treating them as one continuous activation period.

---

### 4.9. SD-08 - Search Directory

Main flow:

Member
→ MemberDirectoryPage
→ DirectoryService
→ API Gateway
→ Directory Component
→ MemberRepository
→ Database

The sequence handles:

- Search criteria.
- Member search.
- Matching members.
- Empty result handling.
- Search result rendering.

A successful empty search returns an HTTP 200 response with an empty list.

---

### 4.10. SD-09 - AI Assistant

Main flow:

Member
→ AIAssistantPage
→ AIService
→ API Gateway
→ AI Service
→ RAG Component
→ Embedding Component
→ Database
→ LLM Integration

The RAG flow includes:

- Query submission.
- Context retrieval.
- Query embedding.
- Semantic search.
- Relevant context retrieval.
- LLM response generation.
- AI response rendering.

The RAG Component maintains an activation period while retrieving context
from the Embedding Component and Database.

---

### 4.11. SD-10 - Admin Moderation

Main flow:

Admin
→ AdminDashboardPage
→ AdminService
→ API Gateway
→ Admin Component

The moderation flow includes:

- Administrator authorization.
- Content retrieval.
- Content approval.
- Content rejection.
- Content status update.
- Audit log creation.
- Notification where required.
- Unauthorized access handling.

The sequence uses nested alternative flows for authorization and moderation
results.

---

## 5. Design Patterns

### 5.1. Repository Pattern

Repositories isolate persistence logic from business logic.

Examples:

- UserRepository
- FamilyRepository
- RelationshipRepository
- PostRepository
- EventRepository
- HeritageRepository
- NotificationRepository
- AuditLogRepository

Benefits:

- Separation of data access and business logic.
- Easier unit testing.
- Reduced database coupling.
- Consistent persistence interface.

---

### 5.2. Service Layer Pattern

Business operations are organized into dedicated service classes.

Examples:

- AuthService
- FamilyService
- GenealogyService
- CommunityService
- EventService
- DirectoryService
- HeritageService
- AIService
- NotificationService
- AdminService

Benefits:

- Centralized business logic.
- Clear responsibilities.
- Reusable operations.
- Easier maintenance.

---

### 5.3. API Gateway Pattern

The API Gateway provides a single entry point between frontend clients and
backend services.

Benefits:

- Centralized routing.
- Authentication boundary.
- Consistent API access.
- Reduced frontend dependency on backend implementation details.

---

### 5.4. Layered Architecture Pattern

The system separates:

- Presentation.
- API access.
- Business services.
- AI processing.
- Persistence.

Benefits:

- Separation of concerns.
- Independent maintenance.
- Easier testing.
- Scalability.

---

### 5.5. Dependency Injection

Backend services can receive repositories and other dependencies through
dependency injection.

Benefits:

- Reduced coupling.
- Easier testing.
- Replaceable implementations.
- Better maintainability.

---

### 5.6. RAG Pattern

The AI Service Layer implements Retrieval-Augmented Generation.

The main flow is:

AI Service
→ RAG Component
→ Embedding Component
→ Database retrieval
→ Context construction
→ LLM Integration
→ Generated response

Benefits:

- Context-aware AI responses.
- Retrieval of relevant family information.
- Reduced hallucination risk.
- Separation between retrieval and generation.

---

### 5.7. State Management Pattern

The frontend uses centralized state stores:

- AuthStore
- FamilyStore
- UIStore

Benefits:

- Consistent application state.
- Reduced prop drilling.
- Centralized state updates.
- Easier frontend maintenance.

---

## 6. Traceability Matrix

### 6.1. Traceability Overview

Traceability ensures consistency between:

SRS
→ Architecture
→ Database
→ UI/UX
→ Classes
→ Components
→ Sequence Diagrams

The following matrices provide the main design traceability.

---

### 6.2. Functional Requirement to Class Matrix

| Functional Requirement | Main Classes |
|---|---|
| FR-US-* | User, AuthService, UserService, UserRepository |
| FR-FG-01 | Family, FamilyService, FamilyRepository |
| FR-FG-02 | FamilyBranch, FamilyService, FamilyRepository |
| FR-FG-03 | FamilyMember, GenealogyService, MemberRepository |
| FR-FG-04 | Relationship, GenealogyService, RelationshipRepository |
| FR-FG-05 | Relationship, GenealogyService, RelationshipRepository |
| FR-COM-01 | Post, CommunityService, PostRepository |
| FR-COM-02 | Comment, Reaction, CommunityService, PostRepository |
| FR-EVT-01 | Event, EventService, EventRepository |
| FR-EVT-02 | EventRSVP, EventService, EventRepository |
| FR-HER-01 | HeritageItem, HeritageService, HeritageRepository |
| FR-HER-02 | FamilyStory, HeritageService, HeritageRepository |
| Notification-related FRs | Notification, NotificationService, NotificationRepository |
| FR-ADM-03 | AuditLog, AdminService, AuditLogRepository |
| AI-related FRs | AIService, RAG Component, Embedding Component, LLM Integration |

The wildcard mappings such as FR-US-* represent all requirements within the
corresponding functional requirement group.

---

### 6.3. Use Case to Sequence Diagram Matrix

| Use Case | Sequence Diagram |
|---|---|
| UC-01 - Login | SD-01 |
| UC-02 - Register | SD-02 |
| UC-03 - Create Family | SD-03 |
| UC-04 - Add Member & Relationship | SD-04 |
| UC-05 - View Genealogy Tree | SD-05 |
| UC-06 - Create Post & Interact | SD-06 |
| UC-07 - Create Event & RSVP | SD-07 |
| UC-08 - Search Directory | SD-08 |
| UC-10 - AI Assistant | SD-09 |
| UC-12 - Admin Moderation | SD-10 |

This provides a direct mapping between the specified Use Cases and runtime
interaction models.

---

### 6.4. Architecture Module to Component Matrix

| Architecture Module | Main Component |
|---|---|
| Authentication | Auth Component |
| Family Management | Family Management Component |
| Genealogy | Genealogy Component |
| Community | Community Component |
| Events | Event Component |
| Directory | Directory Component |
| Heritage | Heritage Component |
| Notifications | Notification Component |
| Administration | Admin Component |
| AI Services | AI Service Component |
| API Access | API Gateway |
| Frontend Shell | Shell Component |
| Frontend Pages | Pages Component |
| Shared UI | Shared Components |
| Frontend Services | Services Component |
| Frontend State | State Management Component |
| Persistence | Database Component |
| File Storage | Storage Component |
| AI Retrieval | RAG Component |
| AI Embedding | Embedding Component |
| LLM Integration | LLM Integration Component |

---

### 6.5. Component to Sequence Diagram Matrix

| Component | Related Sequence Diagrams |
|---|---|
| Auth Component | SD-01, SD-02 |
| Family Management | SD-03 |
| Genealogy Component | SD-04, SD-05 |
| Community Component | SD-06 |
| Event Component | SD-07 |
| Directory Component | SD-08 |
| AI Service | SD-09 |
| RAG Component | SD-09 |
| Embedding Component | SD-09 |
| LLM Integration | SD-09 |
| Admin Component | SD-10 |
| Notification Component | SD-02, SD-06, SD-07, SD-10 |
| API Gateway | SD-01 through SD-10 |

---

### 6.6. UI Component to Backend Component Matrix

| Frontend Component | Backend Component |
|---|---|
| LoginPage | Auth Component |
| RegisterPage | Auth Component |
| FamilyListPage | Family Management |
| FamilyManagementPage | Family Management |
| GenealogyTreePage | Genealogy Component |
| CommunityFeedPage | Community Component |
| PostDetailPage | Community Component |
| EventsListPage | Event Component |
| EventDetailPage | Event Component |
| MemberDirectoryPage | Directory Component |
| MemberProfilePage | Directory / User |
| HeritageArchivePage | Heritage Component |
| AIAssistantPage | AI Service |
| AdminDashboardPage | Admin Component |

---

### 6.7. Requirement Traceability Principle

Every functional requirement should be traceable to at least one domain
class, service, component, or interaction.

The intended traceability chain is:

FR
→ Domain Class
→ Service
→ Component
→ Sequence Diagram
→ UI Component

This structure helps identify missing requirements and design gaps before
implementation.

---

## 7. Appendix

### 7.1. Component List

The FamilyConnect system contains 21 major components:

1. Shell Component
2. Pages Component
3. Shared Components
4. Services Component
5. State Management Component
6. API Gateway
7. Auth Component
8. Family Management Component
9. Genealogy Component
10. Community Component
11. Event Component
12. Directory Component
13. Heritage Component
14. Notification Component
15. Admin Component
16. AI Service Component
17. RAG Component
18. Embedding Component
19. LLM Integration Component
20. Database Component
21. Storage Component

---

### 7.2. Sequence Diagram List

The project contains the following ten Sequence Diagrams:

1. SD-01 - Login
2. SD-02 - Register
3. SD-03 - Create Family
4. SD-04 - Add Member & Relationship
5. SD-05 - View Genealogy Tree
6. SD-06 - Create Post & Interact
7. SD-07 - Create Event & RSVP
8. SD-08 - Search Directory
9. SD-09 - AI Assistant
10. SD-10 - Admin Moderation

---

### 7.3. Diagram Notation

The diagrams use UML-style notation.

Class Diagram notation represents:

- Classes.
- Attributes.
- Methods.
- Primary keys.
- Foreign keys.
- Associations.
- Cardinality.

Component Diagram notation represents:

- Components.
- Architectural boundaries.
- Dependencies.
- Data persistence.
- Storage dependencies.

Sequence Diagram notation represents:

- Actors.
- Lifelines.
- Messages.
- Return messages.
- Activation bars.
- Alternative flows.
- Optional flows.
- Error handling.

---

### 7.4. Naming Conventions

Backend domain classes use PascalCase.

Examples:

- User
- FamilyMember
- EventRSVP

Service classes use the `Service` suffix.

Examples:

- AuthService
- FamilyService
- GenealogyService

Repository classes use the `Repository` suffix.

Examples:

- UserRepository
- FamilyRepository
- EventRepository

Frontend page components use the `Page` suffix.

Examples:

- LoginPage
- FamilyListPage
- AIAssistantPage

Frontend state containers use the `Store` suffix.

Examples:

- AuthStore
- FamilyStore
- UIStore

---

### 7.5. Architectural Assumptions

The Component Design is based on the following assumptions:

- Frontend communicates with backend through the API Gateway.
- Backend services do not expose database implementation details to the
  frontend.
- Repository classes handle persistence operations.
- Service classes contain business logic.
- Database stores structured application data.
- Storage manages large files and media.
- AI Service coordinates AI-related operations.
- RAG retrieves relevant context before generation.
- Embedding Component generates vector representations.
- LLM Integration handles language model interaction.
- Notification operations remain separated from the main business services.
- Audit logs record important administrative actions.

---

### 7.6. Design Review Checklist

#### Class Diagram

- [x] Main domain classes are defined.
- [x] Service classes are defined.
- [x] Repository classes are defined.
- [x] Frontend page components are defined.
- [x] Shared frontend components are defined.
- [x] Frontend services are defined.
- [x] Frontend state management classes are defined.
- [x] Domain relationships are documented.
- [x] Attributes are derived from the provided data dictionary.

#### Component Diagram

- [x] 21 major components are defined.
- [x] Frontend layer is separated.
- [x] API Gateway is defined.
- [x] Backend services are separated by responsibility.
- [x] AI Service Layer is isolated.
- [x] Database and Storage are separated.
- [x] Dependencies are explicitly documented.
- [x] Circular dependencies are avoided.

#### Sequence Diagrams

- [x] SD-01 Login completed.
- [x] SD-02 Register completed.
- [x] SD-03 Create Family completed.
- [x] SD-04 Add Member & Relationship completed.
- [x] SD-05 View Genealogy Tree completed.
- [x] SD-06 Create Post & Interact completed.
- [x] SD-07 Create Event & RSVP completed.
- [x] SD-08 Search Directory completed.
- [x] SD-09 AI Assistant completed.
- [x] SD-10 Admin Moderation completed.
- [x] Error flows are represented.
- [x] Activation bars are used for important processing periods.
- [x] Return messages are distinguished from request messages.

#### Traceability

- [x] Functional requirements are mapped to classes.
- [x] Use Cases are mapped to Sequence Diagrams.
- [x] Architecture modules are mapped to Components.
- [x] Frontend pages are mapped to backend components.
- [x] AI architecture is mapped to SD-09.

---

### 7.7. Conclusion

The FamilyConnect Component Design provides a complete component-level view
of the system.

The design connects requirements, architecture, database entities, frontend
interfaces, backend services, repositories, AI processing, and runtime
interactions.

The combination of Class Diagrams, Component Diagrams, Sequence Diagrams,
Design Patterns, and Traceability Matrices provides a consistent foundation
for the next development activities.

The design also provides a clear boundary between business logic,
presentation logic, persistence, and AI processing.

This architecture supports maintainability, scalability, testability, and
future extension of the FamilyConnect platform.