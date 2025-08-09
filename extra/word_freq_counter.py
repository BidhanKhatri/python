
user_input = input("Enter a text in here: ")

def word_frequency(text):
    common_word = ["the", "is", "in", "and", "of", "a", "to"]
    
    result = {}

    text_list = text.split() # return an list of words


    for word in text_list:

        if word not in common_word:
            if(word in result):
                result[word] += 1
            else:
                result[word] = 1 
        
    
    print(result)


word_frequency(user_input)