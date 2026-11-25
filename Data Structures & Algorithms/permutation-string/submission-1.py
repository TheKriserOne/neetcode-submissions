class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)

        if m > len(s2):
            return False

        s1 = s1.encode()
        s2 = s2.encode()

        target = [0] * 26
        window = [0] * 26

        for c in s1:
            target[c - 97] += 1

        for c in s2[:m]:
            window[c - 97] += 1

        if target == window:
            return True

        for out, inc in zip(s2, s2[m:]):
            window[out - 97] -= 1
            window[inc - 97] += 1

            if target == window:
                return True

        return False