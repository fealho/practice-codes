from c1737 import topFrequencies, digramFrequencyLine, digramFrequency

assert digramFrequencyLine("abccc") == ({"ab": 1, "bc": 1, "cc": 2}, 4)


assert digramFrequency(["aa"])[0]["aa"] == 1
assert  digramFrequency(["aa"])[1] == 1

assert digramFrequency(["abcd", "dd"])[0]["ab"] == 1
assert digramFrequency(["abcd", "dd"])[0]["dd"] == 2
assert digramFrequency(["abcd", "dd"])[1] == 5


assert topFrequencies(["aa"], 1)[0][0] == "aa"
assert topFrequencies(["aa"], 1)[0][1] == 1
assert .9999 < topFrequencies(["aa"], 1)[0][2] < 1.0001

assert topFrequencies(["aa", "ab"], 1)[0][0] == "aa"
assert topFrequencies(["aa", "ab"], 1)[0][1] == 2
assert .6 < topFrequencies(["aa", "ab"], 1)[0][2] < .7

assert topFrequencies(["aa", "ab"], 2)[0][0] == "aa"
assert topFrequencies(["aa", "ab"], 2)[0][1] == 2
assert .6 < topFrequencies(["aa", "ab"], 2)[0][2] < .7

assert topFrequencies(["aa", "ab"], 2)[1][0] == "ab"
assert topFrequencies(["aa", "ab"], 2)[1][1] == 1
assert .3 < topFrequencies(["aa", "ab"], 2)[1][2] < .4