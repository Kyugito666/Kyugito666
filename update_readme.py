import requests
import re
from collections import defaultdict
import os

# Mapping bahasa ke badge dan kategori
LANGUAGE_BADGES = {
    'Python': {
        'badge': 'https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    'JavaScript': {
        'badge': 'https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black',
        'category': 'Languages & Frameworks'
    },
    'TypeScript': {
        'badge': 'https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    'Rust': {
        'badge': 'https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    'Go': {
        'badge': 'https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    'Java': {
        'badge': 'https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    'C++': {
        'badge': 'https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    'C': {
        'badge': 'https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    'C#': {
        'badge': 'https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=csharp&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    'PHP': {
        'badge': 'https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    'Ruby': {
        'badge': 'https://img.shields.io/badge/Ruby-CC342D?style=for-the-badge&logo=ruby&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    'Swift': {
        'badge': 'https://img.shields.io/badge/Swift-FA7343?style=for-the-badge&logo=swift&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    'Kotlin': {
        'badge': 'https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    'Dart': {
        'badge': 'https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    'Shell': {
        'badge': 'https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    'HTML': {
        'badge': 'https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    'CSS': {
        'badge': 'https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white',
        'category': 'Languages & Frameworks'
    },
    'Dockerfile': {
        'badge': 'https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white',
        'category': 'DevOps & Cloud'
    },
    'Makefile': {
        'badge': 'https://img.shields.io/badge/Make-427819?style=for-the-badge&logo=gnu&logoColor=white',
        'category': 'Tools & Environment'
    },
}

# Tech stack tetap (yang selalu ingin ditampilkan)
STATIC_TECH = {
    'DevOps & Cloud': [
        'https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white',
        'https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white',
        'https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white',
        'https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white',
        'https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white',
    ],
    'Tools & Environment': [
        'https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black',
        'https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white',
        'https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white',
        'https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white',
        'https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white',
        'https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white',
    ]
}

def get_all_repos(username, token=None):
    """Ambil semua repo dari user"""
    headers = {}
    if token:
        headers['Authorization'] = f'token {token}'
    
    repos = []
    page = 1
    
    while True:
        url = f'https://api.github.com/users/{username}/repos?per_page=100&page={page}'
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Error fetching repos: {response.status_code}")
            break
            
        data = response.json()
        if not data:
            break
            
        repos.extend(data)
        page += 1
    
    return repos

def get_repo_languages(username, repo_name, token=None):
    """Ambil bahasa dari sebuah repo"""
    headers = {}
    if token:
        headers['Authorization'] = f'token {token}'
    
    url = f'https://api.github.com/repos/{username}/{repo_name}/languages'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    return {}

def analyze_all_repos(username, token=None):
    """Analisa semua repo dan hitung total bytes per bahasa"""
    repos = get_all_repos(username, token)
    language_bytes = defaultdict(int)
    
    print(f"Analyzing {len(repos)} repositories...")
    
    for repo in repos:
        if not repo['fork']:  # Skip forked repos
            languages = get_repo_languages(username, repo['name'], token)
            for lang, bytes_count in languages.items():
                language_bytes[lang] += bytes_count
    
    return dict(language_bytes)

def generate_tech_stack_section(languages):
    """Generate tech stack section dengan kategori"""
    categories = defaultdict(list)
    
    # Tambahkan bahasa yang terdeteksi
    for lang in languages:
        if lang in LANGUAGE_BADGES:
            info = LANGUAGE_BADGES[lang]
            categories[info['category']].append(info['badge'])
    
    # Tambahkan static tech
    for category, badges in STATIC_TECH.items():
        categories[category].extend(badges)
    
    # Remove duplicates dan sort
    for category in categories:
        categories[category] = sorted(list(set(categories[category])))
    
    # Generate markdown
    section = "### 💻 Tech Stack & Tools\n\n"
    
    category_order = ['Languages & Frameworks', 'DevOps & Cloud', 'Tools & Environment']
    
    for category in category_order:
        if category in categories and categories[category]:
            section += f"#### {category}\n"
            section += '<p align="center">\n'
            for badge in categories[category]:
                section += f'  <img src="{badge}" alt="{category}"/>\n'
            section += '</p>\n\n'
    
    return section

def update_readme(username, token=None):
    """Update README dengan tech stack terbaru"""
    # Analisa repos
    languages = analyze_all_repos(username, token)
    
    # Sort by bytes count
    sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    print("\nDetected languages:")
    for lang, bytes_count in sorted_languages[:15]:
        print(f"  {lang}: {bytes_count:,} bytes")
    
    # Generate tech stack section
    tech_section = generate_tech_stack_section([lang for lang, _ in sorted_languages])
    
    # Read README
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace tech stack section
    pattern = r'(### 💻 Tech Stack & Tools.*?)\n---'
    replacement = tech_section + '---'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Write back
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("\n✅ README.md updated successfully!")

if __name__ == '__main__':
    username = 'Kyugito666'
    token = os.getenv('GITHUB_TOKEN')  # Optional: untuk rate limit lebih tinggi
    
    update_readme(username, token)
