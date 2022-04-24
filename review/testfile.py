# with open('../config/pi_value.txt') as file_obj:
#     contents = file_obj.read()
# with open('../config/pi_value.txt') as file_obj:
#     #for data_line in file_obj:
#     lines = file_obj.readline()
#
#
# for line in lines:
#     print(line.rstrip())
filename = '../config/write_value.txt'
with open(filename, 'a') as file_obj:
    file_obj.write('杰 i love python\n')
