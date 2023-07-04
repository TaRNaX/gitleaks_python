import subprocess
import sys
import os

version = "8.17.0"
gz_file = f"gitleaks_{version}_linux_x64.tar.gz"
gitleaks_repo = f'https://github.com/gitleaks/gitleaks/releases/download/v{version}/{gz_file}'


def install_gitleaks() -> None:
    """Download and install gitleaks to $HOME/.local/bin"""

    print(
        f'Installing Gitleaks:v{version} from GitHub, confirm with sudo password')

    subprocess.run(f'wget -c {gitleaks_repo} -O - | tar -xz gitleaks', shell=True, text=True,
                   capture_output=True, check=True)
    subprocess.run("sudo mv gitleaks $HOME/.local/bin/gitleaks", shell=True, text=True,
                   capture_output=True, check=True)
    subprocess.run("sudo chmod +x $HOME/.local/bin/gitleaks", shell=True, text=True,
                   capture_output=True, check=True)


def check_gitleaks_installed() -> None:
    """Check if gitleaks already installed in system"""

    try:
        print("Checking Gitleaks installed...")
        subprocess.run("gitleaks version", shell=True, check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:

        if "gitleaks: not found" in e.stderr.decode().strip():
            install_gitleaks()
        else:
            sys.exit(e.returncode)


def run_gitleaks_check(repo_path: str) -> None:
    """Run Gitleaks check for hardcodded sensitive data"""

    print('trying to check')
    try:
        subprocess.run(f"gitleaks detect --source . -v --report-path=logs.json",
                       shell=True, check=True, capture_output=True,)
        #    stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:

        if "not a git repository" in e.stderr.decode().strip():
            print('Error, not a Git repository')

        else:
            print('Something went wrong...')
            print(e.stderr.decode().strip())


def main() -> None:
    "Main function"

    repo_path = sys.argv[1]

    # Check for Gitleaks to be installed
    check_gitleaks_installed()

    # Scan repository for sensitive data
    run_gitleaks_check(repo_path)


if __name__ == "__main__":
    main()
