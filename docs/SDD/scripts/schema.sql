-- ============================================================
-- FamilyConnect PostgreSQL Database Schema
-- Generated from finalized ERD and SDD02 Database Design
-- ==========================================================--

-- Extensions
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ============================================================
-- Enum Types (used for constrained columns)
-- ============================================================

-- User roles
CREATE TYPE user_role AS ENUM ('USER', 'ADMIN', 'SUPER_ADMIN');

-- User status
CREATE TYPE user_status AS ENUM ('PENDING', 'ACTIVE', 'SUSPENDED', 'DELETED');

-- Family status
CREATE TYPE family_status AS ENUM ('ACTIVE', 'ARCHIVED', 'DELETED');

-- Event status
CREATE TYPE event_status AS ENUM ('OPEN', 'CLOSED', 'CANCELLED');

-- Event type
CREATE TYPE event_type AS ENUM ('BIRTHDAY', 'ANNIVERSARY', 'MEETING', 'OTHER');

-- Relationship type
CREATE TYPE relationship_type AS ENUM ('PARENT_CHILD', 'MARRIAGE', 'SIBLING', 'OTHER');

-- Post visibility scope
CREATE TYPE post_visibility AS ENUM ('FAMILY', 'BRANCH', 'PUBLIC');

-- Post status
CREATE TYPE post_status AS ENUM ('PUBLISHED', 'DRAFT', 'ARCHIVED');

-- Reaction type
CREATE TYPE reaction_type AS ENUM ('LIKE', 'LOVE', 'CARE', 'HAPPY', 'SAD', 'ANGRY', 'WOW');

-- Heritage item type
CREATE TYPE heritage_type AS ENUM ('DOCUMENT', 'IMAGE', 'MAP', 'ARTIFACT', 'STORY');

-- Heritage item category
CREATE TYPE heritage_category AS ENUM ('DOCUMENT', 'STORY', 'OUTSTANDING', 'TRADITION', 'OTHER');

-- Heritage item status
CREATE TYPE heritage_status AS ENUM ('DRAFT', 'PUBLISHED', 'ARCHIVED');

-- Media type
CREATE TYPE media_type AS ENUM ('PHOTO', 'VIDEO', 'DOCUMENT', 'AUDIO');

-- RSVP response type
CREATE TYPE rsvp_response AS ENUM ('YES', 'NO', 'MAYBE', 'DEFERRED');

-- ============================================================
-- Table: users
-- ============================================================
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    role user_role NOT NULL DEFAULT 'USER',
    status user_status NOT NULL DEFAULT 'PENDING',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
);

-- Index on email (unique constraint already creates index, but explicit for clarity)
CREATE INDEX idx_users_email ON users(email);

-- ============================================================
-- Table: families
-- ============================================================
CREATE TABLE families (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    family_name VARCHAR(150) NOT NULL,
    description TEXT,
    created_by UUID NOT NULL,
    status family_status NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    CONSTRAINT fk_users_created_by FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE RESTRICT
);

-- Index on created_by
CREATE INDEX idx_families_created_by ON families(created_by);

-- ============================================================
-- Table: family_branches
-- ============================================================
CREATE TABLE family_branches (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    family_id UUID NOT NULL,
    branch_name VARCHAR(150) NOT NULL,
    founder_id UUID,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    CONSTRAINT fk_family_branches_family FOREIGN KEY (family_id) REFERENCES families(id) ON DELETE CASCADE
);

-- Indexes
CREATE INDEX idx_family_branches_family ON family_branches(family_id);
CREATE INDEX idx_family_branches_founders ON family_branches(founder_id);

-- ============================================================
-- Table: family_members
-- ============================================================
CREATE TABLE family_members (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    family_id UUID NOT NULL,
    branch_id UUID,
    user_id UUID UNIQUE,
    full_name VARCHAR(100) NOT NULL,
    gender VARCHAR(20) NOT NULL DEFAULT 'UNKNOWN',
    date_of_birth DATE,
    is_alive BOOLEAN NOT NULL DEFAULT TRUE,
    date_of_death DATE,
    status user_status NOT NULL DEFAULT 'PENDING',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    CONSTRAINT fk_family_members_family FOREIGN KEY (family_id) REFERENCES families(id) ON DELETE CASCADE,
    CONSTRAINT uq_family_members_user UNIQUE (user_id)
);

-- Indexes
CREATE INDEX idx_family_members_family ON family_members(family_id);
CREATE INDEX idx_family_members_branch ON family_members(branch_id);

ALTER TABLE family_branches ADD CONSTRAINT fk_family_branches_founders
    FOREIGN KEY (founder_id) REFERENCES family_members(id) ON DELETE SET NULL;
ALTER TABLE family_members ADD CONSTRAINT fk_family_members_branch
    FOREIGN KEY (branch_id) REFERENCES family_branches(id) ON DELETE SET NULL;

