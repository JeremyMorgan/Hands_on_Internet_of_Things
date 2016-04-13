class Reading(object):

    def __init__(self, jsoninput):

        self.id = str(jsoninput['id'])
        self.temp1 = str(jsoninput['temp1'])
        self.temp2 = str(jsoninput['temp2'])
        self.tempavg = str(jsoninput['tempavg'])
        self.pressure = str(jsoninput['pressure'])
        self.sealevelpressure = str(jsoninput['sealevelpressure'])
        self.humidity = str(jsoninput['humidity'])
        self.timestamp = str(jsoninput['timestamp'])
