# AI-Document-Assistant

## 📌 معرفی پروژه

AI-Document-Assistant یک دستیار هوشمند مبتنی بر هوش مصنوعی است که به کاربران اجازه می‌دهد فایل‌های PDF خود را آپلود کرده و با محتوای آن‌ها به صورت هوشمند گفتگو کنند.

این پروژه با استفاده از معماری **RAG (Retrieval-Augmented Generation)** ساخته شده است. سیستم ابتدا محتوای اسناد را استخراج کرده، آن‌ها را به بخش‌های کوچک‌تر تقسیم می‌کند، سپس با استفاده از Embedding در یک پایگاه داده برداری ذخیره می‌کند و هنگام پرسش کاربر، مرتبط‌ترین بخش‌های سند را پیدا کرده و برای تولید پاسخ دقیق‌تر در اختیار مدل هوش مصنوعی قرار می‌دهد.

---

# ✨ قابلیت‌ها

* ثبت‌نام و ورود کاربران
* احراز هویت با JWT
* آپلود فایل PDF
* استخراج متن از PDF
* ذخیره اطلاعات اسناد در PostgreSQL
* تبدیل متن به Embedding
* ذخیره و جستجوی برداری با ChromaDB
* گفتگو با فایل‌های شخصی کاربر
* ذخیره تاریخچه گفتگوها
* مدیریت اسناد (مشاهده، حذف)
* محدود کردن دسترسی کاربران به فایل‌های خودشان

---

# 🏗 معماری پروژه

ساختار کلی پروژه:

```
AI-Document-Assistant

├── backend
│
│── app
│   │
│   ├── api
│   │   ├── auth.py
│   │   ├── documents.py
│   │   └── router.py
│   │
│   ├── models
│   │   ├── user.py
│   │   ├── document.py
│   │   └── chat.py
│   │
│   ├── services
│   │
│   ├── rag
│   │
│   ├── core
│   │
│   ├── utils
│   │
│   ├── database.py
│   └── main.py
│
└── README.md
```

---

# 🛠 تکنولوژی‌های استفاده شده

## Backend

* Python
* FastAPI
* Uvicorn
* SQLAlchemy

## Database

* PostgreSQL
* ChromaDB (Vector Database)

## AI / Machine Learning

* RAG Architecture
* Text Embedding
* Vector Similarity Search
* Large Language Model Integration

## Security

* JWT Authentication
* Password Hashing با bcrypt

## Document Processing

* PDF Text Extraction
* Text Chunking

---

# ⚙️ نصب و اجرا

## 1. دریافت پروژه

```bash
git clone https://github.com/USERNAME/AI-Document-Assistant.git
```

---

## 2. ایجاد محیط مجازی

```bash
python -m venv venv
```

فعال‌سازی:

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

---

## 3. نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

---

## 4. تنظیم متغیرهای محیطی

یک فایل `.env` ایجاد کنید:

```
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
AI_API_KEY=your_api_key
```

---

## 5. اجرای Backend

داخل پوشه backend:

```bash
uvicorn main:app --reload
```

سرور اجرا می‌شود:

```
http://127.0.0.1:8000
```

مستندات API:

```
http://127.0.0.1:8000/docs
```

---

# 🔌 API Endpoints

## Authentication

### Register

```
POST /auth/register
```

ایجاد حساب کاربری جدید.

### Login

```
POST /auth/login
```

دریافت توکن دسترسی.

---

# Documents

### Upload PDF

```
POST /documents/upload
```

آپلود فایل PDF.

### دریافت لیست اسناد

```
GET /documents/
```

### دریافت یک سند

```
GET /documents/{document_id}
```

### حذف سند

```
DELETE /documents/{document_id}
```

---

# AI Chat

### گفتگو با سند

```
POST /documents/chat
```

نمونه درخواست:

```json
{
  "question": "این فایل درباره چیست؟",
  "document_id": 1
}
```

---

# 🔄 روند پردازش فایل

```
PDF Upload

      ↓

Text Extraction

      ↓

Text Chunking

      ↓

Embedding Generation

      ↓

ChromaDB Storage

      ↓

User Question

      ↓

Vector Search

      ↓

Relevant Context

      ↓

AI Response
```

---

# 🎯 اهداف آینده

* ساخت رابط کاربری React
* Docker Containerization
* Deploy روی Cloud
* Streaming پاسخ‌های AI
* پشتیبانی از فرمت‌های بیشتر مانند Word و Excel
* جستجو در چندین سند همزمان

---

# 👨‍💻 Developer

ساخته شده با Python و تکنولوژی‌های هوش مصنوعی برای یادگیری و توسعه سیستم‌های RAG.