-- ============================================================
-- Table: relationships
-- ============================================================
CREATE TABLE relationships (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    from_member_id UUID NOT NULL,
    to_member_id UUID NOT NULL,
    type relationship_type NOT NULL,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    CONSTRAINT fk_relationships_from_member FOREIGN KEY (from_member_id) REFERENCES family_members(id) ON DELETE CASCADE,
    CONSTRAINT fk_relationships_to_member FOREIGN KEY (to_member_id) REFERENCES family_members(id) ON DELETE CASCADE,
    CONSTRAINT chk_relationship_different CHECK (from_member_id != to_member_id),
    CONSTRAINT uq_relationship_unique UNIQUE (from_member_id, to_member_id, type)
);

-- Indexes
CREATE INDEX idx_relationships_from_member ON relationships(from_member_id);
CREATE INDEX idx_relationships_to_member ON relationships(to_member_id);

-- ============================================================
-- Table: events
-- ============================================================
CREATE TABLE events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    family_id UUID NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    location VARCHAR(255),
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE,
    type event_type NOT NULL,
    status event_status NOT NULL DEFAULT 'OPEN',
    created_by UUID NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    CONSTRAINT fk_events_family FOREIGN KEY (family_id) REFERENCES families(id) ON DELETE CASCADE,
    CONSTRAINT fk_events_created_by FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE RESTRICT,
    CONSTRAINT chk_event_time_order CHECK (
        (end_time IS NULL) OR (end_time > start_time)
    )
);

-- Indexes
CREATE INDEX idx_events_family ON events(family_id);
CREATE INDEX idx_events_start_time ON events(start_time);
CREATE INDEX idx_events_type ON events(type);

-- ============================================================
-- Table: event_rsvps
-- ============================================================
CREATE TABLE event_rsvps (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_id UUID NOT NULL,
    member_id UUID,
    guest_email VARCHAR(150),
    response rsvp_response NOT NULL,
    responded_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    CONSTRAINT fk_event_rsvps_event FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
    CONSTRAINT fk_event_rsvps_member FOREIGN KEY (member_id) REFERENCES family_members(id) ON DELETE SET NULL,
    CONSTRAINT chk_rsvp_has_identifier CHECK (
        (member_id IS NOT NULL AND guest_email IS NULL) OR
        (member_id IS NULL AND guest_email IS NOT NULL)
    ),
    CONSTRAINT uq_event_rsvp_unique UNIQUE (event_id, member_id, guest_email)
);

-- Indexes
CREATE INDEX idx_event_rsvps_event ON event_rsvps(event_id);
CREATE INDEX idx_event_rsvps_member ON event_rsvps(member_id);

-- ============================================================
-- Table: posts
-- ============================================================
CREATE TABLE posts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    family_id UUID NOT NULL,
    author_id UUID NOT NULL,
    branch_id UUID,
    content TEXT NOT NULL,
    visibility_scope post_visibility NOT NULL DEFAULT 'FAMILY',
    status post_status NOT NULL DEFAULT 'PUBLISHED',
    media_urls JSONB,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    CONSTRAINT fk_posts_family FOREIGN KEY (family_id) REFERENCES families(id) ON DELETE CASCADE,
    CONSTRAINT fk_posts_author FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE RESTRICT,
    CONSTRAINT fk_posts_branch FOREIGN KEY (branch_id) REFERENCES family_branches(id) ON DELETE SET NULL
);

-- Indexes
CREATE INDEX idx_posts_family ON posts(family_id);
CREATE INDEX idx_posts_author ON posts(author_id);
CREATE INDEX idx_posts_visibility ON posts(visibility_scope);

-- ============================================================
-- Table: comments
-- ============================================================
CREATE TABLE comments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    post_id UUID NOT NULL,
    author_id UUID NOT NULL,
    content VARCHAR(1000) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    CONSTRAINT fk_comments_post FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    CONSTRAINT fk_comments_author FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE RESTRICT
);

-- Indexes
CREATE INDEX idx_comments_post ON comments(post_id);
CREATE INDEX idx_comments_author ON comments(author_id);

-- ============================================================
-- Table: post_reactions
-- ============================================================
CREATE TABLE post_reactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    post_id UUID NOT NULL,
    user_id UUID NOT NULL,
    reaction_type reaction_type NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    CONSTRAINT fk_post_reactions_post FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    CONSTRAINT fk_post_reactions_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT uq_post_reaction_unique UNIQUE (post_id, user_id, reaction_type)
);

-- Indexes
CREATE INDEX idx_post_reactions_post ON post_reactions(post_id);
CREATE INDEX idx_post_reactions_user ON post_reactions(user_id);

-- ============================================================
-- Table: heritage_items
-- ============================================================
CREATE TABLE heritage_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    family_id UUID NOT NULL,
    branch_id UUID,
    title VARCHAR(200) NOT NULL,
    type heritage_type NOT NULL,
    category heritage_category NOT NULL,
    period VARCHAR(100),
    content TEXT,
    status heritage_status NOT NULL DEFAULT 'DRAFT',
    media_url VARCHAR(500),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    CONSTRAINT fk_heritage_items_family FOREIGN KEY (family_id) REFERENCES families(id) ON DELETE CASCADE,
    CONSTRAINT fk_heritage_items_branch FOREIGN KEY (branch_id) REFERENCES family_branches(id) ON DELETE SET NULL
);

