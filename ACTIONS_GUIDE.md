# 🎬 GitHub Actions Complete Guide

## 🚀 Setup & Running GitHub Actions

### ⚡ Quick Setup (3 Steps)

#### Step 1: Upload Files
```bash
cd Kyugito666  # Your profile repo
git add .
git commit -m "🤖 Setup auto-update tech stack"
git push origin main
```

#### Step 2: Enable Permissions (CRITICAL!)
1. Go to: `https://github.com/Kyugito666/Kyugito666/settings/actions`
2. Scroll to **"Workflow permissions"**
3. Select: ✅ **"Read and write permissions"**
4. Check: ✅ **"Allow GitHub Actions to create and approve pull requests"**
5. Click **"Save"**

**🚨 WITHOUT THIS, WORKFLOW WILL FAIL!**

#### Step 3: First Manual Run
1. Go to: `https://github.com/Kyugito666/Kyugito666/actions`
2. Click: **"Update README with Latest Tech Stack"**
3. Click: **"Run workflow"** button
4. Select branch: `main`
5. Click: **"Run workflow"**
6. Wait ~30-60 seconds
7. ✅ Done!

---

## 🤖 Is It FULLY AUTO?

### ✅ YES! 100% Fully Automatic After Setup

**What Runs Automatically:**

```
┌─────────────────────────────────────────────────┐
│         AUTOMATIC TRIGGERS (No Action Needed)   │
├─────────────────────────────────────────────────┤
│                                                 │
│  ⏰ DAILY (Default)                            │
│     Every day at 00:00 UTC (07:00 WIB)         │
│     → Scans all repos                          │
│     → Updates tech stack                       │
│     → Commits automatically                    │
│                                                 │
│  📝 ON PUSH (Auto-trigger)                     │
│     When you push to main branch AND           │
│     modify workflow/script files               │
│     → Immediate update                         │
│                                                 │
│  🎯 MANUAL (Optional)                          │
│     You can trigger anytime via Actions tab    │
│     → On-demand update                         │
│                                                 │
└─────────────────────────────────────────────────┘
```

### 📅 Default Schedule

```yaml
# Runs automatically every day at 00:00 UTC
schedule:
  - cron: '0 0 * * *'
```

**Time Zones:**
- 00:00 UTC = 07:00 WIB (Jakarta)
- 00:00 UTC = 08:00 WITA (Makassar)
- 00:00 UTC = 09:00 WIT (Papua)

### 🔄 What Happens Automatically

**Every Day at 07:00 WIB:**
```
1. ✅ GitHub Actions wakes up
2. ✅ Runs update_readme.py script
3. ✅ Fetches all your repositories
4. ✅ Detects languages used
5. ✅ Calculates total bytes per language
6. ✅ Generates tech stack badges
7. ✅ Updates README.md
8. ✅ Commits with message: "🤖 Auto-update tech stack [skip ci]"
9. ✅ Pushes to main branch
10. ✅ Done! (You do NOTHING)
```

**You NEVER need to:**
- ❌ Run script manually
- ❌ Update badges
- ❌ Commit changes
- ❌ Remember to update profile

**You ONLY need to:**
- ✅ Push code to your repos (as usual)
- ✅ System detects & updates automatically!

---

## 🎯 Visual Guide: Running Actions

### 1️⃣ Access Actions Tab

```
https://github.com/Kyugito666/Kyugito666
                                    ↓
                        Click "Actions" tab
```

Screenshot locations:
```
┌────────────────────────────────────────────┐
│  < > Code   Issues   Pull requests         │
│  📊 Actions  👷 Projects  🌐 Wiki  ⚙️ Settings │  ← Click here!
└────────────────────────────────────────────┘
```

### 2️⃣ Find Your Workflow

```
Actions page:
┌────────────────────────────────────────────┐
│  All workflows                             │
│                                            │
│  🤖 Update README with Latest Tech Stack   │  ← Your workflow
│     ↳ Last run: 5 minutes ago ✅          │
│                                            │
└────────────────────────────────────────────┘
```

### 3️⃣ Manual Trigger

```
Workflow page:
┌────────────────────────────────────────────┐
│  🤖 Update README with Latest Tech Stack   │
│                                            │
│  [Run workflow ▼]  ← Click this button    │
│                                            │
│  ┌──────────────────────────────────────┐ │
│  │ Branch: main               ▼         │ │
│  │                                      │ │
│  │      [Run workflow]  ← Then this    │ │
│  └──────────────────────────────────────┘ │
└────────────────────────────────────────────┘
```

