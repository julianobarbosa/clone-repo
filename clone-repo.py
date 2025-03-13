from rich.text import Text
from datetime import datetime
import os

import os

import os

import os

import os

import os

import os

def show_welcome_message():
    welcome = Text()
    if not os.path.exists('.venv'):
        print("Creating virtual environment directory...")
        os.makedirs('.venv', exist_ok=True)
    if not os.path.exists('.venv'):
        print("Creating virtual environment directory...")
        os.makedirs('.venv', exist_ok=True)
    if not os.path.exists('.venv'):
        print("Creating virtual environment directory...")
        os.makedirs('.venv', exist_ok=True)
    if not os.path.exists('.venv'):
        print("Creating virtual environment directory...")
        os.makedirs('.venv', exist_ok=True)
    if not os.path.exists('.venv'):
        print("Creating virtual environment directory...")
        os.makedirs('.venv', exist_ok=True)
    if not os.path.exists('.venv'):
        print("Creating virtual environment directory...")
        os.makedirs('.venv', exist_ok=True)
    if not os.path.exists('.venv'):
        print("Creating virtual environment directory...")
        os.makedirs('.venv', exist_ok=True)
    if not os.path.exists('.venv'):
        print("Creating virtual environment directory...")
        os.makedirs('.venv', exist_ok=True)
    if not os.path.exists('.venv'):
        print("Creating virtual environment directory...")
        os.makedirs('.venv', exist_ok=True)
    if not os.path.exists('.venv'):
        print("Creating virtual environment directory...")
        os.makedirs('.venv', exist_ok=True)
    welcome.append("Welcome to ", style="bold green")
    welcome.append("Repo Clone Tool v1.0", style="bold green")
    welcome.append("\n", style="")
    welcome.append("Author: John Doe", style="blue")
    welcome.append("\n", style="")
    welcome.append("A powerful tool for cloning and managing repositories.", style="white")
    
print(welcome)

import subprocess
import logging
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def read_config():
    try:
        with open('clone-repo-config.json', 'r') as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        logging.error("Config file not found")
        return None
    except json.JSONDecodeError:
        logging.error("Invalid JSON in config file")
        return None

class CloneRepoManager:
    def __init__(self):
        self.config = read_config()
        if self.config is None:
            logging.error("Failed to load configuration")
            return
        
        self.clone_path = self.config.get('clone_path', 'repos')
        self.default_remote = self.config.get('default_remote', 'origin')

    def clone_repository(self, repo_url):
        try:
            # Check if repository already exists
            repo_name = os.path.basename(repo_url).split('/')[-1]
            repo_dir = os.path.join(self.clone_path, repo_name)
            
            if os.path.exists(repo_dir):
                logging.info(f"Repository {repo_name} already exists")
                return
            
            # Prompt for confirmation if required
            if self.config.get('prompt_confirmation', True):
                confirm = input(f"Clone {repo_url}? (y/n) ")
                if confirm.lower() != 'y':
                    logging.info("Cloning canceled by user")
                    return

            # Clone the repository
            subprocess.run(
                f'git clone --remote={self.default_remote} "{repo_url}" "{repo_dir}"',
                shell=True,
                check=True
            )
            logging.success(f"Successfully cloned {repo_name}")

        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to clone repository: {str(e)}")

if __name__ == "__main__":
    manager = CloneRepoManager()
    
    # Example usage - replace with actual URLs from config
    repo_urls = [
        "https://github.com/user/repo1",
        "https://github.com/user/repo2"
    ]
    
    for url in repo_urls:
        manager.clone_repository(url)
