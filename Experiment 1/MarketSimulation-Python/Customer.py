"""
Authors: [Shiva Charan Reddy Kallem]
Customer class representing a customer in the supermarket.
"""

class Customer:
    def __init__(self, arrival_time, service_time):
        self.arrival_time = arrival_time
        self.service_time = service_time

    def __repr__(self):
        return f"Customer(arrival_time={self.arrival_time}, service_time={self.service_time})"
