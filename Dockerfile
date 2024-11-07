# בחר את התמונה הבסיסית (Python 3.11)
FROM python:3.11

# הגדר את תיקיית העבודה
WORKDIR /app

# העתק את קובץ requirements.txt לתוך התמונה
COPY requirements.txt .

# התקן את התלויות
RUN pip install --no-cache-dir -r requirements.txt

# העתק את שאר הקבצים לתוך התמונה
COPY . .

# התקנת דפדפניים ל-Playwright
RUN pip install playwright && playwright install
