# Проект по настройке github actions 


## CI/CD
В репозитории настроен GitHub Actions (`.github/workflows/api-tests.yml`), который автоматически запускает API-тесты при `push` и `pull_request` в ветки `main`

### Просмотр отчётов после прогона

**1. GitHub Pages (HTML-отчёт онлайн)**

После каждого `push` workflow генерирует HTML-отчёт Allure и публикует его на GitHub Pages.
Ссылка:

```
https://medvedeva-olga.github.io/OpenApi_tests/
```

Чтобы отчёт начал публиковаться, нужно **один раз** включить Pages:
`Settings → Pages → Build and deployment → Source: GitHub Actions`.

**2. Скачать артефакт**

На вкладке **Actions** → нужный запуск → блок **Artifacts** →
скачать `allure-results.zip` (сырые результаты) или `allure-report.zip` (готовый HTML-отчёт).

Локальный просмотр сырых результатов:

```bash
allure serve allure_results
```

