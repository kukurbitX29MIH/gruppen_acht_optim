# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import random
import math
# import numpy
import subprocess
import os
import datetime
import pathlib
from subprocess import call


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# x_bit / max_16_bit_num = x_mm / lin_sz_mm_max         proportion
#
def bit_to_mm(lin_sz_bit_loc, lin_sz_mm_max_loc=200,  lin_sz_bit_max_loc=16):
    return round((lin_sz_bit_loc * lin_sz_mm_max_loc) / lin_sz_bit_max_loc)


def sort_by_arg(num_array, result_index_array, n):
    a = enumerate(num_array)
    b = sorted(enumerate(num_array), key=lambda x: x[1])
    for i in range(0, n):
        result_index_array[i] = b[i][0]
    return len(b)


def sort_all_val(mass_array, mass_index_array, crosssec_lin_sz_mm_array, n_amount_of_crossec, u_max_ar, s_mises_max_ar, n_indiv, preftext, is_print_info=False):
    sort_by_arg(mass_array, mass_index_array, n_indiv)
    xx = [[0 for j in range(0, n_amount_of_crossec)] for i in range(n_indiv)]
    x = [0 for j in range(0, n_indiv)]
    for i in range(0, n_indiv):
        for s in range(0, n_amount_of_crossec):
            xx[i][s] = crosssec_lin_sz_mm_array[i][s]
    for i in range(0, n_indiv):
        for s in range(0, n_amount_of_crossec):
            crosssec_lin_sz_mm_array[i][s] = xx[mass_index_array[i]][s]
    for i in range(0, n_indiv):
        x[i] = mass_array[i]
    for i in range(0, n_indiv):
        mass_array[i] = x[mass_index_array[i]]
    for i in range(0, n_indiv):
        x[i] = s_mises_max_ar[i]
    for i in range(0, n_indiv):
        s_mises_max_ar[i] = x[mass_index_array[i]]
    for i in range(0, n_indiv):
        x[i] = u_max_ar[i]
    for i in range(0, n_indiv):
        u_max_ar[i] = x[mass_index_array[i]]
    if is_print_info is True:
        print(preftext)
        for i in range(0, n_indiv):
            print("    >>>indiv: ", i, " m=", mass_array[i],  end="")
            # print("  mises=", s_mises_max_ar[i],  end="")
            # print("  u=", u_max_ar[i],  end=" ")
            for s in range(0, n_amount_of_crossec):
                print(" ", crosssec_lin_sz_mm_array[i][s], end="")
        print("")
    return [u_max_ar[0], s_mises_max_ar[0], mass_array[0], crosssec_lin_sz_mm_array[0]]
    # return [u_max_ar[0], s_mises_max_ar[0], mass_array[0], crosssec_lin_sz_mm_array[0]]


def print_sec_and_mass(pre_text, post_text,  sec_lin_size_ar,  n_sec, mass, u_max_arg, s_mises_max_arg):
    print("    ", end="")
    print(pre_text, end="")
    for i in range(0, n_sec):
        print("   sec  ", end="")
        print(i, end="")
        print(":  ", end="")
        print(sec_lin_size_ar[i], end="")
    print("     mass  ", end="")
    print(mass,  end="")
    print("     u_max  ", end="")
    print(u_max_arg,  end="")
    print("     s_mises_max  ", end="")
    print(s_mises_max_arg,  end="")
    print(post_text, end="")
    return 0


def print_all_indiv(gen_num, crosssec_lin_sz_mm_array_loc, m_loc, n_indiv_loc, n_sec_loc):
    print("\n======  gen: ", gen_num)
    for i in range(0, n_indiv_loc):
        print("   >>>ind ", i, " m=",  m_loc[i], ": ", end="")
        for j in range(0, n_sec_loc):
            print(crosssec_lin_sz_mm_array_loc[i][j], " ", end="")
    # print("\n")
    return 0


def choose_rand_num_excepting(range_including, except_num):
    while 1 == 1:
        x = random.randint(0, range_including)
        if x != except_num:
            return x


def set_lin_size_crosssections_randomly(cross_sec_bit, min_loc, max_loc, n_sec):
    for i in range(0, n_sec):
        cross_sec_bit[i] = random.randint(min_loc, max_loc)
    return 0


