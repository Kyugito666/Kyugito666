# 🤖 GitHub Profile Auto-Update System

<div align="center">

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Automation](https://img.shields.io/badge/Automation-FF6B6B?style=for-the-badge&logo=automation&logoColor=white)

**Sistem otomatis untuk update Tech Stack di GitHub Profile README**

[Quick Start](#-quick-start) • [Features](#-features) • [Installation](#-installation) • [Configuration](#-configuration) • [Docs](#-documentation)

</div>

---

## 📖 Overview

System ini secara otomatis mendeteksi bahasa pemrograman dari semua repository Anda dan meng-update section Tech Stack di profile README. Tidak perlu lagi manual update setiap kali ada repo baru!

### 🎯 Problem yang Diselesaikan

❌ **Manual update membosankan**
- Setiap repo baru harus manual tambah badge
- Lupa update kalau belajar tech baru
- Tidak konsisten dengan repo aktual

✅ **Auto-update solution**
- Deteksi otomatis dari semua repo
- Update sesuai jadwal (daily/weekly)
- Selalu sync dengan repo terbaru
- Zero maintenance

---

## ✨ Features

### Core Features
- 🔍 **Auto Language Detection** - Scan semua repository dan detect bahasa
- 📊 **Smart Categorization** - Group tech stack by category (Languages, DevOps, Tools)
- 🎨 **Beautiful Badges** - Generate professional badges otomatis
- ⏰ **Scheduled Updates** - Run otomatis sesuai jadwal (default: daily)
- 🚀 **Manual Trigger** - Bisa trigger update kapan saja
- 🔄 **Smart Filtering** - Skip forked repos, ignore certain languages

### Advanced Features
- 📈 **Usage Statistics** - Hitung bytes per bahasa
- 🏷️ **Custom Categories** - Bisa buat kategori sendiri
- 🎛️ **Configurable** - Semua aspek bisa di-customize
- 📝 **Detailed Logging** - Track semua changes
- 🔐 **Secure** - Pakai GitHub token otomatis, no secrets needed

---

## 🚀 Quick Start

### Prerequisites
- GitHub Account
- Repository profile (nama: `username/username`)
- 5 menit waktu setup

### Installation

```bash
# 1. Clone atau download files
# 2. Copy files ke repository profile
# 3. Push ke GitHub
git add .
git commit -m "🤖 Setup auto-update"
git push

# 4. Enable workflow permissions di Settings → Actions
# 5. Run workflow manually atau tunggu schedule
```

Baca [QUICKSTART.md](QUICKSTART.md) untuk panduan detail step-by-step.

---

## 📁 File Structure

```
Kyugito666/                        # Profile repository
├── .github/
│   └── workflows/
│       └── update-readme.yml      # GitHub Actions workflow
├── .gitignore                     # Git ignore rules
├── README.md                      # Profile README (akan di-update)
├── update_readme.py               # Main script
├── test_local.py                  # Local testing script
├── requirements.txt               # Python dependencies
├── QUICKSTART.md                  # Quick setup guide
├── SETUP_GUIDE.md                 # Comprehensive guide
└── PROJECT_README.md              # This file
```

---

## 🔧 How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                    GitHub Actions Trigger                    │
│          (Schedule / Manual / Push to main)                  │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   Run Python Script                          │
│                  (update_readme.py)                          │
└───────────────────────────┬─────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐  ┌──────────────────┐  ┌──────────────┐
│  Fetch All   │  │  Get Languages   │  │   Calculate  │
│     Repos    │─▶│   per Repo       │─▶│  Total Bytes │
└──────────────┘  └──────────────────┘  └──────┬───────┘
                                                │
                                                ▼
                                        ┌──────────────┐
                                        │   Generate   │
                                        │  Badge List  │
                                        └──────┬───────┘
                                                │
                                                ▼
                                        ┌──────────────┐
                                        │    Update    │
                                        │  README.md   │
                                        └──────┬───────┘
                                                │
                                                ▼
                                        ┌──────────────┐
                                        │   Commit &   │
                                        │     Push     │
                                        └──────────────┘
```

### Detailed Flow

1. **Trigger**: GitHub Actions diaktifkan (schedule/manual/push)
2. **Fetch Repos**: Ambil semua public repositories via GitHub API
3. **Get Languages**: Untuk setiap repo, ambil language statistics
4. **Calculate**: Hitung total bytes per bahasa across all repos
5. **Generate**: Buat badge list berdasarkan detection + static tech
6. **Categorize**: Group badges by category (Languages/DevOps/Tools)
7. **Update**: Replace section di README dengan yang baru
8. **Commit**: Auto-commit dan push changes ke main branch

---

## ⚙️ Configuration

### Workflow Schedule

Edit `.github/workflows/update-readme.yml`:

```yaml
on:
  schedule:
    # Daily at 00:00 UTC (default)
    - cron: '0 0 * * *'
    
    # Alternative schedules:
    # - cron: '0 */6 * * *'    # Every 6 hours
    # - cron: '0 0 * * 0'      # Weekly (Sunday)
    # - cron: '0 0 1 * *'      # Monthly (1st day)
```

### Add New Language

Edit `update_readme.py`, section `LANGUAGE_BADGES`:

```python
LANGUAGE_BADGES = {
    'Python': {
        'badge': 'https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    # Add your language here:
    'YourLanguage': {
        'badge': 'https://img.shields.io/badge/YourLang-COLOR?style=for-the-badge&logo=icon&logoColor=white',
        'category': 'Languages & Frameworks'
    },
}
```

**Find badges at:**
- [shields.io](https://shields.io/)
- [simpleicons.org](https://simpleicons.org/)

### Add Static Tech Stack

Edit `update_readme.py`, section `STATIC_TECH`:

```python
STATIC_TECH = {
    'DevOps & Cloud': [
        'https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white',
        # Add more DevOps tech
    ],
    'Tools & Environment': [
        'https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black',
        # Add more tools
    ]
}
```

### Ignore Certain Languages

```python
# In update_readme.py, add this function:
IGNORED_LANGUAGES = ['Jupyter Notebook', 'JSON', 'XML']

def analyze_all_repos(username, token=None):
    # ... existing code ...
    
    # Filter ignored languages
    language_bytes = {k: v for k, v in language_bytes.items() 
                     if k not in IGNORED_LANGUAGES}
    
    return language_bytes
```

### Exclude Repositories

```python
# In update_readme.py, modify get_all_repos:
def get_all_repos(username, token=None):
    # ... existing code ...
    
    # Exclude specific repos
    exclude_repos = ['old-project', 'test-repo', 'archived-stuff']
    repos = [r for r in repos if r['name'] not in exclude_repos]
    
    return repos
```

---

## 📊 Language Detection Details

### How Languages Are Detected

1. **GitHub API**: Menggunakan `/repos/{owner}/{repo}/languages` endpoint
2. **Byte Count**: Menghitung total bytes per bahasa di semua files
3. **Aggregation**: Sum bytes dari semua repos
4. **Ranking**: Sort by total bytes (descending)

### Example Output

```
Analyzing 50 repositories...

Detected languages:
  Python: 1,234,567 bytes
  JavaScript: 987,654 bytes
  TypeScript: 456,789 bytes
  Rust: 234,567 bytes
  Shell: 123,456 bytes
```

### What's Counted

✅ **Included:**
- All non-fork repositories
- All language files in main branch
- Vendored code (optional, controlled by .gitattributes)

❌ **Excluded:**
- Forked repositories (by default)
- Languages in `IGNORED_LANGUAGES` list
- Documentation files (if configured)

---

## 🧪 Testing

### Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Run test script
python test_local.py

# With GitHub token (optional, for higher rate limit)
export GITHUB_TOKEN=ghp_your_token_here
python test_local.py

# Test for different user
python test_local.py other_username
```

### Test Output

```
🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 
   GitHub Profile Auto-Update - Local Test
🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 🧪 

============================================================
📦 Testing Repository Fetch
============================================================

✅ Found 50 repositories

First 10 repositories:
 1. awesome-project              📦 Original
 2. automation-scripts           📦 Original
 3. docker-compose-files         📦 Original
...

============================================================
📊 Test Summary
============================================================
Repository Fetch               ✅ PASS
Language Detection             ✅ PASS

🎉 All tests passed! Ready to deploy.
```

### Manual Test in GitHub Actions

1. Go to repository → Actions tab
2. Select "Update README with Latest Tech Stack"
3. Click "Run workflow"
4. Select branch: `main`
5. Click "Run workflow" button
6. Wait ~30 seconds for completion
7. Check the commit in recent history

---

## 🔐 Security & Permissions

### Required Permissions

#### Workflow Permissions
- ✅ **Read**: Repository content
- ✅ **Write**: Commit to main branch
- ✅ **API Access**: GitHub API for language data

**Setup:**
1. Repository Settings → Actions → General
2. Workflow permissions → "Read and write permissions"
3. Save

#### API Token

**Automatic Token (Recommended):**
- Uses `${{ secrets.GITHUB_TOKEN }}` automatically
- No setup needed
- Rate limit: 5,000 requests/hour

**Personal Token (Optional):**
Only needed if you want higher rate limits or access private repos.

```yaml
# In workflow file:
env:
  GITHUB_TOKEN: ${{ secrets.MY_PERSONAL_TOKEN }}
```

### Security Best Practices

✅ **What we do:**
- Use GitHub's automatic token
- Read-only access to public data
- Write only to own repository
- No secrets stored in code
- Bot commits clearly labeled
- `[skip ci]` to prevent loops

❌ **What we DON'T do:**
- No access to private repos (unless you add PAT)
- No access to other users' repos
- No sensitive data in commits
- No third-party API calls

---

## 📈 Performance & Rate Limits

### GitHub API Rate Limits

| Authentication | Rate Limit | When Used |
|----------------|------------|-----------|
| Unauthenticated | 60/hour | Without token |
| GitHub Actions Token | 5,000/hour | Default (recommended) |
| Personal Access Token | 5,000/hour | Optional |

### Script Performance

**Typical execution:**
- 10 repos: ~5 seconds
- 50 repos: ~15 seconds
- 100 repos: ~30 seconds

**Optimization tips:**
- Cache results between runs
- Filter out unnecessary repos
- Use conditional updates

### Workflow Efficiency

```yaml
# Add timeout to prevent hanging
jobs:
  update-readme:
    timeout-minutes: 5  # Kill after 5 minutes
```

---

## 🐛 Troubleshooting

### Common Issues

<details>
<summary><b>❌ Workflow tidak muncul di Actions</b></summary>

**Penyebab:**
- File tidak di path yang benar
- Syntax error di YAML

**Solusi:**
1. Pastikan file di `.github/workflows/update-readme.yml`
2. Validate YAML syntax: https://www.yamllint.com/
3. Check Actions tab untuk error messages
</details>

<details>
<summary><b>❌ Permission denied saat commit</b></summary>

**Penyebab:**
- Workflow permissions tidak enabled

**Solusi:**
1. Settings → Actions → General
2. Workflow permissions
3. Select "Read and write permissions"
4. Save
</details>

<details>
<summary><b>❌ Rate limit exceeded</b></summary>

**Penyebab:**
- Terlalu banyak requests dalam 1 jam
- Running workflow too frequently

**Solusi:**
1. Script sudah pakai `GITHUB_TOKEN` otomatis
2. Kurangi frekuensi schedule
3. Add retry logic with backoff
</details>

<details>
<summary><b>❌ Bahasa tidak terdeteksi</b></summary>

**Penyebab:**
- Bahasa belum ada di dictionary
- File terlalu kecil (< 1000 bytes)

**Solusi:**
1. Tambah bahasa ke `LANGUAGE_BADGES`
2. Lower minimum threshold
3. Check GitHub's language detection
</details>

<details>
<summary><b>❌ README tidak ter-update</b></summary>

**Penyebab:**
- Regex pattern tidak match
- Section marker berubah

**Solusi:**
1. Pastikan marker `### 💻 Tech Stack & Tools` ada
2. Check logs di Actions untuk error
3. Test regex pattern locally
</details>

### Debug Mode

Enable debug logging in workflow:

```yaml
- name: Update README
  env:
    ACTIONS_STEP_DEBUG: true
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: python update_readme.py
```

---

## 📚 Documentation

| File | Description |
|------|-------------|
| [QUICKSTART.md](QUICKSTART.md) | 5-minute setup guide |
| [SETUP_GUIDE.md](SETUP_GUIDE.md) | Comprehensive setup & config |
| [PROJECT_README.md](PROJECT_README.md) | This file - technical docs |
| `update_readme.py` | Main script with inline docs |
| `test_local.py` | Testing script |

---

## 🤝 Contributing

Contributions are welcome! Jika Anda punya improvement ideas:

### How to Contribute

1. **Fork** repository ini
2. **Create** branch: `git checkout -b feature/amazing-feature`
3. **Commit** changes: `git commit -m 'Add amazing feature'`
4. **Push** branch: `git push origin feature/amazing-feature`
5. **Open** Pull Request

### Ideas for Contributions

- 🎨 More badge designs/themes
- 📊 Visual analytics dashboard
- 🌐 Multi-language support
- 📱 Mobile app integration
- 🔔 Discord/Slack notifications
- 📈 Historical tracking
- 🎯 Smart recommendations
- 🔍 Better language detection

---

## 🎯 Roadmap

### Version 1.0 (Current)
- ✅ Basic auto-detection
- ✅ Daily scheduling
- ✅ Manual trigger
- ✅ Category grouping
- ✅ Skip forks

### Version 1.1 (Planned)
- [ ] Language percentage display
- [ ] Wakatime integration
- [ ] Private repo support
- [ ] Custom categories UI

### Version 2.0 (Future)
- [ ] Web dashboard
- [ ] Historical analytics
- [ ] Multi-profile support
- [ ] AI-powered insights

---

## 📊 Stats & Analytics

Want to see usage stats?

```python
# Add to update_readme.py:
def generate_stats_section(languages):
    total_bytes = sum(languages.values())
    total_repos = len(get_all_repos('Kyugito666'))
    
    stats = f"""
### 📊 Coding Statistics

- **Total Repositories**: {total_repos}
- **Languages Used**: {len(languages)}
- **Total Code**: {total_bytes:,} bytes
- **Most Used**: {sorted(languages.items(), key=lambda x: x[1], reverse=True)[0][0]}
    """
    return stats
```

---

## 🌟 Showcase

Profile menggunakan system ini:

- [@Kyugito666](https://github.com/Kyugito666) - Creator
- Add yours here via PR!

---

## 💬 Support

Need help? Multiple channels available:

- 🐛 **Bug Reports**: [Open Issue](https://github.com/Kyugito666/Kyugito666/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/Kyugito666/Kyugito666/discussions)
- 📧 **Email**: siti007.sj@gmail.com
- 💬 **Telegram**: [@i011100110110010101100101u](https://t.me/i011100110110010101100101u)
- 🔷 **Discord**: Kyugito666#0000

---

## 📜 License

```
MIT License

Copyright (c) 2024-2025 Kyugito666

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**TL;DR**: Free to use, modify, distribute! 🎉

---

## 🙏 Acknowledgments

Built with:
- [GitHub API](https://docs.github.com/en/rest) - Repository data
- [Shields.io](https://shields.io/) - Beautiful badges
- [GitHub Actions](https://github.com/features/actions) - Automation
- [Python Requests](https://requests.readthedocs.io/) - HTTP library

Inspired by:
- [github-readme-stats](https://github.com/anuraghazra/github-readme-stats)
- [awesome-github-profile-readme](https://github.com/abhisheknaiidu/awesome-github-profile-readme)

---

## 📞 Contact

**Kyugito666**

- 🌐 GitHub: [@Kyugito666](https://github.com/Kyugito666)
- 📧 Email: siti007.sj@gmail.com
- 💬 Telegram: [@i011100110110010101100101u](https://t.me/i011100110110010101100101u)
- 📷 Instagram: [@galangaditiao](https://instagram.com/galangaditiao)
- 🐦 X/Twitter: [@Dontsuspendpls0](https://x.com/Dontsuspendpls0)

---

<div align="center">

**⭐ Star this project if it helped you!**

Made with ❤️ and ☕ by [Kyugito666](https://github.com/Kyugito666)

[🔝 Back to Top](#-github-profile-auto-update-system)

</div>
