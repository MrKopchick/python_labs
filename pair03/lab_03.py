# #1
# msg = input("sentence:")
# count = 0
# lyter = 0
# digits = 0
# spaces = 0
# vowels = 0
# words = 0
# vowelsType = 'aeiou'
# for char in msg:
#     count+=1
#     if char.isalpha():
#         lyter+=1
#     if char.isdigit():
#         digits+=1
#     if char == " ":
#         spaces+=1
#     if char.lower() in vowelsType:
#         vowels+=1
# words = len(msg.split())
# print("symbols: ", count)
# print("lyters: ", lyter)
# print("digits: ", digits)
# print("spaces: ", spaces)
# print("vowels: ", vowels)
# print("words: ", words)

#2
# pib = input("Enter your full name: ")
# if len(pib.split()) == 3:    
#     last = pib.split()[0].capitalize()
#     first = pib.split()[1].capitalize()[0]
#     father = pib.split()[2].capitalize()[0]
#     print(last, first + ".", father + ".")

#3
# text1 = input("Enter your text1: ").lower().replace(" ", "")
# text2 = input("Enter your text2: ").lower().replace(" ", "")
# tempText2 = text2
# if len(text1) != len(text2):
#     print("no anagram")
# else:
#     for i in text1:
#         if i in tempText2:
#             tempText2 = tempText2.replace(i, "", 1)
#             if len(tempText2) == 0:
#                 print("anagram")
#                 break
#         else:
#             print("no anagram")
#             break

#4
# text = input("Enter your text: ")

# text_list = text.lower().split()
# letter_count = 0
# unique_words = 0
# biggest_word = ""
# smallest_word = ""
# for word in text_list:
#     letter_count += len(word)
#     if len(word) > len(biggest_word):
#         biggest_word = word
#     if len(word) < len(smallest_word) or smallest_word == "":
#         smallest_word = word
#     if text_list.count(word) == 1:
#         unique_words += 1
# print("Biggest word: ", biggest_word)
# print("Smallest word: ", smallest_word)
# print("Unique words: ", unique_words)
# textReplace = input("Enter the word to replace: ")
# textReplaceWith = input("Enter the word to replace with: ")
# text = text.replace(textReplace, textReplaceWith)
# print("Modified text:", text)