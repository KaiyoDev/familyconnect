============================= test session starts ==============================
platform darwin -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0 -- /Library/Frameworks/Python.framework/Versions/3.14/bin/python3
rootdir: /Users/lekhabinh/familyconnect/backend
configfile: pytest.ini
plugins: cov-7.1.0, anyio-4.14.1, asyncio-1.4.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 160 items

backend/tests/unit/domain/test_domain_utils.py::TestPasswordUtils::test_hash_password_success PASSED [  0%]
backend/tests/unit/domain/test_domain_utils.py::TestPasswordUtils::test_verify_password_success PASSED [  1%]
backend/tests/unit/domain/test_domain_utils.py::TestPasswordUtils::test_verify_password_failure PASSED [  1%]
backend/tests/unit/domain/test_domain_utils.py::TestPasswordUtils::test_hash_password_empty_string PASSED [  2%]
backend/tests/unit/domain/test_domain_utils.py::TestJWTUtils::test_create_access_token PASSED [  3%]
backend/tests/unit/domain/test_domain_utils.py::TestJWTUtils::test_create_refresh_token PASSED [  3%]
backend/tests/unit/domain/test_domain_utils.py::TestJWTUtils::test_decode_token_success PASSED [  4%]
backend/tests/unit/domain/test_domain_utils.py::TestJWTUtils::test_decode_token_invalid PASSED [  5%]
backend/tests/unit/repositories/test_ai_repository.py::TestAIRepository::test_create_conversation PASSED [  5%]
backend/tests/unit/repositories/test_ai_repository.py::TestAIRepository::test_get_by_id_found PASSED [  6%]
backend/tests/unit/repositories/test_ai_repository.py::TestAIRepository::test_get_by_id_not_found PASSED [  6%]
backend/tests/unit/repositories/test_ai_repository.py::TestAIRepository::test_list_by_user PASSED [  7%]
backend/tests/unit/repositories/test_ai_repository.py::TestAIRepository::test_delete_conversation PASSED [  8%]
backend/tests/unit/repositories/test_ai_repository.py::TestAIRepository::test_add_message PASSED [  8%]
backend/tests/unit/repositories/test_ai_repository.py::TestAIRepository::test_get_messages PASSED [  9%]
backend/tests/unit/repositories/test_community_event_repos.py::TestPostRepository::test_create PASSED [ 10%]
backend/tests/unit/repositories/test_community_event_repos.py::TestPostRepository::test_get_by_id PASSED [ 10%]
backend/tests/unit/repositories/test_community_event_repos.py::TestPostRepository::test_get_by_id_not_found PASSED [ 11%]
backend/tests/unit/repositories/test_community_event_repos.py::TestPostRepository::test_get_feed PASSED [ 11%]
backend/tests/unit/repositories/test_community_event_repos.py::TestPostRepository::test_update PASSED [ 12%]
backend/tests/unit/repositories/test_community_event_repos.py::TestPostRepository::test_delete PASSED [ 13%]
backend/tests/unit/repositories/test_community_event_repos.py::TestCommentRepository::test_create PASSED [ 13%]
backend/tests/unit/repositories/test_community_event_repos.py::TestCommentRepository::test_get_by_post PASSED [ 14%]
backend/tests/unit/repositories/test_community_event_repos.py::TestReactionRepository::test_get PASSED [ 15%]
backend/tests/unit/repositories/test_community_event_repos.py::TestReactionRepository::test_create PASSED [ 15%]
backend/tests/unit/repositories/test_community_event_repos.py::TestReactionRepository::test_delete PASSED [ 16%]
backend/tests/unit/repositories/test_community_event_repos.py::TestEventRepository::test_create PASSED [ 16%]
backend/tests/unit/repositories/test_community_event_repos.py::TestEventRepository::test_get_by_family PASSED [ 17%]
backend/tests/unit/repositories/test_community_event_repos.py::TestEventRepository::test_get_by_id_found PASSED [ 18%]
backend/tests/unit/repositories/test_community_event_repos.py::TestEventRepository::test_get_by_id_not_found PASSED [ 18%]
backend/tests/unit/repositories/test_community_event_repos.py::TestEventRepository::test_update PASSED [ 19%]
backend/tests/unit/repositories/test_community_event_repos.py::TestEventRepository::test_delete_found PASSED [ 20%]
backend/tests/unit/repositories/test_community_event_repos.py::TestEventRepository::test_delete_not_found PASSED [ 20%]
backend/tests/unit/repositories/test_community_event_repos.py::TestBranchRepository::test_create PASSED [ 21%]
backend/tests/unit/repositories/test_community_event_repos.py::TestBranchRepository::test_get_by_family PASSED [ 21%]
backend/tests/unit/repositories/test_community_event_repos.py::TestBranchRepository::test_get_by_id PASSED [ 22%]
backend/tests/unit/repositories/test_community_event_repos.py::TestMemberRepository::test_create PASSED [ 23%]
backend/tests/unit/repositories/test_community_event_repos.py::TestMemberRepository::test_get_by_family PASSED [ 23%]
backend/tests/unit/repositories/test_community_event_repos.py::TestRelationshipRepository::test_create PASSED [ 24%]
backend/tests/unit/repositories/test_community_event_repos.py::TestRelationshipRepository::test_get_by_member PASSED [ 25%]
backend/tests/unit/repositories/test_repositories.py::TestUserRepository::test_exists_by_email_true PASSED [ 25%]
backend/tests/unit/repositories/test_repositories.py::TestUserRepository::test_exists_by_email_false PASSED [ 26%]
backend/tests/unit/repositories/test_repositories.py::TestUserRepository::test_create_user PASSED [ 26%]
backend/tests/unit/repositories/test_repositories.py::TestUserRepository::test_get_by_email_found PASSED [ 27%]
backend/tests/unit/repositories/test_repositories.py::TestUserRepository::test_get_by_email_not_found PASSED [ 28%]
backend/tests/unit/repositories/test_repositories.py::TestUserRepository::test_get_by_id PASSED [ 28%]
backend/tests/unit/repositories/test_repositories.py::TestUserRepository::test_update_user PASSED [ 29%]
backend/tests/unit/repositories/test_repositories.py::TestUserRepository::test_get_all PASSED [ 30%]
backend/tests/unit/repositories/test_repositories.py::TestUserRepository::test_delete_user PASSED [ 30%]
backend/tests/unit/repositories/test_repositories.py::TestAdminRepository::test_list_users PASSED [ 31%]
backend/tests/unit/repositories/test_repositories.py::TestAdminRepository::test_get_user_found PASSED [ 31%]
backend/tests/unit/repositories/test_repositories.py::TestAdminRepository::test_get_user_not_found PASSED [ 32%]
backend/tests/unit/repositories/test_repositories.py::TestAdminRepository::test_update_user_status PASSED [ 33%]
backend/tests/unit/repositories/test_repositories.py::TestAdminRepository::test_list_audit_logs PASSED [ 33%]
backend/tests/unit/repositories/test_repositories.py::TestAdminRepository::test_moderate_post PASSED [ 34%]
backend/tests/unit/repositories/test_repositories.py::TestAdminRepository::test_moderate_post_not_found PASSED [ 35%]
backend/tests/unit/repositories/test_repositories.py::TestAdminRepository::test_moderate_comment PASSED [ 35%]
backend/tests/unit/repositories/test_repositories.py::TestAdminRepository::test_add_audit_log PASSED [ 36%]
backend/tests/unit/repositories/test_repositories.py::TestAdminRepository::test_get_config PASSED [ 36%]
backend/tests/unit/repositories/test_repositories.py::TestAdminRepository::test_update_config_new PASSED [ 37%]
backend/tests/unit/repositories/test_repositories.py::TestAdminRepository::test_list_users_with_filter PASSED [ 38%]
backend/tests/unit/repositories/test_repositories.py::TestFamilyRepository::test_create_family PASSED [ 38%]
backend/tests/unit/repositories/test_repositories.py::TestFamilyRepository::test_get_by_id PASSED [ 39%]
backend/tests/unit/repositories/test_repositories.py::TestFamilyRepository::test_get_by_id_not_found PASSED [ 40%]
backend/tests/unit/repositories/test_repositories.py::TestFamilyRepository::test_get_all PASSED [ 40%]
backend/tests/unit/repositories/test_rsvp_repository.py::TestRSVPRepository::test_upsert_rsvp_new PASSED [ 41%]
backend/tests/unit/repositories/test_rsvp_repository.py::TestRSVPRepository::test_upsert_rsvp_update PASSED [ 41%]
backend/tests/unit/repositories/test_rsvp_repository.py::TestRSVPRepository::test_get_attendees_all PASSED [ 42%]
backend/tests/unit/repositories/test_rsvp_repository.py::TestRSVPRepository::test_get_attendees_filtered PASSED [ 43%]
backend/tests/unit/services/test_ai_service.py::TestAIService::test_create_conversation PASSED [ 43%]
backend/tests/unit/services/test_ai_service.py::TestAIService::test_get_conversation_with_messages PASSED [ 44%]
backend/tests/unit/services/test_ai_service.py::TestAIService::test_get_conversation_not_found PASSED [ 45%]
backend/tests/unit/services/test_ai_service.py::TestAIService::test_list_conversations PASSED [ 45%]
backend/tests/unit/services/test_ai_service.py::TestAIService::test_delete_conversation PASSED [ 46%]
backend/tests/unit/services/test_ai_service.py::TestAIService::test_delete_conversation_not_found PASSED [ 46%]
backend/tests/unit/services/test_ai_service.py::TestAIService::test_chat_mock_provider PASSED [ 47%]
backend/tests/unit/services/test_ai_service.py::TestAIService::test_semantic_search PASSED [ 48%]
backend/tests/unit/services/test_ai_service.py::TestAIService::test_semantic_search_no_results PASSED [ 48%]
backend/tests/unit/services/test_ai_service.py::TestAIService::test_explain_relationship_parent_child PASSED [ 49%]
backend/tests/unit/services/test_ai_service.py::TestAIService::test_explain_relationship_marriage PASSED [ 50%]
backend/tests/unit/services/test_ai_service.py::TestAIService::test_summarize_short PASSED [ 50%]
backend/tests/unit/services/test_ai_service.py::TestAIService::test_summarize_medium PASSED [ 51%]
backend/tests/unit/services/test_ai_service.py::TestAIService::test_summarize_full PASSED [ 51%]
backend/tests/unit/services/test_ai_service.py::TestAIService::test_summarize_invalid_length PASSED [ 52%]
backend/tests/unit/services/test_auth_admin_service.py::TestAuthService::test_register_success PASSED [ 53%]
backend/tests/unit/services/test_auth_admin_service.py::TestAuthService::test_register_duplicate_email PASSED [ 53%]
backend/tests/unit/services/test_auth_admin_service.py::TestAuthService::test_login_success PASSED [ 54%]
backend/tests/unit/services/test_auth_admin_service.py::TestAuthService::test_login_wrong_password PASSED [ 55%]
backend/tests/unit/services/test_auth_admin_service.py::TestAuthService::test_login_nonexistent_email PASSED [ 55%]
backend/tests/unit/services/test_auth_admin_service.py::TestAuthService::test_get_profile PASSED [ 56%]
backend/tests/unit/services/test_auth_admin_service.py::TestAuthService::test_get_profile_not_found PASSED [ 56%]
backend/tests/unit/services/test_auth_admin_service.py::TestAuthService::test_logout PASSED [ 57%]
backend/tests/unit/services/test_auth_admin_service.py::TestAuthService::test_refresh_token_success PASSED [ 58%]
backend/tests/unit/services/test_auth_admin_service.py::TestAuthService::test_refresh_token_invalid PASSED [ 58%]
backend/tests/unit/services/test_auth_admin_service.py::TestAuthService::test_forgot_password PASSED [ 59%]
backend/tests/unit/services/test_auth_admin_service.py::TestAuthService::test_forgot_password_nonexistent PASSED [ 60%]
backend/tests/unit/services/test_auth_admin_service.py::TestAuthService::test_reset_password_success PASSED [ 60%]
backend/tests/unit/services/test_auth_admin_service.py::TestAuthService::test_reset_password_invalid_token PASSED [ 61%]
backend/tests/unit/services/test_auth_admin_service.py::TestAuthService::test_update_profile PASSED [ 61%]
backend/tests/unit/services/test_auth_admin_service.py::TestAdminService::test_list_users_valid PASSED [ 62%]
backend/tests/unit/services/test_auth_admin_service.py::TestAdminService::test_list_users_invalid_page_size PASSED [ 63%]
backend/tests/unit/services/test_auth_admin_service.py::TestAdminService::test_activate_user_success PASSED [ 63%]
backend/tests/unit/services/test_auth_admin_service.py::TestAdminService::test_activate_user_invalid_status PASSED [ 64%]
backend/tests/unit/services/test_auth_admin_service.py::TestAdminService::test_activate_user_not_found PASSED [ 65%]
backend/tests/unit/services/test_auth_admin_service.py::TestAdminService::test_suspend_user PASSED [ 65%]
backend/tests/unit/services/test_auth_admin_service.py::TestAdminService::test_get_audit_log PASSED [ 66%]
backend/tests/unit/services/test_auth_admin_service.py::TestAdminService::test_moderate_post PASSED [ 66%]
backend/tests/unit/services/test_auth_admin_service.py::TestAdminService::test_moderate_invalid_type PASSED [ 67%]
backend/tests/unit/services/test_auth_admin_service.py::TestAdminService::test_update_config PASSED [ 68%]
backend/tests/unit/services/test_auth_admin_service.py::TestAdminService::test_update_config_empty PASSED [ 68%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_create_post_success PASSED [ 69%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_create_post_empty PASSED [ 70%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_get_feed_success PASSED [ 70%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_get_feed_invalid_page PASSED [ 71%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_get_feed_invalid_page_size PASSED [ 71%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_get_post_not_found PASSED [ 72%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_update_post PASSED [ 73%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_update_post_forbidden PASSED [ 73%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_delete_post PASSED [ 74%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_delete_post_forbidden PASSED [ 75%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_add_comment_success PASSED [ 75%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_add_comment_empty PASSED [ 76%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_add_comment_too_long PASSED [ 76%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_add_reaction_success PASSED [ 77%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_add_reaction_invalid_type PASSED [ 78%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_add_reaction_duplicate PASSED [ 78%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_add_reaction_integrity_error PASSED [ 79%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_remove_reaction_success PASSED [ 80%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_remove_reaction_invalid_type PASSED [ 80%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_remove_reaction_not_found PASSED [ 81%]
backend/tests/unit/services/test_community_service.py::TestCommunityService::test_create_announcement PASSED [ 81%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_create_event_success PASSED [ 82%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_get_events PASSED [ 83%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_get_events_empty PASSED [ 83%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_get_event_success PASSED [ 84%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_get_event_not_found PASSED [ 85%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_update_event_success PASSED [ 85%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_update_event_not_found PASSED [ 86%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_cancel_event_success PASSED [ 86%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_cancel_event_not_found PASSED [ 87%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_rsvp_going PASSED [ 88%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_rsvp_maybe PASSED [ 88%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_rsvp_not_going PASSED [ 89%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_rsvp_invalid_status PASSED [ 90%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_get_attendees_all PASSED [ 90%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_get_attendees_filtered PASSED [ 91%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_get_attendees_empty PASSED [ 91%]
backend/tests/unit/services/test_event_service.py::TestEventService::test_send_reminder PASSED [ 92%]
backend/tests/unit/services/test_family_service.py::test_create_family_creates_default_branch_and_commits PASSED [ 93%]
backend/tests/unit/services/test_family_service.py::test_get_family_raises_when_missing PASSED [ 93%]
backend/tests/unit/services/test_family_service.py::test_update_family PASSED [ 94%]
backend/tests/unit/services/test_family_service.py::test_delete_family PASSED [ 95%]
backend/tests/unit/services/test_family_service.py::test_add_member_to_valid_branch PASSED [ 95%]
backend/tests/unit/services/test_family_service.py::test_add_member_rejects_branch_from_another_family PASSED [ 96%]
backend/tests/unit/services/test_family_service.py::test_update_and_remove_member PASSED [ 96%]
backend/tests/unit/services/test_family_service.py::test_add_parent_child_relationship PASSED [ 97%]
backend/tests/unit/services/test_family_service.py::test_add_marriage_relationship PASSED [ 98%]
backend/tests/unit/services/test_family_service.py::test_relationship_validation PASSED [ 98%]
backend/tests/unit/services/test_family_service.py::test_genealogy_tree_contains_roots_children_and_spouses PASSED [ 99%]
backend/tests/unit/services/test_family_service.py::test_lookup_relationship_returns_direct_relationship PASSED [100%]

=============================== warnings summary ===============================
../../../Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/fastapi/testclient.py:1
  /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

backend/create_app.py:62
  /Users/lekhabinh/familyconnect/backend/create_app.py:62: DeprecationWarning: 
          on_event is deprecated, use lifespan event handlers instead.
  
          Read more about it in the
          [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
          
    @app.on_event("startup")

../../../Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/fastapi/applications.py:4675
../../../Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/fastapi/applications.py:4675
  /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/fastapi/applications.py:4675: DeprecationWarning: 
          on_event is deprecated, use lifespan event handlers instead.
  
          Read more about it in the
          [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
          
    return self.router.on_event(event_type)  # ty: ignore[deprecated]

backend/create_app.py:67
  /Users/lekhabinh/familyconnect/backend/create_app.py:67: DeprecationWarning: 
          on_event is deprecated, use lifespan event handlers instead.
  
          Read more about it in the
          [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
          
    @app.on_event("shutdown")

backend/database.py:5
  /Users/lekhabinh/familyconnect/backend/database.py:5: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    Base = declarative_base()

../../../Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/_pytest/config/__init__.py:1464
  /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/_pytest/config/__init__.py:1464: PytestConfigWarning: Unknown config option: env
  
    self._warn_or_fail_if_strict(f"Unknown config option: {key}\n")

backend/app/schemas/auth.py:34
  /Users/lekhabinh/familyconnect/backend/app/schemas/auth.py:34: PydanticDeprecatedSince20: Support for class-based `config` is deprecated, use ConfigDict instead. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.13/migration/
    class UserResponse(BaseModel):

tests/unit/repositories/test_ai_repository.py::TestAIRepository::test_create_conversation
  /Users/lekhabinh/familyconnect/backend/app/infrastructure/repositories/ai_repository.py:23: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    now = datetime.utcnow()

tests/unit/repositories/test_ai_repository.py::TestAIRepository::test_add_message
  /Users/lekhabinh/familyconnect/backend/app/infrastructure/repositories/ai_repository.py:97: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    now = datetime.utcnow()

tests/unit/repositories/test_rsvp_repository.py::TestRSVPRepository::test_upsert_rsvp_new
  /Users/lekhabinh/familyconnect/backend/app/infrastructure/repositories/rsvp_repository.py:33: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
    responded_at=__import__("datetime").datetime.utcnow(),

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
================================ tests coverage ================================
_______________ coverage: platform darwin, python 3.14.5-final-0 _______________

Name                                                                 Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------------------------------
backend/app/__init__.py                                                  0      0   100%
backend/app/api/__init__.py                                              0      0   100%
backend/app/api/controllers/__init__.py                                  0      0   100%
backend/app/api/controllers/admin_controller.py                         49     24    51%   15, 33-34, 43-46, 51-54, 62-65, 70-73, 78, 83-86
backend/app/api/controllers/ai_controller.py                            68     28    59%   49, 62-66, 76-82, 96-99, 108-111, 126-134, 148-149, 163-168, 182-186
backend/app/api/controllers/auth_controller.py                          29     18    38%   10-12, 16-22, 26-35
backend/app/api/controllers/community_controller.py                     89     48    46%   55, 130-143, 176-193, 215-223, 251-278, 305-321, 350-367, 396-420, 453-470
backend/app/api/controllers/directory_controller.py                     55     10    82%   20, 57, 72, 83, 94, 111, 128, 139, 156, 173
backend/app/api/controllers/event_controller.py                         38     13    66%   22-24, 39-41, 53-54, 62, 71, 79, 88, 97
backend/app/api/controllers/family_controller.py                        43      8    81%   38, 43, 48, 54, 60, 66, 72, 78
backend/app/api/controllers/health_controller.py                         9      2    78%   13-14
backend/app/api/controllers/heritage_controller.py                      63     12    81%   15, 52, 68, 84, 96, 105, 115, 126, 136, 146-147, 158
backend/app/api/dependencies.py                                         35     17    51%   24-37, 42-44, 49, 53
backend/app/api/middleware.py                                           37     21    43%   28-58, 63, 71-72
backend/app/api/requests.py                                              0      0   100%
backend/app/api/responses.py                                             0      0   100%
backend/app/api/routes.py                                               20      0   100%
backend/app/api/schemas/__init__.py                                      0      0   100%
backend/app/api/schemas/auth.py                                         15     15     0%   1-33
backend/app/api/swagger.py                                               6      6     0%   11-24
backend/app/domain/__init__.py                                           0      0   100%
backend/app/domain/constants.py                                          4      4     0%   4-11
backend/app/domain/exceptions.py                                        20      3    85%   24, 31, 38
backend/app/domain/interfaces/__init__.py                               10      0   100%
backend/app/domain/interfaces/auth_service.py                           18      5    72%   8, 12, 16, 20, 24
backend/app/domain/interfaces/branch_repository.py                       5      0   100%
backend/app/domain/interfaces/community_repository.py                   12      2    83%   13, 17
backend/app/domain/interfaces/community_service.py                      12      3    75%   8, 12, 16
backend/app/domain/interfaces/event_repository.py                       13      2    85%   14, 18
backend/app/domain/interfaces/event_service.py                          12      3    75%   8, 12, 16
backend/app/domain/interfaces/family_repository.py                      12      2    83%   13, 17
backend/app/domain/interfaces/family_service.py                         15      4    73%   8, 12, 16, 20
backend/app/domain/interfaces/member_repository.py                       5      0   100%
backend/app/domain/interfaces/relationship_repository.py                 5      0   100%
backend/app/domain/interfaces/repository_base.py                        20      5    75%   11, 15, 19, 23, 27
backend/app/domain/interfaces/unit_of_work.py                            2      0   100%
backend/app/domain/interfaces/user_repository.py                        11      2    82%   12, 16
backend/app/domain/models/__init__.py                                    2      2     0%   1-17
backend/app/domain/models/dtos.py                                       63     63     0%   1-132
backend/app/domain/models/family.py                                     41     41     0%   2-71
backend/app/domain/utils/__init__.py                                     0      0   100%
backend/app/domain/utils/jwt.py                                         19      0   100%
backend/app/domain/utils/password.py                                     6      0   100%
backend/app/infrastructure/__init__.py                                   0      0   100%
backend/app/infrastructure/databases/__init__.py                         0      0   100%
backend/app/infrastructure/databases/base.py                            12      0   100%
backend/app/infrastructure/databases/database.py                        13      5    62%   4-6, 29-30
backend/app/infrastructure/models/__init__.py                            8      0   100%
backend/app/infrastructure/models/admin.py                              25      0   100%
backend/app/infrastructure/models/app_ai_model.py                       19      2    89%   24, 42
backend/app/infrastructure/models/community.py                          41      3    93%   40, 62, 87
backend/app/infrastructure/models/directory.py                          29      2    93%   28, 50
backend/app/infrastructure/models/event.py                              35      2    94%   46, 80
backend/app/infrastructure/models/genealogy.py                          63      4    94%   30, 62, 118, 150
backend/app/infrastructure/models/heritage.py                           33      2    94%   32, 68
backend/app/infrastructure/models/mappers.py                            21     21     0%   2-33
backend/app/infrastructure/models/types.py                              21      0   100%
backend/app/infrastructure/models/user.py                               23      1    96%   38
backend/app/infrastructure/repositories/__init__.py                      6      0   100%
backend/app/infrastructure/repositories/admin_repository.py             61      2    97%   68, 82
backend/app/infrastructure/repositories/ai_repository.py                37      0   100%
backend/app/infrastructure/repositories/branch_repository.py            23      4    83%   28-29, 32-33
backend/app/infrastructure/repositories/comment_repository.py           19      2    89%   37-41
backend/app/infrastructure/repositories/directory_repository.py         66     40    39%   13, 16-19, 22, 29, 32, 35-40, 43-46, 49-51, 54-57, 62-68, 73-79, 86, 89, 92-97, 100-103, 106-108, 111-114, 119-125
backend/app/infrastructure/repositories/event_repository.py             36      1    97%   30
backend/app/infrastructure/repositories/family_repository.py            32     10    69%   28-29, 32-33, 36-39, 42-45, 48-51
backend/app/infrastructure/repositories/heritage_repository.py          61     46    25%   12, 15, 25-32, 46-65, 68-72, 75-78, 81-83, 86-87, 92-95, 100-108
backend/app/infrastructure/repositories/member_repository.py            23      5    78%   14, 28-29, 32-33
backend/app/infrastructure/repositories/post_repository.py              34      3    91%   79, 82, 85
backend/app/infrastructure/repositories/reaction_repository.py          20      0   100%
backend/app/infrastructure/repositories/relationship_repository.py      23      5    78%   14, 31-32, 35-36
backend/app/infrastructure/repositories/rsvp_repository.py              24      0   100%
backend/app/infrastructure/repositories/sqlalchemy_unit_of_work.py       9      3    67%   8, 11, 14
backend/app/infrastructure/repositories/user_repository.py              39      2    95%   35-36
backend/app/infrastructure/services/__init__.py                          0      0   100%
backend/app/main.py                                                      7      7     0%   1-15
backend/app/schemas/__init__.py                                          0      0   100%
backend/app/schemas/auth.py                                             18      0   100%
backend/app/services/__init__.py                                         0      0   100%
backend/app/services/admin_service.py                                   53      5    91%   47, 57, 61, 63, 67
backend/app/services/ai_service.py                                      99     39    61%   35-46, 54-63, 120-153, 210-211
backend/app/services/auth_service.py                                    54      1    98%   43
backend/app/services/community_service.py                               83      1    99%   170
backend/app/services/directory_service.py                              128    103    20%   25-28, 44-55, 92-123, 146-151, 178-203, 215-218, 234-259, 271-274, 279-286, 290, 294, 298, 305
backend/app/services/event_service.py                                   46      0   100%
backend/app/services/family_service.py                                 120     19    84%   23, 34, 37-43, 52, 64, 96, 107, 118, 126-130
backend/app/services/heritage_service.py                                48     29    40%   17-18, 35-41, 63, 66-69, 72-76, 79-80, 95, 100, 112-115, 125, 130-133
backend/app_logging.py                                                  22      0   100%
backend/config.py                                                       18      0   100%
backend/cors.py                                                          0      0   100%
backend/create_app.py                                                   31      5    84%   8-10, 65, 70
backend/database.py                                                      4      1    75%   9
backend/dependency_container.py                                          0      0   100%
backend/error_handler.py                                                 0      0   100%
backend/main.py                                                         10      5    50%   8-10, 18-19
backend/migrations/__init__.py                                           0      0   100%
backend/migrations/env.py                                               36     36     0%   2-87
backend/run.py                                                          10     10     0%   2-16
backend/start.py                                                         8      8     0%   2-11
backend/tests/__init__.py                                                0      0   100%
backend/tests/conftest.py                                               45     23    49%   21-24, 32-38, 42-49, 53-59
backend/tests/fakes/__init__.py                                          0      0   100%
backend/tests/fakes/family_repositories.py                              73     10    86%   14, 28, 31, 34, 52-53, 56, 86, 100, 112
backend/tests/test_auth.py                                              37     37     0%   1-73
backend/tests/test_community.py                                        146    146     0%   14-237
backend/tests/test_event.py                                            132    132     0%   13-225
backend/tests/test_family.py                                            38     38     0%   1-58
backend/tests/unit/__init__.py                                           0      0   100%
backend/tests/unit/domain/test_domain_utils.py                          62      0   100%
backend/tests/unit/repositories/test_ai_repository.py                   84      0   100%
backend/tests/unit/repositories/test_community_event_repos.py          231      0   100%
backend/tests/unit/repositories/test_repositories.py                   218      0   100%
backend/tests/unit/repositories/test_rsvp_repository.py                 64      0   100%
backend/tests/unit/services/__init__.py                                  0      0   100%
backend/tests/unit/services/test_ai_service.py                         119      0   100%
backend/tests/unit/services/test_auth_admin_service.py                 263      0   100%
backend/tests/unit/services/test_community_service.py                  166      0   100%
backend/tests/unit/services/test_event_service.py                      132      0   100%
backend/tests/unit/services/test_family_service.py                     122      3    98%   24, 27, 33
--------------------------------------------------------------------------------------------------
TOTAL                                                                 4446   1186    73%
======================= 160 passed, 11 warnings in 0.39s =======================
