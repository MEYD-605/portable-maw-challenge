#!/usr/bin/env python3
import sys
import os
import subprocess
import requests
import argparse

def catlab_main():
    parser = argparse.ArgumentParser(description="Download a file from a URL.")
    parser.add_argument("url", nargs="?", default="https://gist.githubusercontent.com/nazt/3f9188eb0a5114fffa5d8cb4f14fe5a4/raw", help="The URL of the file to download.")
    parser.add_argument("-f", "--force", action="store_true", help="Overwrite existing file.")
    parser.add_argument("--dest", default="CLAUDE.md", help="The destination file path.")
    
    catlab_args = parser.parse_args()

    print(f"📥 Downloading from {catlab_args.url}...")

    if os.path.exists(catlab_args.dest) and not catlab_args.force:
        print(f"Error: {catlab_args.dest} already exists. Use --force to overwrite.")
        sys.exit(1)

    try:
        response = requests.get(catlab_args.url)
        response.raise_for_status()
        with open(catlab_args.dest, 'w') as f:
            f.write(response.text)
        print(f"✅ {catlab_args.dest} created successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    catlab_main()