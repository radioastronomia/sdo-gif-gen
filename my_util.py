import sys

sys_arg_index = 1

def parse_arg(arg):
    if arg == 'None':
            return ''
    
    splitted_arg = arg.split('=')
    
    if len(splitted_arg) == 1:
        return arg
    
    return splitted_arg[1]

def get_sys_arg():
    global sys_arg_index
    try:
        arg = parse_arg(sys.argv[sys_arg_index])
        sys_arg_index += 1
    except IndexError:
        return None

    return arg