a_s_hours, a_s_minutes, a_s_seconds, a_e_hours, a_e_minutes, a_e_seconds = input().split(' ')
# b_s_hours, b_s_minutes, b_s_seconds, b_e_hours, b_e_minutes, b_e_seconds = input().split(' ')
# c_s_hours, c_s_minutes, c_s_seconds, c_e_hours, c_e_minutes, c_e_seconds = input().split(' ')


def time_calculator(s_h, s_m, s_s, e_h, e_m, e_s):
    end_time = e_h * 60 * 60 + e_m * 60 + e_s
    start_time = s_h * 60 * 60 + s_m * 60 + s_s
    total = end_time - start_time
    return total


a_total = time_calculator(a_s_hours, a_s_minutes, a_s_seconds, a_e_hours, a_e_minutes, a_e_seconds)

a_output_s = a_total % 60
a_output_m = int((a_total / 60) / 24)
a_output_h = int(a_total / 60)
print(a_output_h, a_output_m, a_output_s, sep=" ")



