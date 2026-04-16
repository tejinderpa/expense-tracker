# Project Structure Guide

This document explains the complete structure of the Spendly project, including the Claude Code memory system.

## Full Directory Tree

```
expense-tracker/
├── .claude/                          # [OPTIONAL] Project-local Claude settings
│   ├── settings.json                 # Project-specific Claude Code settings
│   └── scheduled_tasks.json          # Recurring tasks for this project
│
├── CLAUDE.md                         # [IMPORTANT] Project-specific instructions
├── app.py                            # Main Flask application
├── requirements.txt                  # Python dependencies
├── database/
│   ├── __init__.py
│   └── db.py                         # Database connection (placeholder)
├── static/
│   ├── css/
│   │   ├── style.css                 # Main stylesheet (CSS custom properties)
│   │   └── landing.css               # Landing page styles
│   └── js/
│       └── main.js                   # Frontend JavaScript (placeholder)
├── templates/
│   ├── base.html                     # Base template (navbar, footer)
│   ├── landing.html                  # Homepage with hero section
│   ├── login.html                    # Login form
│   ├── register.html                 # Registration form
│   ├── terms.html                    # Terms of service
│   └── privacy.html                  # Privacy policy
└── tests/
    └── conftest.py                   # pytest fixtures

USER MEMORY FOLDER (outside project):
C:\Users\HP\.claude\projects\F--Campusx-expense-tracker-expense-tracker\memory\
├── MEMORY.md                         # Index of all memories (read first)
└── currency_preference.md            # Project uses INR instead of USD
```

---

## The Two Memory Systems

### 1. CLAUDE.md (Project Memory) ✅ IMPORTANT

**Location:** `./CLAUDE.md` (in your project root)

**Purpose:** Documents the codebase itself — architecture, conventions, commands, and patterns that any developer (human or AI) needs to know.

**What goes here:**
- Project overview and purpose
- Tech stack and versions
- Development commands (`npm test`, `python app.py`, etc.)
- File/folder structure explanation
- Key architectural decisions
- Coding conventions specific to this project
- Important file paths and their purposes

**Why it's important:**
- Checked into git — shared with all collaborators
- Survives project moves/copies
- Helps any new developer (or AI) get up to speed
- Documents _why_ things are built a certain way

**Your project's CLAUDE.md contains:**
- Flask + SQLite + vanilla JS stack
- Step-by-step development plan (Steps 1-9)
- Route structure
- CSS custom properties for theming
- Modal implementation pattern
- Template block structure

---

### 2. User Memory Folder (Persistent Preferences)

**Location:** `C:\Users\HP\.claude\projects\F--Campusx-expense-tracker-expense-tracker\memory\`

**Purpose:** Stores _your_ preferences, feedback, and project-specific context that isn't in the code itself.

**Structure:**
```
memory/
├── MEMORY.md              # Index file — lists all memories (read first)
├── user_role.md           # Who you are, your expertise level
├── feedback_testing.md    # "Always use real DB in tests, not mocks"
├── project_deadline.md    # "Launch by March 15 for demo day"
└── currency_preference.md # "Use INR instead of USD"
```

**Types of memories:**

| Type | Description | Example |
|------|-------------|---------|
| `user` | Your role, skills, preferences | "Data scientist new to React" |
| `feedback` | How you want me to work | "No emojis in code", "Real DB in tests" |
| `project` | Current initiatives, deadlines | "Merge freeze after Thursday" |
| `reference` | External resources | "Linear project 'INGEST' for bugs" |

**Why it's separate from CLAUDE.md:**
- Personal to _you_ — not checked into git
- Can contain preferences that aren't code conventions
- Tied to this project folder path on your machine
- You can have different memories for different projects

---

### 3. .claude Folder (Optional Project Settings)

**Location:** `./.claude/` (inside your project)

**Purpose:** Project-specific Claude Code configuration that travels with the repo.

**What goes here:**
- `settings.json` — Permissions, env vars, hooks for this project
- `scheduled_tasks.json` — Recurring tasks specific to this project

**When to use it:**
- Team-wide Claude settings (checked into git)
- Project-specific automations
- Different from user memory: this is _shared_ config

---

## Key Differences Summary

| Feature | CLAUDE.md | User Memory (.claude/projects/.../memory/) | .claude/ (project folder) |
|---------|-----------|-------------------------------------------|---------------------------|
| **Location** | Project root | User's home folder | Project root |
| **Git-tracked** | ✅ Yes | ❌ No (personal) | ✅ Yes (if committed) |
| **Audience** | All developers | Just you | Team (if shared) |
| **Content** | Code architecture | Preferences, feedback | Settings, hooks |
| **Survives move** | ✅ Yes | ❌ No (path-bound) | ✅ Yes |
| **Auto-created** | ❌ You create it | ✅ By Claude Code | ❌ Optional |

---

## How Claude Uses These

1. **On every conversation start:**
   - Reads `CLAUDE.md` from project root
   - Reads `MEMORY.md` from user memory folder
   - Loads individual memory files listed in `MEMORY.md`

2. **During work:**
   - Refers to `CLAUDE.md` for project patterns
   - Applies `feedback` memories to behavior
   - Considers `project` memories for context
   - Respects `user` memories for your perspective

3. **When you teach something:**
   - Code conventions → add to `CLAUDE.md`
   - Personal preference → save to user memory
   - Team setting → add to `.claude/settings.json`

---

## Quick Reference: Where to Put What

```
"I want all developers to know we use 2-space indentation"
→ CLAUDE.md (under Coding Conventions)

"I don't like verbose commit messages, keep them short"
→ User Memory (feedback type)

"Always run prettier before committing"
→ .claude/settings.json (hook) or User Memory (feedback)

"We use INR currency throughout the app"
→ CLAUDE.md (if team needs to know) OR User Memory (if just your preference)

"Legal requires compliance audit before March 30"
→ User Memory (project type)

"Use real database in integration tests, not mocks"
→ User Memory (feedback type) — learned from past failure
```

---

## Your Current Setup

For this Spendly project, you currently have:

**User Memory:**
- ✅ `currency_preference.md` — Use INR instead of USD

**Project Documentation:**
- ✅ `CLAUDE.md` — Full project architecture and conventions

**Missing (optional additions):**
- ⬜ More user memories (preferences, feedback)
- ⬜ `.claude/settings.json` (project-specific settings)
- ⬜ More CLAUDE.md sections (testing strategy, deployment notes)
