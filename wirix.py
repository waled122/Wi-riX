#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
# 👑 WI-RIX FRAMEWORK v6.1 - MULTI-SEARCH ENGINE 👑
# 🔥 DEVELOPER: WI-RIX | THE EXPLOIT KING 🔥
# 🌍 MULTI-SEARCH | 50+ DORKS | ULTIMATE EDITION 🌍
# ============================================================

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

# ======================= [ نظام الألوان الجديد ] =======================
class Colors:
    try:
        from colorama import init, Fore, Back, Style
        init(autoreset=True)
        # الألوان الأساسية - تم تعديل الأزرق إلى سماوي فاتح
        PRIMARY = Fore.CYAN      # اللون الأساسي (بدل الأزرق)
        SUCCESS = Fore.GREEN     # أخضر للنجاح
        ERROR = Fore.RED         # أحمر للأخطاء
        WARNING = Fore.YELLOW    # أصفر للتحذيرات
        INFO = Fore.MAGENTA      # وردي للمعلومات
        TARGET = Fore.WHITE      # أبيض للأهداف
        DORK = Fore.LIGHTYELLOW_EX  # أصفر فاتح للدركات
        RESULT = Fore.LIGHTGREEN_EX # أخضر فاتح للنتائج
        
        BG_HEADER = Back.BLUE
        BG_MENU = Back.CYAN
        
        RESET = Style.RESET_ALL
        BOLD = Style.BRIGHT
        DIM = Style.DIM
        NORMAL = Style.NORMAL
    except:
        PRIMARY=SUCCESS=ERROR=WARNING=INFO=TARGET=DORK=RESULT=BG_HEADER=BG_MENU=RESET=BOLD=DIM=NORMAL=""

col = Colors()
FRAMEWORK_PATH = os.path.dirname(os.path.abspath(__file__))
DEVELOPER = "WI-RIX"
VERSION = "6.1"
EDITION = "MULTI-SEARCH"

# إنشاء المجلدات
for folder in ['exploits', 'reports', 'shells', 'targets', 'logs', 'config', 'backup']:
    os.makedirs(os.path.join(FRAMEWORK_PATH, folder), exist_ok=True)

