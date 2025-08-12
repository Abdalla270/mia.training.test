# main.py
import random  # to get word

# === Step 1 ===
file=open("data/words.txt","r")
words_list=[]
for line in file:
    word =line.strip()
    words_list.append(word)
file.close()


# === Step 2 ===
secretword=random.choice(words_list)


# === Step 3 ===
max_attempts =6
attempts =0
win =0


# === Step 4 ===
while attempts<max_attempts:
    guess =input("Enter a 5 letter word: ").lower()  #get input

    
    if len(guess)!=5:
        print("Wrong ,Word must be 5 letters!!!")
        continue  #input again


    if guess not in words_list:
        print("Wrong, Word not in list!!!")
        continue

    # === Step 5 ===
    result =["_"]*5
    temp_secret=list(secretword) 

 
    for i in range(5):
        if guess[i]==secretword[i]:
            result[i] =guess[i].upper()
            temp_secret[i]="*"

    for i in range(5):
        if result[i]=="_":
            if guess[i] in temp_secret:
                result[i]=guess[i]
                temp_secret[temp_secret.index(guess[i])]="*"

 
    print("Result:"," ".join(result))

    attempts=attempts+1

    if guess==secretword:
        win=1
        break

# === Step 6: ===
if win:
    print("You Win! The word was:", secretword)
else:
    print("You Lose! The word was:", secretword)
