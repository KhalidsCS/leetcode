"""This time my code failed some test cases, "335/354". My approach here is wrong, because no matter how much I tried-
to make workarounds in my technique some borderline testcase failed. I think (maybe) my string matching technique is-
 strictly less powerful than going the conventional known route, but spotting errors in my code and trying
 to maximize successful testcases sharpened my ability to workaround failures and discover new patterns to check for.
  :)"""

'''LEETCODE PROBLEM: REGEX MATCHING
    Github: KhalidsCS'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        history = {".": []}
        p = self.pattern_list(p)
        j = 0
        i = 0
        print(p)
        while i < len(s):
            if j >= len(p):
                return False
            if s[i] == p[j][0] or p[j][0] == ".":
                i += 1
                if len(p[j]) == 3:
                    history = {".": []}
                    p[j] = p[j][0] + str(int(p[j][1]) - 1) + p[j][2]
                    if p[j][2] == "-" and p[j][1] == "0":
                        j += 1
                    elif p[j][2] == "*" and p[j][1] == "0":
                        p[j] = p[j][0] + "*"


                elif len(p[j]) == 2:
                    if p[j][0] not in history.keys():
                        history[p[j][0]] = 1
                    elif p[j][0] == ".":
                        history["."].append(s[i - 1])
                    else:
                        history[p[j][0]] += 1
                    continue
                else:
                    history = {".": []}
                    j += 1
            else:
                if len(p[j]) == 2:
                    j += 1
                else:
                    return False
        if len(history["."]) == 0:
            del history["."]

        print(p)
        if "." in history.keys():
            print(history["."])
        l = len(p) - 1
        print(history)
        past = l
        while l >= j:
            if len(p[l]) == 2:
                l -= 1

            elif len(p[l]) == 1:
                if not history:
                    return False
                if p[l] == list(history.keys())[0] and p[l] != ".":
                    history[p[l]] -= 1
                    if history[p[l]] == 0:
                        del history[p[l]]

                elif "." in list(history.keys())[0]:
                    if p[l] == ".":
                        history["."].pop(-1)
                    elif not self.check_before(p, past, l, history["."]):
                        return False
                    past = l

                    if len(history["."]) == 0:
                        del history["."]
                else:
                    return False
                l -= 1

            else:
                print("hello")
                if not history:
                    return False
                if p[l][0] == list(history.keys())[0] and p[l][0] != ".":
                    print(history.keys())
                    history[p[l][0]] -= 1
                    if history[p[l][0]] == 0:
                        del history[p[l][0]]

                elif "." == list(history.keys())[0]:
                    print("hello")
                    if p[l][0] == ".":
                        history["."].pop(-1)
                    elif not self.check_before(p, past, l, history["."]):
                        return False

                    if len(history["."]) == 0:
                        del history["."]
                else:
                    return False
                p[l] = p[l][0] + str(int(p[l][1]) - 1) + p[l][2]
                if p[l][1] == "0":
                    l -= 1

        print(history)
        return True

    def pattern_list(self, p):
        i = 0
        pattern = []
        while i < len(p) - 1:
            if p[i + 1] == "*":
                pattern.append(p[i] + p[i + 1])
                i += 2
            else:
                pattern.append(p[i])
                i += 1
        if i == len(p) - 1:
            pattern.append(p[i])
        j = 0
        while j < len(pattern) - 1:
            if pattern[j][0] == pattern[j + 1][0]:
                result = self.cumulate_symbols(pattern[j], pattern[j + 1])
                pattern.pop(j)
                pattern.pop(j)
                pattern.insert(j, result)
            else:
                j += 1
        return pattern

    def cumulate_symbols(self, s1, s2):
        num1 = None
        num2 = None
        if len(s1) == 2 and len(s2) < 3:
            if len(s2) == 2:
                return s1
            else:
                return s1[0] + "1*"

        elif len(s2) == 2 and len(s1) < 3:
            if len(s1) == 2:
                return s2
            else:
                return s2[0] + "1*"


        elif len(s1) == 1 and len(s2) == 1:
            return s1 + "2-"

        elif len(s1) == 3:
            if s1[2] == "-":
                if len(s2) == 3:
                    if s2[2] == "-":
                        return s1[0] + str(int(s1[1]) + int(s2[1])) + "-"
                    else:
                        return s1[0] + str(int(s1[1]) + int(s2[1])) + "*"
                elif len(s2) == 2:
                    return s1[0] + str(int(s1[1])) + "*"
                else:
                    return s1[0] + str(int(s1[1]) + 1) + "-"
            else:
                if len(s2) == 3:
                    return s1[0] + str(int(s1[1]) + int(s2[1])) + "*"
                elif len(s2) == 2:
                    return s1[0] + str(int(s1[1])) + "*"
                else:
                    return s1[0] + str(int(s1[1]) + 1) + "*"
        elif len(s2) == 3:
            if s2[2] == "-":
                if len(s1) == 3:
                    if s1[2] == "-":
                        return s2[0] + str(int(s2[1]) + int(s2[1])) + "-"
                    else:
                        return s2[0] + str(int(s2[1]) + int(s1[1])) + "*"
                elif len(s1) == 2:
                    return s2[0] + str(int(s2[1])) + "*"
                else:
                    return s2[0] + str(int(s2[1]) + 1) + "-"
            else:
                if len(s1) == 3:
                    return s2[0] + str(int(s2[1]) + int(s1[1])) + "*"
                elif len(s1) == 2:
                    return s2[0] + str(int(s2[1])) + "*"
                else:
                    return s2[0] + str(int(s2[1]) + 1) + "*"

    def check_before(self, p, past, current, history):
        j = past - 1
        last = None
        while j > current:
            if len(history) > 0 and (p[j][0] == history[-1] or p[j][0] == "."):
                print(len(history), history)
                last = history.pop()
            else:
                j -= 1
        if last is not None and last == p[current][0] or p[current][0] == ".":
            return True
        if len(history) > 0 and (p[current][0] == history[-1] or p[current][0] == "."):
            history.pop()
            return True
        return False

