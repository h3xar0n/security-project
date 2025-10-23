import unittest
import subprocess
import os
import json

class TestTerraformValidation(unittest.TestCase):

    def test_gcs_bucket_is_public(self):
        # This test assumes Terraform is installed and configured.
        # It is for demonstration purposes only and will not be run.

        # Ensure we are in the correct directory
        terraform_dir = os.path.join(os.path.dirname(__file__))
        os.chdir(terraform_dir)

        # Initialize Terraform
        subprocess.run(["terraform", "init"], check=True)

        # Create a plan
        plan_path = "tfplan"
        subprocess.run(["terraform", "plan", "-out", plan_path], check=True)

        # Convert the plan to JSON
        show_result = subprocess.run(["terraform", "show", "-json", plan_path], capture_output=True, text=True, check=True)
        plan_json = json.loads(show_result.stdout)

        # Find the bucket resource and check for public access
        found_public_binding = False
        for resource in plan_json.get("resource_changes", []):
            if resource["type"] == "google_storage_bucket_iam_member" and resource["name"] == "insecure_bucket-public-access":
                if resource["change"]["after"]["member"] == "allUsers" and resource["change"]["after"]["role"] == "roles/storage.objectViewer":
                    found_public_binding = True
                    break
        
        self.assertTrue(found_public_binding, "The GCS bucket is not configured for public access.")

        # Clean up the plan file
        os.remove(plan_path)

        # Change back to the original directory
        os.chdir(os.path.dirname(os.path.dirname(__file__)))

if __name__ == "__main__":
    # This is for demonstration purposes only. Do not run directly without Terraform installed.
    print("This test is for demonstration purposes only and requires Terraform to be installed.")
    # unittest.main()
