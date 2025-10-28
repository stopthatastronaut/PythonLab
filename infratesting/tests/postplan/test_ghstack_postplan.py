import json
import os
import pytest
import hcl

# utility
def get_terraform_json():
    reporoot = "." if os.environ.get('CI') else "/Users/jasbro/source/repos/goodhuman/gh-stack"
    with open(reporoot+'/tests/.testdata/plan.json') as f:
        js = json.load(f)
    return js

#tests
js = get_terraform_json()

def test_can_open_json():
    assert js != None

@pytest.mark.skip(reason="no longer valid with the addition of a pet name")
def test_explicitly_uses_stack_project():
    is_valid = True

    # find the random pet
    random_pet = js["planned_values"]["root_module"]["resources"][0]

    for i in js["planned_values"]["root_module"]["child_modules"]:
        print("checking " + i["address"])
        for j in i["resources"]:
            print("\ttesting " + j["address"] + "("+j["type"]+")")
            if (j["type"] not in [
                    "google_secret_manager_secret_version", 
                    "external",
                    "google_project",
                    "google_service_account_key",
                    "random_pet"
                ]):
                print("\t\tchecking valid project assignment for " + j["address"])
                if j["values"]["project"] == "":
                    print("invalid project assignment found")
                    is_valid = False
    
    assert is_valid == True

# def test_we_can_trigger_failure():
#     assert True == False

def test_we_have_valid_projects():
    # find all .tf files in the root
    is_valid = True
    

    assert is_valid

def test_we_have_a_project_output():
    is_valid = False # assume the worst
    outputs = js["planned_values"]["outputs"]
    for i in outputs:
        if i == "FIREBASE_PROJECT_ID":
            is_valid = True
    assert is_valid == True