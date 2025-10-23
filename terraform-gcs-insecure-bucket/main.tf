provider "google" {
  project = "your-gcp-project-id"
}

resource "google_storage_bucket" "insecure_bucket" {
  name          = "my-insecure-bucket-12345" # Replace with a unique name
  location      = "US"
  project       = "your-gcp-project-id"

  uniform_bucket_level_access = false

  versioning {
    enabled = false
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 365
    }
  }

  # Insecure configuration: granting public access
  iam_member {
    role   = "roles/storage.objectViewer"
    member = "allUsers"
  }
}
