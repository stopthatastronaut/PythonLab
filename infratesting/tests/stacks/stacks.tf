resource "random_pet" "pet_name" {

}

resource "random_pet" "db_pet_name" {

}

module "gh-stack-itest" {
  source = "./../../"

  stack_name    = "gh-it-${random_pet.pet_name.id}"
  db_use_shared = true

  db_shared_target_instance = "goodhuman-infra"
  db_shared_target_project  = "goodhuman-infra"

  db_do_not_import = true

}

/*
module "gh-stack-itest-w-db" {
  source = "./../../"

  stack_name = "gh-dbt-${random_pet.db_pet_name.id}"

  # should stand up a database too, and pubsub queues (turned off 18 Jul 2024 JB)
  db_use_shared        = false

  db_add_replica       = false
  create_pubsub_queues = false

  db_do_not_import = true

}
*/

output "FIREBASE_PROJECT_ID" {
  value = module.gh-stack-itest.firebase_project_id
}

/*
output "FIREBASE_PROJECT_ID_DBTEST" {
  value = module.gh-stack-itest-w-db.firebase_project_id
}
*/
