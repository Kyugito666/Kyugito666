#!/usr/bin/env python3
"""
Script untuk test update_readme.py secara lokal
Tidak akan commit, hanya preview hasil
"""

import sys
import os

# Import main script
from update_readme import (
    get_all_repos,
    analyze_all_repos,
    generate_tech_stack_section
)

def test_detection(username='Kyugito666'):
    """Test language detection"""
    print("=" * 60)
    print("🔍 Testing Language Detection")
    print("=" * 60)
    
    # Test dengan token dari environment (optional)
    token = os.getenv('GITHUB_TOKEN')
    
    if token:
        print("✅ Using GITHUB_TOKEN (higher rate limit)")
    else:
        print("⚠️  No GITHUB_TOKEN found (using anonymous access)")
        print("   Set token: export GITHUB_TOKEN=your_token")
    
    print(f"\n📊 Analyzing repositories for: {username}")
    print("-" * 60)
    
    # Analyze repos
    try:
        languages = analyze_all_repos(username, token)
        
        if not languages:
            print("❌ No languages detected!")
            return False
        
        # Sort by bytes
        sorted_langs = sorted(languages.items(), key=lambda x: x[1], reverse=True)
        
        print(f"\n✅ Found {len(sorted_langs)} languages:\n")
        
        total_bytes = sum(languages.values())
        
        for i, (lang, bytes_count) in enumerate(sorted_langs, 1):
            percentage = (bytes_count / total_bytes) * 100
            bar_length = int(percentage / 2)  # Max 50 chars
            bar = "█" * bar_length + "░" * (50 - bar_length)
            
            print(f"{i:2d}. {lang:20s} {bar} {percentage:5.1f}% ({bytes_count:,} bytes)")
        
        print("\n" + "=" * 60)
        print("📝 Generated Tech Stack Preview:")
        print("=" * 60)
        
        # Generate section
        tech_section = generate_tech_stack_section([lang for lang, _ in sorted_langs])
        print(tech_section)
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_repos_fetch(username='Kyugito666'):
    """Test fetching repositories"""
    print("\n" + "=" * 60)
    print("📦 Testing Repository Fetch")
    print("=" * 60)
    
    token = os.getenv('GITHUB_TOKEN')
    
    try:
        repos = get_all_repos(username, token)
        
        print(f"\n✅ Found {len(repos)} repositories\n")
        
        # Show first 10
        print("First 10 repositories:")
        for i, repo in enumerate(repos[:10], 1):
            fork_status = "🔱 Fork" if repo['fork'] else "📦 Original"
            print(f"{i:2d}. {repo['name']:30s} {fork_status}")
        
        if len(repos) > 10:
            print(f"    ... and {len(repos) - 10} more")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Run all tests"""
    print("\n" + "🧪 " * 20)
    print("   GitHub Profile Auto-Update - Local Test")
    print("🧪 " * 20 + "\n")
    
    username = 'Kyugito666'
    
    if len(sys.argv) > 1:
        username = sys.argv[1]
    
    print(f"Testing for username: {username}\n")
    
    # Run tests
    results = []
    
    results.append(("Repository Fetch", test_repos_fetch(username)))
    results.append(("Language Detection", test_detection(username)))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Summary")
    print("=" * 60)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:30s} {status}")
    
    all_passed = all(result for _, result in results)
    
    if all_passed:
        print("\n🎉 All tests passed! Ready to deploy.")
        print("\nNext steps:")
        print("  1. Commit files to GitHub")
        print("  2. Enable GitHub Actions")
        print("  3. Run workflow manually or wait for schedule")
    else:
        print("\n⚠️  Some tests failed. Check errors above.")
    
    return 0 if all_passed else 1

if __name__ == '__main__':
    sys.exit(main())
