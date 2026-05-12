from app.infrastructure.tasks.celery_app import celery_app


def test_celery_uses_json_serialization() -> None:
    assert celery_app.conf.task_serializer == "json"
    assert celery_app.conf.result_serializer == "json"
    assert celery_app.conf.accept_content == ["json"]


def test_celery_uses_expected_timezone() -> None:
    assert celery_app.conf.timezone == "Asia/Kolkata"
    assert celery_app.conf.enable_utc is True
