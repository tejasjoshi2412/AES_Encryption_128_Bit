# AES Encryption System 128-bit

import math

plain_text = input('Enter the plain text:')
key_in = input('Enter the key:')
constant = ['0', '0', '0', '1', '1', '0', '1', '1']
sbox = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
        ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
        ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
        ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
        ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
        ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
        ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
        ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
        ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
        ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
        ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
        ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
        ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
        ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
        ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
        ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]

def list_to_string(Var1):
    string_out = map(str, Var1)
    string_out = ''.join(string_out)
    return string_out

def fix(Var1):
    if Var1 == '0':
        value = '00'
    elif Var1 == '1':
        value = '01'
    elif Var1 == '2':
        value = '02'
    elif Var1 == '3':
        value = '03'
    elif Var1 == '4':
        value = '04'
    elif Var1 == '5':
        value = '05'
    elif Var1 == '6':
        value = '06'
    elif Var1 == '7':
        value = '07'
    elif Var1 == '8':
        value = '08'
    elif Var1 == '9':
        value = '09'
    elif Var1 == 'a':
        value = '0a'
    elif Var1 == 'b':
        value = '0b'
    elif Var1 == 'c':
        value = '0c'
    elif Var1 == 'd':
        value = '0d'
    elif Var1 == 'e':
        value = '0e'
    elif Var1 == 'f':
        value = '0f'
    else:
        value = Var1
    return value

def shift_to_left(l2, n2):
    return l2[n2:] + l2[:n2]

def shift_1(Var1, Var2):
    return Var1[(len(Var1) - Var2):] + Var1[:(len(Var1) - Var2)]

def left_shift(Var1):
    left = Var1[1:]
    left.append('0')
    return left

def var_binary(Var1):
    log = int(math.log(16, 2))
    bits = len(Var1) * log
    return str(bin(int(Var1, 16))[2:].zfill(bits))

def convert_to_hex(Var1):
    Var1 = int(Var1, 2)
    return hex(Var1).split('alpha')[1]

def segment(Var1):
    array = []
    for sub_1 in Var1:
        array.append(sub_1)
    return array

def xor_operation_1(Var1, Var3):
    array = []
    for sub_1, sub_2 in zip(Var1, Var3):
        if sub_1 == sub_2:
            element = '0'
        else:
            element = '1'
        array.append(element)
    return array

def byte_1(Var1):
    return Var1[1:] + Var1[:1]

def pro_cor(Var1, Var2):
    counter = 0
    Array = []
    mix_coloumn_1 = ['2', '3', '1', '1']
    mix_coloumn_1 = shift_1(mix_coloumn_1, Var2)
    while counter < len(Var1):
        number = Var1[counter]
        number = var_binary(number)
        number = segment(number)
        if mix_coloumn_1[counter] == '2':
            num1 = number
            number = left_shift(number)
            if num1[0] == '1':
                number = xor_operation_1(number, constant)
            number = list_to_string(number)
            number = convert_to_hex(number)
            number = fix(number)
            Array.append(number)

        if mix_coloumn_1[counter] == '3':
            num1 = number
            number = left_shift(number)

            if num1[0] == '1':
                number = xor_operation_1(number, constant)
            number = xor_operation_1(number, num1)
            number = list_to_string(number)
            number = convert_to_hex(number)
            number = fix(number)
            Array.append(number)

        if mix_coloumn_1[counter] == '1':
            number = list_to_string(number)
            number = convert_to_hex(number)
            number = fix(number)
            Array.append(number)
        counter += 1
    temp_set_1 = []
    for sub_1 in Array:
        number = var_binary(sub_1)
        temp_set_1.append(number)
    mix_coloumn_2 = xor_operation_1(temp_set_1[0], temp_set_1[1])
    mix_coloumn_2 = xor_operation_1(mix_coloumn_2, temp_set_1[2])
    mix_coloumn_2 = xor_operation_1(mix_coloumn_2, temp_set_1[3])
    mix_coloumn_2 = list_to_string(mix_coloumn_2)
    mix_coloumn_2 = fix(convert_to_hex(mix_coloumn_2))
    return mix_coloumn_2

def Divide(Var1):
    counter_1 = 0
    array1 = []
    array2 = []
    array3 = []
    array4 = []
    array5 = []
    while counter_1 < len(Var1):
        array1.append(Var1[counter_1:(counter_1 + 2)])
        counter_1 += 2
    array2.append(array1[0])
    array2.append(array1[1])
    array2.append(array1[2])
    array2.append(array1[3])
    array3.append(array1[4])
    array3.append(array1[5])
    array3.append(array1[6])
    array3.append(array1[7])
    array4.append(array1[8])
    array4.append(array1[9])
    array4.append(array1[10])
    array4.append(array1[11])
    array5.append(array1[12])
    array5.append(array1[13])
    array5.append(array1[14])
    array5.append(array1[15])
    return [array2, array3, array4, array5]

def xor_operation_2(Var1, Var2):
    Array_1 = []
    counter = 0
    while counter < 4:
        cat_1 = segment(var_binary(Var1[counter]))
        cat_2 = segment(var_binary(Var2[counter]))
        binary_output = xor_operation_1(cat_1, cat_2)  # gives var_binary out
        binary_output = fix(convert_to_hex(list_to_string(binary_output)))  # var_binary to hex
        Array_1.append(binary_output)
        counter += 1
    return Array_1

