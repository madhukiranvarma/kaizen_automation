# Module for running shell commands
import subprocess

def run_command(command, cwd=None):
    """Run a shell command in the specified directory."""
    result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
    return result
