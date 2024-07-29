def caesar(a,k):
    a1=''
    for i in a:
        registr = 0
        k = k % 33
        if i not in alpha and i.lower() not in alpha:
            a1 += i
        else:
            if i not in alpha:
                i = i.lower()
                registr = 1
            position = alpha.index(i)
            if position + k < len(alpha):
                inew = alpha[position + k]
                if registr == 1:
                    inew = inew.upper()
                a1 += inew
            else:
                ind = position + k - len(alpha)
                inew = alpha[ind]
                if registr == 1:
                    inew = inew.upper()
                a1 += inew
    print(a1)

a = str(input())
alpha = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
counting = []
var1=alpha.index("о")
var2=alpha.index("е")
var3=alpha.index("а")
for i in alpha:
    i = i.lower()
    c = a.count(i)
    counting.append(c)
mx=counting.index(max(counting))
print('Возможные варианты расшифровки:')
caesar(a,(var1-mx))
caesar(a,(var2-mx))
caesar(a,(var3-mx))