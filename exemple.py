import re


ctf_file = open("test.tcf", "r")

chaine = ctf_file.read()



pattern_test_case = "(# Begin Test Case)([\s\S]*?)(# End Test Case)"
result = re.findall(pattern_test_case, chaine)
print(result[0])
