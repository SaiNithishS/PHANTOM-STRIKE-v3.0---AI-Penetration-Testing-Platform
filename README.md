<div align="center">

<img src="https://img.shields.io/badge/PHANTOM%20STRIKE-v3.0-00D4FF?style=for-the-badge&logo=shield&logoColor=white" alt="PHANTOM STRIKE"/>

# ⚡ PHANTOM STRIKE
### AI-Powered Penetration Testing & Security Intelligence Platform

[![Microsoft Foundry IQ](https://img.shields.io/badge/Microsoft-Foundry%20IQ-0078D4?style=flat-square&logo=microsoft&logoColor=white)](https://ai.azure.com)
[![Azure AI](https://img.shields.io/badge/Azure-AI%20Agents-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![React](https://img.shields.io/badge/React-18-61DAFB?style=flat-square&logo=react&logoColor=black)](https://reactjs.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Hackathon](https://img.shields.io/badge/Microsoft-Agents%20League%202026-purple?style=flat-square&logo=microsoft)](https://aka.ms/AgentsLeague)

> **Autonomous codebase security auditing powered by two Microsoft Foundry IQ AI agents - upload a ZIP, get a complete penetration test report in 60 seconds.**

---

[🚀 Quick Start](#-quick-start) • [📸 Screenshots](#-screenshots) • [🏗️ Architecture](#️-architecture) • [✨ Features](#-features) • [📋 Prerequisites](#-prerequisites) • [🤝 Contributing](#-contributing)

</div>

---

## 🎯 What is PHANTOM STRIKE?

**PHANTOM STRIKE** is an AI-driven penetration testing platform that automatically audits application codebases for security vulnerabilities. Upload any ZIP archive of source code and within 60 seconds receive:

- **Vulnerability findings** with CVSS scores, CWE mappings, and MITRE ATT&CK techniques
- **Exploit proof-of-concept payloads** for each finding
- **AI-generated remediation plans** with before/after code diffs
- **Attack chain visualisation** showing how vulnerabilities chain together
- **Compliance scoring** against OWASP ASVS, ISO 27001, and SOC 2
- **Professional PDF report** ready for stakeholders

Built for the **Microsoft Agents League @ AI Skills Fest 2026** - Reasoning Agents track.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Dual-Agent Analysis** | Two specialised Microsoft Foundry IQ agents work sequentially - one finds vulnerabilities, one generates fixes |
| 🧠 **Foundry IQ Knowledge Base** | Agents grounded with OWASP Cheat Sheets, VAPT Playbook, and CWE definitions |
| ⚡ **Real-time Terminal** | Live streaming progress as agents process your codebase |
| 📊 **Interactive Dashboard** | 7-tab security report with risk gauge, compliance bars, attack chain timeline |
| 🛡️ **Pre-scan Engine** | Client-side secret detection and dependency extraction before AI analysis |
| 📄 **Professional PDF Export** | Cover page, executive summary, full findings, code diffs, and compliance mapping |
| 🎮 **Demo Mode** | Full dashboard preview without any API credentials |
| 🔒 **Security First** | Credentials managed via Azure CLI - never stored in code or browser storage |

---
</div>

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    USER BROWSER                              │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │           PHANTOM STRIKE  (index.html)               │   │
│  │           React 18 + Babel + JSZip                   │   │
│  │                                                      │   │
│  │  ① Upload ZIP  →  ② Launch Analysis  →  ③ Dashboard │   │
│  └─────────────────────┬────────────────────────────────┘   │
│                        │ POST /analyse (FormData)            │
└────────────────────────┼────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────┐
│              FLASK BACKEND  (server.py)                      │
│              Python + azure-ai-projects                      │
│                                                              │
│  ① Extract ZIP  →  ② Connect Foundry  →  ③ Call Agents     │
└────────────────────────┬────────────────────────────────────┘
                         │ AzureCliCredential
                         │ openai_client.responses.create()
┌────────────────────────▼────────────────────────────────────┐
│           MICROSOFT FOUNDRY IQ                               │
│                                                              │
│  ┌─────────────────────┐  ┌──────────────────────────────┐  │
│  │  consultant agent   │  │    remediation agent         │  │
│  │                     │  │                              │  │
│  │  • SAST analysis    │  │  • Fix plan generation       │  │
│  │  • CVSS scoring     │  │  • Code diff creation        │  │
│  │  • CWE mapping      │  │  • Compliance mapping        │  │
│  │  • Attack chains    │  │  • Effort estimation         │  │
│  └──────────┬──────────┘  └──────────────────────────────┘  │
│             │                                                 │
│  ┌──────────▼──────────────────────────────────────────────┐ │
│  │              FOUNDRY IQ KNOWLEDGE BASE                  │ │
│  │  OWASP Cheat Sheets • VAPT Playbook • CWE Definitions  │ │
│  └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 Prerequisites

- Python 3.10+
- Azure CLI installed and logged in (`az login`)
- Microsoft Azure subscription
- Azure AI Foundry project with two agents deployed

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/phantom-strike.git
cd phantom-strike
```

### 2. Install dependencies

```bash
pip install flask flask-cors azure-ai-projects azure-identity
```

### 3. Login to Azure

```bash
az login
```

### 4. Configure your Foundry endpoint

Open `server.py` and update:

```python
ENDPOINT = "https://your-resource.services.ai.azure.com/api/projects/your-project"
AGENT1_NAME = "consultant"     # Your pentest agent name
AGENT2_NAME = "remediation"    # Your remediation agent name
```

### 5. Start the backend

```bash
python server.py
```

### 6. Start the app

```bash
python -m http.server 8080
```

### 7. Open in browser

```
http://localhost:8080
```

---

## 🤖 Setting Up Foundry IQ Agents

### Create two agents in [Azure AI Foundry](https://ai.azure.com):

**Agent 1 - Security Consultant (`consultant`)**
- Model: `gpt-4.1-mini` or `gpt-4o`
- Instructions: See [`docs/agent-instructions/consultant.md`](docs/agent-instructions/consultant.md)
- Knowledge: OWASP Cheat Sheets + VAPT Playbook

**Agent 2 - Remediation Specialist (`remediation`)**
- Model: `gpt-4.1-mini` or `gpt-4o`
- Instructions: See [`docs/agent-instructions/remediation.md`](docs/agent-instructions/remediation.md)
- Knowledge: OWASP Cheat Sheets + CWE Mitigations

### Knowledge Base URLs to add:

```
https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html
https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html
```

---

## 📁 Project Structure

```
phantom-strike/
├── index.html          # Complete React frontend (single file)
├── server.py           # Flask backend - Foundry IQ integration
├── run_analysis.py     # CLI analysis script (alternative to server)
├── README.md           # This file
└── docs/
    ├── screenshots/    # App screenshots
    └── agent-instructions/
        ├── consultant.md
        └── remediation.md
```

---

## 🔍 How It Works

```
1. USER uploads ZIP archive of any codebase
        ↓
2. CLIENT-SIDE pre-scan detects secrets and dependencies
        ↓
3. FLASK BACKEND receives ZIP and extracts code
   Priority order: auth → config → API → database → other
   Truncates to 20KB for optimal agent performance
        ↓
4. CONSULTANT AGENT analyses code for:
   • SQL Injection (CWE-89)
   • XSS (CWE-79)  
   • Hardcoded secrets (CWE-798)
   • Broken authentication (CWE-287)
   • Path traversal (CWE-22)
   • Command injection (CWE-78)
   • And more...
        ↓
5. REMEDIATION AGENT generates for each finding:
   • Root cause analysis
   • Step-by-step fix instructions
   • Before/after secure code examples
   • Verification steps
   • OWASP/CWE compliance mapping
        ↓
6. DASHBOARD renders with full findings
        ↓
7. PDF REPORT generated - professional A4 document
```

---

## 🛡️ Security

- **No credentials in source code** - Azure CLI manages authentication
- **Session-only storage** - credentials cleared when browser tab closes
- **Code stays local** - uploaded ZIP processed on your machine
- **Thread cleanup** - Foundry conversation threads deleted after analysis
- **HTTPS only** - all Azure API calls over encrypted connections

---

## 🏆 Hackathon

Built for **Microsoft Agents League @ AI Skills Fest 2026**

- **Track**: Reasoning Agents (Microsoft Foundry IQ)
- **Prize categories targeting**: Best Reasoning Agent • Best Use of IQ Tools
- **Submission deadline**: June 14, 2026
---

## 📊 Supported Vulnerability Types

| Category | CWE | OWASP |
|---|---|---|
| SQL Injection | CWE-89 | A03:2021 |
| Cross-Site Scripting | CWE-79 | A03:2021 |
| Hardcoded Secrets | CWE-798 | A07:2021 |
| Broken Authentication | CWE-287 | A07:2021 |
| Path Traversal | CWE-22 | A01:2021 |
| Command Injection | CWE-78 | A03:2021 |
| Insecure Deserialization | CWE-502 | A08:2021 |
| SSRF | CWE-918 | A10:2021 |
| XXE Injection | CWE-611 | A05:2021 |
| Vulnerable Dependencies | CWE-1395 | A06:2021 |

---

## 🧑‍💻 Built With

- **[Microsoft Foundry IQ](https://ai.azure.com)** - AI agent hosting and knowledge base
- **[Azure AI Projects SDK](https://pypi.org/project/azure-ai-projects/)** - Python agent integration
- **[React 18](https://reactjs.org)** - Frontend UI framework
- **[Flask](https://flask.palletsprojects.com)** - Lightweight Python backend
- **[JSZip](https://stuk.github.io/jszip/)** - Client-side ZIP extraction
- **[html2pdf.js](https://ekoopmans.github.io/html2pdf.js/)** - PDF report generation
- **[OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org)** - Security knowledge base

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

<div align="center">

**Built with ⚡ for Microsoft Agents League @ AI Skills Fest 2026**

[![Microsoft AI](https://img.shields.io/badge/Powered%20by-Microsoft%20Foundry%20IQ-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)](https://ai.azure.com)

*Sai Nithish Sampath • University of Southampton • MSc Cyber Security*

</div>
