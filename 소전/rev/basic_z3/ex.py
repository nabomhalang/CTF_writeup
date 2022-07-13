from z3 import *

data = [Int('x%d'%i) for i in range(10)]

s = Solver()

s.add(316 * data[0]
	 - 901 * data[1]
     + 0 * data[2]
     - 984 * data[3]
     + 359 * data[4]
     - 986 * data[5]
     - 869 * data[6]
     - 733 * data[7]
     - 800 * data[8]
     + 621 * data[9] == -347560)

s.add(754 * data[0]
				     + 103 * data[1]
				     - 230 * data[2]
				     + 359 * data[3]
				     - 516 * data[4]
				     + 133 * data[5]
				     - 16 * data[6]
				     - 500 * data[7]
				     - 343 * data[8]
				     + 980 * data[9] == 31039)

s.add(641 * data[0]
						     +262 * data[1]
						     - 415 * data[2]
						     - 889 * data[3]
						     + 621 * data[4]
						     - 855 * data[5]
						     - 818 * data[6]
						     - 785 * data[7]
						     - 866 * data[8]
						     - 799 * data[9]== -262955 )

s.add(473 * data[0]
							     - 57 * data[1]
							     - 477 * data[2]
							     + 164 * data[3]
							     - 22 * data[4]
							     - 865 * data[5]
							     - 784 * data[6]
							     - 768 * data[7]
							     + 416 * data[8]
							    - 121 * data[9]== -180990)

s.add(944 * data[0]
                                      - 912 * data[1]
                                      + 667 * data[2]
                                      + 303 * data[3]
                                      + 524 * data[4]
                                      - 523 * data[5]
                                      + 227 * data[6]
                                      + 799 * data[7]
                                      - 618 * data[8]
                                      - 739 * data[9]== 156060)

s.add(597 * data[0]
                                              - 381 * data[1]
                                              - 996 * data[2]
                                              + 109 * data[3]
                                              + 476 * data[4]
                                              - 48 * data[5]
                                              - 710 * data[6]
                                              - 384 * data[7]
                                              - 390 * data[8]
                                              - 507 * data[9]== -143022)

s.add(164 * data[0]
                                                      - 300 * data[1]
                                                      - 808 * data[2]
                                                      + 308 * data[3]
                                                      + 311 * data[4]
                                                      - 144 * data[5]
                                                      + 230 * data[6]
                                                      + 251 * data[7]
                                                      + 998 * data[8]
                                                      - 469 * data[9]== 18791)

s.add(301 * data[0]
                                                              + 571 * data[1]
                                                              + 955 * data[2]
                                                              - 462 * data[3]
                                                              - 4 * data[4]
                                                              - 541 * data[5]
                                                              - 380 * data[6]
                                                              + 96 * data[7]
                                                              - 62 * data[8]
                                                              - 452 * data[9]== 60199)

s.add(703 * data[0]
                                                                      - 635 * data[1]
                                                                      - 733 * data[2]
                                                                      + 119 * data[3]
                                                                      - 549 * data[4]
                                                                      + 220 * data[5]
                                                                      + 739 * data[6]
                                                                      + 102 * data[7]
                                                                      + 812 * data[8]
                                                                      - 770 * data[9]== -48454)

s.add(207 * data[0]
                                                                       + 426 * data[1]
                                                                       + 324 * data[2]
                                                                       + 403 * data[3]
                                                                       + 149 * data[4]
                                                                       + 257 * data[5]
                                                                       + 765 * data[6]
                                                                       - 368 * data[7]
                                                                       + 707 * data[8]
                                                                       - 221 * data[9]== 202674)


print(s.check())

m = (s.model())

for i in range(len(data)):
    print(chr(int(str(m.evaluate(data[i])))), end='')
print()