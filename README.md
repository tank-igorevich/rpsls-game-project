# rpsls-game-project
CI CD lab

# 🕹 Rock Paper Scissors Lizard Spock

Гра реалізована мовою **Python** з використанням текстового інтерфейсу. Підтримується як інтерактивний режим, так і запуск із аргументами. Налаштовано автоматичне тестування та перевірку коду через **CI/CD (GitHub Actions)**.

---

## 🚀 Як запустити гру

### 🔸 Інтерактивний режим
```bash
python3 main.py
```
Ви вводите хід кожного гравця вручну:
```
Оберіть: rock, paper, scissors, lizard, spock
Гравець 1: rock
Гравець 2: scissors
Гравець 1 перемагає! Камінь роздавлює ножиці
```

### 🔸 Режим із аргументами
```bash
python3 main.py --player1 rock --player2 lizard
```
Вивід:
```
Гравець 1: rock
Гравець 2: lizard
Гравець 1 перемагає! Камінь роздавлює ящірку
```

---

## 🧪 Тестування

### ✅ Запуск тестів:
```bash
pytest
```

### ✅ Тестування з HTML-звітом:
```bash
pytest --html=report.html
```
Після запуску відкрий `report.html` у браузері.

---

## 🧼 Перевірка стилю коду
```bash
flake8 .
```
Або з HTML-звітом:
```bash
flake8 . --format=html --htmldir=flake8-report
```

---

## ⚙️ CI/CD (GitHub Actions)

При кожному пуші або Pull Request GitHub автоматично:
- запускає `pytest`
- перевіряє стиль через `flake8`
- генерує HTML-звіти

Файл workflow: `.github/workflows/python-ci.yml`

---

## 📦 Залежності
Усі бібліотеки перелічено в `requirements.txt`:
```
pytest
flake8
pytest-html
flake8-html
```

Встановлення:
```bash
pip install -r requirements.txt
```

---

## 👥 Автори
- 👤 Стрілець Олександр — реалізація логіки гри, структура проєкту, use-case діаграма
- 👩‍💻 Абрамова Даша — інтерфейс, argparse, тести, CI/CD, документація

---

## 📄 Ліцензія
MIT License