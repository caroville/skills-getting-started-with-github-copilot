import pytest
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport

from src.app import app

# Ensure pytest recognizes asyncio fixtures (helps with plugin discovery)
pytest_plugins = "pytest_asyncio"


@pytest.fixture
async def async_client():
    """Fixture that yields an `httpx.AsyncClient` for the FastAPI app.

    Uses `AsyncClient(app=app, base_url="http://test")` so tests can call
    endpoints directly without an external server.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
