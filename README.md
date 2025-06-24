# DevSecOps Application (concepts)

## 🔐 Tool Breakdown (Purpose & Category)

### 🕵️‍♂️ Bandit (SAST)
- **Purpose**: Analyzes Python source code to find common security issues such as hardcoded passwords or insecure function calls.
- **Category**: Static Application Security Testing (SAST)

### 🧪 Safety (SCA)
- **Purpose**: Checks Python dependencies for known vulnerabilities using a public CVE database.
- **Category**: Software Composition Analysis (SCA)

### 🧱 Checkov (SAST for IaC)
- **Purpose**: Scans Infrastructure-as-Code (e.g., Terraform, CloudFormation) to detect insecure configurations (e.g., open S3 buckets, unencrypted resources).
- **Category**: Static Analysis for Infrastructure-as-Code (SAST-IaC)

### 🔑 Gitleaks (Secrets Scanning)
- **Purpose**: Detects hardcoded secrets like API keys, tokens, or credentials that may have been committed to version control.
- **Category**: Secrets Detection / Static Security Scanning

### 🐳 Trivy (Container & SCA Scanning)
- **Purpose**: Scans Docker images for vulnerabilities in OS packages, libraries, and dependencies. It also performs configuration checks.
- **Category**: Container Security / Software Composition Analysis (SCA)

> 💡 **SAST** tools analyze source code or configuration without executing it.  
> **SCA** tools inspect third-party packages and dependencies for known vulnerabilities.  
> Secrets scanning identifies accidentally exposed sensitive data.

## 🛡️ Python Security Scan Setup (with Bandit, Safety, Checkov, Gitleak, Trixy)

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
![Image 1: Bandit vulnerabilities scan](https://github.com/user-attachments/assets/b00f7b6a-6aa4-4c2e-bac0-244754479d82)

![Image 2: Bandit vulnerabilities scan](https://github.com/user-attachments/assets/f8a0a603-1b2a-435e-bcfe-737eb1e33065)

![image 3: Bandit vulnerabilities scan](https://github.com/user-attachments/assets/9d92d372-8311-41ce-ba1a-0daa3a62f997)

# Safety

```bash
# Step 1: Use Safety (via Docker) to check your dependencies in requirements.txt for known vulnerabilities
docker run --rm -v "$(pwd)"/requirements.txt:/tmp/requirements.txt ghcr.io/pyupio/safety:latest safety check -r /tmp/requirements.txt
```
![image 4: Safety Vulnerability report](https://github.com/user-attachments/assets/ebdf3841-59ce-4005-821e-8d170789a25d)

![image 5: Safety vulnerability report](https://github.com/user-attachments/assets/5b459053-94d1-4135-b1df-e3305d0fa2fd)

![image 6: Safety vulnerability report](https://github.com/user-attachments/assets/391ff3f5-f6d2-481b-9463-42323a5b0bc7)

# Checkov

```bash
# Step 1: Install Checkov to scan Terraform configurations
pip install checkov
```
```bash

# Step 2: Use Checkov to scan your Terraform file (e.g., bad_s3_bucket.tf)
checkov -f bad_s3_bucket.tf
```
![image 7: Checkov vulnerability scan](https://github.com/user-attachments/assets/b8351160-4b64-432c-a7bc-88f43095754f)

![image 8: Checkov vulnerability scan](https://github.com/user-attachments/assets/d49e133a-d2d1-458c-8149-8057261e3edd)

![image 9: Checkov vulnerability scan](https://github.com/user-attachments/assets/427604b5-0f5d-43b8-9018-e185cf4d962d)

# Gitleaks

```bash
# Step 1: With the files already commited to git, use Gitleaks via docker to scan for exposed credentials and store it in a file called 'gitleaks_report.json'.
docker run --rm -v "$(pwd)":/app zricethezav/gitleaks detect --source=/app --report-path /app/gitleaks_report.json
```
```bash
# Step 2: Open the report where details of the leak are stored.
cat gitleaks_report.json
```
![image 10: Gitleaks vulnerability scan](https://github.com/user-attachments/assets/d20d742b-4c97-4905-a680-25ad5f3c0120)

![image 11: Gitleaks vulnerability report](https://github.com/user-attachments/assets/3c4387d5-f1dd-4c0f-a55a-2050c3f61664)

# Trivy 
```bash
# Step 1: Build docker image 
docker build -t my-devsecops-app:latest .
```
```bash
#Step 2: Run Trivy via Docker image
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image my-devsecops-app:latest
``` 
![image 12: Trivy vulnerability report](https://github.com/user-attachments/assets/0ec779be-39f1-4556-a065-753dd2da21f4)

![image 13: Trivy vulnerability report](https://github.com/user-attachments/assets/f2cbce2b-cf08-4905-8a0a-45b1e227caa5)

---
📫 **Contact**:  
- ✉️ **Email**: genesisojeda@ojedatech.com  
- 💼 **LinkedIn**: [Génesis M. Ojeda](https://www.linkedin.com/in/génesis-ojeda-451576302)  
- 🐙 **GitHub**: [DevQueenPR](https://github.com/DevQueenPR)  
