## 1. Environment
1. Language 
    - Python 3.6
        - pyvenv 사용
2. Framework
    - Flask
3. 사용한 API
    - Clova Speech Synthesis
4. 설정
    - https://www.ncloud.com/product/aiService/css 를 참조하여 `client_id`, `client_secret` 값을 얻는다. 
    - Config.py 의 `client_id`, `client_secret` 를 입력한다..
    - Config.py 의 `server_port` 에 사용할 port 를 입력한다.
        
## 2. Execute
1. 터미널 환경에서 해당 Project 가 있는곳으로 이동한다. 

2. 밑의 명령어을 터미널 환경에서 실행한다. 
    ```
    pip3.6 install -r requirements.txt
    PYTHON_PATH=$PWD FLASK_APP=FlaskSetUp.py  FLASK_DEBUG=1 python -m flask run
    ```
3. 브라우져에서 `localhost:${server_port}` 에 접속 