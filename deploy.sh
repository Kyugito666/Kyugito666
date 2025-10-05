#!/bin/bash

# GitHub Profile Auto-Update Deployment Script
# Author: Kyugito666
# Description: Quick deployment script untuk setup auto-update system

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
REPO_NAME="Kyugito666"
BRANCH="main"

echo -e "${BLUE}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║                                                            ║"
echo "║     GitHub Profile Auto-Update Deployment Script          ║"
echo "║                                                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Function to print colored messages
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check if running in correct directory
check_directory() {
    print_info "Checking current directory..."
    
    if [ ! -d ".git" ]; then
        print_error "Not a git repository. Please run this script in your profile repository."
        exit 1
    fi
    
    CURRENT_REPO=$(basename `git rev-parse --show-toplevel`)
    if [ "$CURRENT_REPO" != "$REPO_NAME" ]; then
        print_warning "Current repo: $CURRENT_REPO"
        read -p "Continue anyway? (y/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi
    
    print_success "Directory check passed"
}

# Check if files exist
check_files() {
    print_info "Checking required files..."
    
    REQUIRED_FILES=(
        "README.md"
        "update_readme.py"
        "requirements.txt"
        ".github/workflows/update-readme.yml"
    )
    
    MISSING_FILES=()
    
    for file in "${REQUIRED_FILES[@]}"; do
        if [ ! -f "$file" ]; then
            MISSING_FILES+=("$file")
        fi
    done
    
    if [ ${#MISSING_FILES[@]} -eq 0 ]; then
        print_success "All required files present"
        return 0
    else
        print_error "Missing files:"
        for file in "${MISSING_FILES[@]}"; do
            echo "  - $file"
        done
        return 1
    fi
}

# Create directory structure
create_structure() {
    print_info "Creating directory structure..."
    
    mkdir -p .github/workflows
    
    print_success "Directory structure created"
}

# Check Python installation
check_python() {
    print_info "Checking Python installation..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version)
        print_success "Python found: $PYTHON_VERSION"
    else
        print_error "Python3 not found. Please install Python 3.7+"
        exit 1
    fi
}

# Install dependencies
install_dependencies() {
    print_info "Installing Python dependencies..."
    
    if [ -f "requirements.txt" ]; then
        pip3 install -q -r requirements.txt
        print_success "Dependencies installed"
    else
        print_warning "requirements.txt not found, skipping..."
    fi
}

# Run local test
run_test() {
    print_info "Running local test..."
    
    if [ -f "test_local.py" ]; then
        if python3 test_local.py; then
            print_success "Local test passed"
            return 0
        else
            print_error "Local test failed"
            return 1
        fi
    else
        print_warning "test_local.py not found, skipping test..."
        return 0
    fi
}

# Check git status
check_git_status() {
    print_info "Checking git status..."
    
    if [ -n "$(git status --porcelain)" ]; then
        print_warning "You have uncommitted changes:"
        git status --short
        echo
        read -p "Continue with deployment? (y/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    else
        print_success "Working tree clean"
    fi
}

# Deploy to GitHub
deploy() {
    print_info "Deploying to GitHub..."
    
    # Add all files
    git add .
    
    # Commit
    git commit -m "🤖 Setup auto-update tech stack system

- Add update_readme.py script
- Add GitHub Actions workflow
- Add documentation files
- Configure auto-update schedule" || print_warning "No changes to commit"
    
    # Push
    if git push origin $BRANCH; then
        print_success "Successfully pushed to GitHub"
    else
        print_error "Failed to push to GitHub"
        exit 1
    fi
}

# Print next steps
print_next_steps() {
    echo
    echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║                  Deployment Successful! 🎉                 ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
    echo
    echo -e "${YELLOW}📋 Next Steps:${NC}"
    echo
    echo "1️⃣  Enable Workflow Permissions:"
    echo "   → Go to: https://github.com/$REPO_NAME/$REPO_NAME/settings/actions"
    echo "   → Select: 'Read and write permissions'"
    echo "   → Save changes"
    echo
    echo "2️⃣  Test the Workflow:"
    echo "   → Go to: https://github.com/$REPO_NAME/$REPO_NAME/actions"
    echo "   → Click: 'Update README with Latest Tech Stack'"
    echo "   → Click: 'Run workflow'"
    echo "   → Wait ~30 seconds"
    echo
    echo "3️⃣  Check Your Profile:"
    echo "   → Visit: https://github.com/$REPO_NAME"
    echo "   → Verify tech stack is updated"
    echo
    echo -e "${BLUE}📚 Documentation:${NC}"
    echo "   → Quick Start: QUICKSTART.md"
    echo "   → Full Guide: SETUP_GUIDE.md"
    echo "   → Project Docs: PROJECT_README.md"
    echo
    echo -e "${GREEN}✨ Your profile will now auto-update daily! ✨${NC}"
    echo
}

# Main execution
main() {
    echo
    print_info "Starting deployment process..."
    echo
    
    # Run checks
    check_directory
    create_structure
    check_python
    
    # Check files
    if ! check_files; then
        print_error "Please ensure all required files are present"
        echo
        echo "Required files:"
        echo "  - README.md"
        echo "  - update_readme.py"
        echo "  - requirements.txt"
        echo "  - .github/workflows/update-readme.yml"
        echo
        exit 1
    fi
    
    # Install and test
    install_dependencies
    
    echo
    read -p "Run local test before deployment? (recommended) (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        if ! run_test; then
            read -p "Test failed. Continue anyway? (y/n) " -n 1 -r
            echo
            if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                exit 1
            fi
        fi
    fi
    
    # Check git and deploy
    check_git_status
    
    echo
    read -p "Ready to deploy to GitHub? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        deploy
        print_next_steps
    else
        print_info "Deployment cancelled"
        exit 0
    fi
}

# Run main function
main

exit 0
