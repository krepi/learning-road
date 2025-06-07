# learning-road
# 🛠️ Automation Lab – Personal DevOps & AML Automation Playground

Welcome to my personal lab repository where I explore and build automation tools and experiments using:

- 🐍 **Python** – scripting, data processing, automation
- 🐚 **Bash** – server scripts and cron jobs (mainly on Ubuntu EC2)
- 📊 **Excel / VBA** – office automation and reporting
- 🐳 **Docker** – containerized environments for testing & deployment
- ☁️ **AWS** – cloud infrastructure and hosting (e.g. EC2, Lightsail, S3)

---

## 🗂️ Folder Structure

```
/python-scripts      # Python automations (e.g. reports, file ops, mini-tools)
/bash-scripts        # Bash scripts for EC2 and Linux automation
/docker              # Dockerfiles and configurations
/aws                 # AWS CLI scripts and config samples (non-sensitive)
/vba                 # Macros and VBA automation tools
```

---

## 🧰 Tools & Environments

| Tool      | Usage                                 |
|-----------|----------------------------------------|
| **Python**| `3.9+`, mostly local & EC2, PyCharm IDE|
| **Bash**  | Ubuntu 22.04 (EC2), scripting practice |
| **VBA**   | MS Excel 365, local macro testing      |
| **Docker**| Local dev + isolated services testing  |
| **AWS**   | EC2, S3, IAM, Lightsail (WordPress blog)|
| **Git**   | Version control + GitHub repo          |

---

## 📄 .gitignore Notes

This project excludes the following from version control:

- PyCharm configs (`.idea/`)
- SSH & EC2 credentials (`*.pem`, `*.key`)
- Word/Excel temporary files (`~$*.docx`, `*.xlsx`)
- macOS & Windows OS junk (`.DS_Store`, `Thumbs.db`)
- Bash temp/backup files (`*.bak`, `*.sh~`)
- Docker override/env files (`*.env`, `docker-compose.override.yml`)
- AWS credentials (`.aws/credentials`, `.aws/config`)

> ✅ See the full `.gitignore` file for details.

---

## 💡 Purpose

This repo supports my learning path toward a role in:

- ⚙️ **DevOps** or **Automation Developer**
- 🧾 **AML automation / process optimization**

I use it to test ideas, store reusable scripts, and document my journey.

---

## 🔐 Security Notice

All private credentials and sensitive config files are **excluded** from this repository using `.gitignore`. This includes:

- AWS credentials
- SSH private keys
- Office temp/autosave files

---

## 📌 Roadmap (Work in Progress)

- [ ] Write Python script to auto-rename & organize files
- [ ] Build Bash tool to monitor EC2 disk usage
- [ ] Create Excel+VBA macro that launches Python script
- [ ] Deploy a Python + Flask mini-app using Docker
- [ ] Automate AWS resource cleanup (EC2, S3)

---

## 🧪 License & Disclaimer

This project is for **learning purposes only** and not intended for production use. Scripts may be unstable or incomplete.
