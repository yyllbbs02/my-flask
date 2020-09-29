import requests
import json

if __name__ == "__main__":

    token_url = "http://192.168.123.83:8080/login"
    token_data = {
	"username":"test",
	"password":"test@12345"
    }
    #token_header = {
    #            'Content-Type': 'application/json',
    #            'Cookie': '__s_sessionid__=vbk28cg86133riah0mm3jd2u50'
    #        }

    SENSOR_HTTP_TIMEOUT = 3
    #res = requests.request("POST", token_url, data=json.dumps(token_data), timeout=SENSOR_HTTP_TIMEOUT)
    res = requests.request("POST", token_url, data=json.dumps(token_data))
            #res = requests.request("POST", token_url, data=json.dumps(token_data))
    res = json.loads(res.text)
    print(res)