### 4️⃣ Monitor Progress

```
Running workflow:
┌────────────────────────────────────────────┐
│  🤖 Auto-update tech stack                 │
│  ⏱️  Running... (30s)                      │
│                                            │
│  ✅ Set up job                             │
│  ⏳ Checkout repository                    │
│  ⏳ Set up Python                          │
│  ⏳ Install dependencies                   │
│  ⏳ Update README                          │
│  ⏳ Commit and push                        │
└────────────────────────────────────────────┘
```

### 5️⃣ Success!

```
Completed workflow:
┌────────────────────────────────────────────┐
│  🤖 Auto-update tech stack                 │
│  ✅ Completed in 45s                       │
│                                            │
│  ✅ Set up job                             │
│  ✅ Checkout repository                    │
│  ✅ Set up Python                          │
│  ✅ Install dependencies                   │
│  ✅ Update README                          │
│  ✅ Commit and push                        │
│                                            │
│  📝 README updated with latest tech stack! │
└────────────────────────────────────────────┘
```

---

## 🔍 Checking Workflow Status

### Via Actions Tab

**All Runs:**
```
https://github.com/Kyugito666/Kyugito666/actions

Shows:
- ✅ Successful runs (green)
- 🔴 Failed runs (red)
- ⏸️ Cancelled runs (grey)
- ⏳ Running (yellow)
```

**Specific Run:**
Click any run to see:
- Detailed logs
- Execution time
- What changed
- Error messages (if any)

### Via Commits

Check recent commits:
```
https://github.com/Kyugito666/Kyugito666/commits/main

Look for:
🤖 Auto-update tech stack [skip ci]
Author: github-actions[bot]
```

### Via Email Notifications

GitHub sends email if workflow fails:
```
📧 [Kyugito666/Kyugito666] Run failed: Update README
   
Click to see error details
```

---

## ⚙️ Customizing Automation

### Change Schedule

Edit `.github/workflows/update-readme.yml`:

```yaml
on:
  schedule:
    # Choose ONE:
    
    # Every day at midnight UTC (default)
    - cron: '0 0 * * *'
    
    # Every 6 hours
    - cron: '0 */6 * * *'
    
    # Every Monday at 9 AM UTC
    - cron: '0 9 * * 1'
    
    # Every month on 1st day
    - cron: '0 0 1 * *'
    
    # Twice a day (6 AM & 6 PM UTC)
    - cron: '0 6,18 * * *'
```

**Cron Expression Guide:**
```
 ┌───────────── minute (0 - 59)
 │ ┌───────────── hour (0 - 23)
 │ │ ┌───────────── day of month (1 - 31)
 │ │ │ ┌───────────── month (1 - 12)
 │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday)
 │ │ │ │ │
 * * * * *
```

**Examples:**
- `0 0 * * *` = Daily at 00:00 UTC
- `0 */6 * * *` = Every 6 hours
- `0 0 * * 0` = Every Sunday
- `0 0 1 * *` = First day of month

**Test your cron:** https://crontab.guru/

### Disable Auto Schedule (Manual Only)

```yaml
on:
  workflow_dispatch:  # Manual trigger only
  # Remove schedule section
```

### Add More Triggers

```yaml
on:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:  # Manual
  push:
    branches: [main]
    paths:
      - '**.py'  # Trigger on Python file changes
  pull_request:
    branches: [main]  # Trigger on PR
```

---

## 🐛 Troubleshooting Actions

### ❌ Workflow Not Showing

**Problem:** Actions tab empty or workflow not listed

**Solutions:**
1. Check file location: `.github/workflows/update-readme.yml`
2. Validate YAML syntax: https://www.yamllint.com/
3. Ensure file is committed and pushed
4. Check if Actions enabled: Settings → Actions → Allow all actions

### ❌ Permission Denied Error

**Problem:** 
```
Error: Permission denied to github-actions[bot]
refusing to allow a GitHub App to create or update workflow
```

**Solution:**
Settings → Actions → General → Workflow permissions
→ Select "Read and write permissions"
→ Save

### ❌ Workflow Runs But No Commit

**Problem:** Workflow succeeds but README not updated

**Possible Causes:**
1. No changes detected (tech stack same)
2. README marker missing (`### 💻 Tech Stack & Tools`)
3. Regex pattern mismatch

