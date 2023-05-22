# set the default input file directory and the default output file directory
default_input_dir = "input_files"
default_output_dir = "output_files"
# set the default temporary map file directory
default_map_dir = "temp_map_files"
# set default number for the map and reduce threads
default_n_mappers = 4
default_n_reducers = 4


# returns the name of the input file to be split into chunks, with the default value
def get_input_file(input_dir=None, extension=".csv"):
    if not (input_dir is None):
        return input_dir + "/data" + extension
    return default_input_dir + "/data" + extension


#  returns the name of the current split file corresponding to the given index, with the default value
def get_input_split_file(index, input_dir=None, extension=".csv"):
    if not (input_dir is None):
        return input_dir + "/data_" + str(index) + extension
    return default_input_dir + "/data_" + str(index) + extension


#  returns the name of the temporary map file corresponding to the given index and reducer number, with the default value
def get_temp_map_file(index, reducer, output_dir=None, extension=".tmp"):
    if not (output_dir is None):
        return output_dir + "/map_data_" + str(index) + "-" + str(reducer) + extension
    return default_output_dir + "/map_data_" + str(index) + "-" + str(reducer) + extension


# returns the name of the output file given its corresponding index, with the default value
def get_output_file(index, output_dir=None, extension=".out"):
    if not (output_dir is None):
        return output_dir + "/reduce_data_" + str(index) + extension
    return default_output_dir + "/reduce_data_" + str(index) + extension


# returns the name of the output join file, with the default value
def get_output_join_file(output_dir=None, extension=".csv"):
    if not (output_dir is None):
        return output_dir + "/output" + extension
    return default_output_dir + "/output" + extension
