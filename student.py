#student.py

class Student:
    """A lost soul...waiting to be found"""

    def __init__(self, first, last, major, OA, time, status=None):
        self.first = first
        self.last = last
        self.major = major
        self.OA = OA
        self.time = time
        self.status = "PENDING"

    def __str__(self):
        outstring = """Name: {} {} \n Major: {} \n OA: {} \n Time: {} \n Status: {}\n""".format(
                        self.first, self.last, self.major, self.OA, self.time, self.status)
        return outstring

