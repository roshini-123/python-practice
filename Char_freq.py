# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Character Frequency")

s = input("Enter String:")
freq = {}
for i in s:
    if i == ' ':
        continue
    
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] = freq[i] + 1
    
print("freq",freq)    
    
    
    
    