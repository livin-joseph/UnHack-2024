def parameters_check(machine_param, step_param):
    for i in step_param:
        if not step_param[i][0] <= machine_param[i] <= step_param[i][1]:
            return False
    return True

def allocate_machine(step, wafer, steps_machine_queue, steps, result):
    t = steps_machine_queue[step['id']]
    print(t)
    free_machine = None
    for i in t:
        print(wafer)
        if parameters_check(i['initial_parameters'], step['parameters']):
            free_machine = i

    if 'start_time' not in free_machine:
        free_machine['start_time'] = 0
        free_machine['end_time'] = free_machine['start_time'] + wafer['processing_times'][step['id']]
    else:
        free_machine['start_time'] = free_machine['end_time']
        free_machine['end_time'] = free_machine['start_time'] + wafer['processing_times'][step['id']]

    result.append([wafer['type'], step, free_machine['machine_id'], free_machine['start_time'], free_machine['end_time']])
    print(result)



def format_and_save(result, filename):
    output = {'schedule': []}
    keys = ['wafer_id', 'step', 'machine', 'start_time', 'end_time']
    for res in result:
        t = {}
        for i, j in zip(keys, res):
            print(i, j)
            t[i] = j
        output['schedule'].append(t)

    import json
    with open(filename, "w") as outfile: 
        json.dump(output, outfile)