# ======================= [ قاعدة بيانات الثغرات مع دركات كثيفة ] =======================
EXPLOITS_DB = {
    "1": {
        "name": "CVE-2026-4885 - Piotnet Addons RCE",
        "cve": "CVE-2026-4885",
        "risk": "💀 CRITICAL",
        "score": 10.0,
        "check": "/wp-content/plugins/piotnet-addons-for-elementor-pro/",
        "type": "upload_shell",
        "dorks": [
            'inurl:"/wp-content/plugins/piotnet-addons-for-elementor-pro/"',
            'intitle:"Piotnet Addons" "Elementor"',
            '"Piotnet Addons" vulnerability',
            'site:.com "/wp-content/plugins/piotnet-addons-for-elementor-pro/"',
            'inurl:"piotnet-addons-for-elementor-pro"',
            '"piotnet addons" file upload',
            'intitle:"Piotnet" "Elementor Pro"',
            'site:.org "/wp-content/plugins/piotnet-addons"',
            'inurl:"wp-content/plugins/piotnet"',
            '"CVE-2026-4885" exploit',
            'piotnet addons for elementor pro vulnerability',
            'inurl:"/piotnet-addons-for-elementor-pro/"',
            'index of /wp-content/plugins/piotnet-addons-for-elementor-pro/',
            '"Piotnet Addons" "RCE"',
            'site:.net "piotnet-addons-for-elementor-pro"'
        ]
    },
    "2": {
        "name": "CVE-2024-6386 - WP Statistics SQLi → RCE",
        "cve": "CVE-2024-6386",
        "risk": "⚠️ HIGH",
        "score": 8.5,
        "check": "/wp-content/plugins/wp-statistics/",
        "type": "sqli_rce",
        "dorks": [
            'inurl:"/wp-content/plugins/wp-statistics/"',
            'intitle:"WP Statistics" vulnerability',
            '"WP Statistics" SQL injection',
            'site:.com "wp-statistics" exploit',
            'inurl:"wp-statistics" "SQL"',
            '"WordPress Statistics" vulnerability 2024',
            'index of /wp-content/plugins/wp-statistics/',
            'site:.org "wp-statistics" CVE',
            'inurl:"wp-statistics" "CVE-2024-6386"',
            'wp-statistics plugin vulnerability',
            'intitle:"WP Statistics" "SQLi"',
            'site:.net "wp-statistics" security',
            '"WP Statistics" RCE',
            'inurl:"wp-statistics" "admin"',
            'wp-statistics database disclosure'
        ]
    },
    "3": {
        "name": "CVE-2023-5360 - Elementor Pro RCE",
        "cve": "CVE-2023-5360",
        "risk": "💀 CRITICAL",
        "score": 9.8,
        "check": "/wp-content/plugins/elementor-pro/",
        "type": "rce",
        "dorks": [
            'inurl:"/wp-content/plugins/elementor-pro/"',
            'intitle:"Elementor Pro" vulnerability',
            '"Elementor Pro" RCE',
            'site:.com "elementor-pro" exploit',
            'inurl:"elementor-pro" "CVE-2023-5360"',
            'index of /wp-content/plugins/elementor-pro/',
            '"Elementor Pro" file upload',
            'site:.org "elementor-pro" security',
            'elementor pro widget injection',
            'inurl:"elementor-pro" "template"',
            '"Elementor Pro" remote code execution',
            'site:.net "elementor-pro" vulnerability',
            'intitle:"Elementor" "Pro" exploit',
            'elementor pro ajax actions',
            'CVE-2023-5360 wordpress plugin'
        ]
    },
    "4": {
        "name": "CVE-2024-2876 - LayerSlider RFI/LFI",
        "cve": "CVE-2024-2876",
        "risk": "🟠 MEDIUM",
        "score": 6.5,
        "check": "/wp-content/plugins/LayerSlider/",
        "type": "rfi",
        "dorks": [
            'inurl:"/wp-content/plugins/LayerSlider/"',
            'intitle:"LayerSlider" vulnerability',
            '"LayerSlider" file inclusion',
            'site:.com "layerslider" RFI',
            'inurl:"layerslider" "LFI"',
            'index of /wp-content/plugins/LayerSlider/',
            '"LayerSlider" remote file inclusion',
            'site:.org "layerslider" exploit',
            'layerslider slider plugin vulnerability',
            'inurl:"layerslider" "CVE-2024-2876"',
            'intitle:"LayerSlider" "WordPress"',
            'site:.net "layerslider" security',
            'layerslider config disclosure',
            'inurl:"layerslider" "include"',
            '"LayerSlider" RCE attempt'
        ]
    },
    "5": {
        "name": "CVE-2024-22147 - Jetpack Backup RCE",
        "cve": "CVE-2024-22147",
        "risk": "💀 CRITICAL",
        "score": 9.5,
        "check": "/wp-content/plugins/jetpack/",
        "type": "rce",
        "dorks": [
            'inurl:"/wp-content/plugins/jetpack/"',
            'intitle:"Jetpack" vulnerability backup',
            '"Jetpack Backup" RCE',
            'site:.com "jetpack" CVE-2024-22147',
            'inurl:"jetpack" "backup" exploit',
            'index of /wp-content/plugins/jetpack/',
            '"Jetpack" remote code execution',
            'site:.org "jetpack" security',
            'jetpack backup restoration vulnerability',
            'inurl:"jetpack" "CVE-2024-22147"',
            'intitle:"Jetpack" "WordPress"',
            'site:.net "jetpack" exploit',
            'jetpack plugin RCE 2024',
            'inurl:"jetpack" "admin-ajax"',
            'jetpack backup privilege escalation'
        ]
    },
    "6": {
        "name": "CVE-2024-31200 - WooCommerce Payments RCE",
        "cve": "CVE-2024-31200",
        "risk": "💀 CRITICAL",
        "score": 9.9,
        "check": "/wp-content/plugins/woocommerce-payments/",
        "type": "rce",
        "dorks": [
            'inurl:"/wp-content/plugins/woocommerce-payments/"',
            'intitle:"WooCommerce Payments" vulnerability',
            '"WooCommerce Payments" RCE',
            'site:.com "woocommerce-payments" exploit',
            'inurl:"woocommerce-payments" "CVE-2024-31200"',
            'index of /wp-content/plugins/woocommerce-payments/',
            '"WooCommerce" payment gateway RCE',
            'site:.org "woocommerce-payments" security',
            'woocommerce payments plugin vulnerability',
            'inurl:"woocommerce-payments" "admin"',
            'intitle:"WooCommerce" "Payments" exploit',
            'site:.net "woocommerce-payments"',
            'woocommerce payments subscription RCE',
            'inurl:"woocommerce-payments" "api"',
            'CVE-2024-31200 wordpress exploit'
        ]
    },
    "7": {
        "name": "Wi-riX Advanced - XML-RPC Brute Force",
        "cve": "CUSTOM-001",
        "risk": "🟡 USER DEFINED",
        "score": 7.0,
        "check": "/xmlrpc.php",
        "type": "bruteforce",
        "dorks": [
            'inurl:"/xmlrpc.php" "WordPress"',
            'intitle:"WordPress" "xmlrpc.php"',
            'site:.com "/xmlrpc.php"',
            'inurl:"xmlrpc.php" "rsd"',
            '"XML-RPC" WordPress enabled',
            'site:.org "xmlrpc.php" "pingback"',
            'index of /xmlrpc.php',
            'inurl:"xmlrpc.php" "system.multicall"',
            'WordPress XML-RPC brute force',
            'site:.net "xmlrpc.php" "WordPress"',
            'intitle:"XML-RPC" "WordPress"',
            'inurl:"xmlrpc.php" "wp"',
            'WordPress xmlrpc.php exposed',
            'site:.com "xmlrpc.php" "method"',
            'XML-RPC WordPress attack surface'
        ]
    },
    "8": {
        "name": "Wi-riX Custom - wp-config.php Disclosure",
        "cve": "CUSTOM-002",
        "risk": "🔵 INFO",
        "score": 5.0,
        "check": "/wp-config.php",
        "type": "info_disclosure",
        "dorks": [
            'inurl:"wp-config.php" "DB_PASSWORD"',
            'intitle:"wp-config.php" "WordPress"',
            'site:.com wp-config.php backup',
            'inurl:"wp-config" "DB_NAME"',
            'index of /wp-config.php',
            '"wp-config.php" "DB_USER"',
            'site:.org "wp-config.php" "define"',
            'inurl:"wp-config" "mysql"',
            'WordPress config file disclosure',
            'site:.net "wp-config.php" "AUTH_KEY"',
            'inurl:"wp-config-sample.php"',
            '"wp-config.php" "database"',
            'site:.com "wp-config" "DB_HOST"',
            'index of /wp-content/wp-config.php',
            'wp-config.php backup file'
        ]
    }
}

