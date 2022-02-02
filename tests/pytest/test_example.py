import json
import pytest


@pytest.mark.parametrize('postman_collection', ['../../tests/pytest/example.json'])
def test_postman_collection_info(postman_collection):
    with open(postman_collection) as f:
        change = json.load(f)
    rule = change['example']
    assert len(rule['title']) >= 0  , "JSON title should be defined"
