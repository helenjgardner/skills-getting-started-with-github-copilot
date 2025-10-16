import pytest


def test_signup_duplicate(client):
    name = 'Chess Club'
    # pick an existing participant from the seeded data
    activities = client.get('/activities').json()
    existing = activities[name]['participants'][0]

    resp = client.post(f"/activities/{name}/signup?email={existing}")
    assert resp.status_code == 400
    assert 'already signed up' in resp.json().get('detail', '') or 'already signed up' in resp.json().get('message', '')


def test_unregister_nonexistent(client):
    name = 'Chess Club'
    email = 'i-dont-exist@example.com'
    resp = client.delete(f"/activities/{name}/unregister?email={email}")
    assert resp.status_code == 404
    assert 'Participant not found in activity' in resp.json().get('detail', '')
