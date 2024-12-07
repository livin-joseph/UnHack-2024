def parameters_check(machine_param, step_param):
    for i in step_param:
        if not step_param[i][0] <= machine_param[i] <= step_param[i][1]:
            return False
    return True


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


def fill_dependencies(wafer, steps_dict):
    for i in wafer.steps:
        if steps_dict[i]['dependency'] == None:
            continue
        wafer.dependencies[i] = steps_dict[i]['dependency'].copy()

def check_dependencies(wafer, possible_machines, steps_dict):
    flag = False
    i = 0
    while i < len(possible_machines):
        step = possible_machines[i].step_id
        if wafer.dependencies[step] == None or wafer.dependencies[step] == []:
            pass
        else:
            flag = True
            possible_machines.pop(i)
            i -= 1
        i += 1
    print("POS", possible_machines)
    return possible_machines, flag

def remove_dependency(wafer, step):
    for j in wafer.dependencies.keys():
        if step in wafer.dependencies[j]:
            print('rrr', step, wafer)
            wafer.dependencies[j].remove(step)
            print('rrr', step, wafer)

