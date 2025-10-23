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

### Vulnerability

The `greeter.py` script contains a command injection vulnerability. It uses `os.system()` to execute a command that includes unsanitized user input. A malicious user could provide input like `&& rm -rf /` to execute arbitrary commands on the system.

### Files

*   `greeter.py`: The vulnerable Python script.
*   `test_greeter.py`: A "happy path" test for the script.

### How to Run the Test

To run the test, navigate to the `python-command-injection` directory and run:

```bash
python3 -m unittest test_greeter.py
```

### How to Exploit

1.  Navigate to the `python-command-injection` directory.
2.  Run the `greeter.py` script with a malicious payload. For example, to execute the `whoami` command, you can run:

    ```bash
    python3 greeter.py "; whoami"
    ```
3.  You will see the output of the `whoami` command, which is your username.

---

## Demo 2: JavaScript XSS (Cross-Site Scripting)

*   **Folder:** `javascript-xss`

### Vulnerability

The `index.html` file demonstrates a cross-site scripting (XSS) vulnerability. It uses Vue.js with the `v-html` directive to render user input directly into the DOM. A malicious user could inject script tags (`<script>alert('XSS!')</script>`) to execute arbitrary JavaScript in the user's browser.

### Files

*   `index.html`: The vulnerable HTML file.
*   `test_xss_structure.py`: A test that checks the structure of the HTML file.

### How to See the Exploit

1.  Open the `index.html` file in a web browser.
2.  In the input field, type the following and press Enter:

    ```html
    <script>alert('XSS!')</script>
    ```
3.  You will see an alert box pop up, demonstrating that the injected script was executed.

---

## Demo 3: Terraform Insecure Google Cloud Storage

*   **Folder:** `terraform-gcs-insecure-bucket`

### Vulnerability

The `main.tf` file defines a Google Cloud Storage bucket with a public-read ACL. The `iam_member` resource grants `roles/storage.objectViewer` to `allUsers`, making all objects in the bucket publicly accessible. This is a common misconfiguration that can lead to data breaches.

### Files

*   `main.tf`: The insecure Terraform configuration.
*   `test_terraform_validation.py`: A test that validates the insecure configuration (requires Terraform to be installed).

### How to Run

To run the validation test (assuming you have Terraform installed and configured), navigate to the `terraform-gcs-insecure-bucket` directory and run:

```bash
python3 -m unittest test_terraform_validation.py
```
