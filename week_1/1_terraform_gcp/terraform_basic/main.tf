terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.13.0"
    }
  }
}

provider "google" {
  # Credentials only needs to be set if you do not have the GOOGLE_APPLICATION_CREDENTIALS set
  project = "fine-rookery-412515"
  region  = "EUROPE-WEST1"
}



resource "google_storage_bucket" "demo-bucket" {
  name     = "fine-rookery-412515-demo-bucket"
  location = "EU"

  # Optional, but recommended settings:
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30 // days
    }
  }

  force_destroy = true
}

resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id = "demo_dataset"
  project    = "fine-rookery-412515"
  location   = "EU"
}
