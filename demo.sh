#!/bin/bash
# OpsFlash Quick Demo Runner
# Run this to see OpsFlash in action!

set -e

echo "=========================================="
echo "  OpsFlash Demo - Governed Git Automation"
echo "=========================================="
echo ""

# Setup
echo "📁 Setting up demo repository..."
cd ~/demo-repo 2>/dev/null || (mkdir ~/demo-repo && cd ~/demo-repo && git init && git config user.name "Demo" && git config user.email "demo@opsflash.dev" && echo "# Demo" > README.md && git add . && git commit -m "init" && git branch -M main)
cd ~/demo-repo
echo "✅ Demo repo ready at ~/demo-repo"
echo ""

# Demo 1: List branches
echo "1️⃣  Listing branches (LOW risk)..."
python ~/opsflash/cli.py list-branches
echo ""
sleep 2

# Demo 2: Create branch
echo "2️⃣  Creating feature branch (LOW risk)..."
python ~/opsflash/cli.py create-branch feature/demo-$(date +%s)
echo ""
sleep 2

# Demo 3: Validate dangerous operation
echo "3️⃣  Validating merge to main (MEDIUM risk)..."
python ~/opsflash/cli.py validate merge main
echo ""
sleep 2

# Demo 4: Try to merge (will be blocked)
echo "4️⃣  Attempting to merge to main (BLOCKED!)..."
git checkout main 2>/dev/null
python ~/opsflash/cli.py merge feature/demo-* 2>&1 || echo "⚠️  Operation blocked by governance!"
echo ""
sleep 2

# Demo 5: Dry-run
echo "5️⃣  Dry-run commit (simulation mode)..."
echo "console.log('demo');" > app.js
git add app.js 2>/dev/null || true
python ~/opsflash/cli.py commit "feat: add demo" --dry-run
echo ""

echo "=========================================="
echo "  ✅ Demo Complete!"
echo "=========================================="
echo ""
echo "Key Features Demonstrated:"
echo "  ✓ Safe Git operations via MCP tools"
echo "  ✓ Risk validation (LOW/MEDIUM/HIGH)"
echo "  ✓ Protected branch enforcement"
echo "  ✓ Structured JSON logging"
echo "  ✓ Dry-run mode"
echo ""
echo "Next: Integrate with Archestra for team-wide deployment!"
echo ""
