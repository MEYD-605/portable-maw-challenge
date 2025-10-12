import sys
import os
import subprocess
import requests
import argparse

def catlab(args):
    """Re-implementation of catlab.sh in Python."""
    parser = argparse.ArgumentParser(description="Download CLAUDE.md guidelines.")
    parser.add_argument("-f", "--force", action="store_true", help="Overwrite existing file")
    parser.add_argument("url", nargs="?", default="https://gist.githubusercontent.com/nazt/3f9188eb0a5114fffa5d8cb4f14fe5a4/raw", help="Gist URL")
    
    # We need to parse only the arguments meant for catlab
    catlab_args = parser.parse_args(args)

    target_file = "CLAUDE.md"
    print(f"📥 Downloading CLAUDE.md from {catlab_args.url}...")

    if os.path.exists(target_file) and not catlab_args.force:
        print(f"Error: {target_file} already exists. Use --force to overwrite.")
        sys.exit(1)

    try:
        response = requests.get(catlab_args.url)
        response.raise_for_status()
        with open(target_file, 'w') as f:
            f.write(response.text)
        print(f"✅ {target_file} created successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: maw <command> [args...]")
        sys.exit(1)

    command = sys.argv[1]
    command_args = sys.argv[2:]

    if command == "catlab":
        catlab(command_args)
    else:
        # Keep the old logic for other potential shell scripts
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        script_path = os.path.join(repo_root, 'scripts', f"{command}.sh")
        if not os.path.exists(script_path):
            print(f"Error: Command '{command}' not found or not implemented in cli.py.")
            sys.exit(1)
        
        executable_command = ["bash", script_path] + command_args
        try:
            subprocess.run(executable_command, check=True, cwd=repo_root)
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"Error executing script for command '{command}': {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()