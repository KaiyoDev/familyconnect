"""Enum types for FamilyConnect domain models."""
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ENUM as PG_ENUM


# ---- PostgreSQL ENUM definitions (created via CREATE TYPE) ----

USER_ROLE_ENUM = PG_ENUM(
    "user_role",
    "ADMIN", "USER", "GUEST",
    name="user_role",
    create_type=True,
)

USER_STATUS_ENUM = PG_ENUM(
    "user_status",
    "PENDING", "ACTIVE", "INACTIVE", "BLOCKED", "SUSPENDED",
    name="user_status",
    create_type=True,
)

FAMILY_STATUS_ENUM = PG_ENUM(
    "family_status",
    "ACTIVE", "INACTIVE",
    name="family_status",
    create_type=True,
)

GENDER_ENUM = PG_ENUM(
    "gender",
    "MALE", "FEMALE", "OTHER", "UNKNOWN",
    name="gender",
    create_type=True,
)

MEMBER_STATUS_ENUM = PG_ENUM(
    "member_status",
    "PENDING", "ACTIVE", "SUSPENDED",
    name="member_status",
    create_type=True,
)

RELATIONSHIP_TYPE_ENUM = PG_ENUM(
    "relationship_type",
    "PARENT_CHILD", "MARRIAGE",
    name="relationship_type",
    create_type=True,
)

EVENT_TYPE_ENUM = PG_ENUM(
    "event_type",
    "MEETING", "WEDDING", "MEMORIAL", "BIRTHDAY", "TRIP", "OTHER",
    name="event_type",
    create_type=True,
)

EVENT_STATUS_ENUM = PG_ENUM(
    "event_status",
    "OPEN", "CANCELLED", "COMPLETED",
    name="event_status",
    create_type=True,
)

RSVP_RESPONSE_ENUM = PG_ENUM(
    "rsvp_response",
    "GOING", "NOT_GOING", "MAYBE", "NO_RESPONSE",
    name="rsvp_response",
    create_type=True,
)

HERITAGE_TYPE_ENUM = PG_ENUM(
    "heritage_type",
    "DOCUMENT", "IMAGE", "MAP", "ARTIFACT", "STORY",
    name="heritage_type",
    create_type=True,
)

HERITAGE_CATEGORY_ENUM = PG_ENUM(
    "heritage_category",
    "STORY", "DOCUMENT", "OUTSTANDING_MEMBER",
    name="heritage_category",
    create_type=True,
)

HERITAGE_STATUS_ENUM = PG_ENUM(
    "heritage_status",
    "DRAFT", "PUBLISHED", "REMOVED",
    name="heritage_status",
    create_type=True,
)

POST_STATUS_ENUM = PG_ENUM(
    "post_status",
    "PUBLISHED", "DRAFT", "REMOVED",
    name="post_status",
    create_type=True,
)

POST_VISIBILITY_ENUM = PG_ENUM(
    "post_visibility",
    "FAMILY", "BRANCH",
    name="post_visibility",
    create_type=True,
)

MEDIA_TYPE_ENUM = PG_ENUM(
    "media_type",
    "IMAGE", "VIDEO", "DOCUMENT",
    name="media_type",
    create_type=True,
)

AUDIT_ACTION_ENUM = PG_ENUM(
    "audit_action",
    "CREATE", "UPDATE", "DELETE", "LOGIN", "ROLE_CHANGE",
    "MODERATE", "BACKUP", "RESTORE",
    name="audit_action",
    create_type=True,
)

NOTIFICATION_TYPE_ENUM = PG_ENUM(
    "notification_type",
    "EVENT_REMINDER", "INVITATION", "NEW_POST", "COMMENT",
    "ANNOUNCEMENT", "ACCOUNT",
    name="notification_type",
    create_type=True,
)

REACTION_TYPE_ENUM = PG_ENUM(
    "reaction_type",
    "LIKE", "LOVE", "HAHA", "WOW", "SAD", "ANGRY",
    name="reaction_type",
    create_type=True,
)

AI_MESSAGE_ROLE_ENUM = PG_ENUM(
    "ai_message_role",
    "user", "assistant",
    name="ai_message_role",
    create_type=True,
)
