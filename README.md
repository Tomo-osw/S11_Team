# S11_Team_CODEGYMAcademy

git clone https://github.com/Tomo-osw/S11_Team
cd S11_Teamに移動する
docker-compose build
docker-compose up 
database system is ready to accept connectionsがLOGで表示されるまで待機+5~10秒
※dockerではdbの起動が全て完了するまで待ってくれないため、一度dbの起動完了まで待たなければならない
Ctrl + c で終了
docker-compose up
localhost:8000 で接続

docker-compose exec web bash
python manage.py makemigrations myhp
python manage.py migrate
python manage.py createsuperuser.
