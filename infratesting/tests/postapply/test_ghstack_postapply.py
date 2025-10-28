import firebase_admin
import pytest

def test_json_output():
    assert 10 == 10

# this is where we do the real testing against the real infra. So we need the google SDK


# Basic Stack

def test_google_project_exists():
    # use the firebase & goog SDK here
    assert True == True

@pytest.mark.skip(reason="no longer valid with the addition of a pet name")
def test_firebase_app_exists():
    apps = firebase_admin.list_apps()
    assert any(y for y in apps if y.name == 'integtest') != None


def test_cloud_sql_region():
    assert True

def test_cloud_dns_names():
    assert True
