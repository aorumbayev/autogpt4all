#!/usr/bin/env python

import argparse
import os
import subprocess
import shutil
import sys
from urllib.request import urlretrieve

# Default values
DEFAULT_MODEL_URL = "https://gpt4all.io/models/ggml-gpt4all-l13b-snoozy.bin"
PROJECTS = ["LocalAI", "Auto-GPT"]
AUTO_GPT_BRANCH = "stable"

# Argument parsing
parser = argparse.ArgumentParser(description="Manage LocalAI and Auto-GPT projects.")
parser.add_argument(
    "--custom_model_url",
    type=str,
    help="Specify a custom URL for the model download step.",
)
parser.add_argument(
    "--uninstall",
    action="store_true",
    help="Uninstall the projects from your local machine.",
)
args = parser.parse_args()

model_url = args.custom_model_url if args.custom_model_url else DEFAULT_MODEL_URL

# Uninstall
if args.uninstall:
    print("Uninstalling...")
    for project in PROJECTS:
        if os.path.isdir(project):
            shutil.rmtree(project)
    sys.exit(0)

# Extra prerequisites for macOS
if sys.platform == "darwin":
    subprocess.run(["brew", "install", "cmake", "go"])
# Extra prerequisites for Linux (assuming apt package manager)
elif sys.platform == "linux":
    subprocess.run(["sudo", "apt", "install", "-y", "cmake", "golang"])
# Extra prerequisites for Windows
elif sys.platform == "win32":
    subprocess.run(["choco", "install", "cmake", "golang"])

# Handle LocalAI
if not os.path.isdir("LocalAI"):
    subprocess.run(["git", "clone", "https://github.com/go-skynet/LocalAI"])
else:
    os.chdir("LocalAI")
    subprocess.run(["git", "pull"])
    os.chdir("..")

os.chdir("LocalAI")
subprocess.run(["make", "build"])
os.chdir("..")

# Only download the model if a custom URL is provided or if the model does not already exist
if args.custom_model_url or not os.path.isfile("LocalAI/models/gpt-3.5-turbo"):
    if sys.platform == "darwin" or sys.platform.startswith("linux"):
        subprocess.run(["wget", model_url, "-O", "LocalAI/models/gpt-3.5-turbo"])
    elif sys.platform == "win32":
        subprocess.run(["curl", "-o", "LocalAI/models/gpt-3.5-turbo", model_url])

# Handle Auto-GPT
if not os.path.isdir("Auto-GPT"):
    subprocess.run(
        [
            "git",
            "clone",
            "-b",
            AUTO_GPT_BRANCH,
            "https://github.com/Significant-Gravitas/Auto-GPT.git",
        ]
    )
    shutil.copy(".env.template", "Auto-GPT/.env")
else:
    os.chdir("Auto-GPT")
    subprocess.run(["git", "pull"])
    os.chdir("..")
