#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
# 🔄 Wi-riX Framework Updater - التحديث التلقائي
# 👑 Developer: Wi-riX
# ============================================================

import os
import sys
import subprocess
import shutil
import requests
import json
from datetime import datetime

# ======================= [ الإعدادات ] =======================
FRAMEWORK_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GITHUB_REPO = "https://api.github.com/repos/waled122/Wi-riX"
GITHUB_RAW = "https://raw.githubusercontent.com/waled122/Wi-riX/main"

# ======================= [ الألوان ] =======================
try:
    from colorama import init, Fore, Style
    init()
    R = Fore.RED; G = Fore.GREEN; Y = Fore.YELLOW; B = Fore.BLUE
    C = Fore.CYAN; W = Fore.WHITE; RESET = Style.RESET_ALL
    BOLD = Style.BRIGHT
except:
    R=G=Y=B=C=W=RESET=BOLD=""

# ======================= [ الوظائف ] =======================
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear_screen()
    print(f"""{BOLD}{C}
╔════════════════════════════════════════════════════════════════════════╗
║                      🔄 نظام التحديث التلقائي 🔄                       ║
║                       Wi-riX Framework Updater                         ║
║                         👑 Developer: Wi-riX 👑                        ║
╚════════════════════════════════════════════════════════════════════════╝{RESET}
""")

