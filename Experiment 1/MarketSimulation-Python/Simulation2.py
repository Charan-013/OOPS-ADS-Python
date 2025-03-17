"""
Authors: [Shiva Charan Reddy Kallem]
Simulation2: Implements the simulation with a single shared queue for all cash registers.
"""

import random
from collections import deque
from customer import Customer

def customerArrives(arrival_probability):
    return random.random() < arrival_probability

def emptiestQueue(queue):
    return queue

def simulate_single_queue(arrival_probability, num_registers, total_minutes):
    # Single shared queue for all registers.
    queue = deque()
    registers = [None for _ in range(num_registers)]
    
    waiting_times = []

    for current_minute in range(total_minutes):
            # INSERT CODE HERE
            #  Use the customerArrives method to determine if a customer 
            #  arrives at this particular minute.
            #  If a customer does arrive, call the emptiestQueue method 
            #  and add a customer to this queue.
            if customerArrives(arrival_probability):
                customer = Customer(current_minute, random.randint(1, 5))
                emptiest_queue = emptiestQueue(queue)
                emptiest_queue.append(customer)
            
            # INSERT CODE HERE
            # Check each register.
            #   If the register is available and there are customers waiting in that 
            #   register's queue,
            #     1.  Remove the customer at the front of the queue.
            #     2.  Update the total number of customers who have successfully 
            #         reached a register
            #     3.  Update the total time that each customer has spent waiting 
            #         in queues before successfully reaching a register
            #     4.  Update the time when this register will be available after
            #         serving this customer.
            for i in range(num_registers):
                if registers[i] != None:
                    cust, remaining_service_time = registers[i]
                    remaining_service_time -= 1
                    if remaining_service_time == 0:
                        registers[i] = None
                    else:
                        registers[i] = (cust, remaining_service_time)
                if registers[i] == None and queue:
                    cust = queue.popleft()
                    waiting_time = current_minute - cust.arrival_time
                    waiting_times.append(waiting_time)
                    registers[i] = (cust, cust.service_time)
    
    average_wait = sum(waiting_times) / len(waiting_times) if waiting_times else 0
    return average_wait

if __name__ == "__main__":
    arrival_probability = 0.3
    num_registers = 3
    total_minutes = 1000

    avg_wait = simulate_single_queue(arrival_probability, num_registers, total_minutes)
    print(f"Average waiting time (single queue): {avg_wait:.2f} minutes")
