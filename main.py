def citire_lista():
    lst = []
    given_string_number = input("Introduceti numere intregi separate printr-un singur spatiu(space): ")
    numbers_as_string = given_string_number.split(" ")
    for i in numbers_as_string:
        lst.append(i)
    return lst


def numere_negative(lst):
    '''
    Returneaza lista formata din numerele negative din lista initiala(lst)
    :param lst: Lista initiala de numere intregi
    :return: lista_de_numere_negative : Lista de numere intregi si negative
    '''
    lista_de_numere_negative = []
    for i in lst:
        if i < 0:
            lista_de_numere_negative.append(i)
    return lista_de_numere_negative


def test_numere_negative():
    assert numere_negative([15, -15, 43, 7, -2]) == [-15, -2]
    assert numere_negative([5125 , 241, 5356, 657, 0]) == []
    assert numere_negative([-5, -67, -56, -3246]) == [-5, -67, -56, -3246]

def get_last_digit(numar):
    '''

    :param numar:
    :return:
    '''
    if numar < 0:
        string = str(numar)
        return int(string[len(string)-1])
    else:
        return numar % 10


def cel_mai_mic_numar_care_se_termina_cu_o_cifra_citita(lst, cifra_citita):
    '''

    :param lst:
    :param cifra_citita:
    :return:
    '''
    minim = 99999
    for i in lst:
        if get_last_digit(i) == cifra_citita and i < minim:
            minim = i
    return minim


def test_cel_mai_mic_numar_care_se_termina_cu_o_cifra_citita():
    assert cel_mai_mic_numar_care_se_termina_cu_o_cifra_citita([521, -43,542, 23, -23, -63,512], 3) == -63

def is_prime(numar):
    if numar < 2 :
        return False
    for i in range(2, numar//2 + 1):
        if numar % i == 0:
            return False
    return True


def numere_superprime(lst):
    '''

    :param lst:
    :return:
    '''
    lista_numere_superprime = []
    for i in lst:
        if i > 1:
            numar = i
            numar_presupunem_ca_este_superprim = True
            while numar != 0:
                if is_prime(numar) is False:
                    numar_presupunem_ca_este_superprim = False
                numar = numar % 10
            if numar_presupunem_ca_este_superprim == True:
                lista_numere_superprime.append(i)
    return lista_numere_superprime


def test_numere_superprime():
    pass


def print_Menu():
    print(" 1. Citirea unei liste de numere intregi")
    print(" 2. Afisarea tuturor numerelor negative nenule din lista")
    print(" 3. Afisarea celui mai mic numar care are ultima cifra egala cu o cifra de la tastatura")
    print(" 4. Afisarea tuturor numerelor din lista care sunt superprime.")
    print(" 5. Afisarea listei obtinute din lista initiala in care numerele pozitive si nenule au fost"
          "inlocuite cu CMMDC-ul lor si numerele negative au cifrele in ordine inversa")
    print(" a. Afisare lista")
    print(" x. Iesire")

def main():
    print_Menu()
    l = []
    while True:
        optiune = input("Introduceti optiunea: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "a":
            print(l)
        elif optiune == "2":
            print(numere_negative(l))
        elif optiune == "3":
            cifra = int(input("Introduceti cifra : "))
            print(cel_mai_mic_numar_care_se_termina_cu_o_cifra_citita(l,cifra))
        elif optiune == "4":
            print(numere_superprime(l))
        elif optiune == "5":
            pass
        elif optiune == "x":
            break
        else:
            print("OPTIUNE GRESITA! REINCERCATI!")


if __name__ == '__main__':
    main()