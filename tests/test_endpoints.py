import pytest


@pytest.mark.asyncio
async def test_signup_and_unregister_flow(async_client):
    # Arrange: choose an activity and a test email
    activity = "Chess Club"
    email = "test.student@mergington.edu"

    # Ensure email is not already in participants (pre-cleanup)
    # Act: sign up
    resp_signup = await async_client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert: signup successful
    assert resp_signup.status_code == 200
    assert "Signed up" in resp_signup.json().get("message", "")

    # Act: try signing up again (should fail)
    resp_duplicate = await async_client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert: duplicate signup returns 400
    assert resp_duplicate.status_code == 400

    # Act: unregister
    resp_unreg = await async_client.delete(f"/activities/{activity}/unregister", params={"email": email})
    # Assert: unregister successful
    assert resp_unreg.status_code == 200
    assert "Unregistered" in resp_unreg.json().get("message", "")

    # Act: unregister again (should fail)
    resp_unreg_again = await async_client.delete(f"/activities/{activity}/unregister", params={"email": email})
    # Assert: unregistering non-signed student returns 400
    assert resp_unreg_again.status_code == 400


@pytest.mark.asyncio
async def test_signup_unknown_activity(async_client):
    # Arrange
    activity = "Nonexistent Club"
    email = "no.one@mergington.edu"

    # Act
    resp = await async_client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 404
