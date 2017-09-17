def right_justify(string_data):
    len_of_string=len(string_data)
    offset_count=70-len_of_string
    print " "*offset_count+string_data
right_justify("Uzair")