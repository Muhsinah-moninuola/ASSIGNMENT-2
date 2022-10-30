#unwanted = ["%20", "360p_"]
word = 'The%20Best%20Way%20To%20Survive%20Lagos%20360p_.mp4'
for i in word:
    movieTitle= word.replace("%20"," ")
    movie=movieTitle.replace('360p_', "")
print (movie)

"""this method can only work if the words to be removed are not much, if the words are many, it will be unrealistic, 
I tried using another way by saving the unwanted words in list, but it did not work out, I guess I did not get the syntax. looking forward to your correction""" 

"""unwanted = ["%20", "360p_"]
word = 'The%20Best%20Way%20To%20Survive%20Lagos%20360p_.mp4'
words = word.split()
for i in list(words):
    if i in unwanted:
        movieTitle = i.remove(unwanted)
        final_string = " ".join(movieTitle)
print(final_string)"""
    

