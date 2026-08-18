import re

text_to_search = "The rain in Spain stays mainly in the plain." 

pattern = r"ain"
matches1 = re.findall(pattern, text_to_search)

# pattern2= re.compile(r'\w')
# matches = pattern2.finditer(text_to_search)


# pattern2= re.compile(r'ain')
pattern3= re.compile(r'\b')

pattern3= re.search(pattern, text_to_search)

print(pattern3)

# print(text_to_search[5:8])
# for match in matches:
#     print(match)

    
# print(matches)
# print(pattern2)


# print(matches)

# print("hi")






