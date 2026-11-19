# COMP 490 - Lab 1 Starter

## Overview

This repository contains a small Python FastAPI application for practicing
AI-assisted software engineering.

## Setup

1. Clone your GitHub repository.
2. Open the project in VS Code.
3. Create and activate a Python virtual environment.

   On macOS or Linux:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   On Windows PowerShell:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   On Windows Command Prompt:

   ```bat
   py -m venv .venv
   .venv\Scripts\activate.bat
   ```

4. Install the dependencies.

   ```bash
   python -m pip install -r requirements.txt
   ```

## Run the Application

```bash
python -m uvicorn app.main:app --reload
```

Visit <http://127.0.0.1:8000/docs>.

## Run Tests

```bash
python -m pytest
```

## Existing Functionality

`GET /health`

Expected response:

```json
{"status": "ok"}
```

## Assignment

Follow the Lab 1 instructions in CI Learn.

You will use Codex to add a `/version` endpoint, write an automated test, and
submit your changes through a GitHub Pull Request.