def mass_calc(cross_sec_mm, one_sec_len_mm_loc, n_sec, density_loc):
    mass = 0
    for i in range(0, n_sec):
        mass += (float(cross_sec_mm[i]) * 0.001 * float(cross_sec_mm[i]) * 0.001 * float(one_sec_len_mm_loc) * 0.001)
    mass *= density_loc
    return mass


def get_min_ar_index(array, array_sz):
    min_arg_index = 0
    min_val = array[0]
    for i in range(1, array_sz):
        if array[i] < min_val:
            min_val = array[i]
            min_arg_index = i
    return min_arg_index


def get_max_ar_index(array, array_sz):
    max_arg_index = 0
    max_val = array[0]
    for i in range(1, array_sz):
        if array[i] > max_val:
            max_val = array[i]
            max_arg_index = i
    return max_arg_index


def print_num_in_binary(x,  is_do_line_feed=True):
    if is_do_line_feed is True:
        print("{0:032b}".format(x & (256 * 256 * 256 * 256 - 1)))
    else:
        print("{0:032b}".format(x & (256 * 256 * 256 * 256 - 1)), end="")
    return 0


def senior_bit_pos_sr(x):
    for i in range(0, 32):
        result_pow = pow(2, 31-i)
        if (x-result_pow) > 0:
            return 31-i
    print("exit")
    return 0


def one_bit_invert(num_loc, bit_pos_loc):
    mybit = (1 << bit_pos_loc)
    mybit_invert = (~(mybit & (256 * 256 * 256 * 256 - 1)))
    if (mybit & num_loc) == 0:
        num_loc = (num_loc | mybit)
    else:
        num_loc = (num_loc & mybit_invert)
    return num_loc


def bit_exchange_crossingover(x, y, bit_start_pos, bit_end_pos,  is_print_debug_info_arg=False):
    # bitlen = bit_end_pos-bit_start_pos+1
    if is_print_debug_info_arg is True:
        print("DEBUG func: bit_exchange_crossingover:")
        print("x=", end="")
        print_num_in_binary(x)
        print("y=", end="")
        print_num_in_binary(y)
    mask = 0
    for i in range(bit_start_pos, bit_end_pos+1):
        mybit1 = 1
        mybit1 = (mybit1 << i)
        mask += mybit1
    mask_invert = (~(mask & (256*256*256*256-1)))
    if is_print_debug_info_arg is True:
        print("mask=", end="")
        print_num_in_binary(mask)
        print("mask_invert=", end="")
        print_num_in_binary(mask_invert)
        print("start_pos=", bit_start_pos,  "  end_pos=", bit_end_pos)
    result_x = (x & mask_invert)+(y & mask)
    result_y = (y & mask_invert)+(x & mask)
    if is_print_debug_info_arg is True:
        print("x=", end="")
        print_num_in_binary(result_x)
        print("y=", end="")
        print_num_in_binary(result_y)
        print("DEBUG --------------------------")

    return [result_x, result_y]


def one_bit_invert_demo():
    print(" >> demo one_bit_invert_demo")
    bit_pos_loc = 3
    my_x = 82782
    print("bit_pos = ",  bit_pos_loc)
    print("--- until bit inverting x:")
    print_num_in_binary(my_x)
    my_x = one_bit_invert(my_x, bit_pos_loc)
    print("--- after bit inverting x:")
    print_num_in_binary(my_x)
    return 0


def bit_exchange_crossingover_demo():
    print(" >> bit_exchange_crossingover_demo")
    a1 = 82782
    a2 = 37162
    bit_pos_start = 0
    bit_pos_end = 5
    print("\n=== === ===  demo  crossingover")
    print("--- until crossing")
    print_num_in_binary(a1)
    print_num_in_binary(a2)
    print("--- after crossing")
    list_a1_a2 = bit_exchange_crossingover(a1, a2, bit_pos_start, bit_pos_end)
    a1 = list_a1_a2[0]
    a2 = list_a1_a2[1]
    print_num_in_binary(a1)
    print_num_in_binary(a2)
    print("\n")
    return 0


