<div align="center">

# 🐍 Small Projects
### مجموعه پروژه‌های کوچک پایتون

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success)
![Level](https://img.shields.io/badge/Level-Beginner%20→%20Intermediate-blue)
![Languages](https://img.shields.io/badge/Docs-English%20%7C%20فارسی-orange)

**[English](#-english) · [فارسی](#-فارسی)**

</div>

---

## 🇬🇧 English

### About

**Small Projects** is a collection of small, focused Python programs. Each one is a self-contained script that practices a core programming idea: loops, conditions, functions, data structures, input validation, working with APIs, and writing cleaner code.

The scripts were first written as quick practice exercises and then **refactored** to follow better practices: small reusable functions, constants instead of magic numbers, input validation, and no repeated code.

### Projects

| File | What it does |
|------|--------------|
| `Average.py` | Reads numbers until `-1` is entered, then prints their average. |
| `Bakery.py` | A bakery simulator: choose a bread, enter a quantity, see the total, and confirm with a password. |
| `Calculation.py` | A quick math quiz with random numbers and operators (`+`, `-`, `*`). |
| `Competition.py` | A text-based horse race with live progress and a winner. |
| `Figures.py` | Finds the largest and smallest digit of a number. |
| `Game_Guess.py` | Number guessing game: human vs. bot (the bot uses binary search). |
| `Multiples.py` | Filters numbers from a list by divisibility and position rules. |
| `Password.py` | Generates secure random passwords with the `secrets` module. |
| `API_SMS.py` | Fetches the live Bitcoin price (CoinLore API) and sends it as an SMS via Kavenegar. |
| `Large/Small_Text.py` | Swaps the case of a text (uppercase ↔ lowercase). |

### Concepts Practiced

- Loops, conditions, and functions
- Dictionaries, lists, sets, and string methods
- Input validation and error handling (`try / except`)
- The `random`, `secrets`, `string`, and `operator` modules
- HTTP requests with `requests` and REST APIs
- Environment variables for keeping secrets out of code
- Clean code: constants, naming, and removing duplication

### Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/AmirDehghanKar/Small_Projects.git
cd Small_Projects/Project

# 2. Run any script
python Average.py
```

**Requirements:** Python 3.10+ (tested on 3.13).

For `API_SMS.py` you also need:

```bash
python -m pip install requests kavenegar
```

and these environment variables (never write your key inside the code):

```powershell
# Windows PowerShell
$env:KAVENEGAR_API_KEY = "your-api-key"
$env:SMS_RECEIVER      = "your-phone-number"
$env:KAVENEGAR_SENDER  = "your-sender-number"   # optional
```

```bash
# Linux / macOS
export KAVENEGAR_API_KEY="your-api-key"
export SMS_RECEIVER="your-phone-number"
```

### Project Structure

```
Small_Projects/
├── README.md
├── .gitignore
└── Project/
    ├── API_SMS.py
    ├── Average.py
    ├── Bakery.py
    ├── Calculation.py
    ├── Competition.py
    ├── Figures.py
    ├── Game_Guess.py
    ├── Multiples.py
    ├── Password.py
    └── Large/
        └── Small_Text.py
```

### Author

**Amirmohammad Dehghankar** — web designer (WordPress) and Python developer who loves learning and building bigger projects step by step.

⭐ If you find this repository useful, feel free to give it a star.

---

## 🇮🇷 فارسی

<div dir="rtl">

### درباره‌ی پروژه

**Small Projects** مجموعه‌ای از برنامه‌های کوچک و هدفمند پایتون است. هر فایل یک اسکریپت مستقل است که یک مفهوم اصلی برنامه‌نویسی را تمرین می‌کند: حلقه‌ها، شرط‌ها، توابع، ساختارهای داده، اعتبارسنجی ورودی، کار با API و نوشتن کد تمیزتر.

این اسکریپت‌ها ابتدا به‌صورت تمرین سریع نوشته شدند و بعد **بازنویسی و بهینه** شدند تا اصول بهتری رعایت شود: توابع کوچک و قابل‌استفاده‌ی مجدد، ثابت‌ها به‌جای اعداد جادویی، اعتبارسنجی ورودی و حذف کد تکراری.

### پروژه‌ها

| فایل | توضیح |
|------|-------|
| `Average.py` | تا وارد کردن `-1` عدد می‌گیرد و میانگین را چاپ می‌کند. |
| `Bakery.py` | شبیه‌ساز نانوایی: انتخاب نان، وارد کردن تعداد، نمایش مبلغ و تأیید با رمز. |
| `Calculation.py` | آزمون سریع ریاضی با اعداد و عملگرهای تصادفی (`+`، `-`، `*`). |
| `Competition.py` | مسابقه‌ی اسب‌دوانی متنی با نمایش لحظه‌ای و اعلام برنده. |
| `Figures.py` | بزرگ‌ترین و کوچک‌ترین رقم یک عدد را پیدا می‌کند. |
| `Game_Guess.py` | بازی حدس عدد: انسان در برابر ربات (ربات از جستجوی دودویی استفاده می‌کند). |
| `Multiples.py` | اعداد یک لیست را با شرط‌های بخش‌پذیری و جایگاه فیلتر می‌کند. |
| `Password.py` | رمز عبور تصادفی و امن با ماژول `secrets` می‌سازد. |
| `API_SMS.py` | قیمت لحظه‌ای بیت‌کوین را از API سایت CoinLore می‌گیرد و با کاوه‌نگار پیامک می‌کند. |
| `Large/Small_Text.py` | حروف کوچک و بزرگ یک متن را برعکس می‌کند. |

### مفاهیم تمرین‌شده

- حلقه‌ها، شرط‌ها و توابع
- دیکشنری، لیست، مجموعه (set) و متدهای رشته
- اعتبارسنجی ورودی و مدیریت خطا (`try / except`)
- ماژول‌های `random`، `secrets`، `string` و `operator`
- درخواست HTTP با `requests` و کار با APIها
- متغیرهای محیطی برای دور نگه داشتن اطلاعات حساس از کد
- کد تمیز: ثابت‌ها، نام‌گذاری و حذف تکرار

### نحوه‌ی اجرا

</div>

```bash
# 1. Clone the repository
git clone https://github.com/AmirDehghanKar/Small_Projects.git
cd Small_Projects/Project

# 2. Run any script
python Average.py
```

<div dir="rtl">

**پیش‌نیاز:** پایتون ۳.۱۰ یا بالاتر (تست‌شده روی ۳.۱۳).

برای `API_SMS.py` باید این کتابخانه‌ها نصب شوند و متغیرهای محیطی (همان‌هایی که در بخش انگلیسی بالا آمده) تنظیم شوند. **کلید API را هرگز داخل کد ننویس.**

</div>

```bash
python -m pip install requests kavenegar
```

<div dir="rtl">

### نویسنده

**امیرمحمد دهقانکار** — طراح وب (وردپرس) و برنامه‌نویس پایتون که عاشق یادگیری و ساختن پروژه‌های بزرگ‌تر قدم‌به‌قدم است.

⭐ اگر این مخزن به کارت آمد، با دادن یک ستاره حمایت کن.

</div>

---

<div align="center">

Made with Love❤️

</div>
