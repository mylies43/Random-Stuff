
from googletrans import Translator

if __name__ == '__main__':

    trans = Translator()


    fuckedLevel = input("From a level of 1 to 10 how messed up do you want this to be:")

    inputWord = input("What do you want to butcher today: ")

    word = trans.translate(inputWord, dest='ja')

    for i in range(0,int(fuckedLevel)):

            word = trans.translate(inputWord,dest='ja')
            word = trans.translate(word.text,dest='hi')
            word = trans.translate(word.text, dest='th')
            word = trans.translate(word.text, dest='zh-CN')
            word = trans.translate(word.text, dest='ru')
            word = trans.translate(word.text, dest='fa')
            word = trans.translate(word.text, dest='pl')
            word = trans.translate(word.text, dest='en')


    print('The output is: ',word.text)
