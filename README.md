# Security Vulnerability Demos

This project contains three demonstrations of common security vulnerabilities, created with the help of the Gemini CLI.

## Dependencies

To run these demos, you will need the following dependencies installed:

*   **Gemini CLI:** For interacting with the Gemini large language model.
*   **Python 3:** For running the Python scripts and tests.
*   **Terraform:** For the insecure Google Cloud Storage demo.

---

## Demo 1: Python Command Injection

*   **Folder:** `python-command-injection`

### Vulnerability (Fixed)

The `greeter.py` script previously contained a command injection vulnerability due to the use of `os.system()` with unsanitized user input. This has been fixed by using `subprocess.run()` with a list of arguments, which prevents the shell from interpreting malicious input.

### Files

*   `greeter.py`: The fixed Python script.
*   `test_greeter.py`: A "happy path" test for the script.

### How to Run the Test

To run the test, navigate to the `python-command-injection` directory and run:

```bash
python3 -m unittest test_greeter.py
```

---

## Demo 2: JavaScript XSS (Cross-Site Scripting)

*   **Folder:** `javascript-xss`

### Vulnerability (Fixed)

The `index.html` file previously demonstrated a cross-site scripting (XSS) vulnerability due to the use of `v-html` with untrusted user input. This has been fixed by using `v-text` instead of `v-html`, which treats user input as plain text and escapes any HTML entities, preventing script execution.

### Files

*   `index.html`: The fixed HTML file.
*   `test_xss_structure.py`: A test that checks the structure of the HTML file.

### How to Run the Test

To run the test, navigate to the `javascript-xss` directory and run:

```bash
python3 -m unittest test_xss_structure.py
```

---

## Demo 3: Terraform Insecure Google Cloud Storage

*   **Folder:** `terraform-gcs-insecure-bucket`

### Vulnerability (Fixed)

The `main.tf` file previously defined a Google Cloud Storage bucket with a public-read ACL. This has been fixed by removing the `iam_member` resource that granted public access and enabling `uniform_bucket_level_access`.

To grant specific access to the bucket, the `google_storage_bucket_iam_binding` resource is used. This allows you to bind a role (like `roles/storage.objectViewer`) to specific members (like `user:jane@example.com`).

### Files

*   `main.tf`: The secure Terraform configuration.
*   `test_terraform_validation.py`: A test that validates the secure configuration (requires Terraform to be installed).

### How to Run

To run the validation test (assuming you have Terraform installed and configured), navigate to the `terraform-gcs-insecure-bucket` directory and run:

```bash
python3 -m unittest test_terraform_validation.py
```
