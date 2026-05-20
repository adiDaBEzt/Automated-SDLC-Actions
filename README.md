# Automated SDLC with Galaxium Travels

This repository demonstrates an automated Software Development Life Cycle (SDLC) using GitHub Actions and Bob AI for code reviews and issue triage.

## Project Structure

- **frontend/** - React + TypeScript frontend for Galaxium Travels booking system
- **python_backend/** - FastAPI backend with SQLite database
- **scripts/** - Automation scripts for CI/CD
- **.github/workflows/** - GitHub Actions workflows for automated reviews and testing

## Quick Start

Run both backend and frontend servers:

```bash
./start.sh
```

This will:
- Create virtual environment if needed
- Install dependencies
- Seed the database with demo data
- Start backend on http://localhost:8082
- Start frontend on http://localhost:3000

## Features

- Automated PR reviews using Bob AI
- Automated issue triage
- Continuous integration and testing
- Full-stack booking system demo

## Documentation

- [Automation README](AUTOMATION_README.md)
- [Frontend Build Spec](frontend/BUILD_SPEC.md)
- [Backend Spec Sheet](python_backend/SPEC_SHEET.md)