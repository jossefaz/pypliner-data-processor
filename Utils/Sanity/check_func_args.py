def check_func_args(arg_list : list, arg_dict : dict) -> list :
    not_found_args = []
    for arg in arg_list :
        if arg not in arg_dict.keys():
            not_found_args.append(arg)
    return not_found_args