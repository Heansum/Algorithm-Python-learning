a_s_hours, a_s_minutes, a_s_seconds, a_e_hours, a_e_minutes, a_e_seconds = map(int, input().split(' '))
b_s_hours, b_s_minutes, b_s_seconds, b_e_hours, b_e_minutes, b_e_seconds = map(int, input().split(' '))
c_s_hours, c_s_minutes, c_s_seconds, c_e_hours, c_e_minutes, c_e_seconds = map(int, input().split(' '))


def time_calculator(s_h, s_m, s_s, e_h, e_m, e_s):
    end_time = e_h * 60 * 60 + e_m * 60 + e_s
    start_time = s_h * 60 * 60 + s_m * 60 + s_s
    total = end_time - start_time
    return total


a_total = time_calculator(a_s_hours, a_s_minutes, a_s_seconds, a_e_hours, a_e_minutes, a_e_seconds)
b_total = time_calculator(b_s_hours, b_s_minutes, b_s_seconds, b_e_hours, b_e_minutes, b_e_seconds)
c_total = time_calculator(c_s_hours, c_s_minutes, c_s_seconds, c_e_hours, c_e_minutes, c_e_seconds)


# a_output_s = a_total % 60
# a_output_m = int((a_total / 60) % 60)
# a_output_h = int((a_total / 60) / 60)
# print(a_output_h, a_output_m, a_output_s, sep=" ")


def output(total):
    output_s = total % 60
    output_m = int((total / 60) % 60)
    output_h = int((total / 60) / 60)
    print(output_h, output_m, output_s, sep=" ")


output(a_total)
output(b_total)
output(c_total)