# ======================= [ نظام البحث متعدد المحركات ] =======================
def ping_target(target):
    """فحص إذا كان الهدف حي"""
    try:
        domain = urlparse(target).netloc
        response = os.system(f"ping -c 1 -W 2 {domain} > /dev/null 2>&1")
        return response == 0
    except:
        return True

def search_google(dork, max_results=20):
    """البحث في Google"""
    results = []
    try:
        from googlesearch import search
        for url in search(dork, num_results=max_results):
            if url.startswith('http') and url not in results:
                results.append(url)
                print(f"    {col.SUCCESS}✓ Google: {url}{col.RESET}")
    except Exception as e:
        print(f"    {col.WARNING}✗ Google: {str(e)[:50]}{col.RESET}")
    return results

def search_bing(dork, max_results=20):
    """البحث في Bing"""
    results = []
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        url = f"https://www.bing.com/search?q={dork.replace(' ', '+')}&count={max_results}"
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            import re
            links = re.findall(r'<a href="(https?://[^"]+)"', r.text)
            for link in links[:max_results]:
                if link.startswith('http') and link not in results:
                    results.append(link)
                    print(f"    {col.SUCCESS}✓ Bing: {link}{col.RESET}")
    except:
        pass
    return results

def search_yahoo(dork, max_results=20):
    """البحث في Yahoo"""
    results = []
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        url = f"https://search.yahoo.com/search?p={dork.replace(' ', '+')}&n={max_results}"
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            import re
            links = re.findall(r'<a href="(https?://[^"]+)"', r.text)
            for link in links[:max_results]:
                if link.startswith('http') and 'yahoo' not in link and link not in results:
                    results.append(link)
                    print(f"    {col.SUCCESS}✓ Yahoo: {link}{col.RESET}")
    except:
        pass
    return results

