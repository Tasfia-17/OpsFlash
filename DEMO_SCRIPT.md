# OpsFlash Demo Script - 2 Fast 2 MCP Hackathon

**Total Time: 2 minutes**

---

## Setup (Do This Before Recording)

### 1. Create a Test Git Repository

```bash
# Create test repo
cd ~
mkdir demo-repo
cd demo-repo
git init
git config user.name "Demo User"
git config user.email "demo@opsflash.dev"

# Create initial commit
echo "# Demo Project" > README.md
git add README.md
git commit -m "initial commit"
git branch -M main
```

### 2. Open Two Terminal Windows

**Terminal 1:** Demo repository (`~/demo-repo`)  
**Terminal 2:** OpsFlash directory (`~/opsflash`)

---

## Demo Recording Script

### Scene 1: Local CLI Demo (30 seconds)

**Location:** Terminal 2 (`~/opsflash`)

```bash
# Show OpsFlash is ready
cd ~/opsflash
ls -la

# 1. List branches (safe operation)
python cli.py list-branches

# 2. Create a feature branch
python cli.py create-branch feature/demo

# 3. Validate a dangerous operation
python cli.py validate merge main

# 4. Show dry-run mode
python cli.py commit "feat: add demo" --dry-run
```

**What to say:**
> "OpsFlash provides governed Git automation through MCP. Watch how it validates operations and blocks dangerous actions."

---

### Scene 2: Governance in Action (45 seconds)

**Location:** Terminal 1 (`~/demo-repo`)

```bash
cd ~/demo-repo

# Make some changes
echo "console.log('demo');" > app.js
git add app.js

# Try to commit using OpsFlash
python ~/opsflash/cli.py commit

# Switch to main branch
git checkout main

# Try to merge (will be blocked!)
python ~/opsflash/cli.py merge feature/demo
```

**Expected output:**
```
❌ BLOCKED: Cannot merge into protected branch: main
📊 Risk Level: MEDIUM
💡 Suggestion: Create a pull request instead
```

**What to say:**
> "OpsFlash automatically protects main branches. It blocks dangerous operations and suggests safe alternatives. Every action is logged with risk levels."

---

### Scene 3: Structured Logging (30 seconds)

**Location:** Terminal 2 (`~/opsflash`)

```bash
# Show the logs from previous operations
# (They were printed to stdout during execution)

# Explain the log format
cat << 'EOF'
{
  "timestamp": "2026-02-15T21:14:57.994Z",
  "action": "create_branch: feature/demo",
  "risk_level": "LOW",
  "details": {
    "command": "git checkout -b feature/demo",
    "output": "Switched to a new branch 'feature/demo'"
  }
}
EOF
```

**What to say:**
> "Every operation generates structured JSON logs for full audit trails. This enables compliance, debugging, and analytics."

---

### Scene 4: Archestra Integration (15 seconds)

**Location:** Browser or show diagram

**Option A - If Archestra is running:**
- Open http://localhost:3000
- Show MCP Registry with OpsFlash
- Show Agent configuration
- Show chat interface

**Option B - If Archestra not running:**
- Show architecture diagram from README
- Explain integration points

**What to say:**
> "OpsFlash is designed for Archestra's MCP platform. It provides team-wide governed Git automation with centralized security, cost controls, and observability."

---

## Quick Demo (If Short on Time - 60 seconds)

**Location:** Terminal 2 (`~/opsflash`)

```bash
cd ~/opsflash

# 1. Show tools
echo "OpsFlash provides 6 MCP tools for safe Git automation:"
python cli.py

# 2. Safe operation
python cli.py create-branch feature/quick-demo

# 3. Blocked operation
python cli.py validate merge main

# 4. Show result
echo "Risk: MEDIUM | Protected: true | Blocked!"
```

**What to say:**
> "OpsFlash transforms Git automation from dangerous shell execution into governed MCP workflows. It validates every operation, blocks dangerous actions, and provides full audit trails. Perfect for teams using Archestra."

---

## Screen Recording Tips

### Tools to Use

**Linux:**
```bash
# Install SimpleScreenRecorder
sudo apt install simplescreenrecorder

# Or use OBS Studio
sudo apt install obs-studio
```

**Record with:**
```bash
# Using ffmpeg (built-in)
ffmpeg -f x11grab -s 1920x1080 -i :0.0 -f alsa -i default \
  -c:v libx264 -preset ultrafast -c:a aac \
  opsflash-demo.mp4

# Stop with Ctrl+C
```

### Recording Checklist

- [ ] Clear terminal history: `clear`
- [ ] Increase font size: `Ctrl + Shift + +`
- [ ] Hide unnecessary UI elements
- [ ] Test audio if narrating
- [ ] Do a practice run first
- [ ] Keep it under 2 minutes

