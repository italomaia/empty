# coding:utf-8

import os
import sys

CURRENT_PATH = os.path.abspath(os.path.dirname('.'))
TEST_APP = os.path.join(CURRENT_PATH, 'tests/test_app')


def test_load_model_loads_correct_model():
    sys.path.insert(0, TEST_APP)
    from blueprint.models import SomeModel
    from empty.loading import load_model
    model = load_model('blueprint.SomeModel')
    assert model is not None
    assert model == SomeModel


def test_load_schema_loads_correct_schema():
    sys.path.insert(0, TEST_APP)
    from blueprint.schemas import SomeModelSchema
    from empty.loading import load_schema
    schema = load_schema('blueprint.SomeModel')
    assert schema is not None
    assert schema == SomeModelSchema


def test_load_blueprint_instance():
    sys.path.insert(0, TEST_APP)
    from blueprint.views import app
    from empty.loading import load_blueprint
    bp = load_blueprint('blueprint')
    assert bp == app
