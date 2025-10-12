import sys
import os
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Usage: maw <command> [args...]")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    # This script lives in src/multi_agent_kit/cli.py.
    # The repo root is 3 levels up.
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    
    # The original shell scripts are in the root 'scripts' dir in the source
    # but get installed to .agents/scripts. We check both for robustness.
    script_path = os.path.join(repo_root, '.agents', 'scripts', f"{command}.sh")
    if not os.path.exists(script_path):
        script_path = os.path.join(repo_root, 'scripts', f"{command}.sh")

    if not os.path.exists(script_path):
        print(f"Error: Command '{command}' not found.")
        sys.exit(1)

    executable_command = ["bash", script_path] + args

    try:
        # Scripts should be run from the repo root
        process = subprocess.run(executable_command, check=True, cwd=repo_root)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)
    except FileNotFoundError:
        print(f"Error: Failed to execute '{script_path}'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