def get_current_version():
    """جلب الإصدار الحالي"""
    version_file = os.path.join(FRAMEWORK_PATH, 'version.json')
    if os.path.exists(version_file):
        with open(version_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('version', '1.0.0')
    return "1.0.0"

def get_latest_version():
    """جلب آخر إصدار من GitHub"""
    try:
        response = requests.get(f"{GITHUB_REPO}/releases/latest", timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get('tag_name', 'v5.0.0').replace('v', '')
    except:
        pass
    
    # لو مفيش release, جلب من main branch
    try:
        response = requests.get(f"{GITHUB_RAW}/version.json", timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get('version', '5.0.0')
    except:
        pass
    
    return "5.0.0"

def backup_files():
    """عمل نسخة احتياطية قبل التحديث"""
    backup_dir = os.path.join(FRAMEWORK_PATH, 'backup')
    os.makedirs(backup_dir, exist_ok=True)
    
    # نسخ الملفات المهمة
    files_to_backup = ['wirix.py', 'exploits/exploits_db.json', 'targets/all_vulnerable.txt', 'shells/shells_found.txt']
    
    for file in files_to_backup:
        src = os.path.join(FRAMEWORK_PATH, file)
        if os.path.exists(src):
            dst = os.path.join(backup_dir, os.path.basename(file) + f"_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
            shutil.copy2(src, dst)
            print(f"{G}[+] تم نسخ: {file}{RESET}")
    
    return backup_dir

def download_file(filename, local_path):
    """تحميل ملف من GitHub"""
    url = f"{GITHUB_RAW}/{filename}"
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(local_path, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        print(f"{R}[-] خطأ في تحميل {filename}: {e}{RESET}")
    return False

def update_framework():
    """تحديث الإطار بالكامل"""
    print(f"\n{Y}[*] جاري التحديث...{RESET}\n")
    
    # قائمة الملفات المطلوب تحديثها
    files_to_update = [
        'wirix.py',
        'requirements.txt',
        'run.bat',
        'install.ps1',
        'scripts/update.py'
    ]
    
    updated = 0
    for file in files_to_update:
        local_path = os.path.join(FRAMEWORK_PATH, file)
        if download_file(file, local_path):
            print(f"{G}[+] تم تحديث: {file}{RESET}")
            updated += 1
        else:
            print(f"{Y}[!] فشل تحديث: {file}{RESET}")
    
    # تحديث قاعدة بيانات الثغرات (إذا وجدت جديدة)
    exploits_backup = os.path.join(FRAMEWORK_PATH, 'exploits', 'exploits_db.json')
    if download_file('exploits/exploits_db.json', exploits_backup):
        print(f"{G}[+] تم تحديث قاعدة بيانات الثغرات{RESET}")
        updated += 1
    
    # تحديث ملف الإصدار
    version_data = {
        "version": get_latest_version(),
        "last_update": datetime.now().isoformat(),
        "updated_files": updated
    }
    version_file = os.path.join(FRAMEWORK_PATH, 'version.json')
    with open(version_file, 'w', encoding='utf-8') as f:
        json.dump(version_data, f, indent=4)
    
    return updated

def update_with_git():
    """تحديث باستخدام Git (الأفضل)"""
    print(f"\n{Y}[*] جاري التحديث عبر Git...{RESET}")
    
    # حفظ التغييرات المحلية
    subprocess.run(["git", "stash"], cwd=FRAMEWORK_PATH, capture_output=True)
    
    # سحب التحديثات
    result = subprocess.run(["git", "pull", "origin", "main"], cwd=FRAMEWORK_PATH, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"{G}[+] تم التحديث بنجاح!{RESET}")
        print(f"{C}{result.stdout}{RESET}")
        return True
    else:
        print(f"{R}[-] خطأ في التحديث: {result.stderr}{RESET}")
        return False

def restore_backup():
    """استعادة النسخة الاحتياطية"""
    backup_dir = os.path.join(FRAMEWORK_PATH, 'backup')
    if not os.path.exists(backup_dir):
        print(f"{R}[-] لا توجد نسخة احتياطية!{RESET}")
        return
    
    backups = [f for f in os.listdir(backup_dir) if f.endswith('.txt') or f.endswith('.json')]
    if backups:
        print(f"\n{Y}النسخ الاحتياطية المتاحة:{RESET}")
        for i, b in enumerate(backups, 1):
            print(f"  {i}. {b}")
        
        try:
            choice = int(input(f"{B}اختر رقم النسخة: {RESET}")) - 1
            if 0 <= choice < len(backups):
                backup_file = os.path.join(backup_dir, backups[choice])
                
                # استعادة الملف
                if 'exploits' in backup_file:
                    dest = os.path.join(FRAMEWORK_PATH, 'exploits', 'exploits_db.json')
                elif 'vulnerable' in backup_file:
                    dest = os.path.join(FRAMEWORK_PATH, 'targets', 'all_vulnerable.txt')
                elif 'shells' in backup_file:
                    dest = os.path.join(FRAMEWORK_PATH, 'shells', 'shells_found.txt')
                else:
                    dest = os.path.join(FRAMEWORK_PATH, 'wirix.py')
                
                shutil.copy2(backup_file, dest)
                print(f"{G}[+] تم استعادة: {backups[choice]}{RESET}")
        except:
            pass

# ======================= [ القائمة الرئيسية ] =======================
def main_menu():
    while True:
        banner()
        
        current = get_current_version()
        latest = get_latest_version()
        
        print(f"""
{Y}╔══════════════════════════════════════════════════════════════╗
║                    {W}✨ قائمة التحديث ✨{Y}                      ║
╠══════════════════════════════════════════════════════════════╣
║                                                                ║
║  📌 الإصدار الحالي: {C}{current}{RESET}                                      
║  📌 آخر إصدار: {G}{latest}{RESET}                                            
║                                                                ║
╠══════════════════════════════════════════════════════════════╣
║                                                                ║
║  {C}[1]{RESET} 🔄 تحديث تلقائي (Git)                                   ║
║      └─ اسحب آخر التحديثات من GitHub                           ║
║                                                                ║
║  {C}[2]{RESET} 📥 تحديث يدوي (تحميل الملفات)                            ║
║      └─ حمل أحدث الملفات من GitHub                            ║
║                                                                ║
║  {C}[3]{RESET} 💾 عمل نسخة احتياطية                                       ║
║      └─ احفظ بياناتك الحالية قبل التحديث                       ║
║                                                                ║
║  {C}[4]{RESET} 🔄 استعادة نسخة احتياطية                                    ║
║      └─ استرجع بيانات قديمة                                    ║
║                                                                ║
║  {C}[5]{RESET} ℹ️  معلومات الإصدار                                       ║
║      └─ اعرض تفاصيل التحديثات                                  ║
║                                                                ║
║  {C}[6]{RESET} 🔙 رجوع                                                    ║
║                                                                ║
╚══════════════════════════════════════════════════════════════╝
""")
        
        choice = input(f"{B}[?] اختر خيار (1-6): {RESET}")
        
        if choice == "1":
            print(f"\n{C}{'═'*60}{RESET}")
            print(f"{BOLD}{W}🔄 التحديث عبر Git{RESET}")
            print(f"{C}{'═'*60}{RESET}")
            
            # عمل نسخة احتياطية تلقائية
            backup_files()
            
            # تحديث
            if update_with_git():
                print(f"\n{G}✅ تم التحديث بنجاح!{RESET}")
                print(f"{Y}[!] أعد تشغيل الأداة لتطبيق التحديثات{RESET}")
            else:
                print(f"\n{R}❌ فشل التحديث!{RESET}")
            
            input(f"\n{Y}[!] اضغط Enter للمتابعة...{RESET}")
        
        elif choice == "2":
            print(f"\n{C}{'═'*60}{RESET}")
            print(f"{BOLD}{W}📥 التحديث اليدوي{RESET}")
            print(f"{C}{'═'*60}{RESET}")
            
            # عمل نسخة احتياطية
            backup_files()
            
            # تحديث
            updated = update_framework()
            
            if updated > 0:
                print(f"\n{G}✅ تم تحديث {updated} ملف بنجاح!{RESET}")
                print(f"{Y}[!] أعد تشغيل الأداة لتطبيق التحديثات{RESET}")
            else:
                print(f"\n{R}❌ لا توجد تحديثات جديدة!{RESET}")
            
            input(f"\n{Y}[!] اضغط Enter للمتابعة...{RESET}")
        
        elif choice == "3":
            print(f"\n{C}{'═'*60}{RESET}")
            print(f"{BOLD}{W}💾 عمل نسخة احتياطية{RESET}")
            print(f"{C}{'═'*60}{RESET}")
            backup_files()
            print(f"\n{G}✅ تم عمل نسخة احتياطية بنجاح!{RESET}")
            input(f"\n{Y}[!] اضغط Enter للمتابعة...{RESET}")
        
        elif choice == "4":
            print(f"\n{C}{'═'*60}{RESET}")
            print(f"{BOLD}{W}🔄 استعادة نسخة احتياطية{RESET}")
            print(f"{C}{'═'*60}{RESET}")
            restore_backup()
            input(f"\n{Y}[!] اضغط Enter للمتابعة...{RESET}")
        
        elif choice == "5":
            print(f"\n{C}{'═'*60}{RESET}")
            print(f"{BOLD}{W}ℹ️  معلومات الإصدار{RESET}")
            print(f"{C}{'═'*60}{RESET}")
            print(f"""
  📌 الإصدار الحالي: {current}
  📌 آخر إصدار: {latest}
  📌 المسار: {FRAMEWORK_PATH}
  📌 آخر تحديث: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
  
  {Y}للتحديث إلى الإصدار {latest}:{RESET}
    1. اختر [1] أو [2] من القائمة
    2. انتظر حتى يكتمل التحديث
    3. أعد تشغيل الأداة
""")
            input(f"\n{Y}[!] اضغط Enter للمتابعة...{RESET}")
        
        elif choice == "6":
            break
        
        else:
            print(f"{R}[-] خيار غير صحيح!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        import urllib3
        urllib3.disable_warnings()
    except:
        pass
    
    main_menu()