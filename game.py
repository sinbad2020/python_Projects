#الكمبيوتر بيختار كلمه عشوائيه من ليسته
#بنعرض شرط بنفس عدد حروف الكلمه 
#بنعمل لوب علي الكلمه ونطلب من المستخدم يدخل تخمين للحرف
#لو الحرف صح نبدل الاندكس بتاعه في الشرط
#=6 لو التخمين غلط بنخسر المستتخدم محاوله
#لو خمن صح قبل المحاولات ما تخلص =0 يفوز
#لو خلصت المحاولات يخسر
import random
words = ["bad", "ugly", "good"]
random_word = random.choice(words) #bad
"""
random_word[0] 
random_word[1]
random_word[2]
"""
hangman_stages = ['''😀''','''😁''','''😋''','''😥''','''🙄''','''😣''','''😫''']
#display = ["_" for i in range(len(random_word))]
display = ["_"] * len(random_word) #best
print(' '.join(display))

#لمنع خسارة محاوله اذا خمن نفس الحرف مرتين 
guessed = []
print(f"\n{hangman_stages[0]}")
tries = 6
#بتعمل لوب بعدد حروف الكلمه  العدد ده بيمثل الاندكس بتاع الحرف 
while tries > 0 and '_' in display:
    user_guess = input("guess the letter: ")
    if user_guess in guessed:
        print(f"{user_guess} already guessed ")
        continue
    for letter in range(len(random_word)):
        if random_word[letter] == user_guess:
            display[letter] = random_word[letter]
                    
    if user_guess not in random_word:
        tries -=1
        guessed.append(user_guess)
        print(f"\n{hangman_stages[6-tries]}")
    print(' '.join(display))
    print(f"you have {tries} tries left")
        
if tries == 0:
    print("you Looose")
    
else:
    print("you Win")


