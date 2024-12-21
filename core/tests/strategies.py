from abc import abstractmethod, ABC
from rest_framework.test import APIClient


class TestStrategy(ABC):

    @abstractmethod
    def arrange(self, client: APIClient, url:str, data: dict):
        pass

    @abstractmethod
    def act(self):
        pass

    @abstractmethod
    def assert_(self, expected_response: dict):
        pass


class CreateStrategy(TestStrategy):
    def arrange(self, client, url, data):
        self.client = client
        self.url = url
        self.data = data
    
    def act(self):
        self.response = self.client.post(self.url, data=self.data, format="json")
    
    def assert_(self, expected_response=None):
        assert self.response.status_code == 201

class BadRequestStrategy(TestStrategy):
    def arrange(self, client, url):
        self.client = client
        self.url = url
        self.data = {}
    
    def act(self):
        self.response = self.client.post(self.url, data=self.data, format="json")
    
    def assert_(self, expected_response=None):
        assert self.response.status_code == 400

    