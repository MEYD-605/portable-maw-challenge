import sys
import os
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Usage: maw <command> [args...]")
        # To find the real repo root from src/multi_agent_kit, we go up three levels.
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
        scripts_dir = os.path.join(repo_root, '.agents', 'scripts')
        if os.path.exists(scripts_dir):
            available_scripts = [f.replace('.sh', '') for f in os.listdir(scripts_dir) if f.endswith('.sh')]
            print(f"Available commands: {', '.join(available_scripts)}")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    # Find the script in the .agents/scripts directory relative to the repo root
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    script_path = os.path.join(repo_root, '.agents', 'scripts', f"{command}.sh")

    if not os.path.exists(script_path):
        # Fallback for finding scripts if the structure is different than expected
        script_path = os.path.join(repo_root, 'scripts', f"{command}.sh")
        if not os.path.exists(script_path):
             print(f"Error: Command '{command}' not found.")
             sys.exit(1)

    executable_command = ["bash", script_path] + args

    try:
        # We need to run from the repo root for the scripts to work correctly
        process = subprocess.run(executable_command, check=True, cwd=repo_root)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)
    except FileNotFoundError:
        print(f"Error: Failed to execute '{script_path}'. Make sure bash is installed.")
        sys.exit(1)

if __name__ == "__main__":
    main()