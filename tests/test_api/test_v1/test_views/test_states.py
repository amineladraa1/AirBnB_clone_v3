#!/usr/bin/python3
"""UnitTest for states module"""

from unittest import TestCase
from models.state import State
from models import storage
from api.v1.app import app
import json


class TestStates(TestCase):
    """Test Class for app"""

    def setUp(self):
        """setup app"""
        self.app = app.test_client()

    def test_states_get(self):
        """Test index status endpoint"""
        response = self.app.get('http://0.0.0.0:5000/api/v1/states')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.get_json(), list))

    def test_states_get_id(self):
        """Test index states endpoint"""
        s = State(name="California")
        s.save()
        response = self.app.get('http://0.0.0.0:5000/api/\
v1/states/{}'.format(s.id))
        self.assertEqual(response.status_code, 200)
        json_dc = response.get_json()
        self.assertEqual(json_dc, s.to_dict())
        self.assertEqual(json_dc['id'], s.id)
        self.assertEqual(json_dc['name'], 'California')
        response2 = self.app.get('http:\
//0.0.0.0:5000/api/v1/states/{}'.format(343462))
        self.assertEqual(response2.json, {"error": "Not found"})

    def test_states_post(self):
        """Test index states endpoint"""
        contentype = 'application/json'
        data = "name NewYork"
        url = 'http:/0.0.0.0:5000/api/v1/states'
        response01 = self.app.post(url, data=json.dumps(data),
                                  content_type=contentype)
        self.assertEqual(response01.status_code, 400)
        data = {"game": "NewYork"}
        response02 =\
            self.app.post(url, data=json.dumps(data), content_type=contentype)
        self.assertEqual(response02 .status_code, 400)
        s = State()
        data = {"name": "NewYork"}

        response =\
            self.app.post(url, data=json.dumps(data), content_type=contentype)
        self.assertEqual(response.status_code, 201)

    def test_states_delete(self):
        """Test index states endpoint"""
        response2 = self.app.delete('http\
://0.0.0.0:5000/api/v1/states/{}'.format(343462))
        self.assertEqual(response2.json, {"error": "Not found"})
        s = State(name="New Mexico")
        s.save()
        response = self.app.get('http:\
//0.0.0.0:5000/api/v1/states/{}'.format(s.id))
        self.assertEqual(response.status_code, 200)

    def test_states_put(self):
        """Test index states endpoint"""
        response2 = self.app.delete('http\
://0.0.0.0:5000/api/v1/states/{}'.format(343462))
        self.assertEqual(response2.json, {"error": "Not found"})
        s = State()
        s.save()
        url = 'http:/0.0.0.0:5000/api/v1/states/{}'.format(s.id)
        data = 1
        response1 = self.app.put(url, data=json.dumps(data),
                                 content_type='application/json')
        self.assertEqual(response1.status_code, 400)
        self.assertEqual(response.json, {"message": "Not a JSON"})
        s = State()
        s.save()
        updated_data = {"name": "Benguerir"}
        response =\
            self.app.put('http:/0.0.0.0:5000/api/v1/states/{}'.format(s.id),
                         data=json.dumps(updated_data),
                         content_type='application/json')
        self.assertEqual(response.status_code, 200)