def paste_rect_secd_in_file(filename_of_script_arg, sec_lin_size_mm_array):
    rfile_is_opened_ok = True
    file_content = ""
    try:
        file = open(filename_of_script_arg, 'r')
    except IOError:
        # print("File wasn't opened: ", filename_of_script_arg, "!")
        # rfile_is_opened_ok = False
        return False
    else:
        # print("File opened succesfully: ", filename_of_script_arg, "!")
        rfile_is_opened_ok = True
    finally:
        pass

    if rfile_is_opened_ok is True:
        file_content = file.read()
        file.close()

    file_content = file_content.splitlines()

    try:
        file = open(filename_of_script_arg, 'w')
    except IOError:
        # print("File wasn't opened: ", filename_1, "!")
        rfile_is_opened_ok = False
        return False
    else:
        # print("File opened succesfully: ", filename_1, "!")
        rfile_is_opened_ok = True
    finally:
        pass

    if rfile_is_opened_ok is True:
        sec_counter = 0
        content_to_paste_in_file = ""
        for i in range(0, len(file_content)):
            line_fragment = file_content[i].split(",")
            if len(line_fragment) > 2:
                line_fragment[0].strip()
                if line_fragment[0] == "secd":
                    line_fragment[1] = str(sec_lin_size_mm_array[sec_counter]*0.001)
                    line_fragment[2] = str(sec_lin_size_mm_array[sec_counter]*0.001)
                    sec_counter += 1
            content_to_paste_in_file += ",".join(line_fragment)
            content_to_paste_in_file += "\n"
        file.write(content_to_paste_in_file)
        file.close()
    return True


def extract_u_s_mises_m_from_file(filename_result,  is_print_vals=False):
    # print(filename_result)
    is_print_vals = True
    s_mises_max = 0
    u_max = 0
    m = 0
    rfile_is_opened_ok = True

    try:
        file = open(filename_result, 'r')
    except IOError:
        # print("File wasn't opened: ", filename_result, "!")
        # rfile_is_opened_ok = False
        return [0, 0]
    else:
        # print("File opened succesfully: ", filename_result, "!")
        rfile_is_opened_ok = True
    finally:
        pass

    if rfile_is_opened_ok is True:
        file_content = file.read()
        file.close()
    # splitting analizing and output
    file_content_splited = file_content.splitlines()
    for i in range(0, len(file_content_splited)):
        line_fragment = file_content_splited[i].split("=")
        if len(line_fragment) > 1:
            line_fragment[0] = line_fragment[0].strip()
            line_fragment[1] = line_fragment[1].strip()
            if line_fragment[0] == 'u':
                u_max = line_fragment[1]
        if len(line_fragment) > 1:
            line_fragment[0] = line_fragment[0].strip()
            line_fragment[1] = line_fragment[1].strip()
            if line_fragment[0] == 's':
                s_mises_max = line_fragment[1]
        if len(line_fragment) > 1:
            line_fragment[0] = line_fragment[0].strip()
            line_fragment[1] = line_fragment[1].strip()
            if line_fragment[0] == 'v':
                m = line_fragment[1]
    # if is_print_vals is True:
    #     print("u=", u_max, "   s=", s_mises_max, "   m=", m, end="\n")
    return [u_max, s_mises_max, m]


def runAPDL(ansyscall, workingdir, scriptFilename):
    """
    runs the APDL script: scriptFilename.inp
    located in the folder: workingdir
    using APDL executable invoked by: ansyscall
    using the number of processors in: numprocessors
    returns the number of Ansys errors encountered in the run
    """
    inputFile = os.path.join(workingdir,
                             scriptFilename + ".txt")
    """
    # make the output file be the input file plus timestamp

    """
    outputFile = os.path.join(workingdir,
                              scriptFilename +
                              '{:%Y%m%d%H%M%S}'.format(datetime.datetime.now()) +
                              ".out")
    outputFile = os.path.join(workingdir,
                              scriptFilename +
                              ".out")

    """
    myoutpath="res.txt"
    outputFile = os.path.join(workingdir,
                              myoutpath)
    """

    # keep the standard ansys jobname
    # np - number of cores
    jobname = "file"
    callString = ("\"{}\" -p ansys -smp -np 4"
                  " -dir \"{}\" -j \"{}\" -s read"
                  " -b -i \"{}\" -o \"{}\"").format(
        ansyscall,
        workingdir,
        jobname,
        inputFile,
        outputFile)
    #    print("invoking ansys with: ",callString)
    call(callString, shell=False)
    # print('Start ANSYS')
    # check output file for errors
    #    print("checking for errors")
    numerrors = "undetermined"
    try:
        searchfile = open(outputFile, "r")
    except IOError:
        print("could not open", outputFile)
    else:
        for line in searchfile:
            if "NUMBER OF ERROR" in line:
                # print(line)
                numerrors = int(line.split()[-1])
        searchfile.close()
    return numerrors


