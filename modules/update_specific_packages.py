# Module for updating package.json files

import os
import json

PACKAGE_JSON = "package.json"

def update_package_json(repo, package_name, new_version):
    """Update the specified package version in package.json."""
    package_json_path = os.path.join(repo, PACKAGE_JSON)
    
    if not os.path.exists(package_json_path):
        print(f"{PACKAGE_JSON} not found in {repo}. Skipping...")
        return False

    with open(package_json_path, "r+") as file:
        data = json.load(file)

        # Update the version in either dependencies or devDependencies
        if package_name in data.get("dependencies", {}):
            data["dependencies"][package_name] = new_version
        elif package_name in data.get("devDependencies", {}):
            data["devDependencies"][package_name] = new_version
        else:
            print(f"{package_name} not found in {PACKAGE_JSON} for {repo}. Skipping...")
            return False

        # Write the updated package.json back to the file
        file.seek(0)
        json.dump(data, file, indent=2)
        file.truncate()
    
    print(f"Updated {PACKAGE_JSON} in {repo} with {package_name} version {new_version}.")
    return True
