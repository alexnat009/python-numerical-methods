import numpy as np


class Student():
    n_instances = 0

    def __init__(self, sid, name, gender):
        self.name = name
        self.gender = gender
        self.sid = sid
        self.type = "learner"
        Student.n_instances += 1

    def say_name(self):
        print(f'My name is {self.name}')

    def report(self, score):
        self.say_name()
        print(f'My id is {self.sid}')
        print(f'My score is {score}')

    @staticmethod
    def num_instances():
        print(f'We have {Student.n_instances} instances')


student1 = Student("001", "Susan", "F")
student1.num_instances()
student2 = Student("002", "Mary", "D")
student3 = Student("003", "Alex", "A")
student3.num_instances()
student1.num_instances()


class Sensor():

    def __init__(self, name, location, record_date):
        self.record_date = record_date
        self.location = location
        self.name = name
        self.data = {}

    def clear_data(self):
        self.data = {}
        print(f'Data cleared!')

    def add_data(self, t, data):
        self.data['time'] = t
        self.data['data'] = data
        print(f'We have {data.__len__()} points saved')


sensor1 = Sensor("sensor1", "Berkely", "2019-01-01")
data = np.random.randint(-10, 10, 10)
sensor1.add_data(np.arange(10), data)
print(sensor1.data)


class Accelerometer(Sensor):
    def show_type(self):
        print(f'I am accelerometer')


acc = Accelerometer("acc1", "Oakland", "2019-02-01")
acc.show_type()
data = np.random.randint(-10, 10, 10)
acc.add_data(np.arange(10), data)
print(acc.data)


class USBAcc(Accelerometer):
    def show_type(self):
        print(f'I am {self.name}, created at UC {self.location}')


acc_ucb = USBAcc("UCBAcc", "Berkeley", "2019-03-01")
acc_ucb.show_type()


class NewSensor(Sensor):

    # def __init__(self, name, location, record_date, brand):
    #     self.name = name
    #     self.location = location
    #     self.record_date = record_date
    #     self.brand = brand
    #     self.data = {}
    def __init__(self, name, location, record_date, brand):
        super().__init__(name, location, record_date)
        self.brand = brand


new_sensor = NewSensor("OK", "SF", "2019-01-05", "XYZ")
print(new_sensor.brand)


class Sensor():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.__version = "1.0"

    def get_version(self):
        return self.__version

    def set_version(self, version):
        self.__version = version


sensor1 = Sensor("Acc", "Berkeley")
print(sensor1.name)
print(sensor1.location)
print(sensor1.get_version())
