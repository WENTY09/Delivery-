# Delivery Bot

Проект для симуляции доставки посылок с веб-интерфейсом и Telegram-ботом.

## Развёртывание на Render.com

- Добавлен `Procfile` и `render.yaml` для конфигурации сервисов:
  - Web-сервис запускается командой `gunicorn main:app`
  - Worker-сервис запускает бота командой `python main.py bot`
