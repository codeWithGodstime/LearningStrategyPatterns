import pytest
from core.tests.factories import program_factory
from rest_framework.test import APIClient

@pytest.fixture
def program() -> program_factory.ProgramFactory:
    return program_factory.ProgramFactory


@pytest.fixture
def client() -> APIClient:
    return APIClient()