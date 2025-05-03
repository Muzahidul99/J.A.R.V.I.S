import requests
import os
import sys
import time

UPDATE_URL = "https://raw.githubusercontent.com/YourGitHubUsername/YourRepo/main/jarvis_v1.py"  # এখানে তোমার GitHub Repo URL দিবে
LOCAL_FILE = "jarvis_v1.py"

def download_update():
    try:
        response = requests.get(UPDATE_URL)
        if response.status_code == 200:
            with open(LOCAL_FILE, "w", encoding='utf-8') as f:
                f.write(response.text)
            print("✅ Update downloaded successfully.")
            return True
        else:
            print("⚠️ No update found.")
    except Exception as e:
        print("❌ Update failed:", e)
    return False

def restart_jarvis():
    print("🔁 Restarting JARVIS...")
    time.sleep(1)
    os.execv(sys.executable, ['python'] + [LOCAL_FILE])

# Run update check
print("🔍 Checking for updates...")
if download_update():
    restart_jarvis()
else:
    print("✅ You're using the latest version.")
