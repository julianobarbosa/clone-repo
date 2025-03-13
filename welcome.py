import json
import logging
from datetime import datetime
import subprocess

class WelcomeConfigHandler:
    def __init__(self):
        self.config = self._load_config()
        self._setup_logging()

    def _load_config(self):
        try:
            with open("welcomeconfig.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error("Config file not found.")
            raise

    def _setup_logging(self):
        logging.basicConfig(
            level=self.config["logging"]["level"],
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename=self.config["logging"]["file"]
        )

    def clone_repository(self, repository_url):
        repo_path = self.config["repository_path"]
        try:
            subprocess.run(["git", "clone", repository_url, repo_path], check=True)
            logging.info(f"Repository cloned to {repo_path}")
            return True
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to clone repository: {e}")
            return False

    def check_updates(self):
        current_date = datetime.now().strftime("%Y-%m-%d")
        last_check_file = "last_update_check.txt"
        
        try:
            with open(last_check_file, "r") as f:
                last_check = f.read().strip()
            if last_check == current_date:
                logging.info("Today's update check has already been performed.")
                return
        except FileNotFoundError:
            pass

        logging.info("Performing daily update check.")
        
        with open(last_check_file, "w") as f:
            f.write(current_date)

if __name__ == "__main__":
    handler = WelcomeConfigHandler()
    # Example usage:
    # handler.clone_repository("https://github.com/user/repo.git")
    # handler.check_updates()