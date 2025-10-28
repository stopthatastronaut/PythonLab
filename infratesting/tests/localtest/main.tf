terraform {
  backend "gcs" {
    bucket = "goodhuman-terraform"
    prefix = "terraform/gh-stack/localtest/state"
  }

  required_providers {
    google = {
      # requires a keyfile referenced in GOOGLE_APPLICATION_CREDENTIALS
      source  = "hashicorp/google"
      version = "4.85.0"
    }

    random = {
      source  = "hashicorp/random"
      version = "3.3.2"
    }

    github = {
      source  = "integrations/github"
      version = ">=5.16.0"
    }
  }
}

provider "google" {
  project = "goodhuman-stack"
}

provider "github" {
  owner = "goodhuman-me"
}

provider "google" { # test1, from where we clone some settings
  project = "goodhuman-test1"
  alias   = "test1"
}

provider "google" { # the shared DB project
  project = "gh-test-76726"
  alias   = "shared"
}

provider "google" { # the infra store (for known-good secrets)
  project = "goodhuman-infra"
  alias   = "infra"
}
