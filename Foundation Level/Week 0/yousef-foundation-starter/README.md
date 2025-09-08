# yousef-foundation-starter — أسبوع (0) قبل البداية

مرحبًا يوسف! 👋  
ده "Starter Kit" علشان نجهز بيئة العمل قبل الأسبوع الأول. امشِ على الخطوات بالترتيب، ولو أي خطوة وقفت معاك سجّلها في Daily Log.

---

## 🎯 أهداف أسبوع (0)
1) تثبيت الأدوات (Python, VSCode, Git).  
2) إنشاء مشروع جاهز على جهازك + بيئة افتراضية (venv).  
3) تشغيل سكريبت بسيط + نوتبوك Jupyter.  
4) تهيئة أدوات الجودة (Black, Ruff) + pytest.  
5) عمل أول مستودع على GitHub ودفع أول Commit.  

> الوقت المتوقع: 2 جلسات × (60–90 دقيقة).

---

## 1) تثبيت الأدوات
- Python 3.12+: https://www.python.org/downloads/
- VSCode: https://code.visualstudio.com/
- Git: https://git-scm.com/downloads

**امتدادات VSCode المقترحة:**
- Python (Microsoft)
- Pylance
- Jupyter
- GitLens
- Error Lens
- Black Formatter
- Ruff

---

## 2) إنشاء بيئة المشروع (venv)

### Windows (PowerShell):
```powershell
cd %USERPROFILE%\Desktop
python --version
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### macOS / Linux:
```bash
cd ~/Desktop
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

> لو الأمر `python` مش شغال على ماك/لينكس جرّب `python3`.

---

## 3) تجربة التشغيل
- شغّل:
```bash
python src/week00_hello/main.py
```
- شغّل الاختبارات:
```bash
pytest -q
```

- افتح النوتبوك:
```bash
jupyter notebook notebooks/00_sanity_check.ipynb
```

---

## 4) تهيئة Git و GitHub
1) افتح Terminal داخل مجلد المشروع.  
2) نفّذ:
```bash
git init
git add .
git commit -m "chore: week0 starter kit"
```
3) أنشئ مستودع جديد على GitHub باسم `yousef-foundation`.  
4) اربطه وادفع:
```bash
git remote add origin https://github.com/<USERNAME>/yousef-foundation.git
git branch -M main
git push -u origin main
```

---

## 5) Daily Log (سجل يومي)
أنشأت لك قالب في `tasks/daily_log_template.md`.  
كل يوم اكتب سطرين: ماذا تعلمت؟ ما الصعب؟ الخطوة التالية؟

---

## 6) مهام تأكيد النجاح (Week 0 Checklist)
- [ ] Python + VSCode + Git مثبتين.  
- [ ] تفعيل venv وتثبيت المتطلبات.  
- [ ] تشغيل `main.py` وظهور رسالة النجاح.  
- [ ] تشغيل اختبار `pytest` بنجاح.  
- [ ] فتح نوتبوك Jupyter وتشغيل الخلية الأولى.  
- [ ] إنشاء Repo على GitHub + رفع أول Commit.  
- [ ] ملء Daily Log ليومين على الأقل.  

لو خلّصت ده كله، نبدأ الأسبوع 1 بثقة 👌
