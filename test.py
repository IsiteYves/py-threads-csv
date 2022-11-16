import threading
import time
'''
A Dummy function that accepts 2 arguments i.e. Filename and encryption type
and sleeps for 5 seconds in a loop while printing few lines.
This is to simulate a heavey function that takes 10 seconds to complete
'''


def loadContents(fileName, encryptionType):
    print('Started loading contents from file : ', fileName)
    print('Encryption Type : ', encryptionType)
    for i in range(5):
        print('Loading ... ')
        time.sleep(1)
    print('Finished loading contents from file : ', fileName)


def main():
    # Create a thread from a function with arguments
    th = threading.Thread(target=loadContents, args=('users.csv', 'ABC'))
    # Start the thread
    th.start()


if __name__ == '__main__':
    main()
