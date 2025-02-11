import logging
import os
import platform
import subprocess
import json
from configparser import ConfigParser

from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.common.exceptions import NoSuchDriverException


class WebScraper:
    selected_webdriver = ""
    language_module = None
    driver = None

    def __init__(self, selected_webdriver):
        print("Initializing WebScraper.")
        self.selected_webdriver = selected_webdriver
        if(selected_webdriver not in ["Chrome", "Firefox", "Edge"]):
            print(f"tookie-osint doesn't recognize webdriver {selected_webdriver}!")
            print("We're going to try to use Chrome.")
            selected_webdriver = "Chrome"

        if selected_webdriver == "Chrome":
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.headless = True
            prefs = {"profile.managed_default_content_settings.images": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument(
                "--log-level=3"
            )  # Set the log level to suppress logging
            WebScraper.driver = webdriver.Chrome(options=chrome_options)
        elif selected_webdriver == "Firefox":
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--headless")
            firefox_options.headless = True
            firefox_options.set_preference('permissions.default.image', 2)
            firefox_options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
            firefox_options.add_argument(
                "--log-level=3"
            )  # Set the log level to suppress logging
            WebScraper.driver = webdriver.Firefox(options=firefox_options)
        elif selected_webdriver == "Edge":
            edge_options = EdgeOptions()
            edge_options.use_chromium = True
            edge_options.add_argument("--headless")
            edge_options.headless = True
            prefs = {"profile.managed_default_content_settings.images": 2}
            edge_options.add_experimental_option("prefs", prefs)
            edge_options.add_argument(
                "--log-level=3"
            )  # Set the log level to suppress logging
            WebScraper.driver = webdriver.Edge(options=edge_options)
        else:
            print(WebScraper.language_module.error10)
            return None

    def get_default_browser_windows():
        try:
            browser_key = r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice"
            with os.popen(
                f'reg query "HKEY_CURRENT_USER\\{browser_key}" /v ProgId'
            ) as reg_query:
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
            # Check the BROWSER environment variable
            browser = os.getenv("BROWSER")
            if browser:
                return browser
            # Try using xdg-settings
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
        elif os_name == "Darwin":  # macOS
            return WebScraper.get_default_browser_mac()
        elif os_name == "Linux":
            return WebScraper.get_default_browser_linux()
        else:
            return "Unknown"

    # web scraper
    def scrape(self, url, target_error_message, language_module):
        try:
            # Set the log level to suppress webdriver console output
            LOGGER.setLevel(logging.ERROR)

            WebScraper.driver.get(url)
            WebScraper.driver.implicitly_wait(0.5)
            elements = WebScraper.driver.find_elements(
                By.XPATH, f'//*[contains(text(), "{target_error_message}")]'
            )
            if elements:
                there = "Yes"
                # line 133 is for dev testing
                # print(f"Found the error message: '{target_error_message} {url}'")
                return there
            else:  # f"Error message '{target_error_message}' not found on the page."
                there = "No"
                # line 138 is for dev testing
                # print(f"Error message '{target_error_message}' not found on the page. '{url}'")
                return there
        except selenium.exceptions.common.NoSuchDriverException:
            print("Uh Oh! Looks Like Your Device Does Not Support Our WebScraper :(e)")    
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
            error_message = site_data.get("error")
            
            try:
                print(f"\nChecking {site_name}...")
                
                # Attempt to access login page
                WebScraper.driver.get(login_url)
                WebScraper.driver.implicitly_wait(2)
                
                # Look for login form fields
                if "feilds" in site_data:
                    login_field = site_data["feilds"].get("login")
                    if login_field:
                        # Check if email input exists
                        try:
                            email_input = WebScraper.driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
                            results.append({
                                "site": site_name,
                                "url": login_url,
                                "found": True,
                                "status": "Email input found"
                            })
                        except:
                            results.append({
                                "site": site_name, 
                                "url": login_url,
                                "found": False,
                                "status": "No email input found"
                            })
                            
            except Exception as e:
                results.append({
                    "site": site_name,
                    "url": login_url, 
                    "found": False,
                    "status": f"Error: {str(e)}"
                })
                
        return results