def search_duckduckgo(dork, max_results=20):
    """البحث في DuckDuckGo"""
    results = []
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        url = f"https://html.duckduckgo.com/html/?q={dork.replace(' ', '+')}"
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            import re
            links = re.findall(r'<a href="(https?://[^"]+)"', r.text)
            for link in links[:max_results]:
                if link.startswith('http') and 'duckduckgo' not in link and link not in results:
                    results.append(link)
                    print(f"    {col.SUCCESS}✓ DuckDuckGo: {link}{col.RESET}")
    except:
        pass
    return results

def multi_search(dorks, max_per_engine=10):
    """البحث في جميع محركات البحث"""
    print(f"\n{col.PRIMARY}{'═' * 60}{col.RESET}")
    print(f"{col.BOLD}{col.INFO}🔍 بدء البحث متعدد المحركات...{col.RESET}")
    print(f"{col.PRIMARY}{'═' * 60}{col.RESET}")
    
    all_targets = []
    total_dorks = len(dorks)
    
    for i, dork in enumerate(dorks[:10], 1):  # حد أقصى 10 دركات
        print(f"\n{col.WARNING}[{i}/{min(total_dorks,10)}] دورة البحث عن: {col.DORK}{dork[:80]}{col.RESET}")
        print(f"{col.PRIMARY}{'─' * 50}{col.RESET}")
        
        # بحث في كل محرك
        targets = []
        targets.extend(search_google(dork, max_per_engine))
        time.sleep(1)
        targets.extend(search_bing(dork, max_per_engine))
        time.sleep(1)
        targets.extend(search_yahoo(dork, max_per_engine))
        time.sleep(1)
        targets.extend(search_duckduckgo(dork, max_per_engine))
        
        for t in targets:
            if t not in all_targets:
                all_targets.append(t)
        
        print(f"    {col.INFO}📊 إجمالي هذه الدورة: {len(targets)} هدف جديد{col.RESET}")
        time.sleep(2)  # انتظار بين الدركات عشان ما يتشبش
    
    return all_targets

