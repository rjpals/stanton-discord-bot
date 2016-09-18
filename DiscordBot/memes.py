import json, requests #urllib, json, urllib.request

USERNAME = 'ryanjpals'
PASSWORD = 'mickeyeatsass'
URL = "https://api.imgflip.com/caption_image"
def meme_request(toptext, bottomtext):
    upload_data = {}
    upload_data['template_id'] = 61579
    upload_data['username'] = USERNAME
    upload_data['password'] = PASSWORD
    upload_data['text0'] = toptext
    upload_data['text1'] = bottomtext
    upload_json = json.dumps(upload_data).encode('utf8')

    r = requests.post(URL, data=upload_data)
    #request=urllib.request.Request('http://myserver/inout-tracker', data=upload_json)
    data = json.loads(r.text)
    data = json.loads(json.dumps(data['data']))
    return (data['url'])
    #data = json.loads(request.read().decode('utf-8'))
    #print(data['url'])
    #print((str(urllib.request.Request.data)))


if __name__ == "__main__":
    main()