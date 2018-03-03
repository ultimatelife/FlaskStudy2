from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
import urllib
import Config

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def celeb_search_get():
    if request.method == "GET":
        return render_template('home.html')
    else:
        file = request.files['book']
        filename = f"static/" + file.filename
        file.save(filename)
        music_file = get_celeb_list(filename)
        return render_template('home.html', music_file=music_file)


def get_celeb_list(filename) -> str:
    headers = {
        "X-Naver-Client-Id": Config.client_id,
        "X-Naver-Client-Secret": Config.client_secret,
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    filetype = filename.split(".")[-1]
    if filetype == "txt":
        with open(filename, mode="r", encoding="utf8") as f:
            book_content = "".join(f.readlines())
            encText = urllib.parse.quote(book_content)
    elif filetype == "pdf":
        encText = "pdf는 아직 지원이 안됩니다."
    else:
        encText = "해당 파일은 아직 지원이 안됩니다."

    data = "speaker=mijin&speed=0&text=" + encText
    url = "https://openapi.naver.com/v1/voice/tts.bin"
    result = requests.post(url=url, data=data, headers=headers)
    if result.status_code == 200:
        print("TTS mp3 저장")
        response_body = result.content
        music_file = filename + '.mp3'
        with open(music_file, 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + str(result.status_code))
        print(result.headers)
        print(result.text)
    return music_file


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Config.server_port)
