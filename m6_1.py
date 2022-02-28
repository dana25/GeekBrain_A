from time import sleep

class TrafficLight:
    _color = "black"

    def running(self):
        while True:
            print("RED")
            sleep(5)
            print("Yellow")
            sleep(2)
            print("GREEN")
            sleep(5)
            break

trafficlight=TrafficLight()
trafficlight.running()