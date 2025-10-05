# ⚡ Quick Start Guide

Panduan singkat untuk setup auto-update GitHub Profile dalam 5 menit!

## 🚀 Setup Super Cepat (5 Menit)

### 1️⃣ Download Files (1 menit)

Copy 4 files ini ke repository `Kyugito666/Kyugito666`:

```
📁 Kyugito666/
├── 📄 README.md (artifact #1)
├── 🐍 update_readme.py (artifact #2)
├── 📋 requirements.txt (artifact #5)
└── 📁 .github/
    └── 📁 workflows/
        └── ⚙️ update-readme.yml (artifact #3)
```

### 2️⃣ Enable Permissions (1 menit)

1. Buka: `https://github.com/Kyugito666/Kyugito666/settings/actions`
2. Scroll ke **"Workflow permissions"**
3. Pilih: ✅ **"Read and write permissions"**
4. Save changes

### 3️⃣ Commit & Push (1 menit)

```bash
git add .
git commit -m "🤖 Setup auto-update tech stack"
git push origin main
```

### 4️⃣ Test Run (2 menit)

1. Buka: `https://github.com/Kyugito666/Kyugito666/actions`
2. Klik: **"Update README with Latest Tech Stack"**
3. Klik: **"Run workflow"** → **"Run workflow"**
4. Tunggu ~30 detik
5. ✅ Done! Check README Anda!

---

## 🎯 Tes Lokal (Optional)

Sebelum deploy, test dulu di komputer lokal:

```bash
# Install dependencies
pip install -r requirements.txt

# Test detection
python test_local.py

# Kalau mau pakai GitHub token (optional, untuk rate limit lebih tinggi)
export GITHUB_TOKEN=ghp_your_token_here
python test_local.py
```

Output akan show:
- ✅ Repo yang terdeteksi
- ✅ Bahasa yang ditemukan
- ✅ Preview tech stack section

---

## 📝 Checklist

Sebelum deploy, pastikan:

- [ ] File structure sudah benar
- [ ] Workflow permissions enabled
- [ ] Test lokal berhasil (optional)
- [ ] README.md backup (optional)
- [ ] Commit & push semua files
- [ ] Workflow muncul di Actions tab
- [ ] Manual run berhasil

---

## ⚙️ Konfigurasi Cepat

### Ubah Jadwal Update

Edit `.github/workflows/update-readme.yml`:

```yaml
schedule:
  - cron: '0 0 * * *'    # Setiap hari jam 00:00 UTC
  # - cron: '0 */6 * * *' # Setiap 6 jam
  # - cron: '0 0 * * 0'   # Setiap minggu
```

### Tambah Bahasa Baru

Edit `update_readme.py`, tambah di `LANGUAGE_BADGES`:

```python
'NamaBahasa': {
    'badge': 'https://img.shields.io/badge/Nama-COLOR?style=for-the-badge&logo=icon&logoColor=white',
    'category': 'Languages & Frameworks'
},
```

### Tambah Tech Stack Tetap

Edit `update_readme.py`, tambah di `STATIC_TECH`:

```python
'DevOps & Cloud': [
    'https://img.shields.io/badge/NewTech-COLOR?style=for-the-badge&logo=icon&logoColor=white',
],
```

---

## 🐛 Troubleshooting Cepat

### ❌ Workflow tidak muncul
→ Pastikan file di `.github/workflows/update-readme.yml`

### ❌ Permission denied
→ Enable write permissions di Settings → Actions

### ❌ Rate limit exceeded
→ Tambah `GITHUB_TOKEN` secret (optional, biasanya tidak perlu)

### ❌ Bahasa tidak muncul
→ Tambahkan ke dictionary `LANGUAGE_BADGES`

---

## 📚 Docs Lengkap

Baca `SETUP_GUIDE.md` untuk:
- Advanced configuration
- Customization options
- Performance optimization
- Integration ideas
- Troubleshooting detail

---

## ✅ Setelah Setup Berhasil

### Auto-Update akan jalan:
- ✅ Setiap hari jam 00:00 UTC (07:00 WIB)
- ✅ Saat push ke main (file workflow/script berubah)
- ✅ Manual trigger kapan saja

### Yang di-update otomatis:
- ✅ Tech Stack & Tools (dari script)
- ✅ Most Used Languages (sudah otomatis)
- ✅ GitHub Stats (sudah otomatis)
- ✅ Contribution Graph (sudah otomatis)

---

## 🎉 Done!

Profile Anda sekarang auto-update! 

Setiap kali Anda:
- ✅ Push repo dengan bahasa baru
- ✅ Tambah code di bahasa existing
- ✅ Delete repo

Tech stack akan auto-refresh sesuai jadwal!

**No more manual updates!** 🚀

---

<div align="center">

### Butuh Bantuan?

📧 Email: siti007.sj@gmail.com
💬 Telegram: [@i011100110110010101100101u](https://t.me/i011100110110010101100101u)

**Star ⭐ repository ini jika membantu!**

</div>
