provider "google" {
  project = "your-gcp-project-id"
}

resource "google_storage_bucket" "secure_bucket" {
  name          = "my-secure-bucket-12345" # Replace with a unique name
  location      = "US"
  project       = "your-gcp-project-id"

  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 365
    }
  }
}

# To grant access to the bucket, you can use the google_storage_bucket_iam_binding resource.
# This example grants the storage.objectViewer role to a specific user.
resource "google_storage_bucket_iam_binding" "binding" {
  bucket = google_storage_bucket.secure_bucket.name
  role   = "roles/storage.objectViewer"
  members = [
    "user:jane@example.com",
  ]
}
