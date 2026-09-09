from uuid import UUID

from sqlalchemy.exc import IntegrityError

from app.infrastructure.models.community import (
    Post,
    Comment,
    PostReaction,
)

from app.infrastructure.repositories.post_repository import (
    PostRepository,
)

from app.infrastructure.repositories.comment_repository import (
    CommentRepository,
)

from app.infrastructure.repositories.reaction_repository import (
    ReactionRepository,
)


class CommunityServiceError(Exception):
    pass


class NotFoundError(CommunityServiceError):
    pass


class ForbiddenError(CommunityServiceError):
    pass


class ValidationError(CommunityServiceError):
    pass


class ConflictError(CommunityServiceError):
    pass


class CommunityService:

    ALLOWED_REACTIONS = {
        "like",
        "love",
        "haha",
        "sad",
        "angry",
    }

    def __init__(
        self,
        post_repository: PostRepository,
        comment_repository: CommentRepository,
        reaction_repository: ReactionRepository,
    ):
        self.post_repository = post_repository
        self.comment_repository = comment_repository
        self.reaction_repository = reaction_repository

    # =========================================================
    # CREATE POST
    # FR-COM-01
    # =========================================================

    async def create_post(
        self,
        family_id: UUID,
        author_id: UUID,
        content: str,
        media_urls: list | None = None,
        visibility_scope: str = "FAMILY",
        branch_id: UUID | None = None,
    ) -> Post:

        content = content.strip()

        if not content:
            raise ValidationError(
                "Post content cannot be empty."
            )

        return await self.post_repository.create(
            family_id=family_id,
            author_id=author_id,
            content=content,
            media_urls=media_urls,
            visibility_scope=visibility_scope,
            branch_id=branch_id,
        )

    # =========================================================
    # GET FEED
    # FR-COM-03
    # =========================================================

    async def get_feed(
        self,
        family_id: UUID,
        page: int = 1,
        page_size: int = 20,
    ) -> list[Post]:

        if page < 1:
            raise ValidationError(
                "page must be greater than or equal to 1."
            )

        if page_size < 1 or page_size > 100:
            raise ValidationError(
                "page_size must be between 1 and 100."
            )

        offset = (page - 1) * page_size

        return await self.post_repository.get_feed(
            family_id=family_id,
            offset=offset,
            limit=page_size,
        )

    # =========================================================
    # GET POST
    # =========================================================

    async def get_post(
        self,
        post_id: UUID,
    ) -> Post:

        post = await self.post_repository.get_by_id(
            post_id
        )

        if post is None:
            raise NotFoundError(
                "Post not found."
            )

        return post

    # =========================================================
    # UPDATE POST
    # =========================================================

    async def update_post(
        self,
        post_id: UUID,
        current_user_id: UUID,
        content: str | None = None,
        media_urls: list | None = None,
        visibility_scope: str | None = None,
        branch_id: UUID | None = None,
    ) -> Post:

        post = await self.get_post(post_id)

        if post.author_id != current_user_id:
            raise ForbiddenError(
                "Only the post author can update this post."
            )

        if content is not None:
            content = content.strip()

            if not content:
                raise ValidationError(
                    "Post content cannot be empty."
                )

        return await self.post_repository.update(
            post=post,
            content=content,
            media_urls=media_urls,
            visibility_scope=visibility_scope,
            branch_id=branch_id,
        )

    # =========================================================
    # DELETE POST
    # =========================================================

    async def delete_post(
        self,
        post_id: UUID,
        current_user_id: UUID,
    ):

        post = await self.get_post(post_id)

        if post.author_id != current_user_id:
            raise ForbiddenError(
                "Only the post author can delete this post."
            )

        await self.post_repository.delete(post)

    # =========================================================
    # ADD COMMENT
    # FR-COM-02
    # =========================================================

    async def add_comment(
        self,
        post_id: UUID,
        author_id: UUID,
        content: str,
    ) -> Comment:

        await self.get_post(post_id)

        content = content.strip()

        if not content:
            raise ValidationError(
                "Comment content cannot be empty."
            )

        if len(content) > 1000:
            raise ValidationError(
                "Comment cannot exceed 1000 characters."
            )

        return await self.comment_repository.create(
            post_id=post_id,
            author_id=author_id,
            content=content,
        )

    # =========================================================
    # ADD REACTION
    # FR-COM-02
    # =========================================================

    async def add_reaction(
        self,
        post_id: UUID,
        user_id: UUID,
        reaction_type: str,
    ) -> PostReaction:

        await self.get_post(post_id)

        reaction_type = reaction_type.lower().strip()

        if reaction_type not in self.ALLOWED_REACTIONS:
            raise ValidationError(
                "Reaction must be one of: "
                "like, love, haha, sad, angry."
            )

        # Check duplicate
        existing = await self.reaction_repository.get(
            post_id=post_id,
            user_id=user_id,
            reaction_type=reaction_type,
        )

        if existing is not None:
            raise ConflictError(
                "This reaction already exists."
            )

        try:

            return await self.reaction_repository.create(
                post_id=post_id,
                user_id=user_id,
                reaction_type=reaction_type,
            )

        except IntegrityError as exc:

            raise ConflictError(
                "This reaction already exists."
            ) from exc

    # =========================================================
    # REMOVE REACTION
    # =========================================================

    async def remove_reaction(
        self,
        post_id: UUID,
        user_id: UUID,
        reaction_type: str,
    ):

        await self.get_post(post_id)

        reaction_type = reaction_type.lower().strip()

        if reaction_type not in self.ALLOWED_REACTIONS:
            raise ValidationError(
                "Invalid reaction type."
            )

        deleted = await self.reaction_repository.delete(
            post_id=post_id,
            user_id=user_id,
            reaction_type=reaction_type,
        )

        if not deleted:
            raise NotFoundError(
                "Reaction not found."
            )

    # =========================================================
    # CREATE ANNOUNCEMENT
    # FR-COM-05
    # =========================================================

    async def create_announcement(
        self,
        family_id: UUID,
        author_id: UUID,
        content: str,
        media_urls: list | None = None,
    ) -> Post:

        return await self.create_post(
            family_id=family_id,
            author_id=author_id,
            content=content,
            media_urls=media_urls,
            visibility_scope="FAMILY",
        )