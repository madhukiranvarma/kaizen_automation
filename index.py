# main.py

import os
from modules.repo_ops import update_repo
from modules.config import get_config

def main():
    config = get_config()
    base_dir = config["base_dir"]
    
    print('config:', config)
    # Iterate over each directory in the base directory
    for parent_dir in os.listdir(base_dir):
        parent_path = os.path.join(base_dir, parent_dir)
        if os.path.isdir(parent_path):
            # Inside each directory, find the actual repo
            for repo_name in os.listdir(parent_path):
                repo_path = os.path.join(parent_path, repo_name)
                if os.path.isdir(repo_path):
                    update_repo(repo_path, config["new_branch"], config["package_version"], config["registry_url"])

if __name__ == "__main__":
    main()
    print("All micro frontends processed.")