**Solutions:**
1. Check workflow logs for "No changes detected"
2. Ensure README has correct section marker
3. Run test locally: `python test_local.py`

### ❌ Rate Limit Exceeded

**Problem:**
```
API rate limit exceeded
```

**Solution:**
- Should NOT happen (uses GITHUB_TOKEN with 5000 req/hour)
- If happens, wait 1 hour
- Check if running too frequently

### ❌ Script Errors

**Problem:** Python script fails

**Solutions:**
1. Check logs in Actions tab
2. Test locally: `python test_local.py`
3. Verify all files present
4. Check requirements.txt installed

---

## 📊 Monitoring & Maintenance

### Weekly Check (First Month)

```
✅ Check Actions tab for failed runs
✅ Verify commits from github-actions[bot]
✅ Confirm tech stack accurate
✅ Review workflow execution time
```

### Monthly Check (After Stable)

```
✅ Quick glance at Actions status
✅ Verify profile looks good
✅ That's it! (Fully automated)
```

### What to Monitor

**Good Signs:** ✅
- Regular commits from bot
- No failed workflows
- Tech stack matches repos
- Execution time ~30-60s

**Warning Signs:** ⚠️
- Occasional failures (check logs)
- Execution time >2 minutes
- Missing languages

**Red Flags:** 🚨
- Consistent failures
- No commits from bot
- Permission errors
- API errors

---

## 🎯 Advanced Actions Usage

### View Detailed Logs

1. Actions tab → Click workflow run
2. Click "Update README" job
3. Expand steps to see:
   - Python output
   - Detected languages
   - Files changed
   - Commit message

### Download Logs

1. Workflow run page
2. Click ⋯ (three dots)
3. "Download log archive"
4. Analyze offline

### Re-run Failed Workflow

1. Failed workflow page
2. Click "Re-run jobs"
3. Choose:
   - Re-run failed jobs
   - Re-run all jobs

### Cancel Running Workflow

1. Running workflow page
2. Click "Cancel workflow"
3. Confirm cancellation

---

## 🚀 Pro Tips

### Tip 1: First Run Test

After setup, don't wait for schedule:
```
1. Trigger manually
2. Watch it run
3. Verify success
4. Then let it auto-run
```

### Tip 2: Workflow Badge

Add workflow status badge to README:

```markdown
![Auto Update](https://github.com/Kyugito666/Kyugito666/workflows/Update%20README%20with%20Latest%20Tech%20Stack/badge.svg)
```

Shows: ![Auto Update](https://img.shields.io/badge/auto--update-passing-brightgreen)

### Tip 3: Notifications

Get notified on failures:
- Settings → Notifications
- Check "Send notifications for failed workflows"

### Tip 4: Debugging

Enable debug mode:
```yaml
env:
  ACTIONS_STEP_DEBUG: true
  ACTIONS_RUNNER_DEBUG: true
```

### Tip 5: Dry Run

Test without committing:
```yaml
- name: Update README
  run: |
    python update_readme.py
    git diff README.md  # Show changes only
    # Don't commit (remove commit steps)
```

---

## 📱 Mobile Access

### GitHub Mobile App

**iOS/Android:**
1. Install GitHub app
2. Login
3. Navigate to repository
4. Tap Actions tab
5. View/trigger workflows

**Features:**
- ✅ View workflow runs
- ✅ Trigger manual runs
- ✅ Check logs
- ✅ Get push notifications

---

## ✅ Success Checklist

**Initial Setup:**
- [ ] Files uploaded to GitHub
- [ ] Workflow permissions enabled
- [ ] First manual run successful
- [ ] README updated correctly
- [ ] Bot commit visible

**Ongoing (Automatic):**
- [ ] Workflow runs daily
- [ ] No failures in Actions
- [ ] Tech stack stays current
- [ ] Zero manual intervention needed

**You're done!** System is 100% automatic! 🎉

---

## 🎉 Congratulations!

Your GitHub profile now:
- ✅ Updates automatically every day
- ✅ Detects new languages automatically
- ✅ Maintains itself with zero effort
- ✅ Always shows accurate tech stack
- ✅ Impresses recruiters & visitors

**Set it and forget it!** 🚀

---

<div align="center">

**Questions about Actions?**

📧 siti007.sj@gmail.com  
💬 [@i011100110110010101100101u](https://t.me/i011100110110010101100101u)

</div>
