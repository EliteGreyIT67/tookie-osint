
import tkinter as tk
from tkinter import ttk, scrolledtext
from modules.webscrape import WebScraper
from modules.configcheck import colorSchemeGrabber
import configparser
import re

class TookieGUI:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config/config.ini")
        self.color = colorSchemeGrabber(self.config, None)
        
        self.window = tk.Tk()
        self.window.title("Tookie OSINT GUI")
        self.window.geometry("800x600")
        
        # Create main frame
        self.main_frame = ttk.Frame(self.window, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Input frame
        self.input_frame = ttk.LabelFrame(self.main_frame, text="Target Input", padding="5")
        self.input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        
        self.target_label = ttk.Label(self.input_frame, text="Target:")
        self.target_label.grid(row=0, column=0, padx=5)
        
        self.target_entry = ttk.Entry(self.input_frame, width=50)
        self.target_entry.grid(row=0, column=1, padx=5)
        
        # Options frame
        self.options_frame = ttk.LabelFrame(self.main_frame, text="Options", padding="5")
        self.options_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        
        self.fast_mode = tk.BooleanVar()
        self.fast_check = ttk.Checkbutton(self.options_frame, text="Fast Mode", variable=self.fast_mode)
        self.fast_check.grid(row=0, column=0, padx=5)
        
        self.nsfw = tk.BooleanVar()
        self.nsfw_check = ttk.Checkbutton(self.options_frame, text="Show NSFW Sites", variable=self.nsfw)
        self.nsfw_check.grid(row=0, column=1, padx=5)
        
        # Buttons
        self.scan_button = ttk.Button(self.main_frame, text="Start Scan", command=self.start_scan)
        self.scan_button.grid(row=2, column=0, pady=10)
        
        # Results area
        self.results_frame = ttk.LabelFrame(self.main_frame, text="Results", padding="5")
        self.results_frame.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.results_text = scrolledtext.ScrolledText(self.results_frame, width=80, height=20)
        self.results_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        
    def start_scan(self):
        target = self.target_entry.get()
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, f"Starting scan for: {target}\n")
        
        email = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', target)
        if email:
            self.results_text.insert(tk.END, "Starting Email OSINT scan...\n")
            scraper = WebScraper("Chrome")
            results = scraper.email_scrape(target, None)
            
            for result in results:
                self.results_text.insert(tk.END, f"\nSite: {result['site']}\n")
                self.results_text.insert(tk.END, f"URL: {result['url']}\n")
                self.results_text.insert(tk.END, f"Found: {result['found']}\n")
                self.results_text.insert(tk.END, f"Status: {result['status']}\n")
        else:
            self.results_text.insert(tk.END, "Starting username scan...\n")
            # Implement username scanning logic here
            
    def run(self):
        self.window.mainloop()
