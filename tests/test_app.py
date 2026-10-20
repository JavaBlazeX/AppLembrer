import pytest
from app import create_app

@pytest.fixture
def client(tmp_path):
    app = create_app({'TESTING': True, 'DATABASE': str(tmp_path / 'test.sqlite3')})
    return app.test_client()

def sample():
    return {'title':'Estudar Python','description':'Revisar Flask','category':'Estudos','due_at':'2026-11-02T14:30','repeat_rule':'none'}

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'AppLembrer' in response.data

def test_create_list_update_complete_delete(client):
    created = client.post('/api/reminders',json=sample())
    assert created.status_code == 201
    item_id=created.json['id']
    assert len(client.get('/api/reminders').json)==1
    changed=sample()|{'title':'Estudar testes'}
    assert client.put(f'/api/reminders/{item_id}',json=changed).json['title']=='Estudar testes'
    assert client.patch(f'/api/reminders/{item_id}/complete',json={'completed':True}).json['completed']==1
    assert client.delete(f'/api/reminders/{item_id}').status_code==204
    assert client.get('/api/reminders').json==[]

def test_validation(client):
    assert client.post('/api/reminders',json=sample()|{'title':''}).status_code==400
    assert client.post('/api/reminders',json=sample()|{'due_at':'invalid'}).status_code==400
    assert client.post('/api/reminders',json=sample()|{'category':'unknown'}).status_code==400
    assert client.patch('/api/reminders/999/complete',json={'completed':'yes'}).status_code==400
    assert client.delete('/api/reminders/999').status_code==404
