"""
Author: Isaac Jarrells
Student ID: 2585173
File Name: jarrells_sensors.py
Date: 2/2/2024
Description: Creates classes of types of sensors and allows for polymorphism, mixin, and
             inheritance of these classes to gain a base understanding of OOP in Python.
Resources: None were used at the time of this version's creation.
Version: 1.0
"""


class Sensor:
    """Sensor class with name, urls, and its polling frequency."""
    def __init__(self, name: str, url: str, polling_frequency: int) -> None:
        """Initialize the sensor with values that will be provided at calls."""
        self.name = name
        self.url = url
        self.polling_frequency = polling_frequency

    def display(self) -> None:
        """Displays the base Sensors with all its data fields."""
        print(f'Name: {self.name} \nURL: {self.url} \nPollingFrequency: {self.polling_frequency} seconds\n')

    def adjust_polling_frequency(self, adjustment) -> None:
        """Adjust the polling frequency depending on user arguments."""
        self.polling_frequency = adjustment


class SensorMixin:
    def to_dict(self) -> dict:
        """Convert the sensor to a dictionary."""
        return self.__dict__


class StorySensor(Sensor, SensorMixin):
    """Story sensor that allows for a category field"""
    def __init__(self, name: str, url: str, polling_frequency: int, category: str) -> None:
        super().__init__(name, url, polling_frequency)
        self.category = category

    def display(self) -> None:
        print(f'Name: {self.name} \nURL: {self.url} \nPollingFrequency: {self.polling_frequency} seconds \nCategory: {self.category}\n')


class EventSensor(Sensor,SensorMixin):
    """Event Sensor that adds event types and locations in zip code format"""
    def __init__(self, name: str, url: str, polling_frequency: int, event_type: str, location: str) -> None:
        super().__init__(name, url, polling_frequency)
        self.event_type = event_type
        self.loaction = location

    def display(self) -> None:
        print(f'Name: {self.name} \nURL: {self.url} \nPollingFrequency: {self.polling_frequency} seconds \nLocation: {self.loaction}, \nType: {self.event_type}\n')


class DataSensor(Sensor, SensorMixin):
    """Data Sensor that allows for a data type field"""
    def __init__(self, name: str, url: str, polling_frequency: int, data_type: str) -> None:
        super().__init__(name, url, polling_frequency)
        self.data_type = data_type
    def display(self) -> None:
        print(f'Name: {self.name} \nURL: {self.url} \nPollingFrequency: {self.polling_frequency} seconds \nData Type: {self.data_type}\n')



print("Implementations and Data fills of Classes: ")
"""Example of StorySensor implementation"""
sensor1 = StorySensor("Fox 10 News","https://www.fox10phoenix.com/",10, "Environmental")
#sensor1.display()  #display option
print(isinstance(sensor1, StorySensor)) # Is sensor 1 a story sensor


"""Example of EventSensor Implementation"""
sensor2 = EventSensor("Prescott Valley Government","https://www.prescottvalley-az.gov/427/Emergency-Alerts",2, "Winter Advisory", "86314")
#ensor2.display()  #display option
print(isinstance(sensor2, EventSensor)) # Is sensor 2 an event sensor

"""Example of DataSensor Implementation"""
sensor3 = DataSensor("National Weather Service","https://www.weather.gov/", 5,"Inches")
#sensor3.display()  #display option
print(isinstance(sensor3, DataSensor),'\n') # Is sensor 3 a data sensor

"""Subclass Checking"""
print("Subclass Checks:")
print(issubclass(DataSensor, Sensor))  # Is DataSensor a subclass of Sensor
print(issubclass(StorySensor, Sensor))  # Is StorySensor a subclass of Sensor
print(issubclass(EventSensor, Sensor))  # Is EventSensor a subclass of Sensor
print(issubclass(Sensor, object))  # Is Sensor a subclass of an object
print(issubclass(StorySensor, object))  # Is StorySensor a subclass of object
print(issubclass(Sensor, EventSensor),'\n')  # Is Sensor a subclass of EventSensor

"""Polymorphism"""
sensors = [sensor1, sensor2, sensor3]
for sensor in sensors:
    sensor.display()

"""Mixin Example"""
for sensor in sensors:
    print(sensor.to_dict())
