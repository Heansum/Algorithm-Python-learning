_output_1, _input_1 = map(int, input().split())
_output_2, _input_2 = map(int, input().split())
_output_3, _input_3 = map(int, input().split())
_output_4, _input_4 = map(int, input().split())

_arr = []
person_num = _input_1
_arr.append(person_num)

person_num = person_num + _input_2 - _output_2
_arr.append(person_num)

person_num = person_num + _input_3 - _output_3
_arr.append(person_num)

person_num = person_num + _input_4 - _output_4
_arr.append(person_num)

result = max(_arr)
print(result)
