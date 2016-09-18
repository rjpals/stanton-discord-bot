#export CLARIFAI_APP_ID="liaC8mXdQhNJWkYjKOuVBA9pezdApXR3AFez7uH5"
#export CLARIFAI_APP_SECRET="b0SHM4M6EQFfo1P4spoHZJ38xoX4WfaYFAd592Kv"

from clarifai.client import ClarifaiApi

clarifai_api = ClarifaiApi()
result = clarifai_api.tag_images(open('C:\meme\harambe.jpg', 'rb'))

print(result)

