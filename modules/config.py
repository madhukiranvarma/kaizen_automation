# This module will handle the configuration setup, either from environment variables or defaults.
import os


DEFAULT_BASE_DIR = os.getenv("BASE_DIR", os.path.expanduser("~/Documents/micro-frontend-repos"))
DEFAULT_NEW_BRANCH = os.getenv("NEW_BRANCH", "chore/falcon_version_upgrade")
DEFAULT_REGISTRY_URL = os.getenv("REGISTRY_URL", "http://10.138.33.36:4873")

def get_config():
    """Return a dictionary of configuration values."""
    return {
        "base_dir": input(f"Enter base directory (default: {DEFAULT_BASE_DIR}): ") or DEFAULT_BASE_DIR,
        "new_branch": input(f"Enter new branch name (default: {DEFAULT_NEW_BRANCH}): ") or DEFAULT_NEW_BRANCH,
        "package_name": input("Enter package name (e.g., @meesho/falcon): "),
        "package_version": input("Enter package version (e.g., 1.0.0): "),
        "registry_url": input(f"Enter registry URL (default: {DEFAULT_REGISTRY_URL}): ") or DEFAULT_REGISTRY_URL
    }

