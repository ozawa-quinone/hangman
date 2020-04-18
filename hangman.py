

def hangman(word):
    wrong=0
    stages=["",
            "________       ",
            "|              ",
            "|      |       ",
            "|      0       ",
            "|     /|\      ",
            "|      |       ",
            "|     / \      ",
            "|              "]

    rletters=list(word)
    borad=['_']*len(word)
    win=False
    print('welcome to hangman')

    while wrong<len(stages) -1 :
        print("\n")
        msg='a word input'
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            borad[cind]=char
            rletters[cind]="$"

        else:
            wrong+=1
        print(" ".join(borad))
        e=wrong+1
        print("\n".join(stages[0:e]))

        if '_' not in borad :
            print(" you  win")
            print(" ".join(borad))
            win = True
            break

    if not win :
        print("\n".join(stages[0:wrong+1]))
        print(" you loose !!the answer is {}".format(word))

if __name__ == '__main__':
    words=input('please tell me the word')
    hangman(words)
    
