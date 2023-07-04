###  Python script to install and run gitleaks on linux with amd64 arch

Usage:
1) Download python script to any directory
2) Run script in terminal with one required parameter 'repo_path' and - the path to git repository to check commits for hard secrets, tokens, etc.
   - example for python script inside git repo: `python3 gitleaks_linux_amd64.py '.'`
   - example with absolute path to git repo: `python3 gitleaks_linux_amd64.py /home/ububtu/work/project'`
3) Python script will install Gitleaks in `$HOME/.local/bin` if not installed (sudo password required)
4) Script will check for correct path to git repository
