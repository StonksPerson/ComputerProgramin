letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',',','.','?','"',':',"'",'-',"/","(",")"]
morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','.----','..---','...--','....-','.....','-....','--...','---..','----.','-----','--..--','.-.-.-','..--..','.-..-.','---...','.----.','-....-','-..-.','-.--.','-.--.-']
mes = ""
message = input("Type you message: ")

for i in range(len(message)):
        mes = mes + morse[letters.index(message[i])] + " "

print(mes)