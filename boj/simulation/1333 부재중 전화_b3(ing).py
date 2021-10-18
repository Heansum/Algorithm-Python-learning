count_of_songs, length_of_songs, cycle_of_ring = input().split(' ')
count_of_songs = int(count_of_songs)
length_of_songs = int(length_of_songs)
cycle_of_ring = int(cycle_of_ring)


# Can hear his phone call in this time
# L < time <= L+5
# cycle_of_songs < cycle <= cycle_of_songs
# plus

# 1. 곡을 다듣지 않고 중간에 전화벨을 듣는다.
#   (1) count
# 2. 모든 곡을 다듣고 전화벨을 듣는다.

# 이렇게 두 가지.


def solution(count_of_songs, length_of_songs, cycle_of_ring):
    end_time = count_of_songs * length_of_songs + (count_of_songs - 1) * 5
    time = 0
    count = 1

    flag = 1
    flag_2 = 1
    while flag:
        # 1번 경우
        while (count < count_of_songs) & (time <= end_time):
            you_can_listen_time = length_of_songs + 5
            you_can_listen_time = you_can_listen_time * count

            ring = cycle_of_ring * count
            if (you_can_listen_time - 5) < time <= you_can_listen_time:
                if (time >= ring) & (time <= (ring + 1)):
                    flag = 0
                    return time
            if (time % cycle_of_ring == 0) & time != 0:
                count += 1
            time += 1
        time -= 1
        count += 1
        ring = cycle_of_ring * count
        while time < ring:
            if (time >= ring) & (time <= (ring + 1)):
                flag = 0
            # if time % cycle_of_ring == 0:
            #     count += 1
            time += 1
        return time


output = solution(count_of_songs, length_of_songs, cycle_of_ring)
print(output)
