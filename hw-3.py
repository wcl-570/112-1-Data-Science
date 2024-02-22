#Two words are a “reverse pair” if each is the reverse of the other. Write a function that finds all the reverse pairs in the word list 

def find_reverse_pair(word_list):
    reverse_pair_list = []
    for item in word_list:
        if len(item) == len(set(item)):
            #::-1檢測reverse pair,並添加至list
            reverse_pair_list.append((item, item[::-1]))
    return reverse_pair_list 

slist = input().split(",")
print(find_reverse_pair(slist))