def run(scriptFilename, pathansys, pathwork):
    global error
    ansyscall = pathansys
    workingdir = pathwork
    nErr = runAPDL(ansyscall,
                   workingdir,
                   scriptFilename)
    return nErr


#    print ("number of Ansys errors: ",nErr)


def launch_ansys(filename_of_script_loc,  filename_of_result_loc, path_loc, ansyscall_loc,  sec_lin_size_mm_array):
    paste_rect_secd_in_file(filename_of_script_loc, sec_lin_size_mm_array)
    run(scriptFilename, ansyscall_loc, path_loc)
    u_s_mises_m = extract_u_s_mises_m_from_file(filename_of_result_loc, False)
    return u_s_mises_m


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#

# -------------
# ============
#             \
#              \ ______
#                     \
#   ooo  ==             v

# ================================================
# parameters
# ===============================================

is_do_comments = False


# ------------------------
# main GA
# ------------------------
n_amount_of_crossec = 2
n_amount_of_steps = 25
n_indiv = 20
lin_sz_mm_min = 10
lin_sz_mm_max = 200
# n_crg_per_step = round(n_indiv/10)
n_mut_per_step = round(n_indiv/2)
n_mut_per_step = round(n_indiv/2)
prob_of_mut_in_step = 0.5

# ------------------------
# derivative
# ------------------------
#   min_16_bit_num / max_16_bit_num = lin_sz_mm_min / lin_sz_mm_max         proportion
n_indiv_div_2 = round(n_indiv/2)
crg_jun_bit = 4
crg_sen_bit = 8
crg_len_bit = crg_sen_bit-crg_jun_bit
lin_sz_bit_max = pow(2, crg_sen_bit+1)-1
lin_sz_bit_min = round((lin_sz_mm_min * lin_sz_bit_max) / lin_sz_mm_max)

# ------------------------
# material and geometry
# ------------------------
density = 8000
one_sec_len = 500

# ------------------------
# given limit
# ------------------------
u_max_lim = -0.02
s_mises_max_lim = 200000000

scriptFilename = "script"
filename_of_script = "script.txt"
filename_of_result = "res.txt"
path = pathlib.Path().resolve()
# "C:\programming_windows\python\optimization_lab_1_v2\launch_script_dir"
ansyscall = "C:\\Program Files\\ANSYS Inc_2\\ANSYS Student\\v222\\ansys\\bin\\winx64\\ANSYS222.exe"
#                       ^
#                ______/
#              /
# -------------
# ============


filename_converg_on_mass = "data_converg_on_mass.txt"
file_converg_on_mass = open(filename_converg_on_mass, 'w')
crosssec_lin_sz_mm_array = [[0 for j in range(0, n_amount_of_crossec)] for i in range(n_indiv)]
mass_array = [0 for j in range(0, n_indiv)]
mass_index_array = [0 for j in range(0, n_indiv)]
min_mass_cross_total = [0 for j in range(0, n_amount_of_crossec)]
min_mass_cross_cur = [0 for j in range(0, n_amount_of_crossec)]
is_out_of_lim_ar = [0 for j in range(0, n_indiv)]
u_max_ar = [0 for i in range(0, n_indiv)]
s_mises_max_ar = [0 for i in range(0, n_indiv)]
min_mass_cur = 0
u_max_cur = 0
s_mises_cur = 0
min_mass_total = 0
n_success_crsg_total = 0
u_max_total = 0
s_mises_max_total = 0


def set_random_indexes_half_seq(rand_seq_ar_arg, n):
    for i in range(0, n):
        rand_seq_ar_arg[i] = i
    random.shuffle(rand_seq_ar_arg)


def do_crossingover_v1(crosssec_lin_sz_mm_array, n_amount_of_crossec, n,  n_div_2):
    rand_seq_ar = [0 for i in range(0, n_indiv_div_2)]
    for s in range(0, n_amount_of_crossec):
        set_random_indexes_half_seq(rand_seq_ar, n_indiv_div_2)
        for i in range(0, n_div_2):
            crosssec_lin_sz_mm_array[n_div_2+rand_seq_ar[i]][s] = crosssec_lin_sz_mm_array[i][s]
    return 0


