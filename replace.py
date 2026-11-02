sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
# Replace all instances of '!' with a space
modified_sentence = sentence.replace("!", " ") # Output sentence is printed where ! is replaced with a space
reversed_sentence = " ".join(modified_sentence.split()[::-1])
print(modified_sentence)  
print(modified_sentence.upper()) # Output sentence is printed in uppercase letters
print(reversed_sentence)  # Output reversed sentence

