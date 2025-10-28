module "gh-stack-minimal-test" {
  source = "./../../"

  stack_name       = "mtest-${random_pet.pet_name.id}"
  db_use_shared    = true
  redis_use_shared = true # turn off redis, which is slow to create

  db_shared_target_instance = "goodhuman-infra"
  db_shared_target_project  = "goodhuman-infra"

  db_source_database = "goodhuman-test1"

}

module "gh-stack-itest" {
  source = "./../../"

  stack_name    = "gh-it-${random_pet.pet_name.id}"
  db_use_shared = true

  db_shared_target_instance = "goodhuman-infra"
  db_shared_target_project  = "goodhuman-infra"

  db_do_not_import = true

}

module "gh-stack-itest-w-db" {
  source = "./../../"

  stack_name = "gh-dbt-${random_pet.db_pet_name.id}"

  # should stand up a database too, and pubsub queues
  db_use_shared        = false
  db_add_replica       = true
  create_pubsub_queues = true
}

resource "random_pet" "pet_name" {

}

resource "random_pet" "db_pet_name" {

}

# pass on our outputs
output "firebase_project_id" {
  value = module.gh-stack-minimal-test.firebase_project_id
}

output "database_ip_address" {
  value = "placeholder"
}

output "stack_created_as" {
  value = module.gh-stack-minimal-test.stack_created_as
}