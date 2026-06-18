time_to_BOoOoOm = int(input("how many time to die :"))
sec = 1
all_sec = time_to_BOoOoOm * sec
min = all_sec // 60
new_sec = all_sec % 60
hour = min // 60
new_min = min % 60
day = hour // 24
new_hour = hour % 24
print(f"{day:02} : {new_hour:02} : {new_min:02} : {new_sec:02}")
