
from typing import ChainMap


print("==================================")
print("=         Central Library        =")
print("==================================")
books = ["Python", "C", "Java", "JavaScript", "PHP", "C++"]
helps = ''' 
            help                    - Show all helps.
            show books              - Show all available books.
            buy -n <book name>      - for example
                                      buy -n <python>
            books price             - show all books prcice
            exit                    - Leave this software.
        '''
books_price = '''
                 Python       :    29$
                 C            :    95$
                 Java         :    45$
                 JavaScript   :    12$
                 PHP          :    56$
                 C++          :    120$
                 HTML         :    35$
                 CSS          :    78$
                 Django       :    91$
              '''

while(True):
    command = input("CentralLibrary: ")
    if(command=="help"):
        print(helps)
    elif(command=="exit"):
        break
    elif(command=="books price"):
        print(books_price)
    elif(command=="show books" or command=="Show Books"):
        print(books)

    elif(command=="buy -n python" or command=="buy -n Python"):

        python = ''' 
                    Book Name     :   Python
                    Writer        :   Manisha Mire
                    Price         :   29$
                    Released Date :   2017
                 '''
        print(python)
        print("     Thankyou for purchase this book")
    elif(command=="buy -n c" or command=="buy -n C"):

        c = ''' 
                    Book Name     :   C
                    Writer        :   Abhi
                    Price         :   95$
                    Released Date :   2018
                 '''
        print(c)
        print("     Thankyou for purchase this book")
    elif(command=="buy -n java" or command=="buy -n Java"):

        java = ''' 
                    Book Name     :   Java
                    Writer        :   Tilak
                    Price         :   45$
                    Released Date :   2021
                 '''
        print(java)
        print("     Thankyou for purchase this book")
    elif(command=="buy -n javascript" or command=="buy -n JavaScrip" or command=="buy -n Javascript"):

        javascript = ''' 
                    Book Name     :   JavaScript
                    Writer        :   Twinkle
                    Price         :   12$
                    Released Date :   2019
                 '''
        print(javascript)
        print("     Thankyou for purchase this book")
    elif(command=="buy -n php" or command=="buy -n PHP" or command=="buy -n Php"):

        php = ''' 
                    Book Name     :   PHP
                    Writer        :   Swati Nishad
                    Price         :   56$
                    Released Date :   2014
                 '''
        print(php)
        print("     Thankyou for purchase this book")


print("Thanks for Using")
    