# ======================= [ نظام الفحص المتقدم ] =======================
def advanced_scan(targets, exploit):
    """فحص الأهداف مع اختبار الـ ping أولاً"""
    print(f"\n{col.PRIMARY}{'═' * 60}{col.RESET}")
    print(f"{col.BOLD}{col.INFO}🔍 بدء الفحص المتقدم على {len(targets)} هدف...{col.RESET}")
    print(f"{col.PRIMARY}{'═' * 60}{col.RESET}")
    
    vulnerable = []
    total = len(targets)
    
    for i, target in enumerate(targets, 1):
        print(f"\n{col.WARNING}[{i}/{total}] فحص: {col.TARGET}{target}{col.RESET}")
        
        # Ping test
        print(f"    {col.INFO}📡 اختبار الاتصال...{col.RESET}")
        if ping_target(target):
            print(f"    {col.SUCCESS}✓ الهدف حي ومستجيب{col.RESET}")
        else:
            print(f"    {col.WARNING}⚠️ الهدف لا يستجيب للـ ping - قد يكون محجوب{col.RESET}")
        
        check_url = urljoin(target, exploit['check'])
        try:
            r = requests.get(check_url, timeout=10, verify=False, 
                            headers={"User-Agent": "Mozilla/5.0"})
            
            if r.status_code == 200:
                print(f"    {col.SUCCESS}✓ الملف أو المجلد موجود (HTTP 200){col.RESET}")
                print(f"    {col.ERROR}💀 الهدف ثغر لـ {exploit['name']}!{col.RESET}")
                vulnerable.append(target)
                
            elif r.status_code == 403:
                print(f"    {col.WARNING}⚠️ الملف موجود لكن محمي (HTTP 403) - قد يكون ثغر{col.RESET}")
                vulnerable.append(target)
                
            elif r.status_code == 404:
                print(f"    {col.ERROR}✗ الملف غير موجود (HTTP 404) - الهدف غير ثغر{col.RESET}")
            else:
                print(f"    {col.WARNING}⚠️ استجابة غير متوقعة (HTTP {r.status_code}){col.RESET}")
                
        except requests.exceptions.ConnectionError:
            print(f"    {col.ERROR}✗ فشل الاتصال - الموقع لا يستجيب{col.RESET}")
        except requests.exceptions.Timeout:
            print(f"    {col.WARNING}⚠️ انتهى الوقت - الموقع بطيء{col.RESET}")
        except Exception as e:
            print(f"    {col.ERROR}✗ خطأ: {str(e)[:50]}{col.RESET}")
        
        time.sleep(0.5)
    
    return vulnerable

