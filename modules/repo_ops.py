# this module will handle the repository operations like stashing, branching, and committing changes.

from modules.commands import run_command
from modules.update_specific_packages import update_package_json
from modules.update_registry import update_npmrc_file

def update_repo(repo, new_branch, falcon_version, registry_url):
    """Perform the necessary operations for each micro frontend repository."""
    print(f"Processing {repo}...")

    # Stash any local changes
    run_command("git stash -u", cwd=repo)

    # Check out to the develop branch
    run_command("git checkout develop", cwd=repo)

    # Pull the latest changes from develop
    run_command("git pull origin develop", cwd=repo)

    # Create a new branch
    run_command(f"git checkout -b {new_branch}", cwd=repo)

    # Update the .npmrc file to point to the correct registry
    update_npmrc_file(repo, registry_url)

    # Update the package.json file
    if not update_package_json(repo, falcon_version):
        return

    # Remove node_modules and package-lock.json
    run_command("rm -rf node_modules package-lock.json", cwd=repo)

    # Install the dependencies
    run_command("npm install", cwd=repo)

    # Stage all changes
    run_command("git add .", cwd=repo)

    # Commit the changes
    run_command(f"git commit -m 'chore: Falcon version upgrade to {falcon_version}'", cwd=repo)

    # Push the branch to origin
    run_command(f"git push origin {new_branch}", cwd=repo)

    print(f"Completed processing {repo}.")
