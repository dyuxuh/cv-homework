# CV Project

Чекунов Анзор Хусеевич БКНАД 253

Резюме на LaTeX, собирается через Docker и GitHub Actions.
[https://dyuxuh.github.io/cv-homework/resume.pdf](https://dyuxuh.github.io/cv-homework/resume.pdf)


## Инструкция для проверяющего

### 1. Проверка Dockerfile

```bash
docker build -t cv .
docker run --name cv_container cv
docker cp cv_container:/cv/CV/main.pdf resume.pdf
docker rm cv_container
```

### 2. Проверка GitHub Actions
Зайдите в раздел Actions репозитория. Должны быть два успешных workflow:

Build CV — проверяет сборку Docker образа

Deploy PDF to GitHub Pages — деплоит PDF на GitHub Pages


### 3. Проверка GitHub Pages
Резюме доступно по ссылке:
https://dyuxuh.github.io/cv-homework/resume.pdf

### 4. Проверка choose_system.py

Запустите скрипт:

```bash
python choose_system.py
```