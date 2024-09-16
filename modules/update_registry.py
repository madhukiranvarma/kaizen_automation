#  Module for updating .npmrc files

import os
import re

NPMRC_FILE = ".npmrc"

def update_npmrc_file(repo, registry_url):
    """Update the .npmrc file to activate the specified registry URL."""
    npmrc_path = os.path.join(repo, NPMRC_FILE)
    
    if not os.path.exists(npmrc_path):
        print(f"{NPMRC_FILE} not found in {repo}. Skipping...")
        return False

    with open(npmrc_path, "r+") as file:
        content = file.read()

        # Comment all registry lines and activate only the specified registry
        updated_content = re.sub(r'@meesho:registry=http.*', r'# \g<0>', content)  # Comment all registries
        updated_content = re.sub(rf'#\s*@meesho:registry={re.escape(registry_url)}', rf'@meesho:registry={registry_url}', updated_content)  # Uncomment the desired registry

        file.seek(0)
        file.write(updated_content)
        file.truncate()
    
    print(f"Updated {NPMRC_FILE} in {repo}.")
    return True
