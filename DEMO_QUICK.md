# 🎬 OpsFlash Demo - Quick Visual Guide

## Option 1: Automated Demo (Easiest - 2 minutes)

### Just run this:
```bash
cd ~/opsflash
./demo.sh
```

This will automatically:
- ✅ Create demo repository
- ✅ Run 5 demo commands
- ✅ Show governance in action
- ✅ Display structured logs
- ✅ Demonstrate all key features

**Perfect for screen recording!**

---

## Option 2: Manual Demo (More Control - 2 minutes)

### Terminal Setup
```bash
# Terminal 1: Demo repo
cd ~/demo-repo

# Terminal 2: OpsFlash
cd ~/opsflash
```

### Commands to Run (Copy-paste these)

#### 1. List Branches (5 sec)
```bash
python ~/opsflash/cli.py list-branches
```
**Shows:** Safe operation, LOW risk, structured log

#### 2. Create Branch (5 sec)
```bash
python ~/opsflash/cli.py create-branch feature/demo
```
**Shows:** Branch creation, LOW risk

#### 3. Validate Merge (5 sec)
```bash
python ~/opsflash/cli.py validate merge main
```
**Shows:** Risk assessment, protected branch detection

#### 4. Try to Merge (10 sec)
```bash
cd ~/demo-repo
git checkout main
python ~/opsflash/cli.py merge feature/demo
```
**Shows:** ❌ BLOCKED! Governance in action

#### 5. Dry-Run Commit (5 sec)
```bash
echo "test" > test.txt
git add test.txt
python ~/opsflash/cli.py commit "test" --dry-run
```
**Shows:** Simulation mode, no actual execution

---

## Option 3: Screenshot Demo (No Video - 5 minutes)

### Take 4 Screenshots:

#### Screenshot 1: Safe Operations
```bash
cd ~/opsflash
python cli.py list-branches
python cli.py create-branch feature/demo
```
📸 **Capture:** Terminal showing successful operations

#### Screenshot 2: Governance Blocking
```bash
cd ~/demo-repo
git checkout main
python ~/opsflash/cli.py merge feature/demo
```
📸 **Capture:** Error message showing blocked operation

#### Screenshot 3: Risk Validation
```bash
python ~/opsflash/cli.py validate merge main
```
📸 **Capture:** JSON output showing risk assessment

#### Screenshot 4: Architecture
- Open README.md in browser
- Scroll to architecture section
📸 **Capture:** Architecture diagram

---

## What Each Command Shows

| Command | Shows | Time |
|---------|-------|------|
| `list-branches` | Safe operation, LOW risk | 5s |
| `create-branch` | Branch creation, logging | 5s |
| `validate merge main` | Risk assessment, protected branch | 5s |
| `merge main` (blocked) | **Governance in action** 🔥 | 10s |
| `commit --dry-run` | Simulation mode | 5s |

**Total: 30 seconds of commands**

---

## Recording Tips

### Before Recording:
```bash
# Clear terminal
clear

# Increase font size
# Ctrl + Shift + + (or Cmd + + on Mac)

# Set terminal to 80x24 or larger
resize -s 24 80
```

### During Recording:
1. **Speak slowly** - Explain what you're doing
2. **Pause between commands** - Let output show
3. **Highlight key points** - Point to risk levels, blocked operations
4. **Show logs** - Emphasize structured JSON output

### After Recording:
```bash
# If using ffmpeg, stop with Ctrl+C
# Video saved as opsflash-demo.mp4
```

---

## Quick Test (30 seconds)

Run this to verify everything works:

```bash
cd ~/opsflash
./demo.sh
```

If you see:
- ✅ Branches listed
- ✅ Branch created
- ✅ Risk validation shown
- ✅ Merge blocked
- ✅ Dry-run simulated

**You're ready to record!** 🎬

---

## Upload Options

### Option A: YouTube (Unlisted)
1. Go to https://youtube.com/upload
2. Upload video
3. Set to "Unlisted"
4. Copy link

### Option B: Streamable (No Account)
1. Go to https://streamable.com
2. Upload video
3. Copy link

### Option C: Vimeo
1. Go to https://vimeo.com/upload
2. Upload video
3. Copy link

---

## Add to Submission

### 1. Update README
```bash
cd ~/opsflash
nano README.md
```

Add at the top:
```markdown
## 🎥 Demo Video

Watch OpsFlash in action: [Demo Video](YOUR_VIDEO_LINK)
```

### 2. Commit and Push
```bash
git add README.md demo.sh DEMO_SCRIPT.md DEMO_QUICK.md
git commit -m "docs: add demo materials"
git push origin main
```

### 3. Submit to Hackathon
- **Project Name:** OpsFlash
- **Tagline:** Governed Git automation via MCP and Archestra
- **GitHub:** https://github.com/Tasfia-17/OpsFlash
- **Demo Video:** [Your link]
- **Description:** (Copy from README)

---

## Troubleshooting

### "Command not found"
```bash
# Make sure you're in the right directory
cd ~/opsflash
python3 cli.py list-branches
```

### "Git not initialized"
```bash
# Create demo repo
cd ~
mkdir demo-repo
cd demo-repo
git init
echo "# Demo" > README.md
git add .
git commit -m "init"
git branch -M main
```

### "Module not found"
```bash
# Install dependencies
cd ~/opsflash
pip install -r requirements.txt
```

---

## Time Estimate

- **Setup:** 2 min
- **Practice:** 5 min
- **Record:** 10 min (2-3 takes)
- **Upload:** 3 min
- **Submit:** 5 min
- **Total:** 25 minutes

**You have 75 minutes remaining - plenty of time!** ⏰

---

## Ready? Let's Go! 🚀

1. Run `./demo.sh` to test
2. Practice your narration
3. Record the demo
4. Upload and submit

**Good luck!** 🏆
