from config import Settings
from main import app


def test_settings_load_expected_defaults():
    settings = Settings(_env_file=None)

    assert settings.app_name == "FamilyConnect API"
    assert settings.jwt_algorithm == "HS256"
    assert settings.ai_provider == "mock"


def test_health_route_is_registered():
    paths = {
        nested_route.path
        for route in app.routes
        for nested_route in getattr(
            getattr(route, "original_router", route), "routes", []
        )
        if getattr(nested_route, "path", None)
    }

    assert "/health" in paths