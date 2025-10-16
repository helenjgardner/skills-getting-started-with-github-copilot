def test_get_activities(client):
    resp = client.get('/activities')
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    # Expect some example activities present
    assert 'Chess Club' in data


def test_signup_and_unregister_flow(client):
    name = 'Programming Class'
    email = 'pytest_student@mergington.edu'

    # ensure clean state
    activities = client.get('/activities').json()
    if email in activities[name]['participants']:
        # try to remove if present
        client.delete(f"/activities/{name}/unregister?email={email}")

    # Sign up
    resp = client.post(f"/activities/{name}/signup?email={email}")
    assert resp.status_code == 200
    assert 'Signed up' in resp.json().get('message', '')

    # Unregister
    resp2 = client.delete(f"/activities/{name}/unregister?email={email}")
    assert resp2.status_code == 200
    assert 'Unregistered' in resp2.json().get('message', '')
