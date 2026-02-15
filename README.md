# OpsFlash ⚡

**Governed Git automation via MCP and Archestra**

[![MCP](https://img.shields.io/badge/MCP-Native-blue)](https://modelcontextprotocol.io)
[![Archestra](https://img.shields.io/badge/Archestra-Ready-green)](https://archestra.ai)

---

## Overview

OpsFlash is a governance-first Git automation agent built on the Model Context Protocol (MCP). It provides safe, observable, and controlled Git operations through structured tool interfaces designed for orchestration platforms like Archestra.

### The Problem

Traditional AI-powered Git automation faces critical challenges:

- **Uncontrolled Execution**: LLMs generate raw shell commands that execute without validation
- **Security Risks**: No protection against dangerous operations (force push, branch deletion)
- **Lack of Observability**: No audit trail of what AI agents are doing
- **No Governance**: Cannot enforce team policies or protected branch rules
- **Unpredictable Behavior**: Shell command generation is inconsistent and error-prone

### The OpsFlash Solution

OpsFlash transforms Git automation from dangerous shell execution into a governed, observable workflow:

**Traditional Approach:**
```
LLM → Raw Shell Commands → Uncontrolled Execution → No Audit Trail
```

**OpsFlash Approach:**
```
LLM → Structured MCP Tools → Risk Validation → Safe Execution → Structured Logs
```

### Key Benefits

- ✅ **Controlled Git State Mutation** - All operations go through validated tool interfaces
- ✅ **Risk-Aware Execution** - Every action is assessed (LOW/MEDIUM/HIGH risk)
- ✅ **Protected Branch Enforcement** - Automatic blocking of dangerous operations on main/master/production
- ✅ **Dry-Run Validation** - Test operations before execution
- ✅ **Full Observability** - Structured JSON logs for every action
- ✅ **Centralized Orchestration** - Designed for Archestra's MCP platform
- ✅ **Policy Enforcement** - Team-wide governance rules

---

## Core Features

### 🔒 Governance & Safety

#### Protected Branch Enforcement
OpsFlash automatically protects critical branches from dangerous operations:

```python
PROTECTED_BRANCHES = ["main", "master", "production", "prod"]
```

**Blocked Operations:**
- ❌ Force push to protected branches
- ❌ Direct deletion of protected branches
- ❌ Unreviewed merges to protected branches

**Example:**
```bash
$ python cli.py merge main
❌ BLOCKED: Cannot merge into protected branch: main
📊 Risk Level: HIGH
💡 Suggestion: Create a pull request instead
```

#### Risk Assessment System

Every Git operation is evaluated before execution:

| Risk Level | Description | Requires Confirmation | Examples |
|------------|-------------|----------------------|----------|
| **LOW** | Safe operations | No | Create branch, list branches, stash |
| **MEDIUM** | Potentially disruptive | Yes | Merge to non-protected branch |
| **HIGH** | Dangerous operations | Yes + Blocking | Force push, delete protected branch, merge to main |

**Risk Validation Tool:**
```bash
$ python cli.py validate merge main
{
  "action_type": "merge",
  "branch_name": "main",
  "risk_level": "MEDIUM",
  "requires_confirmation": true,
  "is_protected": true
}
```

#### Dry-Run Mode

Test any operation without executing it:

```bash
# Simulate a commit
$ python cli.py commit "feat: add authentication" --dry-run
🔍 DRY RUN: Would execute: git commit -m "feat: add authentication"
📊 Risk: LOW | Safe to proceed

# Simulate a merge
$ python cli.py merge feature/auth --dry-run
🔍 DRY RUN: Would execute: git merge feature/auth
📊 Risk: MEDIUM | Review before executing
```

### 🛠️ MCP-Native Tools

OpsFlash exposes 6 structured MCP tools for Git operations:

#### 1. `create_branch`
Create and checkout a new Git branch safely.

**Arguments:**
```json
{
  "branch_name": "string",
  "dry_run": "boolean (optional)"
}
```

**Example:**
```python
# Via MCP
create_branch(branch_name="feature/user-auth", dry_run=False)

# Via CLI
python cli.py create-branch feature/user-auth
```

**Behavior:**
- Validates branch name format
- Checks for existing branches
- Creates and checks out the new branch
- Logs the operation with timestamp

#### 2. `list_branches`
List all local and remote Git branches.

**Arguments:**
```json
{}
```

**Returns:**
```json
{
  "status": "success",
  "output": "* main\n  feature/auth\n  remotes/origin/main"
}
```

**Example:**
```bash
$ python cli.py list-branches
* main
  feature/auth
  feature/dashboard
  remotes/origin/main
  remotes/origin/develop
```

#### 3. `safe_commit`
Stage changes and create a commit with optional AI-generated message.

**Arguments:**
```json
{
  "message": "string (optional)",
  "auto_generate": "boolean (optional)",
  "dry_run": "boolean (optional)"
}
```

**Features:**
- Automatically stages all changes (`git add -A`)
- Generates commit message from diff if `auto_generate=true`
- Follows conventional commit format
- Validates message before committing

**AI Message Generation:**
```python
# Analyzes staged changes and generates appropriate message:
- "test: add/update tests" (if test files changed)
- "docs: update documentation" (if docs/README changed)
- "feat: implement changes" (for feature additions)
- "chore: update files" (default fallback)
```

**Example:**
```bash
# Manual message
$ python cli.py commit "feat: add user authentication"

# Auto-generated message
$ python cli.py commit --auto-generate

# Dry-run first
$ python cli.py commit "fix: resolve login bug" --dry-run
```

#### 4. `merge_branch`
Merge source branch into current branch with safety checks.

**Arguments:**
```json
{
  "source_branch": "string",
  "dry_run": "boolean (optional)"
}
```

**Safety Features:**
- Detects current branch automatically
- Blocks merges into protected branches
- Assesses merge risk level
- Checks for potential conflicts
- Requires confirmation for MEDIUM/HIGH risk

**Example:**
```bash
# Safe merge
$ python cli.py merge feature/auth
✅ Merged feature/auth into develop

# Blocked merge
$ python cli.py merge feature/auth
# (when on main branch)
❌ BLOCKED: Cannot merge into protected branch: main
```

#### 5. `stash_changes`
Stash current changes with optional auto-apply.

**Arguments:**
```json
{
  "apply_after": "boolean (optional)",
  "dry_run": "boolean (optional)"
}
```

**Use Cases:**
- Temporarily save work in progress
- Switch branches without committing
- Clean working directory for operations
- Auto-apply after branch switch

**Example:**
```bash
# Simple stash
$ python cli.py stash

# Stash and immediately pop
$ python cli.py stash --apply-after
```

#### 6. `validate_git_action`
Pre-execution risk assessment for any Git action.

**Arguments:**
```json
{
  "action_type": "string",
  "branch_name": "string (optional)"
}
```

**Returns:**
```json
{
  "action_type": "merge",
  "branch_name": "main",
  "risk_level": "MEDIUM",
  "requires_confirmation": true,
  "is_protected": true
}
```

**Supported Action Types:**
- `create_branch`
- `commit`
- `merge`
- `stash`
- `force_push`
- `delete_branch`

**Example:**
```bash
# Validate before executing
$ python cli.py validate merge main
$ python cli.py validate force_push
$ python cli.py validate delete_branch production
```

### 📊 Observability & Logging

Every OpsFlash operation generates structured JSON logs for full audit trails.

#### Log Format

```json
{
  "timestamp": "2026-02-15T21:01:17.583Z",
  "action": "create_branch: feature/auth",
  "risk_level": "LOW",
  "details": {
    "command": "git checkout -b feature/auth",
    "output": "Switched to a new branch 'feature/auth'"
  }
}
```

#### Log Levels

- **INFO**: Successful operations
- **ERROR**: Failed operations with error details
- **WARNING**: Blocked operations (governance enforcement)

#### Example Log Sequence

```json
// Branch creation
{
  "timestamp": "2026-02-15T21:00:00.000Z",
  "action": "create_branch: feature/auth",
  "risk_level": "LOW",
  "details": {
    "command": "git checkout -b feature/auth",
    "output": "Switched to a new branch 'feature/auth'"
  }
}

// Commit with auto-generated message
{
  "timestamp": "2026-02-15T21:00:30.000Z",
  "action": "commit: feat: implement changes",
  "risk_level": "LOW",
  "details": {
    "command": "git commit -m 'feat: implement changes'",
    "output": "[feature/auth abc1234] feat: implement changes"
  }
}

// Blocked merge attempt
{
  "timestamp": "2026-02-15T21:01:00.000Z",
  "action": "merge: feature/auth -> main",
  "status": "BLOCKED",
  "risk_level": "HIGH",
  "details": {
    "reason": "Cannot merge into protected branch: main",
    "suggestion": "Create a pull request instead"
  }
}
```

#### Benefits of Structured Logging

- **Audit Compliance**: Complete trail of all Git operations
- **Debugging**: Trace issues back to specific actions
- **Analytics**: Analyze team Git patterns
- **Security**: Detect suspicious or dangerous operations
- **Integration**: Easy to parse and forward to monitoring systems

### 🎯 Archestra Integration

OpsFlash is purpose-built for Archestra's MCP orchestration platform.

#### What is Archestra?

Archestra is a centralized, MCP-native AI platform that enables teams to run, orchestrate, secure, and observe AI agents across an organization. It provides:

- **Centralized Agent Runtime** - Deploy agents once, use everywhere
- **Security Guardrails** - Prevent prompt injection and data exfiltration
- **Cost Controls** - Monitor and limit API usage
- **Observability** - Metrics, traces, and logs for all agent operations
- **Multi-LLM Support** - Use different models for different tasks

#### Why OpsFlash + Archestra?

| Component | Provides | Benefit |
|-----------|----------|---------|
| **OpsFlash** | Safe Git primitives | Structured, validated Git operations |
| **OpsFlash** | MCP tool interfaces | Standard protocol for agent communication |
| **OpsFlash** | Risk assessment | Pre-execution validation |
| **Archestra** | Centralized runtime | Deploy once, team-wide access |
| **Archestra** | Security layer | Additional prompt injection protection |
| **Archestra** | Cost tracking | Monitor Git automation API costs |
| **Archestra** | Observability | Aggregate logs across all agents |
| **Together** | Governed Git automation | Safe, scalable, observable Git workflows |

#### Deployment Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Archestra Platform                    │
│  ┌────────────────────────────────────────────────────┐ │
│  │              Git Assistant Agent                    │ │
│  │  System Prompt: "You are OpsFlash..."             │ │
│  │  Tools: All OpsFlash MCP tools                    │ │
│  └────────────────────────────────────────────────────┘ │
│                          │                               │
│                          ▼                               │
│  ┌────────────────────────────────────────────────────┐ │
│  │           OpsFlash MCP Server                      │ │
│  │  • create_branch    • merge_branch                │ │
│  │  • list_branches    • stash_changes               │ │
│  │  • safe_commit      • validate_git_action         │ │
│  └────────────────────────────────────────────────────┘ │
│                          │                               │
│                          ▼                               │
│  ┌────────────────────────────────────────────────────┐ │
│  │         Governance & Validation Layer              │ │
│  │  • Risk Assessment  • Protected Branches          │ │
│  │  • Dry-Run Support  • Structured Logging          │ │
│  └────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
                  ┌───────────────┐
                  │  Git Repository│
                  └───────────────┘
```

#### Integration Steps

**1. Add OpsFlash as MCP Server**

In Archestra's MCP Registry:
```yaml
Name: OpsFlash
Type: Local MCP Server
Command: python /path/to/opsflash/server.py
Description: Governed Git automation agent
```

**2. Create Git Assistant Agent**

Configure agent in Archestra:
```yaml
Agent Name: Git Assistant
System Prompt: |
  You are OpsFlash, a governed Git operations agent.
  
  Core Principles:
  - Convert natural language into structured MCP tool calls
  - Never output raw shell commands
  - Never invent Git syntax
  - Always use available MCP tools
  - Require confirmation for destructive operations
  - Prefer dry_run when risk is MEDIUM or HIGH
  - Log every action taken
  
  You operate under governance enforced by Archestra.
  
  When a user requests a Git operation:
  1. Validate the action using validate_git_action
  2. If risk is HIGH, explain why and suggest alternatives
  3. If risk is MEDIUM, ask for confirmation
  4. If risk is LOW, proceed with execution
  5. Always log the result

Enabled Tools:
  - create_branch
  - list_branches
  - safe_commit
  - merge_branch
  - stash_changes
  - validate_git_action

Model: claude-3-5-sonnet (or your preferred LLM)
```

**3. Configure Governance Policies**

Set up Archestra policies:
```yaml
Policies:
  - name: "Block Force Push"
    rule: "Reject any operation containing 'force' or '--force'"
    severity: HIGH
    
  - name: "Protect Main Branch"
    rule: "Block direct commits/merges to main/master"
    severity: HIGH
    
  - name: "Require PR for Production"
    rule: "All production branch changes require pull request"
    severity: MEDIUM
    
  - name: "Audit All Operations"
    rule: "Log all Git operations to audit trail"
    severity: INFO
```

**4. Team-Wide Deployment**

Once configured, all team members can access the Git Assistant through Archestra's chat interface:

```
User: "Create a feature branch for user authentication"
Agent: ✅ Created branch: feature/user-auth
       📊 Risk: LOW | Logged: Yes

User: "Commit my changes with a good message"
Agent: ✅ Committed: "feat: add user authentication module"
       📊 Risk: LOW | Auto-generated message

User: "Merge this into main"
Agent: ❌ BLOCKED: Cannot merge into protected branch: main
       📊 Risk: HIGH
       💡 Suggestion: Create a pull request instead
       
       Would you like me to:
       1. Create a PR with AI-generated description
       2. Merge into develop branch instead
       3. Show merge preview (dry-run)
```

#### Multi-Agent Workflows

OpsFlash can participate in complex multi-agent workflows orchestrated by Archestra:

**Example: Automated Feature Development**

```
┌──────────────────┐
│  Planning Agent  │ → Creates feature specification
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  OpsFlash Agent  │ → Creates feature branch
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Coding Agent    │ → Implements feature
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  OpsFlash Agent  │ → Commits with AI message
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Review Agent    │ → Reviews code quality
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  OpsFlash Agent  │ → Creates PR (blocked from direct merge)
└──────────────────┘
```

#### Cost Optimization with Archestra

Archestra's multi-LLM support enables cost-optimized Git automation:

| Operation | Complexity | Recommended Model | Cost |
|-----------|-----------|-------------------|------|
| Create branch | Low | Gemini Flash | $0.0001 |
| List branches | Low | Gemini Flash | $0.0001 |
| Simple commit | Low | GPT-3.5 Turbo | $0.0005 |
| AI commit message | Medium | Claude Haiku | $0.002 |
| Complex merge | High | Claude Opus | $0.015 |
| Conflict resolution | High | GPT-4 | $0.03 |

**Estimated Savings:** 70% compared to using GPT-4 for all operations

#### Observability in Archestra

Archestra aggregates OpsFlash logs with platform-wide observability:

**Metrics Dashboard:**
- Total Git operations per day/week/month
- Operations by risk level (LOW/MEDIUM/HIGH)
- Blocked operations (governance enforcement)
- Most active repositories
- Most common operations
- Error rates and types

**Trace View:**
```
Request: "Create feature branch and commit changes"
├─ validate_git_action (create_branch) - 50ms - LOW risk
├─ create_branch (feature/auth) - 200ms - SUCCESS
├─ validate_git_action (commit) - 45ms - LOW risk
└─ safe_commit (auto-generated) - 300ms - SUCCESS
Total: 595ms
```

**Audit Trail:**
```
2026-02-15 21:00:00 | user@example.com | create_branch | feature/auth | SUCCESS
2026-02-15 21:00:30 | user@example.com | safe_commit | "feat: add auth" | SUCCESS
2026-02-15 21:01:00 | user@example.com | merge_branch | main | BLOCKED
2026-02-15 21:01:15 | user@example.com | merge_branch | develop | SUCCESS
```

---

## Architecture

### System Design

OpsFlash follows a clean, modular architecture optimized for safety and observability:

```
opsflash/
├── server.py              # MCP server entrypoint (FastMCP)
├── cli.py                 # CLI interface for testing
├── requirements.txt       # Python dependencies
│
├── tools/                 # MCP tool implementations
│   ├── branch.py         # Branch operations
│   ├── commit.py         # Commit with AI message
│   ├── merge.py          # Safe merge operations
│   ├── stash.py          # Stash operations
│   └── safety.py         # Risk validation
│
└── core/                  # Core infrastructure
    ├── executor.py       # Git command wrapper
    ├── logger.py         # Structured logging
    └── validator.py      # Risk assessment
```

### Data Flow

```
User Request
    ↓
MCP Tool Call
    ↓
Risk Validation (LOW/MEDIUM/HIGH)
    ↓
├─ HIGH → Block or require approval
├─ MEDIUM → Require confirmation
└─ LOW → Proceed
    ↓
Git Execution (with dry-run support)
    ↓
Structured Logging
    ↓
Return Result
```

---

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Git 2.0 or higher
- pip package manager

### Quick Install

```bash
# Clone the repository
git clone https://github.com/Tasfia-17/OpsFlash.git
cd OpsFlash

# Install dependencies
pip install -r requirements.txt
```

### Dependencies

- **fastmcp** (>=0.2.0) - FastMCP framework for MCP server
- **gitpython** (>=3.1.0) - Git command wrapper (optional, for advanced features)
- **pydantic** (>=2.0.0) - Data validation

---

## Usage

### Running as MCP Server

Start the OpsFlash MCP server:

```bash
python server.py
```

The server will start and listen for MCP tool calls. This is the recommended mode for Archestra integration.

### Using the CLI (Testing & Development)

The CLI provides a convenient way to test OpsFlash tools locally:

#### Basic Commands

```bash
# Create a new branch
python cli.py create-branch feature/new-feature

# List all branches
python cli.py list-branches

# Commit with manual message
python cli.py commit "feat: add new feature"

# Commit with auto-generated message
python cli.py commit

# Merge a branch
python cli.py merge feature/new-feature

# Stash changes
python cli.py stash

# Stash and auto-apply
python cli.py stash --apply-after

# Validate an action before executing
python cli.py validate merge main
python cli.py validate force_push
```

#### Using Dry-Run Mode

Test operations without executing them:

```bash
# Dry-run a branch creation
python cli.py create-branch feature/test --dry-run

# Dry-run a commit
python cli.py commit "test commit" --dry-run

# Dry-run a merge
python cli.py merge feature/test --dry-run
```

### CLI Help

```bash
python cli.py --help
```

Output:
```
Usage: python cli.py <command> [args]

Commands:
  create-branch <name> [--dry-run]    Create and checkout a new branch
  list-branches                        List all local and remote branches
  commit <message> [--dry-run]        Commit staged changes
  merge <source> [--dry-run]          Merge source branch into current
  stash [--apply-after] [--dry-run]   Stash current changes
  validate <action> [branch]          Validate action risk level

Flags:
  --dry-run                           Simulate operation without executing
  --apply-after                       Auto-apply stash after stashing
```

---

## Archestra Integration

### 1. Add OpsFlash as MCP Server

In Archestra:
1. Go to **MCP Registry**
2. Add new MCP server
3. Point to OpsFlash server endpoint
4. Configure as "Git Operations Agent"

### 2. Create Governed Agent

```yaml
Agent: Git Automation Assistant
System Prompt: |
  You are OpsFlash, a governed Git operations agent.
  
  You must:
  - Convert natural language into structured MCP tool calls
  - Never output raw shell commands
  - Always use available MCP tools
  - Require confirmation for destructive operations
  - Prefer dry_run when risk is MEDIUM or HIGH
  - Log every action taken
  
  You operate under governance enforced by Archestra.

Tools: All OpsFlash tools
```

### 3. Set Policies

Configure in Archestra:
- ❌ Block force push to main/master
- ❌ Block delete of protected branches
- ⚠️ Require approval for merges to main
- ✅ Allow all other operations

---

## Architecture

```
opsflash/
├── server.py              # MCP server entrypoint
├── tools/
│   ├── branch.py         # Branch operations
│   ├── commit.py         # Commit operations
│   ├── merge.py          # Merge operations
│   ├── stash.py          # Stash operations
│   └── safety.py         # Validation tools
├── core/
│   ├── executor.py       # Git execution wrapper
│   ├── logger.py         # Structured logging
│   └── validator.py      # Risk assessment
├── cli.py                # Test CLI
└── requirements.txt
```

---

## Example Workflows

### Workflow 1: Feature Development

```bash
# 1. Create feature branch
$ python cli.py create-branch feature/user-auth
✅ Created and checked out: feature/user-auth
📊 Risk: LOW | Logged: Yes

# 2. Make changes to code...
# (edit files)

# 3. Commit with AI-generated message
$ python cli.py commit
📝 Analyzing staged changes...
✅ Committed: "feat: add user authentication module"
📊 Risk: LOW | Auto-generated message

# 4. Try to merge directly to main (blocked)
$ python cli.py merge main
❌ BLOCKED: Cannot merge into protected branch: main
📊 Risk: HIGH
💡 Suggestion: Create a pull request instead

# 5. Merge to develop instead
$ git checkout develop
$ python cli.py merge feature/user-auth
✅ Merged feature/user-auth into develop
📊 Risk: MEDIUM | Confirmed
```

### Workflow 2: Safe Experimentation

```bash
# 1. Validate before executing
$ python cli.py validate merge main
{
  "action_type": "merge",
  "branch_name": "main",
  "risk_level": "MEDIUM",
  "requires_confirmation": true,
  "is_protected": true
}

# 2. Use dry-run to test
$ python cli.py merge feature/test --dry-run
🔍 DRY RUN: Would execute: git merge feature/test
📊 Risk: MEDIUM | Safe to proceed

# 3. Execute after validation
$ python cli.py merge feature/test
✅ Merged feature/test into current branch
```

### Workflow 3: Quick Context Switch

```bash
# 1. Stash current work
$ python cli.py stash
✅ Stashed changes
📊 Risk: LOW

# 2. Switch to another branch
$ git checkout hotfix/critical-bug

# 3. Work on hotfix...

# 4. Return and restore work
$ git checkout feature/original
$ python cli.py stash --apply-after
✅ Applied stashed changes
📊 Risk: LOW
```

---

## Real-World Use Cases

### Use Case 1: Preventing Production Disasters

**Scenario:** Developer accidentally tries to force push to main

```bash
$ git push origin main --force
# Traditional: Executes and overwrites history ❌

# With OpsFlash governance:
$ python cli.py validate force_push main
{
  "risk_level": "HIGH",
  "requires_confirmation": true,
  "blocked": true,
  "reason": "Force push to protected branch"
}
```

**Impact:** Prevents data loss and broken production deployments

### Use Case 2: Consistent Commit Messages

**Scenario:** Team needs standardized commit messages

```bash
# Without OpsFlash: Inconsistent messages
$ git commit -m "fixed stuff"
$ git commit -m "updates"
$ git commit -m "asdf"

# With OpsFlash: AI-generated conventional commits
$ python cli.py commit
✅ "feat: add user authentication module"
✅ "fix: resolve login validation bug"
✅ "docs: update API documentation"
```

**Impact:** Better Git history, easier changelog generation, clearer code review

### Use Case 3: Team-Wide Governance

**Scenario:** Enforce branch protection across 50 developers

**Traditional Approach:**
- Configure GitHub/GitLab branch protection
- Developers can still mess up locally
- No pre-execution validation
- Reactive (blocks at push time)

**OpsFlash Approach:**
- Proactive validation before execution
- Consistent rules across all repos
- Clear error messages with suggestions
- Audit trail of all attempts

**Impact:** Reduced incidents, faster onboarding, better compliance

### Use Case 4: AI-Assisted Git Operations

**Scenario:** Junior developer needs help with Git

**Chat with Archestra + OpsFlash:**

```
User: "I need to work on the login feature"

Agent: I'll help you set up a feature branch.
       [Uses create_branch tool]
       ✅ Created: feature/login-improvements
       You're now on the new branch and ready to code!

User: "I made some changes, what should I do?"

Agent: Let me commit those for you with a good message.
       [Uses safe_commit with auto_generate]
       ✅ Committed: "feat: improve login form validation"
       Your changes are now saved!

User: "Can I merge this to main?"

Agent: ⚠️ I cannot merge directly to main (protected branch).
       Instead, I recommend:
       1. Merge to develop branch first
       2. Create a pull request for review
       3. After approval, merge to main via PR
       
       Would you like me to merge to develop?
```

**Impact:** Reduced Git mistakes, faster learning, safer operations

---

## Built for 2 Fast 2 MCP Hackathon

OpsFlash demonstrates:
- ✅ MCP-native tool design
- ✅ Archestra orchestration
- ✅ Security and governance
- ✅ Production-ready architecture
- ✅ Clear value proposition

**Tagline:** Governed Git automation via MCP and Archestra.

---

## License

MIT

---

## Acknowledgments

Built for the [2 Fast 2 MCP Hackathon](https://devpost.com/hackathons) sponsored by [Archestra.ai](https://archestra.ai)