def step_functn(Var1):
    sub_1 = 0
    Array_2 = []
    Var1 = Var1.replace(" ", "")
    while sub_1 <= len(Var1) - 1:
        sub_3 = Var1[sub_1] + Var1[sub_1 + 1]
        Array_2.append(sub_3)
        sub_1 += 2
    return Array_2

def condtiton_1(Var1, Var2):
    if Var2 == 4:
        out_val = '01'
    if Var2 == 8:
        out_val = '02'
    if Var2 == 12:
        out_val = '04'
    if Var2 == 16:
        out_val = '08'
    if Var2 == 20:
        out_val = '10'
    if Var2 == 24:
        out_val = '20'
    if Var2 == 28:
        out_val = '40'
    if Var2 == 32:
        out_val = '80'
    if Var2 == 36:
        out_val = '1b'
    if Var2 == 40:
        out_val = '36'
    alpha = fix(convert_to_hex(list_to_string(xor_operation_1(segment(var_binary(out_val)), segment(var_binary(Var1))))))
    return alpha

def trans(Var1, Var2):
    cat_1 = byte_sub(byte_1(Var1))
    sub_3 = condtiton_1(cat_1[0], Var2)
    del cat_1[0]
    cat_1.insert(0, sub_3)
    return cat_1

############ Round Key Addition Module ###############

def add_round_key(Var1, Var2):
    sub_4 = step_functn(Var1)
    sub_4 = step_functn(Var2)
    sub_1 = 0
    Array_3 = []
    while sub_1 < len(sub_4):
        sub_6 = sub_4[sub_1]
        sub_5 = sub_4[sub_1]
        sub_6 = var_binary(sub_6)
        sub_5 = var_binary(sub_5)
        sub_6 = segment(sub_6)
        sub_5 = segment(sub_5)
        sub_7 = xor_operation_1(sub_6, sub_5)
        sub_7 = list_to_string(sub_7)
        sub_7 = convert_to_hex(sub_7)
        sub_7 = fix(sub_7)
        Array_3.append(sub_7)
        sub_1 += 1
    return Array_3

############## Byte Sub System ###############
def byte_sub(char_2):
    Array_4 = []
    for char_1 in char_2:
        temporary = var_binary
(char_1)
        char_3 = temporary[0:4]
        char_4 = temporary[4:8]
        char_3 = int(char_3, 2)
        char_4 = int(char_4, 2)
        char_5 = sbox[char_3][char_4]
        Array_4.append(char_5)
    return Array_4

    varriable2 = len(Var1) / 4
    while counter < (len(Var1)):
        idnn = Var1[int(counter):int((varriable2 + gen))]
        varx = pro_cor(idnn, 0)
        Array_8.append(varx)
        varx = pro_cor(idnn, 1)
        Array_8.append(varx)
        varx = pro_cor(idnn, 2)
        Array_8.append(varx)
        varx = pro_cor(idnn, 3)
        Array_8.append(varx)
        counter += varriable2
        gen += varriable2
    return Array_8

############## Key Schedule System ###############
# ##### gives list that has key_in for round 0 to 10 ######

def key_schedule(Var1):
    Var1 = Var1.replace(" ", "")
    f = Divide(Var1)
    index = 4
    while index < 44:
        if (index % 4) == 0:
            var_a = xor_operation_2(f[(index - 4)], trans(f[(index - 1)], index))
            f.append(var_a)
        else:
            var_a = xor_operation_2(f[(index - 4)], f[(index - 1)])
            f.append(var_a)
        index += 1
    counter = counter_1 = 0
    Array_7 = []
    while counter < 11:
        charecter = f[counter_1] + f[counter_1 + 1] + f[counter_1 + 2] + f[counter_1 + 3]
        Array_7.append(charecter)
        counter += 1
        counter_1 += 4
    return Array_7

########## Advanced Encryption System Implementation ##########

print('Original Plaintext and Key:')
print('Input ', plain_text)
print('Key      :', key_in)
print('----------------------------------------------------------------------------------------------------------')
print('Modified AES::::Key Schedule Results for Each Round:')
print('----------------------------------------------------------------------------------------------------------')
Round = key_schedule(key_in)
counter = 0
while counter < 11:
    print('Round', counter, ':')
    print('     Key:', Round[counter], '\n')
    counter += 1
print('----------------------------------------------------------------------------------------------------------')
print('Modified AES:::: Plain text Results at Each Round:')
print('----------------------------------------------------------------------------------------------------------')
print('Round 0 : ')
print('-----Start :', step_functn(plain_text))
fn_call_out = add_round_key(plain_text, key_in)
print('----Output:', fn_call_out, '\n')
counter = 1
while counter < 10:
    print('Round', counter, ':')
    fn_call_out = byte_sub(fn_call_out)
    fn_call_out = shift_row(fn_call_out)
    fn_call_out = MC(fn_call_out)
    fn_call_out = add_round_key(list_to_string(fn_call_out), list_to_string(Round[counter]))
    print('----Output:', fn_call_out, '\n')
    counter += 1
print('Round 10:')
fn_call_out = byte_sub(fn_call_out)
fn_call_out = shift_row(fn_call_out)
fn_call_out = add_round_key(list_to_string(fn_call_out), list_to_string(Round[10]))
print('----Output:', fn_call_out)