# ======================= [ الوظيفة الرئيسية للبحث ] =======================
def search_for_exploits():
    """البحث عن ثغرات باستخدام جميع محركات البحث"""
    # عرض الثغرات
    print(f"\n{col.PRIMARY}{'═' * 60}{col.RESET}")
    print(f"{col.BOLD}{col.INFO}📋 قائمة الثغرات المتاحة{col.RESET}")
    print(f"{col.PRIMARY}{'═' * 60}{col.RESET}")
    
    for eid, exp in EXPLOITS_DB.items():
        print(f"\n  {col.SUCCESS}[{eid}]{col.RESET} {exp['name']}")
        print(f"      {col.WARNING}CVE: {exp['cve']} | Risk: {exp['risk']} | Score: {exp['score']}{col.RESET}")
        print(f"      {col.INFO}📁 {exp['check']}{col.RESET}")
    
    exploit_id = input(f"\n{col.INFO}[?] اختر رقم الثغرة (1-8): {col.RESET}")
    
    if exploit_id not in EXPLOITS_DB:
        print(f"{col.ERROR}✗ رقم ثغرة غير صحيح!{col.RESET}")
        return
    
    exploit = EXPLOITS_DB[exploit_id]
    
    print(f"\n{col.PRIMARY}{'═' * 60}{col.RESET}")
    print(f"{col.BOLD}{col.INFO}🎯 الثغرة المختارة: {exploit['name']}{col.RESET}")
    print(f"{col.PRIMARY}{'═' * 60}{col.RESET}")
    
    print(f"\n  {col.SUCCESS}[1]{col.RESET} 🔍 بحث تلقائي (كل محركات البحث + {len(exploit['dorks'])} درك)")
    print(f"  {col.SUCCESS}[2]{col.RESET} ✏️ إضافة دروك مخصص")
    print(f"  {col.SUCCESS}[3]{col.RESET} 📝 إضافة رابط مباشر")
    print(f"  {col.SUCCESS}[4]{col.RESET} 🔙 رجوع")
    
    choice = input(f"\n{col.INFO}[?] اختر خيار (1-4): {col.RESET}")
    
    targets = []
    
    if choice == "1":
        targets = multi_search(exploit['dorks'], max_per_engine=10)
    elif choice == "2":
        custom_dork = input(f"{col.INFO}[?] أدخل الدروك المخصص: {col.RESET}")
        targets = multi_search([custom_dork], max_per_engine=15)
    elif choice == "3":
        print(f"{col.INFO}[*] أدخل الروابط (اكتب 'done' عند الانتهاء):{col.RESET}")
        while True:
            url = input(f"{col.INFO}رابط> {col.RESET}")
            if url.lower() == 'done':
                break
            if url.startswith('http'):
                targets.append(url)
                print(f"    {col.SUCCESS}✓ تم إضافة: {url}{col.RESET}")
    elif choice == "4":
        return
    else:
        print(f"{col.ERROR}✗ خيار غير صحيح!{col.RESET}")
        return
    
    if targets:
        # حفظ الأهداف
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        targets_file = os.path.join(FRAMEWORK_PATH, 'targets', f"targets_{timestamp}.txt")
        with open(targets_file, 'w', encoding='utf-8') as f:
            for t in targets:
                f.write(t + '\n')
        
        print(f"\n{col.SUCCESS}✅ تم حفظ {len(targets)} هدف في: {targets_file}{col.RESET}")
        
        # فحص الأهداف
        vulnerable = advanced_scan(targets, exploit)
        
        if vulnerable:
            # حفظ الأهداف الثغرية
            victims_file = os.path.join(FRAMEWORK_PATH, 'targets', f"victims_{timestamp}.txt")
            with open(victims_file, 'w', encoding='utf-8') as f:
                for v in vulnerable:
                    f.write(f"{v} | {exploit['name']} | {exploit['cve']}\n")
            
            print(f"\n{col.SUCCESS}{'═' * 60}{col.RESET}")
            print(f"{col.SUCCESS}✅ تم العثور على {len(vulnerable)} هدف ثغر!{col.RESET}")
            print(f"{col.SUCCESS}{'═' * 60}{col.RESET}")
            
            for i, v in enumerate(vulnerable, 1):
                print(f"  {col.WARNING}[{i}]{col.RESET} {v}")
            
            exploit_choice = input(f"\n{col.INFO}[?] هل تريد استغلال أحد الأهداف؟ (y/n): {col.RESET}")
            if exploit_choice.lower() == 'y':
                try:
                    target_idx = int(input(f"{col.INFO}اختر رقم الهدف: {col.RESET}")) - 1
                    if 0 <= target_idx < len(vulnerable):
                        print(f"{col.WARNING}[*] جاري الاستغلال...{col.RESET}")
                except:
                    pass
        else:
            print(f"\n{col.WARNING}[!] لم يتم العثور على أهداف ثغرية!{col.RESET}")
            print(f"{col.INFO}[*] نصيحة: حاول ثغرة أخرى أو استخدم دروك مختلف{col.RESET}")
    else:
        print(f"\n{col.WARNING}[!] لم يتم العثور على أهداف!{col.RESET}")
        print(f"{col.INFO}[*] الأسباب المحتملة:{col.RESET}")
        print(f"    1. جرب مرة أخرى بعد دقيقة - محركات البحث قد تكون حدتك")
        print(f"    2. استخدم دروك مختلف من الخيار [2]")
        print(f"    3. استخدم الخيار [3] لإضافة أهداف يدوياً")
        print(f"    4. تأكد من اتصالك بالإنترنت")
    
    input(f"\n{col.WARNING}[!] اضغط Enter للمتابعة...{col.RESET}")

