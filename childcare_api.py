from utils import clean_fields
import requests
import json


class ChildcareAPI():
    def __init__(self, db, url):
        self.db = db
        self.url = url

    def add_all(self):
        d = json.loads(requests.get(self.url).content)
        for p in d['providers']:
            fields = clean_fields({
                'name': p['provider_name'],
                'id': p['id'],
                'phone': p['phone'],
                'email': p['email'],
                'owner': p['owner_name'],
            })
            self.db.add_provider(fields=fields)
        return self
