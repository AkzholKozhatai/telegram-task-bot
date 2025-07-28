# 🤖 Company Bot

Телеграм-бот для внутренней системы компании. Возможности:

- 📩 Отправка и приём отчётов
- 👥 Управление сотрудниками
- 🔐 Админ-панель

## 📁 Структура проекта

company_bot/
├── bot.py # Точка входа
├── config.py # Конфигурации
├── requirements.txt # Зависимости
├── README.md # Описание
│
├── db/ # Работа с базой данных
│ ├── database.py
│ └── models.py
│
├── handlers/ # Обработчики команд
│ ├── start_handler.py
│ ├── report_handler.py
│ └── admin_handler.py
│
├── keyboards/ # Кнопки
│ └── default.py
│
└── utils/ # Вспомогательные функции
└── helpers.py

## 🚀 Запуск

```bash
pip install -r requirements.txt
python bot.py