# ======================= [ القائمة الرئيسية ] =======================
def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{col.PRIMARY}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██╗    ██╗██╗██████╗ ██╗██╗  ██╗    ███████╗██╗  ██╗██████╗ ██╗             ║
║   ██║    ██║██║██╔══██╗██║╚██╗██╔╝    ██╔════╝╚██╗██╔╝██╔══██╗██║             ║
║   ██║ █╗ ██║██║██████╔╝██║ ╚███╔╝     █████╗   ╚███╔╝ ██████╔╝██║             ║
║   ██║███╗██║██║██╔══██╗██║ ██╔██╗     ██╔══╝   ██╔██╗ ██╔═══╝ ██║             ║
║   ╚███╔███╔╝██║██║  ██║██║██╔╝ ██╗    ███████╗██╔╝ ██╗██║     ██║             ║
║    ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝             ║
║                                                                              ║
║   🔥 WI-RIX FRAMEWORK {VERSION} - {EDITION} EDITION 🔥                              ║
║   👑 DEVELOPER: {DEVELOPER} | THE EXPLOIT KING 👑                                  ║
║   🌍 MULTI-SEARCH ENGINE | 50+ DORKS | ULTIMATE EDITION 🌍                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝{col.RESET}
""")

def print_menu():
    print(f"""
{col.PRIMARY}╔════════════════════════════════════════════════════════════════════════╗
║                         ✨ القائمة الرئيسية ✨                         ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                         ║
║  {col.SUCCESS}[1]{col.RESET} 🔍 البحث عن ثغرات (Google + Bing + Yahoo + DuckDuckGo)   ║
║      └─ استعرض كل الثغرات واختر الثغرة المناسبة                        ║
║                                                                         ║
║  {col.SUCCESS}[2]{col.RESET} 🎯 استهداف موقع مباشر                                         ║
║      └─ أدخل رابط الموقع لاختباره مباشرة                               ║
║                                                                         ║
║  {col.SUCCESS}[3]{col.RESET} 📁 فحص ملف كامل (مجموعة أهداف)                                ║
║      └─ حمل ملف أهداف وافحصهم كلهم دفعة واحدة                          ║
║                                                                         ║
║  {col.SUCCESS}[4]{col.RESET} 📊 التقارير والمخترقات                                        ║
║      └─ اعرض كل التقارير والمواقع المخترقة                             ║
║                                                                         ║
║  {col.SUCCESS}[5]{col.RESET} 🔄 تحديث الأداة                                                   ║
║      └─ تحديث إلى أحدث إصدار من GitHub                                 ║
║                                                                         ║
║  {col.SUCCESS}[6]{col.RESET} ❌ خروج                                                           ║
║                                                                         ║
╚════════════════════════════════════════════════════════════════════════╝{col.RESET}
""")

def main():
    try:
        import urllib3
        urllib3.disable_warnings()
    except:
        pass
    
    while True:
        try:
            print_banner()
            print_menu()
            choice = input(f"\n{col.INFO}{DEVELOPER}@framework> {col.RESET}")
            
            if choice == "1":
                search_for_exploits()
            elif choice == "2":
                print(f"{col.WARNING}[*] قيد التطوير...{col.RESET}")
                input(f"{col.WARNING}[!] اضغط Enter للمتابعة...{col.RESET}")
            elif choice == "3":
                print(f"{col.WARNING}[*] قيد التطوير...{col.RESET}")
                input(f"{col.WARNING}[!] اضغط Enter للمتابعة...{col.RESET}")
            elif choice == "4":
                print(f"{col.WARNING}[*] قيد التطوير...{col.RESET}")
                input(f"{col.WARNING}[!] اضغط Enter للمتابعة...{col.RESET}")
            elif choice == "5":
                print(f"{col.WARNING}[*] جاري سحب آخر التحديثات...{col.RESET}")
                os.system("git pull origin main --allow-unrelated-histories")
                input(f"{col.WARNING}[!] اضغط Enter للمتابعة...{col.RESET}")
            elif choice == "6":
                print(f"{col.SUCCESS}👑 مع السلامة يا بطل! استمر في التألق 👑{col.RESET}")
                sys.exit(0)
            else:
                print(f"{col.ERROR}✗ خيار غير صحيح!{col.RESET}")
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{col.WARNING}[!] تم الإلغاء بواسطة المستخدم{col.RESET}")
            sys.exit(0)

if __name__ == "__main__":
    main()