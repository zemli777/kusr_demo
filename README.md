# Последовательность действий

1) Создаем каталог проекта и настраиваем там виртуальное окружение питона

```bash
mkdir hw1
cd hw1
sudo apt install python3-pip
sudo apt install python3.10-venv
python3 -m venv venv
```

2) Запускаем виртуальное окружение и устанавливаем необходимые пакеты

```bash
source venv/bin/activate
source .env
pip install -r requirements.txt
```
3) Переходим на [сервис прогноза погоды](https://www.visualcrossing.com/sign-up), регистрируемся и из профиля сохраняем API_KEY в .env
4) Запускаем сервер

```bash
uvicorn main:app --reload --port $PORT
```
5) Переходим на [эндпоинт общей информации сервера](http://localhost:8000/info) (нужно поменять порт на указаный в .env)

6) Переходим на [эндпоинт информации о погоде сервера](http://localhost:8000/info/weather) (нужно поменять порт на указаный в .env)
