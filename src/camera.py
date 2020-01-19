from picamera import PiCamera
from google.cloud import vision
from datetime import datetime
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('./whosthere-6385b11d40f1.json')

client = vision.ImageAnnotatorClient(credentials=credentials)
camera = PiCamera()

def takePhoto(fileName):
    global camera
    camera.capture(fileName)

def personOrPackage():
    now = datetime.now()
    time_now = now.strftime("%H%M%S_%d%m%Y")
    fileName = '../bin/' + time_now + '.jpg'
    takePhoto(fileName)
    with open(fileName, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    objects = client.object_localization(image=image).localized_object_annotations

    package = False
    person = False

    for obj in objects:
        print(obj.name)
        if(obj.name == "Person"):
            person = True
        elif(obj.name == "Packaged goods"):
            package = True
    
    
    return fileName, person, package
