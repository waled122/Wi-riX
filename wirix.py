#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
# 👑 Wi-riX WordPress Exploitation Framework v5.0 👑
# 🔥 Developed by: Wi-riX | The Exploit King 🔥
# 📍 Repository: https://github.com/waled122/Wi-riX
# ============================================================

import os
import sys
import json
import time
import requests
import threading
from datetime import datetime
from urllib.parse import urljoin

VERSION = "5.0.0"
DEVELOPER = "Wi-riX"
FRAMEWORK_PATH = os.path.dirname(os.path.abspath(__file__))

# Colors for Windows
try:
    from colorama import init, Fore, Style
    init()
    R = Fore.RED
    G = Fore.GREEN
    Y = Fore.YELLOW
    B = Fore.BLUE
    C = Fore.CYAN
    W = Fore.WHITE
    RESET = Style.RESET_ALL
    BOLD = Style.BRIGHT
except:
    R = G = Y = B = C = W = RESET = BOLD = ""

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{BOLD}{C}
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║   {R}██╗    ██╗██╗██████╗ ██╗██╗  ██╗{C}    {R}███████╗██╗  ██╗██████╗ ██╗{C}         ║
║   {R}██║    ██║██║██╔══██╗██║╚██╗██╔╝{C}    {R}██╔════╝╚██╗██╔╝██╔══██╗██║{C}         ║
║   {R}██║ █╗ ██║██║██████╔╝██║ ╚███╔╝{C}     {R}█████╗   ╚███╔╝ ██████╔╝██║{C}         ║
║   {R}██║███╗██║██║██╔══██╗██║ ██╔██╗{C}     {R}██╔══╝   ██╔██╗ ██╔═══╝ ██║{C}         ║
║   {R}╚███╔███╔╝██║██║  ██║██║██╔╝ ██╗{C}    {R}███████╗██╔╝ ██╗██║     ██║{C}         ║
║   {R} ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝{C}    {R}╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝{C}         ║
║                                                                            ║
║   {W}🔥 Wi-riX WordPress Exploitation Framework {VERSION} 🔥{C}                   ║
║   {W}👑 Developer: {DEVELOPER} | Ethical Hacking Tool 👑{C}                      ║
║   {W}📦 Repository: github.com/waled122/Wi-riX{C}                               ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝{RESET}
""")

# Create necessary directories
def setup_directories():
    dirs = ['exploits', 'reports', 'shells', 'targets', 'logs', 'config', 'tests', 'docs', 'screenshots']
    for d in dirs:
        os.makedirs(os.path.join(FRAMEWORK_PATH, d), exist_ok=True)

# Load exploits database
def load_exploits():
    db_path = os.path.join(FRAMEWORK_PATH, 'exploits', 'exploits_db.json')
    if os.path.exists(db_path):
        with open(db_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "1": {
            "name": "CVE-2026-4885 - Piotnet Addons RCE",
            "cve": "CVE-2026-4885",
            "risk": "Critical",
            "check": "/wp-content/plugins/piotnet-addons-for-elementor-pro/",
            "type": "upload"
        }
    }

# Scan targets
def scan_targets(targets_file):
    if not os.path.exists(targets_file):
        print(f"{R}[-] File not found: {targets_file}{RESET}")
        return []
    
    with open(targets_file, 'r', encoding='utf-8') as f:
        targets = [line.strip() for line in f if line.strip()]
    
    exploits = load_exploits()
    results = []
    
    print(f"{Y}[*] Scanning {len(targets)} targets...{RESET}")
    
    for target in targets:
        print(f"{B}[*] Checking: {target}{RESET}")
        for eid, exp in exploits.items():
            url = urljoin(target, exp['check'])
            try:
                r = requests.get(url, timeout=10, verify=False)
                if r.status_code in [200, 403]:
                    print(f"{G}[+] VULNERABLE: {target} - {exp['name']}{RESET}")
                    results.append({
                        "target": target,
                        "exploit": exp['name'],
                        "cve": exp['cve'],
                        "timestamp": datetime.now().isoformat()
                    })
            except Exception as e:
                pass
    
    # Save report
    report_path = os.path.join(FRAMEWORK_PATH, 'reports', f"scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4)
    
    print(f"{G}[+] Report saved: {report_path}{RESET}")
    return results

# Create targets file
def create_targets_file():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(FRAMEWORK_PATH, 'targets', f"targets_{timestamp}.txt")
    
    print(f"{Y}[*] Enter targets (one per line). Type 'done' to finish:{RESET}")
    with open(filename, 'w', encoding='utf-8') as f:
        while True:
            target = input(f"{B}target> {RESET}")
            if target.lower() == 'done':
                break
            if target.startswith('http'):
                f.write(target + '\n')
                print(f"{G}[+] Added: {target}{RESET}")
    
    print(f"{G}[+] Targets saved: {filename}{RESET}")
    return filename

# Add new exploit
def add_exploit():
    exploits = load_exploits()
    new_id = str(len(exploits) + 1)
    
    print(f"{C}\n[+] Add New Exploit{RESET}")
    name = input(f"{B}Exploit Name: {RESET}")
    cve = input(f"{B}CVE ID: {RESET}")
    risk = input(f"{B}Risk Level: {RESET}")
    check_path = input(f"{B}Check Path: {RESET}")
    
    exploits[new_id] = {
        "name": name,
        "cve": cve,
        "risk": risk,
        "check": check_path,
        "type": "custom",
        "date_added": datetime.now().isoformat()
    }
    
    db_path = os.path.join(FRAMEWORK_PATH, 'exploits', 'exploits_db.json')
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(exploits, f, indent=4)
    
    print(f"{G}[+] Exploit added successfully!{RESET}")

# List exploits
def list_exploits():
    exploits = load_exploits()
    print(f"{C}\n📚 Available Exploits:{RESET}")
    for eid, exp in exploits.items():
        print(f"  {C}[{eid}]{RESET} {exp['name']} - {exp['cve']} [{exp['risk']}]")

# Main menu
def main_menu():
    setup_directories()
    
    while True:
        banner()
        print(f"""
{Y}╔════════════════════════════════════════════════════════════════════════╗
║                           {W}✨ MAIN MENU ✨{Y}                               ║
╠════════════════════════════════════════════════════════════════════════╣
║  {C}[1]{RESET} 🎯 Create Targets File                                      ║
║  {C}[2]{RESET} 🔍 Scan Targets                                             ║
║  {C}[3]{RESET} 📚 Exploit Database Manager                                 ║
║  {C}[4]{RESET} 📊 Show Reports                                             ║
║  {C}[5]{RESET} ❌ Exit                                                     ║
╚════════════════════════════════════════════════════════════════════════╝
""")
        choice = input(f"{B}{DEVELOPER}@framework> {RESET}")
        
        if choice == "1":
            create_targets_file()
            input(f"{Y}[!] Press Enter to continue...{RESET}")
        
        elif choice == "2":
            targets_dir = os.path.join(FRAMEWORK_PATH, 'targets')
            files = [f for f in os.listdir(targets_dir) if f.endswith('.txt')]
            if files:
                print(f"{Y}Available targets files:{RESET}")
                for i, f in enumerate(files, 1):
                    print(f"  {i}. {f}")
                try:
                    idx = int(input(f"{B}Choose: {RESET}")) - 1
                    if 0 <= idx < len(files):
                        scan_targets(os.path.join(targets_dir, files[idx]))
                except:
                    pass
            else:
                print(f"{R}[-] No targets files found. Create one first.{RESET}")
            input(f"{Y}[!] Press Enter to continue...{RESET}")
        
        elif choice == "3":
            print(f"""
{C}╔════════════════════════════════════════╗
║      📚 EXPLOIT DATABASE MANAGER      ║
╚════════════════════════════════════════╝{RESET}
{Y}[1] List Exploits{RESET}
{Y}[2] Add New Exploit{RESET}
{Y}[3] Back{RESET}
""")
            sub = input(f"{B}Choose: {RESET}")
            if sub == "1":
                list_exploits()
            elif sub == "2":
                add_exploit()
            input(f"{Y}[!] Press Enter to continue...{RESET}")
        
        elif choice == "4":
            reports_dir = os.path.join(FRAMEWORK_PATH, 'reports')
            reports = [f for f in os.listdir(reports_dir) if f.endswith('.json')]
            if reports:
                print(f"{Y}Recent reports:{RESET}")
                for r in reports[-5:]:
                    print(f"  📄 {r}")
            else:
                print(f"{R}[-] No reports found.{RESET}")
            input(f"{Y}[!] Press Enter to continue...{RESET}")
        
        elif choice == "5":
            print(f"{G}[+] Goodbye {DEVELOPER}! Stay Legendary 👑{RESET}")
            sys.exit(0)

if __name__ == "__main__":
    try:
        from colorama import init
        init()
    except:
        pass
    
    # Disable SSL warnings
    try:
        import urllib3
        urllib3.disable_warnings()
    except:
        pass
    
    main_menu()