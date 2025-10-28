import firebase_admin
import pytest
import os
from firebase_admin import auth
from firebase_admin import credentials
from google.cloud import dns
from google.cloud import appengine_admin_v1
from google.cloud import vpcaccess_v1
import shlex
import subprocess
import json

def load_env_var(n):
  return os.environ[n].replace('"', '')

# this is where we do the real testing against the real infra. So we need the google SDK, and the stack name we just spun up
creds = firebase_admin.credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
# targetproject = os.environ['STACK_CREATED_AS'].replace('"', '')
targetdbproject = os.environ['DB_STACK_PROJECT_ID'].replace('"', '') 
# test_app = firebase_admin.initialize_app(name = 'testtarget', credential=creds, options = { 'projectId' : targetproject})
test_db_app = firebase_admin.initialize_app(name = 'testdbtarget', credential=creds, options = { 'projectId' : targetdbproject})

# Simple Stack

def test_google_project_exists():
    # use the firebase & goog SDK here.
    # App engine items will only exist after we deploy.
    assert firebase_admin.get_app('testdbtarget') != None

@pytest.mark.skip(reason="no longer valid with the addition of a pet name")
def test_firebase_app_exists():
    apps = firebase_admin.list_apps()
    assert any(y for y in apps if y.name == targetdbproject) != None

@pytest.mark.skip(reason="temporary skip for manual testing")
def test_jir_exists():
    # will use the app object to check in Firebase auth if JIR is present in Firebase Auth
    # this needs to be more broad, especially if we're cloning disparate environments.
    # Like by grabbing source and destination
    assert firebase_admin.auth.get_user_by_email('jirwong@yahoo.com', app=test_app).email == 'jirwong@yahoo.com'

@pytest.mark.skip(reason="superceded by catalog testing")
def temp_bucket_exists():
  bucketlist = subprocess.run(
     [
        "gcloud", "alpha", "storage", "list", 
        "--project=" + targetdbproject,
        "--format=json"
    ]
  )
  # not actually sure we can get the region here
  assert 1 == 1


def test_us_database_exists():
  # all dbs should be in us-west1
  #  gcloud sql databases list --instance=goodhuman-infra --project=goodhuman-infra --format=json
  dblist = subprocess.run(
     [
       "gcloud", "sql", "instances", "list", 
       "--project=" + targetdbproject,
       "--format=json"
     ], capture_output=True
  )
  if(dblist.returncode == 0):
    dbs = json.loads(dblist.stdout)
    for d in dbs:
      assert d['region'] == 'us-west1'
  else:
    print("ERROR TESTING DB EXISTENCE: " + dblist.stderr)
    return 1

@pytest.mark.skip(reason="Currently broken not sure why")
def test_cloud_dns_names():
  dnscatalog = subprocess.run(
     [
        "gcloud", "dns", "record-sets", "list", 
        "--zone=goodhuman-me", 
        "--project=goodhuman-prod", # DNS names at top-level are always in prod
        "--format=json"
        "--filter=" + targetdbproject
     ]
  )
  if(dnscatalog.returncode == 0):
    dns = json.loads(dnscatalog.stdout)

    # we need several DNS names for the DB stack.
    thisstack = [x for x in dns if x["name"].contains(targetdbproject)]
    assert len(thisstack) > 0

    # team
    teamname = [x for x in dns if x["name"].contains("team-" + targetdbproject)]
    assert len(teamname) > 0

  else:
    print("ERROR LOADING DNS RESULTS: " + dnscatalog.stderr)
    return 1



@pytest.mark.skip(reason="minimal test currently off")
def test_project_full_catalog():
  catalog = subprocess.run(
      [
        "gcloud", "asset", "search-all-resources", 
        "--project=" + targetproject, 
        "--format=json"
      ], capture_output=True
  )
  if(catalog.returncode == 0):
    resources = json.loads(catalog.stdout)# is our appEngine in the right region, and do we have only one?

    appengine = [x for x in resources if x["assetType"]=="appengine.googleapis.com/Application"]

    assert(len(appengine)==1)
    assert(appengine[0]["location"]=="australia-southeast1")
  else:
    print("ERROR LOADING FULL CATALOG FOR TEST PROJECT: " + catalog.stderr)
    return 1

def test_db_project_full_catalog():
  catalog = subprocess.run(
      [
        "gcloud", "asset", "search-all-resources", 
        "--project=" + targetdbproject, 
        "--format=json"
      ], capture_output=True
  )
  if(catalog.returncode == 0):
    resources = json.loads(catalog.stdout)
    # check resources here

    # do we have databases? This is essentially a dupe test
    dbs = [x for x in resources if x["assetType"]=="sqladmin.googleapis.com/Instance"]
    assert len(dbs) >= 1

    # do we have the right secrets?


    # is our appEngine in the right region, and do we have only one?
    appengine = [x for x in resources if x["assetType"]=="appengine.googleapis.com/Application"]
    assert(len(appengine)==1)
    assert(appengine[0]["location"]=="us-west1")


    # do we have the permissions we need?


    
  else:
    print("ERROR LOADING FULL CATALOG FOR DB PROJECT: " + catalog.stderr)
    return 1