# Minimum Window Substring

class Solution0: # Adapted from NC solution, see https://youtu.be/jSto0O4AJbM
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {} # Hash maps that represent the count of each character in t, 
                                # and the count of each character in our window respectively
                                # (Note that this would be a good place to use python's Counter class)
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0 # Have represents the number of the number of characters of t that we have in our window.
        # NOTE: If t has more than one of a character, we need to have all duplicates to increment have.
        resIndices = [-1, -1] # Start and end indices of the result string
        resLen = float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]: # If the current character fulfills our need for that character in t, increment have
                have += 1

            while have == len(countT): # While the window is valid
                # update our result
                if (r - l + 1) < resLen:
                    resIndices = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]: # If we drop below our need for the popped char, decrement have
                    have -= 1
                l += 1

        l, r = resIndices
        return s[l : r + 1] if resLen != float("inf") else ""


# I thought about implementing a solution with some Counter shenanigans, maybe using some of it's fun methods.
# I decided that I probably shouldn't waste time though.