# Последовательность действий

1) Создаем каталог проекта и настраиваем там виртуальное окружение питона

```bash
mkdir hw1
cd hw1
sudo apt install python3-pip
sudo apt install python3.10-venv
python3 -m venv venv
```

2) запускаем виртуальное окружение и устанавливаем необходимые пакеты

```bash
source venv/bin/activate
python3 -m pip install requests
python3 -m pip install fastapi
python3 -m pip install "uvicorn[standard]"
python3 -m pip install python-dotenv
```
3) Переходим на [сервис прогноза погоды](https://www.visualcrossing.com/sign-up), регистрируемся и из профиля сохраняем API_KEY в [файл](./.env)
4) запускаем сервер

```bash
uvicorn main:app --reload
```
5) переходим на [страницу общей информации сервера](http://localhost:8000/info)

6) переходим на [страницу информации о погоде сервера](http://localhost:8000/info/weather)
