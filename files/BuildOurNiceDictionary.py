# BOND v. 0.5.0
# Pawel Szoltysek
# 11.05.2007

# This program uses *.txt dictionary file and spawns some nice files
#  which SnakeReader uses while checking his OCR output with a correct
#  form in dictionary. Those files are used only while Universal
#  Dictionary Structure won't work properly, and only one of these
#  files might be in use in one moment so fear not about size of
#  output files (it's [*.txt file size] times [[average length of words]
#  choose [two]]), at most one file will be in one moment loaded into
#  your RAM.

#sciezka=raw_input("Choose dictionary file: ")
sciezka="dict/slo.txt"
slownik=file(sciezka,"r")

for linijka in slownik:
    linijka=linijka.lower()
    for i in range(0,len(linijka)-1):
        for j in range(i+1,len(linijka)-1):
            NazwaPliku=linijka[i]
            for k in range(i+1,j):
                NazwaPliku=NazwaPliku+'_'
            NazwaPliku=NazwaPliku+linijka[j]
            NowySlownik=file("dict/slo/"+NazwaPliku+".txt",'a')
            if i>9:
                NowySlownik.write(str(i))
            else:
                NowySlownik.write('0')
                NowySlownik.write(str(i))
            NowySlownik.write(linijka)
            NowySlownik.close()
slownik.close()
