import json
from collections import defaultdict

from Classes import Wafer, Machine
from Functions import *

def allocate_machine(wafer, machine, result):
    print('START: ', wafer, machine)
    if len(wafer.processing_times) == 0:
        return

    machine.start_time = max(machine.end_time, wafer.time)
    machine.end_time = machine.start_time + wafer.processing_times[machine.step_id]

    wafer.time = machine.end_time
    result.append([f"{wafer.type}-{wafer.id}", machine.step_id, machine.id, machine.start_time, machine.end_time])
    print(result)

    machine.curr_n -= 1

    if machine.curr_n == 0:
        machine.end_time += machine.cooldown_time
        machine.curr_n = machine.n

    wafer.steps.remove(machine.step_id)
    wafer.processing_times.pop(machine.step_id)
    print('END: ', wafer, machine)

result = []

input_filename = 'Milestone0.json'
with open(rf"Input\{input_filename}") as file:
    data = json.load(file)

machines = data['machines']
m = []
for machine in machines:
    m.append(Machine(machine['machine_id'], machine['step_id'], machine['cooldown_time'], machine['initial_parameters'], machine['fluctuation'], machine['n']))
print('MACHINES')
print(m)
for tm in m:
    print(tm)

steps = data['steps']

wafers = data['wafers']
w = []
for wafer in wafers:
    for i in range(wafer['quantity']):
        w.append(Wafer(wafer['type'], wafer['processing_times'].copy(), i+1, wafer['quantity']))
print('WAFERS')
print(w)
for tw in w:
    print(tw)

steps_dict = defaultdict()
steps_wafer_queue = defaultdict(list)
steps_machine_queue = defaultdict(list)

for step in steps:
    steps_dict[step['id']] = step
print('STEPS')
print(steps_dict)

flag = True
time = defaultdict(int)
tt = 0
while flag == True:
    flag = False
    for ind_w in range(len(w)):
        possible_machines = [i if i.step_id in w[ind_w].steps else None for i in m]
        print(possible_machines)
        while None in possible_machines:
            possible_machines.remove(None)
        if len(possible_machines) == 0:
            continue
        possible_machines.sort()
        allocate_machine(w[ind_w], possible_machines[0], result)
        flag = True



print()
print(result)

format_and_save(result, input_filename)
