import face_recognition
import camera
import time

knownPicture, knownFace, unknownPicture, unknownFace = [], [], [], []

def getSamplePhotos():
    print('Getting unknown faces...')
    for i in range(5):
        fileName = '../bin/unknownFaces/sample0.jpg'
        camera.takePhoto(fileName)
        unknownPicture.append(face_recognition.load_image_file(fileName))
        unknownFace.append(face_recognition.face_encodings(unknownPicture[i])[0])

def isPersonRecognized():
    print('Getting known faces...')
    knownPicture.append(face_recognition.load_image_file('../bin/knownFaces/Nate1.jpg'))
    knownPicture.append(face_recognition.load_image_file('../bin/knownFaces/Nate2.jpg'))
    knownPicture.append(face_recognition.load_image_file('../bin/knownFaces/Nate3.jpg'))
    knownPicture.append(face_recognition.load_image_file('../bin/knownFaces/Nate4.jpg'))
    knownPicture.append(face_recognition.load_image_file('../bin/knownFaces/Nate5.jpg'))

    knownFace.append(face_recognition.face_encodings(knownPicture[0])[0])
    knownFace.append(face_recognition.face_encodings(knownPicture[1])[0])
    knownFace.append(face_recognition.face_encodings(knownPicture[2])[0])
    knownFace.append(face_recognition.face_encodings(knownPicture[3])[0])
    knownFace.append(face_recognition.face_encodings(knownPicture[4])[0])

    try:
        getSamplePhotos()
    except:
        if unknownFace == []:
            print('No face found.')
            return False

    print('Processing faces...')
    endResults = False
    for i in range(len(unknownFace)):
        for j in range(len(knownFace)):
            results = face_recognition.compare_faces([knownFace[j]], unknownFace[i], tolerance=0.70)
            if results == True:
                if j < 5:
                    endResults = "Nate"
                break
        if endResults is not False:
            break

    if endResults is not False:
            print("Welcome home " + endResults + "!")
    else:
            print("Please state your name and reason for visit.")
    return endResults

isPersonRecognized()
