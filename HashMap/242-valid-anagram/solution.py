def compare_character_counts(s, t):
    # Step 1: Check if lengths are different
    if len(s) != len(t):
        return False

    # Step 2: Initialize dictionaries to store character counts
    countS, countT = {}, {}

    # Step 3: Loop through each character in both strings
    for i in range(len(s)):
        # Update count for string s
        if s[i] in countS:
            countS[s[i]] += 1
        else:
            countS[s[i]] = 1

        # Update count for string t
        if t[i] in countT:
            countT[t[i]] += 1
        else:
            countT[t[i]] = 1

    # Step 4: Compare the two dictionaries
    return countS == countT




# Alternate solution 
        # return sorted(s) == sorted(t)

# Another alternate solution
# return Counter(s) == Counter(t)
