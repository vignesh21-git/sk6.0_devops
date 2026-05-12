import asyncio

from app.main import health


def test_health_returns_ok_payload() -> None:
    assert asyncio.run(health()) == {"status": "ok"}
