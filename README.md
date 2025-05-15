# 🧪 Тестовое Workmate

![Python Version](https://img.shields.io/badge/python-3.13-blue)

**Техническое задание**: [Открыть Google Doc](https://docs.google.com/document/d/1Kyj6X7poy2e1lKUaZasNDIFnMYdAlyDdQ9FCBkBCe1s)

✅ Выполнены все требования из ТЗ, включая блок «Дополнительно».  
📐 Проект написан по **DDD**.  
🧪 Покрытие тестами: **100%**  
🛠 Настроены линтеры, форматтеры и статическая проверка типов.

Код документировал только в каких-то важных или не очевиных местах.
Если нужно - покрою докстрингами полностью

---

## 📦 Технологии

- **Форматирование**: [`black`](https://github.com/psf/black) + [`isort`](https://github.com/PyCQA/isort)
- **Линтинг**: [`ruff`](https://github.com/astral-sh/ruff)
- **Анализ типов**: [`mypy`](http://mypy-lang.org/)
- **Пре-коммит хуки**: [`pre-commit`](https://pre-commit.com/)
- **Тестирование**: `pytest`, `pytest-cov`, `hypothesis`, `pytest-mock`, `pytest-html`, `pytest-mypy`

---

## 🛠 Makefile

Проект содержит удобный `Makefile` с командами для разработки, тестирования, проверки качества кода и генерации coverage отчета.  
**Цель по умолчанию**: `make lint`


### 📦 Установка и очистка

| Команда                  | Описание                                     |
|--------------------------|----------------------------------------------|
| `make install`           | Установка зависимостей + установка хуков     |
| `make clean`             | Удаление кэшей, временных файлов и артефактов |


### 🧹 Качество кода

| Команда           | Описание                                     |
|-------------------|----------------------------------------------|
| `make lint`       | Проверка кода: `black`, `isort`, `ruff`      |
| `make format`     | Автоформатирование `black` + `isort`         |
| `make type-check` | Проверка типов с `mypy`                      |
| `make check`      | Запуск всех проверок: `lint + type + test`   |


### ✅ Тестирование

| Команда                     | Описание                                                       |
|-----------------------------|----------------------------------------------------------------|
| `make test`                 | Запуск тестов (`pytest`)                                       |
| `make test-ci-codecov`      | Запуск тестов с покрытием (для CI, сохраняет `coverage.xml`)   |
| `make test-coverage`        | Запуск тестов с HTML-отчётом покрытия (`htmlcov/`)             |
| `make test-coverage-view`   | Открыть HTML-отчёт покрытия в браузере                         |

---

## 🚀 Использование

> ⚠️ Основной запуск **не требует зависимостей**, но тесты и разработка — да.

### 🧾 Установка репозитория

```bash
git clone https://github.com/iriswolf/testovoe-workmate.git
cd testovoe-workmate
````

### 🛠 Установка Poetry

Poetry используется как пакетный менеджер:

```bash
pip install poetry
```

---

## ▶️ Запуск

### ✅ Основной запуск (без зависимостей)

```bash
python -m app --type payout --input ./path-to-file1.csv ./path-to-file2.csv
```

---

## 🧪 Тесты

Для запуска тестов:

```bash
poetry install --with test --no-root
poetry run pytest tests
```

---

## 👨‍💻 Разработка

Установка зависимостей для разработки:

```bash
poetry install --no-root
```

Будут установлены две группы:

### `dev` — для форматирования и анализа:

* `black`, `isort` — автоформатирование
* `ruff` — линтинг
* `mypy` — проверка типов
* `pre-commit` — хуки

### `test` — для тестирования:

* `pytest`, `pytest-cov`, `pytest-html`, `pytest-mock`
* `pytest-mypy`, `hypothesis`

---

## ➕ Добавление нового отчёта

1. Создать `ValueObject` отчёта в `app/domain/reports/entities/report/value_objects.py`.
2. При необходимости — добавь валидацию в `app/domain/reports/entities/report/validators/`.
3. Реализовать логику в существующем или новом сервисе (`app/domain/reports/services/`).
4. При необходимости реализовать адаптеры:
   * **Formatter** → `infrastructure/adapters/application/formatters`
   * **Writer** → `infrastructure/adapters/application/writers`
   * **Parser** → `infrastructure/adapters/domain/parsers`
   * **Reader** → `infrastructure/adapters/domain/readers`
5. Создать интерактор в `app/application/reports/interactors/`.
6. Добавить вызов интерактора в `app/__main__.py`.