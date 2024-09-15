with open("books/frankenstein.txt") as f:
    file_contents=f.read()

def count_words(text):
    words=text.split()
    counter=0
    for i in range (0,len(words)):
        counter+=1
    return counter

def count_chars(text):
    text=text.lower()
    words=text.split()
    unique_chars=set()
    all_chars=[]
    char_dict={}
    counter=0
    
    for i in words:
        for j in i:
            unique_chars.add(j)
            all_chars.append(j)

    for i in all_chars:
        char_dict[i]=0

    for i in unique_chars:
        for j in all_chars:
            if i==j:
                counter+=1
                char_dict[i]=counter
        counter=0

    return char_dict

def main():
    print (count_words(file_contents))
    print (count_chars(file_contents))

main()

