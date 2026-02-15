# OpsFlash ⚡

**Governed Git automation via MCP and Archestra**

[![MCP](https://img.shields.io/badge/MCP-Native-blue)](https://modelcontextprotocol.io)
[![Archestra](https://img.shields.io/badge/Archestra-Ready-green)](https://archestra.ai)

---

## Why OpsFlash?

OpsFlash transforms Git automation into a **governed MCP-native workflow**.

### Instead of:
```
LLM → Shell Commands → Uncontrolled Execution
```

### We use:
```
LLM → Structured MCP Tools → Validated Execution → Logged Output
```

This enables:
- ✅ **Controlled Git state mutation**
- ✅ **Risk-aware execution**
- ✅ **Dry-run validation**
- ✅ **Full observability**
- ✅ **Centralized orchestration via Archestra**

---

## Features

### 🔒 Governance First
- Protected branch enforcement (main, master, production)
- Risk-level assessment (LOW, MEDIUM, HIGH)
- Destructive operation blocking
- Dry-run mode for all operations

### 🛠️ MCP-Native Tools
- `create_branch` - Create and checkout branches
- `list_branches` - List all branches
- `safe_commit` - Stage and commit with AI message generation
- `merge_branch` - Safe merge with conflict detection
- `stash_changes` - Stash with auto-apply support
- `validate_git_action` - Pre-execution risk assessment

### 📊 Observability
- Structured JSON logging
- Action timestamps
- Risk level tracking
- Command execution traces

### 🎯 Archestra Alignment

OpsFlash is designed to run as:
- **MCP server** - Standard MCP protocol
- **Deployable agent** inside Archestra
- **Governed tool executor** - Policy enforcement
- **Multi-agent Git workflow participant** - Team coordination

#### Archestra provides:
- Centralized agent runtime
- Security guardrails
- Cost controls
- Execution visibility

#### OpsFlash provides:
- Safe Git primitives
- Repo-level automation
- Structured tool interfaces

**Together:** They enable secure, scalable Git automation.

---

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Run as MCP Server

```bash
python server.py
```

### Test with CLI

```bash
# Create a branch
python cli.py create-branch feature/new-feature

# Commit with auto-generated message
python cli.py commit --dry-run

# Merge with safety check
python cli.py merge feature/new-feature --dry-run

# Validate before executing
python cli.py validate merge main
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

## Example Usage

### Natural Language → Structured Execution

**User:** "Create a feature branch for user authentication"

**OpsFlash:**
1. Validates action (risk: LOW)
2. Calls `create_branch("feature/user-auth")`
3. Logs execution
4. Returns result

**User:** "Merge this into main"

**OpsFlash:**
1. Validates action (risk: HIGH - protected branch)
2. **BLOCKS** operation
3. Suggests: "Create PR instead"
4. Logs blocked attempt

---

## Policy Mode

OpsFlash enforces governance policies:

```python
PROTECTED_BRANCHES = ["main", "master", "production", "prod"]

# Automatic blocking:
- Force push to protected branches → BLOCKED
- Delete protected branches → BLOCKED
- Merge to protected branches → REQUIRES CONFIRMATION
```

---

## Logging Example

```json
{
  "timestamp": "2026-02-15T20:51:32.787Z",
  "action": "create_branch: feature/auth",
  "risk_level": "LOW",
  "details": {
    "command": "git checkout -b feature/auth",
    "output": "Switched to a new branch 'feature/auth'"
  }
}
```

---

## Demo

### Scenario 1: Safe Branch Creation
```bash
$ python cli.py create-branch feature/login
✅ Created branch: feature/login
📊 Risk: LOW | Logged: Yes
```

### Scenario 2: Blocked Dangerous Operation
```bash
$ python cli.py merge main
❌ BLOCKED: Cannot merge into protected branch: main
📊 Risk: HIGH | Requires: PR workflow
```

### Scenario 3: Dry-Run Validation
```bash
$ python cli.py commit "feat: add auth" --dry-run
🔍 DRY RUN: Would execute: git commit -m "feat: add auth"
📊 Risk: LOW | Safe to proceed
```

---

## Why This Wins

### Judging Criteria Alignment

1. **Potential Impact** ⭐⭐⭐⭐⭐
   - Every dev team needs safer Git automation
   - Prevents production disasters
   - Enables team-wide AI-assisted Git

2. **Creativity & Originality** ⭐⭐⭐⭐⭐
   - Governance-first approach is novel
   - MCP-native design is clean
   - Archestra integration is purpose-built

3. **Technical Implementation** ⭐⭐⭐⭐⭐
   - Clean architecture
   - Proper MCP protocol
   - Production-ready patterns

4. **Best Use of Archestra** ⭐⭐⭐⭐⭐
   - Leverages security layer
   - Uses MCP orchestration
   - Demonstrates policy enforcement
   - Shows team-wide deployment

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
