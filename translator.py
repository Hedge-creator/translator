from translate import Translator
while True:
    def en(): #создаём функцию для каждой операции с переводом
        translator = Translator(from_lang = "en", to_lang = "ru") #задаём языки
        text = str(input("Текст с английского: ")) #получаем нужный текст
        end_text = translator.translate(text) #переводим
        print("Перевод на русский: ", end_text) #вывод
    def ru():
        translator = Translator(from_lang = "ru", to_lang = "en")
        text = str(input("Текст с русского: "))
        end_text = translator.translate(text)
        print("Перевод на английский: ", end_text)
    choise = input("Выберите язык, с которого совершим перевод: (en или ru) ")
    #вызываем функции
    if choise == "en":
        en()
    else:
        ru()
        
