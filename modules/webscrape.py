import logging
import os
import platform
import subprocess
import json
from configparser import ConfigParser
import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, selected_webdriver):
        print("Initializing WebScraper.")
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def get_default_browser_windows():
        try:
            browser_key = r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice"
            with os.popen(f'reg query "HKEY_CURRENT_USER\\{browser_key}" /v ProgId') as reg_query:
                output = reg_query.read()
            browser_name = output.split()[-1].strip()
            return browser_name
        except Exception:
            return None

    def get_default_browser_mac():
        try:
            command = "osascript -e 'get id of app id \"com.apple.Safari\"'"
            output = subprocess.check_output(command, shell=True, text=True)
            if "Safari" in output:
                return "Safari"
            else:
                return "Unknown"
        except Exception:
            return None

    def get_default_browser_linux():
        try:
            browser = os.getenv("BROWSER")
            if browser:
                return browser
            xdg_browser_command = "xdg-settings get default-web-browser"
            browser = os.popen(xdg_browser_command).read().strip()
            if browser:
                return browser
            return "Unknown"
        except Exception:
            return None

    def get_default_browser():
        os_name = platform.system()
        if os_name == "Windows":
            return WebScraper.get_default_browser_windows()
        elif os_name == "Darwin":
            return WebScraper.get_default_browser_mac()
        elif os_name == "Linux":
            return WebScraper.get_default_browser_linux()
        else:
            return "Unknown"

    def scrape(self, url, target_error_message, language_module):
        try:
            response = self.session.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            text_content = soup.get_text()

            if target_error_message.lower() in text_content.lower():
                return "Yes"
            return "No"

        except Exception as e:
            print(f"{language_module.error11}{e}")
            return None

    def load_json(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
            return None
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse JSON - {e}")
            return None

    def email_scrape(email, language_module):
        """Scan email across multiple sites"""
        json_file_path = "sites/emailsites.json"
        data = WebScraper.load_json(json_file_path)
        results = []

        for site_name, site_list in data.items():
            site_data = site_list[0]
            login_url = site_data.get("login")

            try:
                print(f"\nChecking {site_name}...")
                response = self.session.get(login_url, timeout=10)
                soup = BeautifulSoup(response.text, 'html.parser')

                if "feilds" in site_data:
                    login_field = site_data["feilds"].get("login")
                    if login_field:
                        email_input = soup.find('input', {'type': 'email'})
                        results.append({
                            "site": site_name,
                            "url": login_url,
                            "found": email_input is not None,
                            "status": "Email input found" if email_input else "No email input found"
                        })

            except Exception as e:
                results.append({
                    "site": site_name,
                    "url": login_url,
                    "found": False,
                    "status": f"Error: {str(e)}"
                })

        return results