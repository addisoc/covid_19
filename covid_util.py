
import os
import datetime
import inspect

def datastr_to_datetime(datestr):
    dt_array = datestr.split('/')
    dt = datetime.datetime(
        year = 2000 + int(dt_array[2]),
        month = int(dt_array[0]), day   = int(dt_array[1]) )
    return(dt)

def convert_date(col_list):
    date_list = list()
    for index in range(0, len(col_list)):
        dt_array = col_list[index].split('/')
        dt =datetime.datetime( year = 2000 + int(dt_array[2]),
                                            month = int(dt_array[0]),
                                            day   = int(dt_array[1]) )
        date_list.append(dt)
        #print(col_list[index], date_list[ -1:])
    return(date_list)

def retrieve_name(var):
        """
        Gets the name of var. Does it from the out most frame inner-wards.
        :param var: variable to get name from.
        :return: string
        """
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            print(fi)
            if len(names) > 0:
                return names[0]



