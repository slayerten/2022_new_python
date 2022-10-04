
from time import sleep

class Countdown(object):

    def __init__(self, hour=0, minute=0, second=0):    
        self._hour = hour
        self._minute = minute
        self._second = second
    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)
    
    def run(self):
        # while True:
            self._second -= 1
            if self._second == -1:
                self._minute -= 1
                self._second = 59
                if self._minute == -1:
                    self._hour -= 1
                    self._minute = 59   
                    # if self._hour == -1 :
                    #     return
def main():
    clountdown = Countdown(0,0,15)
    while True:
        print(clountdown.show())
        sleep(1)
        clountdown.run()
    

if __name__ == '__main__':
    main()