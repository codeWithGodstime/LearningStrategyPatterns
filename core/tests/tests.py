import pytest
from django.urls import reverse

from utilities.test_helper import TestDataHelper
from core.tests.strategies import CreateStrategy, BadRequestStrategy

pytestmark = pytest.mark.django_db


def test_program(program):
    s = TestDataHelper().get_data(program)
    print(s)

def test_create_program(client, program):
    data = TestDataHelper().get_data(program)

    t = CreateStrategy()
    t.arrange(client, reverse("programs-list"), data)
    t.act()
    t.assert_()

def test_bad_request_create_program(client, program):

    data = TestDataHelper().get_data(program)

    t = BadRequestStrategy()
    t.arrange(client, reverse("programs-list"))
    t.act()
    t.assert_()