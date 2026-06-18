from math import ceil

area_length = int(input(" please write your area length : "))
area_width = int(input(" please write your area width : "))
parquet_length = int(input(" please write your parquet length : "))
parquet_width = int(input(" please write your parquet width : "))

all_meter_area = area_length * area_width

parquet_meter = parquet_length * parquet_width

all_parquet_need = ceil(all_meter_area / parquet_meter)

# if all_meter_area % parquet_meter == 0:
# all_parquet_need = all_parquet_need
# else:
# all_parquet_need += 1

print("you are need", all_parquet_need , "parquet for parquet all your area")
