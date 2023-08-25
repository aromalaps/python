# Write a function named reverse_words_in_sentence that takes a sentence (a string) as an argument
# and returns the sentence with the order of words reversed.?
list="hello world"

def reverse_words_in_sentence(li):
   s=""
   store=li.split()
   print(store)
   for i in store:
      rev=i[::-1]
      s+=rev + " "
   return s
print(reverse_words_in_sentence(list))