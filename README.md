# My awesome DevSecOps Application

## 🛡️ Python Security Scan Setup (with Bandit, Safety, Checkov)

Follow the steps below to set up a secure Python environment and scan your code and dependencies:

# Bandit 

```bash
# Step 1: Create a virtual environment named 'venv' and activate it
python3 -m venv venv && source venv/bin/activate
```

```bash
# Step 2: Install Bandit for static code analysis
pip install bandit
```

```bash
# Step 3: Scan your codebase (e.g., vulnerable_app.py) with Bandit
bandit -r vulnerable_app.py
```

# Safety

```bash
# Step 1: Use Safety (via Docker) to check your dependencies in requirements.txt for known vulnerabilities
docker run --rm -v "$(pwd)"/requirements.txt:/tmp/requirements.txt ghcr.io/pyupio/safety:latest safety check -r /tmp/requirements.txt
```

# Checkov

```bash
# Step 1: Install Checkov to scan Terraform configurations
pip install checkov
```
```bash

# Step 2: Use Checkov to scan your Terraform file (e.g., bad_s3_bucket.tf)
checkov -f bad_s3_bucket.tf
```


![Image 1: Bandit vulnerabilities scan](https://github.com/user-attachments/assets/b00f7b6a-6aa4-4c2e-bac0-244754479d82)

![Image 2: Bandit vulnerabilities scan](https://github.com/user-attachments/assets/f8a0a603-1b2a-435e-bcfe-737eb1e33065)

![image 3: Bandit vulnerabilities scan](https://github.com/user-attachments/assets/9d92d372-8311-41ce-ba1a-0daa3a62f997)

![image 4: Safety Vulnerability report](https://github.com/user-attachments/assets/ebdf3841-59ce-4005-821e-8d170789a25d)

![image 5: Safety vulnerability report](https://github.com/user-attachments/assets/5b459053-94d1-4135-b1df-e3305d0fa2fd)

![image 6: Safety vulnerability report](https://github.com/user-attachments/assets/391ff3f5-f6d2-481b-9463-42323a5b0bc7)

![image 7: Checkov vulnerability scan](https://github.com/user-attachments/assets/b8351160-4b64-432c-a7bc-88f43095754f)

![image 8: Checkov vulnerability scan](https://github.com/user-attachments/assets/d49e133a-d2d1-458c-8149-8057261e3edd)

![image 9: Checkov vulnerability scan](https://github.com/user-attachments/assets/427604b5-0f5d-43b8-9018-e185cf4d962d)

