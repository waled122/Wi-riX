# 👑 Wi-riX إطار عمل اختبار اختراق الووردبريس

## 🔥 المقدمة

**Wi-riX Framework** هو أداة احترافية عربية لاختبار اختراق مواقع الووردبريس.

## ✨ الميزات

- **المسح الذكي**: اكتشاف الثغرات تلقائياً
- **الاستغلال التلقائي**: تشغيل الإكسبلويت بضغطة زر
- **قاعدة بيانات الثغرات**: إضافة ثغرات جديدة بسهولة
- **التقارير**: حفظ النتائج بصيغة JSON
- **متعدد المنصات**: يعمل على Windows و Linux

## 📥 التثبيت

```bash
git clone https://github.com/waled122/Wi-riX.git
cd Wi-riX
pip install -r requirements.txt
python wirix.py



عمل الاداء الامر التالى 
python wirix.py
👑 المطور

Wi-riX

⚠️ تنبيه
هذه الأداة للأغراض التعليمية فقط.

text

### 7️⃣ **ملف `.github/workflows/release.yml`**

```yaml
name: Release Wi-riX Framework

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Create Release
        uses: softprops/action-gh-release@v1
        with:
          files: |
            wirix.py
            requirements.txt
            install.ps1
          generate_release_notes: true
