# Последовательность действий 

1) Создаем каталог проекта и настраиваем там виртуальное окружение питона 

```bash 
mkdir hw1 
cd hw1
sudo apt install python3-pip
sudo apt install python3.8-venv
python3 -m venv venv 
```

2) запускаем виртуальное окружение и устанавливаем необходимые пакеты

```bash 
python3 -m pip install requests

```
3) запускаем сервер 

```bash 
python -m http.server
```
4) переходим на [страницу общей информации сервера](http://localhost:8000/info) 

5) переходим на [страницу информации о погоде сервера](http://localhost:8000/info/weather) 