---

## Alternative: Screenshot Demo

If video is difficult, create screenshots:

### Screenshot 1: CLI Usage
```bash
cd ~/opsflash
python cli.py create-branch feature/demo
# Take screenshot
```

### Screenshot 2: Blocked Operation
```bash
python cli.py validate merge main
# Take screenshot showing HIGH risk
```

### Screenshot 3: Structured Logs
```bash
# Show JSON log output
# Take screenshot
```

### Screenshot 4: Architecture
- Open README.md in browser
- Scroll to architecture diagram
- Take screenshot

---

## What to Show in Each Scene

### Scene 1: Local CLI (30s)
✅ Show OpsFlash directory structure  
✅ Run 3-4 commands  
✅ Show successful operations  

### Scene 2: Governance (45s)
✅ Create branch  
✅ Make changes  
✅ Try dangerous operation  
✅ Show it gets blocked  
✅ Show error message with suggestion  

### Scene 3: Logging (30s)
✅ Show structured JSON logs  
✅ Point out timestamp, risk level, details  
✅ Explain audit trail value  

### Scene 4: Archestra (15s)
✅ Show integration architecture  
✅ Explain team-wide deployment  
✅ Mention security + observability  

---

## Narration Script

### Opening (5 seconds)
"Hi, I'm presenting OpsFlash - governed Git automation via MCP and Archestra."

### Scene 1 (25 seconds)
"OpsFlash provides six MCP-native tools for safe Git operations. Watch as I create a branch, validate actions, and use dry-run mode. Every operation is validated before execution."

### Scene 2 (40 seconds)
"Here's the key feature: governance. I'll try to merge into the main branch - a protected branch. OpsFlash blocks the operation, shows the risk level, and suggests a safe alternative. This prevents production disasters."

### Scene 3 (25 seconds)
"Every operation generates structured JSON logs with timestamps, risk levels, and command details. This provides a complete audit trail for compliance and debugging."

### Scene 4 (15 seconds)
"OpsFlash integrates with Archestra for team-wide deployment, adding centralized security, cost controls, and observability. It transforms Git automation from dangerous shell execution into governed MCP workflows."

### Closing (10 seconds)
"OpsFlash: Safe, observable, governed Git automation. Built for MCP, designed for Archestra. Thank you!"

---

## Backup: Text-Only Demo

If recording is not possible, create a text demo:

### demo.txt
```
$ python cli.py create-branch feature/demo
✅ Created branch: feature/demo
📊 Risk: LOW | Logged: Yes

$ python cli.py validate merge main
{
  "action_type": "merge",
  "branch_name": "main",
  "risk_level": "MEDIUM",
  "requires_confirmation": true,
  "is_protected": true
}

$ python cli.py merge main
❌ BLOCKED: Cannot merge into protected branch: main
📊 Risk: MEDIUM
💡 Suggestion: Create a pull request instead

Log output:
{
  "timestamp": "2026-02-15T21:14:57.994Z",
  "action": "merge: feature/demo -> main",
  "status": "BLOCKED",
  "risk_level": "MEDIUM",
  "details": {
    "reason": "Cannot merge into protected branch: main"
  }
}
```

---

## Final Checklist

Before recording:
- [ ] Test all commands work
- [ ] Clear terminal history
- [ ] Increase font size
- [ ] Close unnecessary windows
- [ ] Prepare narration notes
- [ ] Do a practice run
- [ ] Check recording software works

During recording:
- [ ] Speak clearly and not too fast
- [ ] Pause between scenes
- [ ] Show outputs clearly
- [ ] Highlight key points

After recording:
- [ ] Review video
- [ ] Check audio quality
- [ ] Trim if needed
- [ ] Export as MP4
- [ ] Upload to YouTube/Vimeo
- [ ] Add link to submission

---

## Upload & Submit

### 1. Upload Video
```bash
# Upload to YouTube (unlisted)
# Or use: https://streamable.com (no account needed)
# Or use: https://vimeo.com
```

### 2. Add to README
```markdown
## Demo Video

Watch OpsFlash in action: [Demo Video](https://your-video-link)
```

### 3. Commit and Push
```bash
cd ~/opsflash
git add README.md
git commit -m "docs: add demo video link"
git push origin main
```

### 4. Submit to Hackathon
- Project URL: https://github.com/Tasfia-17/OpsFlash
- Demo Video: [Your video link]
- Description: Use README intro
- Built With: Python, FastMCP, Archestra

---

## Time Remaining: ~75 minutes

**Recommended timeline:**
- Setup test repo: 5 min
- Practice demo: 10 min
- Record demo: 15 min (3-4 takes)
- Upload video: 5 min
- Submit: 5 min
- **Total: 40 minutes**
- **Buffer: 35 minutes**

**You're ready! 🎬**
