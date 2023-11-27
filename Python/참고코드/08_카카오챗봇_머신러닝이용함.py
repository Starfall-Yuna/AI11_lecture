from flask import Flask, request, jsonify
from flask import Flask
import sys
application = Flask(__name__)

def test1(num):
    return str((num+1))


@application.route("/")
def hello():
    return "<h1>안녕</h1>"


@application.route("/aa")
def hello2():
    return "<h1>안녕2{}</h1>".format(test1(100))


@application.route("/animal",methods=['POST'])
def animal():
    req = request.get_json()
    animal_type = ""
    answer = "Wait for Learning"
    try : 
        animal_type = req["action"]["detailParams"]["Animal_type"]["value"]	# json파일 읽기
        answer = animal_type
    except :
        pass
    
    if answer=='고양이':
    # 답변 텍스트 설정
        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            "imageUrl": 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Cat_poster_1.jpg/450px-Cat_poster_1.jpg',
                            "altText" : "hello Cat"
                        }
                    }
                ]
            }
        }    
    else:
    # 답변 텍스트 설정
        res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": answer
                        }
                    }
                ]
            }
        }    
        

    # 답변 전송
    return jsonify(res)

if __name__ == "__main__":
    #print(sys.argv)
    application.run(host='0.0.0.0', port=5001, threaded=True)
