# 🤖 AI Bug Detection Agent

An automated code review pipeline that triggers every time a Pull Request is opened on GitHub. The agent reads the changed code, identifies bugs and security vulnerabilities, posts a detailed review comment on the PR, and sends an email alert — all within seconds of a push.

---

## How It Works

```
Developer pushes code → PR opened → GitHub Actions triggers
→ AI reads the diff → Posts review comment on PR → Sends email alert
```

1. A developer pushes code and opens a Pull Request
2. GitHub Actions automatically triggers the workflow
3. The AI agent reads every changed Python file
4. It identifies bugs, security issues, and logic errors with exact file names and line numbers
5. It posts a detailed review comment on the PR with severity ratings and fix suggestions
6. If bugs are found, it sends an email alert to the configured address instantly

---

## Demo

This repo includes a purposefully buggy Python file to demonstrate the agent in action. The file contains 5 real-world bugs:

| # | Bug | Severity | What Could Go Wrong |
|---|-----|----------|---------------------|
| 1 | SQL Injection via f-string | 🔴 Critical | Attacker dumps or destroys your entire database |
| 2 | No input validation on discount % | 🟠 High | Negative prices or 200% discounts |
| 3 | Division by zero | 🟠 High | App crashes when no students exist |
| 4 | Off-by-one error (`len + 1`) | 🟠 High | IndexError on every list iteration |
| 5 | KeyError risk (no `.get()`) | 🟡 Medium | App crashes on any missing config key |

When the buggy code is pushed and a PR is opened, the agent catches all 5 bugs automatically.

---

## Setup

### Prerequisites
- A GitHub account
- A Gmail account with 2-Step Verification enabled
- An OpenAI API key

### 1. Fork or clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/claude-bug-fix-demo.git
cd claude-bug-fix-demo
git remote set-url origin https://github.com/YOUR_USERNAME/claude-bug-fix-demo.git
```

### 2. Add GitHub Secrets

Go to your repo → **Settings → Secrets and variables → Actions** and add these secrets:

| Secret Name | Value |
|-------------|-------|
| `OPENAI_API_KEY` | Your OpenAI API key (`sk-...`) |
| `EMAIL_ADDRESS` | Your Gmail address |
| `EMAIL_APP_PASSWORD` | Your Gmail App Password (see below) |

**Generating a Gmail App Password:**
1. Go to [myaccount.google.com](https://myaccount.google.com) → Security
2. Make sure 2-Step Verification is turned on
3. Search for "App Passwords" → Create one named `github-actions`
4. Copy the 16-character password and paste it as the `EMAIL_APP_PASSWORD` secret

### 3. Update the email recipient

In `.github/workflows/claude-bug-fix.yml`, find this line and change it to your email:

```python
to_email = "your@email.com"
```

---

## Running the Demo

Use these commands to reset and re-run the demo at any time:

```bash
# Reset
git checkout main
git branch -D demo/buggy-code
git push origin --delete demo/buggy-code

# Create buggy branch
git checkout -b demo/buggy-code
cp app/buggy_user_service.py app/user_service.py
git add app/user_service.py
git commit -m "feat: refactor user service to use direct DB queries"
git push origin demo/buggy-code
```

Then open a PR at:
```
https://github.com/YOUR_USERNAME/claude-bug-fix-demo/compare/main...demo/buggy-code
```

The agent will trigger automatically within seconds of opening the PR.

---

## Project Structure

```
claude-bug-fix-demo/
├── .github/
│   └── workflows/
│       └── claude-bug-fix.yml   # The GitHub Actions workflow
├── app/
│   ├── user_service.py          # Clean, working version of the code
│   └── buggy_user_service.py    # Intentionally buggy version for demo
├── tests/
│   └── test_user_service.py     # Test suite
├── requirements.txt
└── README.md
```

---

## What the Agent Reviews

The agent looks for the following categories of issues in every PR:

- **Security vulnerabilities** — SQL injection, hardcoded secrets, unsafe input handling
- **Unhandled exceptions** — division by zero, KeyError, IndexError, None dereference
- **Input validation gaps** — missing bounds checks, type checks, null checks
- **Logic errors** — off-by-one errors, wrong operators, incorrect conditionals

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| CI/CD | GitHub Actions |
| AI Model | GPT-4o via OpenAI API |
| Email Alerts | Gmail SMTP |
| Language | Python 3.11 |

---

## Extending This

This agent can be dropped into any existing Python repository with no changes to the application code — just add the workflow file and secrets. It works on any PR that touches `.py` files.

To adapt it for other languages, update the `-- '*.py'` filter in the workflow to match your file types (e.g. `-- '*.js'`, `-- '*.ts'`).