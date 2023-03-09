import random
import sys

def randomHelperWord() -> str:
        # Open the file in read mode
    with open("/Users/jpanct/Desktop/cy.2550/Untitled/project3/words.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
    return random.choice(words)
def help()-> str:
    return "Generate a secure, memorable password using the XKCD method" + "\n" + "    -h, --help                                       show this help message and exit" + "\n" + "    -w, --words WORDS                                include WORDS words in the password" +"\n"+ "    -c CAPS, --caps CAPS                             capitalize the first letter of CAPS random words"+ "    -n NUMBERS, --numbers NUMBERS                    insert NUMBERS random numbers in the password"+ "    -s SYMBOLS, --symbols SYMBOLS                    insert SYMBOLS random symbols in the password"
def word(num)-> str:
    word = ''
    count = 0
    while(count < num):
        word += randomHelperWord()
        count += 1
    return word   
def caps(num)-> str:
    count = 0
    word = ''
    list = []
    while(count < 4):
        if num != 0:
            list.append(randomHelperWord().capitalize())
            num -= 1
        else:
            list.append(randomHelperWord())
        count += 1
    random.shuffle(list)
    return "".join([str(item) for item in list])
def numbers(nums):
    count = 0
    count1 = 0
    list = []
    while(count < 4):
        list.append(randomHelperWord())
        count+=1
    while count1 < nums:
        list.append(str(random.randint(0, 9)))
        count1+=1
    random.shuffle(list)
    return "".join([str(item) for item in list])          
def symbols(num)-> str:
    count = 0
    symbols = ['~','!','@','#','$','%','^','&','*','.',':',';']
    count = 0
    count1 = 0
    list = []
    while(count < 4):
        list.append(randomHelperWord())
        count+=1
    while count1 < num:
        list.append(str(random.choice(symbols)))
        count1+=1
    random.shuffle(list)
    return "".join([str(item) for item in list])
def generatingPassword(numN, numS)-> str:
    count = 0
    symbols = ['~','!','@','#','$','%','^','&','*','.',':',';']
    list = []
    while(count < 4):
        list.append(randomHelperWord())
        count+=1
    while numS != 0:
        list.append(str(random.choice(symbols)))
        numS -= 1
    while numN !=0:
        list.append(str(random.randint(0, 9)))
        numN -= 1
    random.shuffle(list)
    return "".join([str(item) for item in list])

def main():
    n = len(sys.argv)
    for x in range (1,n):
        if n == 2 and sys.argv[x] == "xkcdpwgen":
            print(word(4))
        if sys.argv[x] == "-h" or sys.argv[x] == "--help":
            print(help())
        if sys.argv[x] == "-w" or sys.argv[x] == "--words":
            print(word(int(sys.argv[x+1])))
        if sys.argv[x] == "-c" or sys.argv[x] == "--caps":
            print(caps(int(sys.argv[x+1])))
        if sys.argv[x] == "-n" or sys.argv[x] == "--numbers":
            print(numbers(int(sys.argv[x+1])))
        if sys.argv[x] == "-s" or sys.argv[x] == "--symbols":
            print(symbols(int(sys.argv[x+1])))   
        if sys.argv[x] == "-n" and sys.argv[x+2] == "--s":
            print(generatingPassword(int(sys.argv[x+1]), int(sys.argv[x+3])))
        if sys.argv[x] == "quit":
            break

if __name__ == "__main__":
    ##print(generatingPassword(11,4))
    main()