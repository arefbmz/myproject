c_number = int(input(" please write carbon you need : "))
h_number = int(input(" please write hydrogen you need : "))
o_number = int(input(" please write oxygen you need : "))
main_mass = int(input(" please write your main mass : "))
amc = 12
amh = 1
amo = 16
empirical_mass = (c_number * amc) + \
(h_number * amh) + \
(o_number * amo)
if main_mass > 0 and (main_mass % empirical_mass) == 0:
    n_factor = main_mass // empirical_mass
    fcc = c_number * n_factor
    fhc = h_number * n_factor
    foc = o_number * n_factor
    print (f"C{fcc}H{fhc}O{foc}")
else :
    print ("Not valid!")