def set_lens_of_sec_for_set_of_indiv(crosssec_lin_sz_mm_array, lin_sz_mm_min, lin_sz_mm_max, n_amount_of_crossec, n_start, n_end, rand_set_all_sec_size_before=False):
    for i in range(n_start, n_end+1):
        if rand_set_all_sec_size_before is True:
            for s in range(0, n_amount_of_crossec):
                crosssec_lin_sz_mm_array[i][s] = random.randint(lin_sz_mm_min, lin_sz_mm_max + 1)
        else:
            number_of_sec = random.randint(0, n_amount_of_crossec - 1)
            crosssec_lin_sz_mm_array[i][number_of_sec] = random.randint(lin_sz_mm_min, lin_sz_mm_max + 1)
    return 0


def calc_set_by_ansys_with_correc(crosssec_lin_sz_mm_array, mass_array, u_max_ar, s_mises_max_ar, u_max_lim, s_mises_max_lim, lin_sz_mm_min, lin_sz_mm_max, n_amount_of_crossec, n_start, n_end, filename_of_script, filename_of_result, path, ansyscall):
    u__s_mises__m = [0, 0, 0]
    for i in range(n_start, n_end+1):
        is_into_lim = False
        while is_into_lim is False:
            u__s_mises__m = launch_ansys(filename_of_script, filename_of_result, path, ansyscall, crosssec_lin_sz_mm_array[i])
            u_max_ar[i] = float(u__s_mises__m[0])
            s_mises_max_ar[i] = float(u__s_mises__m[1])
            mass_array[i] = float(u__s_mises__m[2])
            if float(-u_max_ar[i]) <= float(-u_max_lim) and float(s_mises_max_ar[i]) <= float(s_mises_max_lim):
                is_into_lim = True
            else:
                is_into_lim = False
                number_of_sec = random.randint(0, n_amount_of_crossec-1)
                crosssec_lin_sz_mm_array[i][number_of_sec] = random.randint(lin_sz_mm_min, lin_sz_mm_max+1)
    return 0



def do_test_out_of_lim(is_out_of_lim_ar, u_max_ar, s_mises_max_ar, u_max_lim, s_mises_max_lim, mass_array, n_indiv):
    mass_sum = 0
    counter_success = 0
    for i in range(0, n_indiv):
        if float(-u_max_ar[i]) <= float(u_max_lim) and float(s_mises_max_ar[i]) <= float(s_mises_max_lim):
            is_out_of_lim_ar[i] = True
            mass_sum += mass_array[i]
            counter_success += 1
        else:
            is_out_of_lim_ar[i] = False
    return mass_sum/counter_success

#  calc initials crosss-sections sizes and masses
#

set_lens_of_sec_for_set_of_indiv(crosssec_lin_sz_mm_array, lin_sz_mm_min, lin_sz_mm_max, n_amount_of_crossec, 0, n_indiv-1, True)
calc_set_by_ansys_with_correc(crosssec_lin_sz_mm_array, mass_array, u_max_ar, s_mises_max_ar, u_max_lim, s_mises_max_lim, lin_sz_mm_min, lin_sz_mm_max, n_amount_of_crossec, 0, n_indiv-1, filename_of_script, filename_of_result, path, ansyscall)

print(" ")
# print_all_indiv(-1, crosssec_lin_sz_mm_array, mass_array, n_indiv, n_amount_of_crossec)
[u_max_cur, s_mises_max_cur, min_mass_cur, min_mass_cross_cur] = sort_all_val(mass_array, mass_index_array, crosssec_lin_sz_mm_array, n_amount_of_crossec, u_max_ar, s_mises_max_ar, n_indiv, "==== initial ====", True)
[u_max_total, s_mises_max_total, min_mass_total, min_mass_cross_total] = [u_max_cur, s_mises_max_cur, min_mass_cur, min_mass_cross_cur]

print_sec_and_mass("   evolution of cross-sections and mass in cur step:", "  \n", min_mass_cross_cur, n_amount_of_crossec, min_mass_cur, u_max_cur, s_mises_max_cur)
print_sec_and_mass("   evolution of cross-sections and mass total:", "  \n", min_mass_cross_total, n_amount_of_crossec, min_mass_total, u_max_total, s_mises_max_total)
print("   evolution of sum of all masses:", sum(mass_array), "  kg   ")
text_loc = str(sum(mass_array)).__add__("\n")
file_converg_on_mass.write(text_loc)
print(" ")



