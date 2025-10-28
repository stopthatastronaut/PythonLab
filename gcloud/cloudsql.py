import firebase_admin
import google.cloud
import pytest
import os
from firebase_admin import auth
from firebase_admin import credentials
import shlex
import subprocess
import json

targetproject = "goodhuman-prod"
targetinstance = "goodhuman-production"

def get_sql_databases():
  dblist = subprocess.run(
      [
        "gcloud", "sql", "databases", "list", 
        "--instance=" + targetinstance, 
        "--project=" + targetproject,
        "--format=json"
      ]
    )
  # now check dblist for the params we want
  print(dblist)

def get_sql_instance():
  # gcloud sql instances list --project goodhuman-prod --format json
  instancelist = subprocess.run(
    [
      "gcloud", "sql", "instances", "list",
      "--project", targetproject,
        "--format=json"
    ], capture_output=True
  )
  # open it in json
  if instancelist.returncode == 0:
    instances = json.loads(instancelist.stdout)
    for i in instances:
      print("==============")
      print(i["connectionName"])
      print(i["gceZone"])
      print(i["region"])
  else:
    print(instancelist.stderr)
    



get_sql_instance()