-- Indexes
CREATE INDEX idx_heritage_items_family ON heritage_items(family_id);
CREATE INDEX idx_heritage_items_branch ON heritage_items(branch_id);

-- ============================================================
-- Table: media_assets
-- ============================================================
CREATE TABLE media_assets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_id UUID,
    family_id UUID,
    uploaded_by UUID NOT NULL,
    caption VARCHAR(255),
    url VARCHAR(500) NOT NULL,
    media_type media_type NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    CONSTRAINT fk_media_assets_event FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
    CONSTRAINT fk_media_assets_family FOREIGN KEY (family_id) REFERENCES families(id) ON DELETE CASCADE,
    CONSTRAINT fk_media_assets_user FOREIGN KEY (uploaded_by) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT chk_media_at_least_one_parent CHECK (
        (event_id IS NOT NULL AND family_id IS NULL) OR
        (event_id IS NULL AND family_id IS NOT NULL)
    )
);

-- Indexes
CREATE INDEX idx_media_assets_event ON media_assets(event_id);
CREATE INDEX idx_media_assets_family ON media_assets(family_id);
CREATE INDEX idx_media_assets_uploaded_by ON media_assets(uploaded_by);

-- ============================================================
-- Table: employment_profiles
-- ============================================================
CREATE TABLE employment_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    member_id UUID NOT NULL,
    company_name VARCHAR(200) NOT NULL,
    position VARCHAR(100),
    start_date DATE,
    end_date DATE,
    is_current BOOLEAN NOT NULL DEFAULT FALSE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    CONSTRAINT fk_employment_profiles_member FOREIGN KEY (member_id) REFERENCES family_members(id) ON DELETE CASCADE
);

-- Indexes
CREATE INDEX idx_employment_profiles_member ON employment_profiles(member_id);

-- ============================================================
-- Table: education_profiles
-- ============================================================
CREATE TABLE education_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    member_id UUID NOT NULL,
    school_name VARCHAR(200) NOT NULL,
    degree VARCHAR(100),
    field_of_study VARCHAR(100),
    start_year SMALLINT,
    end_year SMALLINT,
    gpa NUMERIC(3, 2),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    CONSTRAINT fk_education_profiles_member FOREIGN KEY (member_id) REFERENCES family_members(id) ON DELETE CASCADE
);

-- Indexes
CREATE INDEX idx_education_profiles_member ON education_profiles(member_id);

-- ============================================================
-- Table: ai_conversations
-- ============================================================
CREATE TABLE ai_conversations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL,
    title VARCHAR(200),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    CONSTRAINT fk_ai_conversations_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Indexes
CREATE INDEX idx_ai_conversations_user ON ai_conversations(user_id);

-- ============================================================
-- Table: ai_messages
-- ============================================================
CREATE TABLE ai_messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    conversation_id UUID NOT NULL,
    role VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    CONSTRAINT fk_ai_messages_conversation FOREIGN KEY (conversation_id) REFERENCES ai_conversations(id) ON DELETE CASCADE
);

-- Indexes
CREATE INDEX idx_ai_messages_conversation ON ai_messages(conversation_id);

-- ============================================================
-- View: family_tree_summary
-- ============================================================
-- Provides a summary of the family tree structure for quick querying
-- ============================================================
CREATE OR REPLACE VIEW family_tree_summary AS
SELECT
    f.id AS family_id,
    f.family_name,
    fm.user_id,
    fm.full_name AS member_name,
    fm.gender,
    fm.is_alive,
    r.type AS relationship_type,
    r.from_member_id,
    r.to_member_id
FROM families f
LEFT JOIN family_members fm ON f.id = fm.family_id
LEFT JOIN relationships r ON (r.from_member_id = fm.id OR r.to_member_id = fm.id)
WHERE fm.user_id IS NOT NULL;

-- Grant permissions (adjust as needed for your environment)
-- GRANT ALL ON ALL TABLES TO your_role;
-- GRANT USAGE ON ALL SEQUENCES TO your_role;

-- ============================================================
-- Schema Validation Queries
-- ============================================================
-- Verify all PKs are present
SELECT
    kcu.table_name,
    kcu.column_name
FROM information_schema.key_column_usage kcu
JOIN information_schema.table_constraints tc
    ON kcu.constraint_name = tc.constraint_name
    AND kcu.table_schema = tc.table_schema
WHERE tc.table_schema = 'public' AND tc.constraint_type = 'PRIMARY KEY'
ORDER BY kcu.table_name, kcu.ordinal_position;

SELECT
    kcu.table_name,
    kcu.column_name,
    kcu.constraint_name,
    kcu.referenced_table_name,
    kcu.referenced_column_name
FROM information_schema.key_column_usage kcu
JOIN information_schema.table_constraints tc
    ON kcu.constraint_name = tc.constraint_name
    AND kcu.table_schema = tc.table_schema
WHERE tc.table_schema = 'public' AND tc.constraint_type = 'FOREIGN KEY'
ORDER BY kcu.table_name, kcu.constraint_name;