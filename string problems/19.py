#Check whether a given substring exists in the main string. 
main_str = input("write any sentence: ")
sub_str = input("write any sub-sentence: ")
if sub_str in main_str:
    print("Found")
else:
    print("Not Found")