import pytest


@pytest.mark.asyncio
async def test_get_activities_status(async_client):
    # Arrange: the fixture `async_client` prepares the app client

    # Act: request the activities list
    response = await async_client.get("/activities")

    # Assert: status code and basic structure
    assert response.status_code == 200
    json_body = response.json()
    assert isinstance(json_body, dict)
    assert "Chess Club" in json_body
