
import curses
import time
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
import os

class CliGui:
    def __init__(self):
        self.console = Console()
        self.layout = Layout()
        
    def draw_header(self):
        header_text = """
 _____ _____ _____ _   _ _____ _____      _____ _____ _____ _   _ _____ 
|_   _|     |     | | | |     |   __|    |     |   __|     | | | |_   _|
  | | |  |  |  |  | | | | | | |   __|    |  |  |__   |  |  | | |   | |  
  |_| |_____|_____|_|___|_|_|_|_____|    |_____|_____|_____|_|_|   |_|  
        """
        return Panel(header_text, title="Tookie OSINT", border_style="green")

    def draw_menu(self, options, selected=0):
        menu_items = []
        for i, option in enumerate(options):
            if i == selected:
                menu_items.append(f"[green]> {option}[/green]")
            else:
                menu_items.append(f"  {option}")
        return Panel("\n".join(menu_items), title="Menu", border_style="blue")

    def draw_status(self, status_text):
        return Panel(status_text, title="Status", border_style="yellow")

    def main_screen(self):
        options = [
            "Start Scan",
            "Web Scraping",
            "Fast Mode",
            "Show All Results",
            "Show NSFW Sites",
            "Configure Settings",
            "WebUI Mode",
            "Exit"
        ]
        
        selected = 0
        while True:
            self.console.clear()
            self.layout.split_column(
                Layout(self.draw_header(), size=10),
                Layout(self.draw_menu(options, selected)),
                Layout(self.draw_status("Use 'w' to move up, 's' to move down, Enter to select"), size=3)
            )
            self.console.print(self.layout)
            
            try:
                import sys
                import tty
                import termios
                
                def getch():
                    fd = sys.stdin.fileno()
                    old_settings = termios.tcgetattr(fd)
                    try:
                        tty.setraw(sys.stdin.fileno())
                        ch = sys.stdin.read(1)
                    finally:
                        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                    return ch
                
                key = getch()
                
                if key == 'w':  # Up
                    selected = (selected - 1) % len(options)
                elif key == 's':  # Down
                    selected = (selected + 1) % len(options)
                elif key == '\r':  # Enter
                    if options[selected] == "WebUI Mode":
                        if os.name == "nt":
                            os.system("python.exe webui/webui.py")
                        else:
                            os.system("python3 webui/webui.py")
                    return options[selected]
                
            except (ImportError, termios.error):
                # Fallback for environments where termios is not available
                key = input().lower()
                if key == 'w':
                    selected = (selected - 1) % len(options)
                elif key == 's':
                    selected = (selected + 1) % len(options)
                elif key == '':  # Enter key
                    if options[selected] == "WebUI Mode":
                        if os.name == "nt":
                            os.system("python.exe webui/webui.py")
                        else:
                            os.system("python3 webui/webui.py")
                    return options[selected]

def run_cli_gui():
    gui = CliGui()
    selected_option = gui.main_screen()
    return selected_option
