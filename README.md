# Тестовое Workmate

**ТЗ**: https://docs.google.com/document/d/1Kyj6X7poy2e1lKUaZasNDIFnMYdAlyDdQ9FCBkBCe1s

Проект написан по **DDD**.

Покрытие тестами - **100%**.

Настроены линтер, форматтер и анализатор типов:
- **Форматирование**: `black` + `isort`
- **Линтинг**: `ruff`
- **Анализ типов**: `mypy`

Настроены прекоммит-хуки на `pre-commit`.

В `Makefile` прописаны все необходимые команды.

Команда `make test-coverage-view` откроет отчёт покрытия `pytest-cov` в браузере с помощью `pytest-html`.

---

### Добавление нового типа отчёта

1. Создать `ValueObject` для возвращаемых данных отчёта в `app/domain/reports/entities/report/value_objects.py`.

2. При необходимости — добавить валидацию для `ValueObject` в `app/domain/reports/entities/report/validators/`.

3. Дописать бизнес-логику в существующие сервисы или создать новый в `app/domain/reports/services`.

4. При необходимости — реализовать адаптеры:
   - **Formatter**: `app/infrastructure/adapters/application/formatters`
   - **Writer**: `app/infrastructure/adapters/application/writers`
   - **Parser**: `app/infrastructure/adapters/domain/parsers`
   - **Reader**: `app/infrastructure/adapters/domain/readers`

5. Создать интерактор в `app/application/reports/interactors`.

6. Добавить вызов интерактора в `app/__main__.py`.