for i in range(0, n_amount_of_steps):
    #
    # ============              ============
    #  >>>>>>>>>>  crossingover <<<<<<<<<<<
    #                ^ ^ ^ ^
    if is_do_comments is True:
        print("step = ", i,   end="")

    print("crossingover")
    do_crossingover_v1(crosssec_lin_sz_mm_array, n_amount_of_crossec, n_indiv, n_indiv_div_2)
    calc_set_by_ansys_with_correc(crosssec_lin_sz_mm_array, mass_array, u_max_ar, s_mises_max_ar, u_max_lim,
                                  s_mises_max_lim, lin_sz_mm_min, lin_sz_mm_max, n_amount_of_crossec, 0, n_indiv - 1,
                                  filename_of_script, filename_of_result, path, ansyscall)

    [u_max_cur, s_mises_max_cur, min_mass_cur, min_mass_cross_cur] = sort_all_val(mass_array, mass_index_array,
                                                                                  crosssec_lin_sz_mm_array,
                                                                                  n_amount_of_crossec, u_max_ar,
                                                                                  s_mises_max_ar, n_indiv, "====  generation "+str(i), False)
    [u_max_total, s_mises_max_total, min_mass_total, min_mass_cross_total] = [u_max_cur, s_mises_max_cur, min_mass_cur,
                                                                              min_mass_cross_cur]

    # ============              ============
    #  >>>>>>>>>>    mutation   <<<<<<<<<<<
    #                ^ ^ ^ ^
    n_success_mut_cur = 0

    for k in range(0, n_mut_per_step):
        print("mutation ", k)
        num_of_indiv_for_mut = random.randint(0, n_indiv-1)
        num_of_indiv_for_mut = n_indiv - k - 1
        is_do_sort_on_the_last_step = True
        # print("debug  ", crosssec_lin_sz_mm_array[num_of_indiv_for_mut][0], " ", a)
        set_lens_of_sec_for_set_of_indiv(crosssec_lin_sz_mm_array, lin_sz_mm_min, lin_sz_mm_max, n_amount_of_crossec, num_of_indiv_for_mut,
                                     num_of_indiv_for_mut, True)
        # print("debug sec ", crosssec_lin_sz_mm_array[num_of_indiv_for_mut][0])
        calc_set_by_ansys_with_correc(crosssec_lin_sz_mm_array, mass_array, u_max_ar, s_mises_max_ar, u_max_lim,
                                      s_mises_max_lim, lin_sz_mm_min, lin_sz_mm_max, n_amount_of_crossec, num_of_indiv_for_mut,
                                      num_of_indiv_for_mut,
                                      filename_of_script, filename_of_result, path, ansyscall)
        if is_do_sort_on_the_last_step is False or k == (n_mut_per_step-1):
            [u_max_cur, s_mises_max_cur, min_mass_cur, min_mass_cross_cur] = sort_all_val(mass_array, mass_index_array,
                                                                                  crosssec_lin_sz_mm_array,
                                                                                  n_amount_of_crossec, u_max_ar,
                                                                                  s_mises_max_ar, n_indiv,
                                                                                  "====  generation " + str(i), False)
            [u_max_total, s_mises_max_total, min_mass_total, min_mass_cross_total] = [u_max_cur, s_mises_max_cur, min_mass_cur,
                                                                              min_mass_cross_cur]
        # print("debug  i=", i, " k=", k, " ")
        # print_all_indiv(i, crosssec_lin_sz_mm_array, mass_array, n_indiv, n_amount_of_crossec)
        # print("\n")
    print_all_indiv(i, crosssec_lin_sz_mm_array, mass_array, n_indiv, n_amount_of_crossec)
    print_sec_and_mass("\n   evolution of cross-sections and min mass in cur step:", "  \n",  min_mass_cross_cur,  n_amount_of_crossec, min_mass_cur, u_max_cur, s_mises_max_cur)
    print_sec_and_mass("   evolution of cross-sections and min mass total:", "  \n",  min_mass_cross_total,  n_amount_of_crossec, min_mass_total, u_max_total, s_mises_max_total)
    print("   evolution of sum of all masses:",  sum(mass_array), "  kg   \n")
    text_loc = str(sum(mass_array)).__add__("\n")
    file_converg_on_mass.write(text_loc)

file_converg_on_mass.close()

#  extract_u_s_mises_from_file("launch_script_dir\\res.txt",  True)
#  paste_rect_secd_in_file("launch_script_dir\\script.txt",  [3.1, 8.2])


