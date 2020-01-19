import camera
import time

personName = input('Please type your name: ')

for i in range(1, 6):
    time.sleep(1)
    print('Here\'s for photo', i, 'of 5:')
    time.sleep(2)

    # Countdown
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    
    print('Taking Photo...\n')
    fileName = '../bin/knownFaces/' + personName + str(i) + '.jpg'
    camera.takePhoto(fileName)
    
print("\nAll done! Your face will now be recognized.")
