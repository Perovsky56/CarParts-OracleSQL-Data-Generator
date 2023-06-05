import getpass
import string
import oracledb
import random


def dzialy_produktowe(records):
    f = open("dzialy_produktowe.txt", "w")
    insert_sql1 = "INSERT INTO dzialy_produktowe (id_dzialu, nazwa_dzialu, sektor_magazynu, opis_dzialu) VALUES (:1, :2, :3, :4)"
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM dzialy_produktowe")
            count = cursor.fetchone()[0]
            if count == 0:
                max_id = 0
            else:
                cursor.execute("SELECT MAX(id_dzialu) FROM dzialy_produktowe")
                max_id = cursor.fetchone()[0]
            if records == 0:
                total_rows = int(input("Podaj ilość rekordów do wstawienia do tabeli działy produktowe: "))
                print("Wprowadzono: ", total_rows, " rekordów.")
            else:
                total_rows = records
            for i in range(max_id + 1, max_id + 1 + total_rows):
                id_dzialu = i
                nazwa_dzialu = f"Dział_{i}"
                sektor_magazynu = random.choice(["A", "B", "C", "D"])
                opis_dzialu = f"Opis działu_{i}"
                cursor.execute(insert_sql1, [id_dzialu, nazwa_dzialu, sektor_magazynu, opis_dzialu])
                f.write(
                    "INSERT INTO dzialy_produktowe (id_dzialu, nazwa_dzialu, sektor_magazynu, opis_dzialu) VALUES ({0}, '{1}', '{2}', '{3}');\n".format(
                        id_dzialu, nazwa_dzialu, sektor_magazynu, opis_dzialu))
                print(
                    f"Wstawiono rekord nr {i} - id_dzialu: {id_dzialu}, nazwa_dzialu: {nazwa_dzialu}, sektor_magazynu: {sektor_magazynu}, opis_dzialu: {opis_dzialu}")
            connection.commit()
            print(f"Wstawiono {total_rows} rekordów do tabeli DZIAŁY PRODUKTOWE.")
    except KeyboardInterrupt:
        print("Przerwano skrypt.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    f.close()


def stanowiska(records):
    f = open("stanowiska.txt", "w")
    insert_sql2 = "INSERT INTO stanowiska (id_stanowiska, nazwa_stanowiska, pensja_miesieczna, zakres_obowiazkow) VALUES (:1, :2, :3, :4)"
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM stanowiska")
            count = cursor.fetchone()[0]
            if count == 0:
                max_id = 0
            else:
                cursor.execute("SELECT MAX(id_stanowiska) FROM stanowiska")
                max_id = cursor.fetchone()[0]
            if records == 0:
                total_rows = int(input("Podaj ilość rekordów do wstawienia do tabeli stanowiska produktowych: "))
                print("Wprowadzono: ", total_rows, " rekordów.")
            else:
                total_rows = records
            for i in range(max_id + 1, max_id + 1 + total_rows):
                id_stanowiska = i
                nazwa_stanowiska = f"Stanowisko_{i}"
                pensja_miesieczna = round(random.uniform(3000.00, 8500.00), 2)
                zakres_obowiazkow = f"Zakres obowiazkow_{i}"
                cursor.execute(insert_sql2, [id_stanowiska, nazwa_stanowiska, pensja_miesieczna, zakres_obowiazkow])
                f.write(
                    "INSERT INTO stanowiska (id_stanowiska, nazwa_stanowiska, pensja_miesieczna, zakres_obowiazkow) VALUES ({0}, '{1}', {2}, '{3}');\n".format(
                        id_stanowiska, nazwa_stanowiska, pensja_miesieczna, zakres_obowiazkow))
                print(
                    f"Wstawiono rekord nr {i} - id_stanowiska: {id_stanowiska}, nazwa_stanowiska: {nazwa_stanowiska}, pensja_miesieczna: {pensja_miesieczna}, zakres_obowiazkow: {zakres_obowiazkow}")
            connection.commit()
            print(f"Wstawiono {total_rows} rekordów do tabeli STANOWISKA.")
    except KeyboardInterrupt:
        print("Przerwano skrypt.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    f.close()


def pracownicy(records):
    f = open("pracownicy.txt", "w")
    insert_sql3 = "INSERT INTO pracownicy (id_pracownika, imie, nazwisko, data_zatrudnienia, nr_tel, stanowiska_id_stanowiska) VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6)"
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM pracownicy")
            count = cursor.fetchone()[0]
            if count == 0:
                max_id = 0
            else:
                cursor.execute("SELECT MAX(id_pracownika) FROM pracownicy")
                max_id = cursor.fetchone()[0]
            if records == 0:
                total_rows = int(input("Podaj ilość rekordów do wstawienia do tabeli pracownicy: "))
                print("Wprowadzono: ", total_rows, " rekordów.")
            else:
                total_rows = records
            cursor.execute("SELECT MAX(id_stanowiska) FROM stanowiska")
            count2 = cursor.fetchone()[0]
            for i in range(max_id + 1, max_id + 1 + total_rows):
                id_pracownika = i
                imie = f"Imie_{i}"
                nazwisko = f"Nazwisko_{i}"

                day = i
                month = 1
                year = 2020
                while (day > 28):
                    month = month + 1
                    day = day - 28
                while (month > 12):
                    year = year + 1
                    month = 1
                data_zatrudnienia = '{0}-{1}-{2}'.format(year, month, day)

                nr_tel = f"+48" + str(random.randint(111111111, 999999999))
                stanowiska_id_stanowiska = random.randint(1, count2)
                formatted_sql3 = "INSERT INTO pracownicy (id_pracownika, imie, nazwisko, data_zatrudnienia, nr_tel, stanowiska_id_stanowiska) VALUES ({0}, '{1}', '{2}', DATE '{3}', '{4}', {5});\n".format(
                    id_pracownika, imie, nazwisko, data_zatrudnienia, nr_tel, stanowiska_id_stanowiska)
                f.write(formatted_sql3)
                cursor.execute(insert_sql3,
                               [id_pracownika, imie, nazwisko, data_zatrudnienia, nr_tel, stanowiska_id_stanowiska])
                print(
                    f"Wstawiono rekord nr {i} - id_pracownika: {id_pracownika}, imie: {imie}, nazwisko: {nazwisko}, data_zatrudnienia: {data_zatrudnienia}, nr_tel: {nr_tel}, stanowiska_id_stanowiska: {stanowiska_id_stanowiska}")
            connection.commit()
            print(f"Wstawiono {total_rows} rekordów do tabeli PRACOWNICY.")
    except KeyboardInterrupt:
        print("Przerwano skrypt.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    f.close()


def firmy_zamawiajace(records):
    f = open("firmy_zamawiajace.txt", "w")
    insert_sql4 = "INSERT INTO firmy_zamawiajace (id_firmy, nazwa_firmy, nip_firmy, miasto, kod_poczt, ulica, numer_bud, numer_lok, tel_firmowy, data_dodania) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, TO_DATE(:10, 'YYYY-MM-DD'))"
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM firmy_zamawiajace")
            count = cursor.fetchone()[0]
            if count == 0:
                max_id = 0
            else:
                cursor.execute("SELECT MAX(id_firmy) FROM firmy_zamawiajace")
                max_id = cursor.fetchone()[0]
            if records == 0:
                total_rows = int(input("Podaj ilość rekordów do wstawienia do tabeli firmy zamawiające: "))
                print("Wprowadzono: ", total_rows, " rekordów.")
            else:
                total_rows = records
            for i in range(max_id + 1, max_id + 1 + total_rows):
                id_firmy = i
                nazwa_firmy = f"Firma_{i}"
                nip_firmy = random.randint(1000000000, 9999999999)
                miasto = f"Miasto_{i}"
                kod_poczt = f"4" + str(random.randint(1111, 9999))
                ulica = f"Ulica_{i}"
                numer_bud = str(random.randint(1, 199))
                numer_lok = str(random.randint(1, 48))
                tel_firmowy = f"+48" + str(random.randint(111111111, 999999999))

                day = i
                month = 1
                year = 2021
                while (day > 28):
                    month = month + 1
                    day = day - 28
                while (month > 12):
                    year = year + 1
                    month = 1
                data_dodania = '{0}-{1}-{2}'.format(year, month, day)

                formatted_sql4 = "INSERT INTO firmy_zamawiajace (id_firmy, nazwa_firmy, nip_firmy, miasto, kod_poczt, ulica, numer_bud, numer_lok, tel_firmowy, data_dodania) VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', DATE '{9}');\n".format(
                    id_firmy, nazwa_firmy, nip_firmy, miasto, kod_poczt, ulica, numer_bud, numer_lok, tel_firmowy,
                    data_dodania)
                f.write(formatted_sql4)
                cursor.execute(insert_sql4,
                               [id_firmy, nazwa_firmy, nip_firmy, miasto, kod_poczt, ulica, numer_bud, numer_lok,
                                tel_firmowy, data_dodania])
                print(
                    f"Wstawiono rekord nr {i} - id_firmy: {id_firmy}, nazwa_firmy: {nazwa_firmy}, nip_firmy: {nip_firmy}, miasto: {miasto}, kod_poczt: {kod_poczt}, ulica: {ulica}, numer_bud: {numer_bud}, numer_lok: {numer_lok}, tel_firmowy: {tel_firmowy}, data_dodania: {data_dodania}")
            connection.commit()
            print(f"Wstawiono {total_rows} rekordów do tabeli FIRMY_ZAMAWIAJACE.")
    except KeyboardInterrupt:
        print("Przerwano skrypt.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    f.close()


def klienci_detaliczni(records):
    f = open("klienci_detaliczni.txt", "w")
    insert_sql5 = "INSERT INTO klienci_detaliczni (id_klienta, imie, nazwisko, nr_telefonu, data_dodania) VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'))"
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM klienci_detaliczni")
            count = cursor.fetchone()[0]
            if count == 0:
                max_id = 0
            else:
                cursor.execute("SELECT MAX(id_klienta) FROM klienci_detaliczni")
                max_id = cursor.fetchone()[0]
            if records == 0:
                total_rows = int(input("Podaj ilość rekordów do wstawienia do tabeli klienci detaliczni: "))
                print("Wprowadzono: ", total_rows, " rekordów.")
            else:
                total_rows = records
            for i in range(max_id + 1, max_id + 1 + total_rows):
                id_klienta = i
                imie = f"Imie_{i}"
                nazwisko = f"Nazwisko_1"
                nr_telefonu = f"+48" + str(random.randint(111111111, 999999999))

                day = i
                month = 1
                year = 2021
                while (day > 28):
                    month = month + 1
                    day = day - 28
                while (month > 12):
                    year = year + 1
                    month = 1
                data_dodania = '{0}-{1}-{2}'.format(year, month, day)

                formatted_sql5 = "INSERT INTO klienci_detaliczni (id_klienta, imie, nazwisko, nr_telefonu, data_dodania) VALUES ({0}, '{1}', '{2}', '{3}', DATE '{4}');\n".format(
                    id_klienta, imie, nazwisko, nr_telefonu, data_dodania)
                f.write(formatted_sql5)
                cursor.execute(insert_sql5, [id_klienta, imie, nazwisko, nr_telefonu, data_dodania])
                print(
                    f"Wstawiono rekord nr {i} - id_klienta: {id_klienta}, imie: {imie}, nazwisko: {nazwisko}, nr_telefonu: {nr_telefonu}, data_dodania: {data_dodania}")
            connection.commit()
            print(f"Wstawiono {total_rows} rekordów do tabeli KLIENCI_DETALICZNI.")
    except KeyboardInterrupt:
        print("Przerwano skrypt.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    f.close()


def produkty(records):
    f = open("produkty.txt", "w")
    insert_sql6 = "INSERT INTO produkty (id_produktu, kod_produktu, kod_regalu, data_dodania, dostepnych_sztuk, cena_produktu, opis_produktu, dzialy_produktowe_id_dzialu) VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6, :7, :8)"
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM produkty")
            count = cursor.fetchone()[0]
            if count == 0:
                max_id = 0
            else:
                cursor.execute("SELECT MAX(id_produktu) FROM produkty")
                max_id = cursor.fetchone()[0]
            if records == 0:
                total_rows = int(input("Podaj ilość rekordów do wstawienia do tabeli produkty: "))
                print("Wprowadzono: ", total_rows, " rekordów.")
            else:
                total_rows = records
            cursor.execute("SELECT MAX(id_dzialu) FROM dzialy_produktowe")
            count6 = cursor.fetchone()[0]
            for i in range(max_id + 1, max_id + 1 + total_rows):
                id_produktu = i
                kod_produktu = "".join(random.choice(string.digits) for _ in range(12))
                kod_regalu = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))

                day = i
                month = 1
                year = 2020
                while (day > 28):
                    month = month + 1
                    day = day - 28
                while (month > 12):
                    year = year + 1
                    month = 1
                data_dodania = '{0}-{1}-{2}'.format(year, month, day)

                dostepnych_sztuk = random.randint(1, 999)
                cena_produktu = round(random.uniform(3.99, 1900.00), 2)
                opis_produktu = "".join(random.choice(string.ascii_uppercase) for _ in range(10))
                dzialy_produktowe_id_dzialu = random.randint(1, count6)
                formatted_sql6 = "INSERT INTO pracownicy (id_produktu, kod_produktu, kod_regalu, data_dodania, dostepnych_sztuk, cena_produktu, opis_produktu, dzialy_produktowe_id_dzialu) VALUES ({0}, '{1}', '{2}', DATE '{3}', {4}, {5}, '{6}', {7});\n".format(
                    id_produktu, kod_produktu, kod_regalu, data_dodania, dostepnych_sztuk, cena_produktu, opis_produktu,
                    dzialy_produktowe_id_dzialu)
                f.write(formatted_sql6)
                cursor.execute(insert_sql6,
                               [id_produktu, kod_produktu, kod_regalu, data_dodania, dostepnych_sztuk, cena_produktu,
                                opis_produktu, dzialy_produktowe_id_dzialu])
                print(
                    f"Wstawiono rekord nr {i} - id_produktu: {id_produktu}, kod_produktu: {kod_produktu}, kod_regalu: {kod_regalu}, data_dodania: {data_dodania}, dostepnych_sztuk: {dostepnych_sztuk}, cena_produktu: {cena_produktu}, opis_produktu: {opis_produktu}, dzialy_produktowe_id_dzialu: {dzialy_produktowe_id_dzialu}")
            connection.commit()
            print(f"Wstawiono {total_rows} rekordów do tabeli PRODUKTY.")
    except KeyboardInterrupt:
        print("Przerwano skrypt.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    f.close()


def zamowienia(records):
    f = open("zamowienia.txt", "w")
    insert_sql7 = "INSERT INTO zamowienia (id_zamowienia, kwota, data_utw, rabat, inf_dodatkowe, pracownicy_id_pracownika, firmy_zamawiajace_id_firmy, klienci_detaliczni_id_klienta) VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5, :6, :7, :8)"
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM zamowienia")
            count = cursor.fetchone()[0]
            if count == 0:
                max_id = 0
            else:
                cursor.execute("SELECT MAX(id_zamowienia) FROM zamowienia")
                max_id = cursor.fetchone()[0]
            if records == 0:
                total_rows = int(input("Podaj ilość rekordów do wstawienia do tabeli zamowienia: "))
                print("Wprowadzono: ", total_rows, " rekordów.")
            else:
                total_rows = records
            cursor.execute("SELECT MAX(id_pracownika) FROM pracownicy")
            count7p = cursor.fetchone()[0]
            cursor.execute("SELECT MAX(id_firmy) FROM firmy_zamawiajace")
            count7f = cursor.fetchone()[0]
            cursor.execute("SELECT MAX(id_klienta) FROM klienci_detaliczni")
            count7k = cursor.fetchone()[0]
            for i in range(max_id + 1, max_id + 1 + total_rows):
                id_zamowienia = i
                kwota = round(random.uniform(150.00, 3000.00), 2)

                day = i
                month = 6
                year = 2022
                while (day > 28):
                    month = month + 1
                    day = day - 28
                while (month > 12):
                    year = year + 1
                    month = 1
                data_utw = '{0}-{1}-{2}'.format(year, month, day)

                if i % 2 == 0:
                    rabat = round(random.uniform(1.00, 999.99))
                else:
                    rabat = 0.00
                inf_dodatkowe = "".join(random.choice(string.ascii_uppercase) for _ in range(10))
                pracownicy_id_pracownika = random.randint(1, count7p)
                y = random.randint(1, 2)
                if y == 1:
                    firmy_zamawiajace_id_firmy = random.randint(1, count7f)
                    klienci_detaliczni_id_klienta = None
                    formatted_sql7 = "INSERT INTO zamowienia (id_zamowienia, kwota, data_utw, rabat, inf_dodatkowe, pracownicy_id_pracownika, firmy_zamawiajace_id_firmy, klienci_detaliczni_id_klienta) VALUES ({0}, {1}, DATE '{2}', {3}, '{4}', {5}, {6}, NULL);\n".format(
                        id_zamowienia, kwota, data_utw, rabat, inf_dodatkowe, pracownicy_id_pracownika,
                        firmy_zamawiajace_id_firmy)
                else:
                    firmy_zamawiajace_id_firmy = None
                    klienci_detaliczni_id_klienta = random.randint(1, count7k)
                    formatted_sql7 = "INSERT INTO zamowienia (id_zamowienia, kwota, data_utw, rabat, inf_dodatkowe, pracownicy_id_pracownika, firmy_zamawiajace_id_firmy, klienci_detaliczni_id_klienta) VALUES ({0}, {1}, DATE '{2}', {3}, '{4}', {5}, NULL, {6});\n".format(
                        id_zamowienia, kwota, data_utw, rabat, inf_dodatkowe, pracownicy_id_pracownika,
                        klienci_detaliczni_id_klienta)
                f.write(formatted_sql7)
                cursor.execute(insert_sql7,
                               [id_zamowienia, kwota, data_utw, rabat, inf_dodatkowe, pracownicy_id_pracownika,
                                firmy_zamawiajace_id_firmy, klienci_detaliczni_id_klienta])
                print(
                    f"Wstawiono rekord nr {i} - id_zamowienia: {id_zamowienia}, kwota: {kwota}, data_utw: {data_utw}, rabat: {rabat}, inf_dodatkowe: {inf_dodatkowe}, pracownicy_id_pracownika: {pracownicy_id_pracownika}, firmy_zamawiajace_id_firmy: {firmy_zamawiajace_id_firmy}, klienci_detaliczni_id_klienta: {klienci_detaliczni_id_klienta}")
            connection.commit()
            print(f"Wstawiono {total_rows} rekordów do tabeli ZAMOWIENIA.")
    except KeyboardInterrupt:
        print("Przerwano skrypt.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    f.close()


def zamowienia_produkty(records):
    f = open("zamowienia_produkty.txt", "w")
    insert_sql8 = "INSERT INTO zamowienia_produkty (zamowienia_id_zamowienia, produkty_id_produktu) VALUES (:1, :2)"
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM zamowienia_produkty")
            if records == 0:
                skip_further = input("Wciśnij enter, aby uzupełnić tabelę zamówienia_produkty.")
            cursor.execute("SELECT MAX(id_zamowienia) FROM zamowienia")
            count8z = cursor.fetchone()[0]
            cursor.execute("SELECT MAX(id_produktu) FROM produkty")
            count8p = cursor.fetchone()[0]
            for i in range(1, count8z + 1):
                zamowienia_id_zamowienia = i
                produkty_id_produktu = random.randint(1, count8p)
                formatted_sql8 = "INSERT INTO zamowienia_produkty (zamowienia_id_zamowienia, produkty_id_produktu) VALUES ({0}, {1});\n".format(
                    zamowienia_id_zamowienia, produkty_id_produktu)
                f.write(formatted_sql8)
                cursor.execute(insert_sql8, [zamowienia_id_zamowienia, produkty_id_produktu])
                print(
                    f"Wstawiono rekord nr {i} - zamowienia_id_zamowienia: {zamowienia_id_zamowienia}, produkty_id_produktu: {produkty_id_produktu}")
            connection.commit()
            print(f"Wstawiono {count8z} rekordów do tabeli ZAMOWIENIA_PRODUKTY.")
    except KeyboardInterrupt:
        print("Przerwano skrypt.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    f.close()


def faktury(records):
    f = open("faktury.txt", "w")
    insert_sql9 = "INSERT INTO faktury (id_faktury, kwota, data_wystawienia, termin_platnosci, zamowienia_id_zamowienia) VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), TO_DATE(:4, 'YYYY-MM-DD'), :5)"
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM faktury")
            cursor.execute("SELECT MAX(id_zamowienia) FROM zamowienia")
            count9 = cursor.fetchone()[0]
            if records == 0:
                total_rows = int(input("Podaj ilość rekordów do wstawienia do tabeli faktury: "))
            else:
                total_rows = records
            if total_rows > count9:
                print(
                    "Ilość wprowadzonych rekordów faktur jest większa, niż liczba zamówień. Nowa ilość rekordów faktur do wstawnia:",
                    count9)
                total_rows = count9
            else:
                print("Wprowadzono: ", total_rows, " rekordów.")
            for i in range(1, total_rows + 1):
                id_faktury = i
                kwota = round(random.uniform(150.00, 3000.00), 2)

                day = i
                month = 6
                year = 2022
                while (day > 28):
                    month = month + 1
                    day = day - 28
                while (month > 12):
                    year = year + 1
                    month = 1
                data_wystawienia = '{0}-{1}-{2}'.format(year, month, day)

                day2 = i + 1
                month2 = 6
                year2 = 2022
                while (day2 > 28):
                    month2 = month2 + 1
                    day2 = day2 - 28
                while (month2 > 12):
                    year2 = year2 + 1
                    month2 = 1
                termin_platnosci = '{0}-{1}-{2}'.format(year2, month2, day2)

                zamowienia_id_zamowienia = i
                formatted_sql9 = f"INSERT INTO faktury (id_faktury, kwota, data_wystawienia, termin_platnosci, zamowienia_id_zamowienia) VALUES ({0}, {1}, DATE '{2}', DATE '{3}', {4});\n".format(
                    id_faktury, kwota, data_wystawienia, termin_platnosci, zamowienia_id_zamowienia)
                f.write(formatted_sql9)
                cursor.execute(insert_sql9,
                               [id_faktury, kwota, data_wystawienia, termin_platnosci, zamowienia_id_zamowienia])
                print(
                    f"Wstawiono rekord nr {i} - id_faktury: {id_faktury}, kwota: {kwota}, data_wystawienia: {data_wystawienia}, termin_platnosci: {termin_platnosci}, zamowienia_id_zamowienia: {zamowienia_id_zamowienia}")
            connection.commit()
            print(f"Wstawiono {total_rows} rekordów do tabeli FAKTURY.")
    except KeyboardInterrupt:
        print("Przerwano skrypt.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    f.close()


def dostawy(records):
    f = open("dostawy.txt", "w")
    insert_sql10 = "INSERT INTO dostawy (id_dostawy, nr_etykiety, data_dostawy, miasto, kod_pocztowy, ulica, numer_budynku, numer_mieszkania, zamowienia_id_zamowienia) VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5, :6, :7, :8, :9)"
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM dostawy")
            cursor.execute("SELECT MAX(id_zamowienia) FROM zamowienia")
            count10 = cursor.fetchone()[0]
            if records == 0:
                total_rows = int(input("Podaj ilość rekordów do wstawienia do tabeli dostawy: "))
            else:
                total_rows = records
            if total_rows > count10:
                print(
                    "Ilość wprowadzonych rekordów dostaw jest większa, niż liczba zamówień. Nowa ilość rekordów faktur do wstawnia:",
                    count10)
                total_rows = count10
            else:
                print("Wprowadzono: ", total_rows, " rekordów.")
            for i in range(1, total_rows + 1):
                id_dostawy = i
                nr_etykiety = random.randint(100000000, 999999999)

                day2 = i + 2
                month2 = 6
                year2 = 2022
                while (day2 > 28):
                    month2 = month2 + 1
                    day2 = day2 - 28
                while (month2 > 12):
                    year2 = year2 + 1
                    month2 = 1
                data_dostawy = '{0}-{1}-{2}'.format(year2, month2, day2)

                miasto = f"Miasto_{i}"
                kod_pocztowy = f"4" + str(random.randint(1111, 9999))
                ulica = f"Ulica_{i}"
                numer_budynku = str(random.randint(1, 199))
                numer_mieszkania = str(random.randint(1, 48))
                zamowienia_id_zamowienia = i
                formatted_sql10 = "INSERT INTO dostawy (id_dostawy, nr_etykiety, data_dostawy, miasto, kod_pocztowy, ulica, numer_budynku, numer_mieszkania, zamowienia_id_zamowienia) VALUES ({0}, {1}, DATE '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', {8});\n".format(
                    id_dostawy, nr_etykiety, data_dostawy, miasto, kod_pocztowy, ulica, numer_budynku, numer_mieszkania,
                    zamowienia_id_zamowienia)
                f.write(formatted_sql10)
                cursor.execute(insert_sql10,
                               [id_dostawy, nr_etykiety, data_dostawy, miasto, kod_pocztowy, ulica, numer_budynku,
                                numer_mieszkania, zamowienia_id_zamowienia])
                print(
                    f"Wstawiono rekord nr {i} - id_dostawy: {id_dostawy}, nr_etykiety: {nr_etykiety}, data_dostawy: {data_dostawy}, miasto: {miasto}, kod_pocztowy: {kod_pocztowy}, ulica: {ulica}, numer_budynku: {numer_budynku}, numer_mieszkania: {numer_mieszkania}, zamowienia_id_zamowienia: {zamowienia_id_zamowienia}")
            connection.commit()
            print(f"Wstawiono {total_rows} rekordów do tabeli DOSTAWY.")
    except KeyboardInterrupt:
        print("Przerwano skrypt.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    f.close()

def clear_database():
    print("Czy na pewno chcesz usunąć zawartość wszystkich tabel? (y/n)")
    print("y - tak")
    print("n - nie\n")
    selection = "w"
    while selection != "y" and selection != "n" and selection != "Y" and selection != "N":
        selection = input("Wybierz y, jeżeli chcesz usunąć. Wybierz n, jeżeli nie chcesz usunąć.")
    if selection == "n" or selection == "N":
        return
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM DOSTAWY")
            connection.commit()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM FAKTURY")
            connection.commit()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM ZAMOWIENIA_PRODUKTY")
            connection.commit()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM ZAMOWIENIA")
            connection.commit()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM PRODUKTY")
            connection.commit()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM KLIENCI_DETALICZNI")
            connection.commit()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM FIRMY_ZAMAWIAJACE")
            connection.commit()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM PRACOWNICY")
            connection.commit()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM STANOWISKA")
            connection.commit()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM DZIALY_PRODUKTOWE")
            connection.commit()
        print(f"Usunięto zawartość wszystkich tabel.")
    except KeyboardInterrupt:
        print("Przerwano skrypt.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")


def main():
    print("Zalogowano pomyślnie.\n")
    while (True):
        records = 0
        print("1 - Wstaw określoną ilość rekordów do całej bazy.")
        print("2 - Wstaw określoną ilość rekordów do każdej tabeli.")
        print("3 - Usuń zawartość tabel.")
        print("4 - Wyjdź\n")
        choice = int(input("Wybierz opcję i wciśnij 'ENTER'.\n"))
        if (choice == 1):
            flag = 0
            while (flag == 0):
                try:
                    records = int(input("\nPodaj ilość rekordów do umieszczenia w każdej tabelce:\n"))
                except Exception as e:
                    print("Wprowadzono niepoprawny typ. Program przyjmuje tylko cyfry od 1 do 3.")
                if records > 0:
                    flag = 1
                else:
                    print("Podana wartość jest niepoprawna. Program przyjmuje tylko cyfry od 1 do 3.")
            dzialy_produktowe(records)
            print()
            stanowiska(records)
            print()
            pracownicy(records)
            print()
            firmy_zamawiajace(records)
            print()
            klienci_detaliczni(records)
            print()
            produkty(records)
            print()
            zamowienia(records)
            print()
            zamowienia_produkty(records)
            print()
            faktury(records)
            print()
            dostawy(records)
            print()
        elif (choice == 2):
            dzialy_produktowe(records)
            print()
            stanowiska(records)
            print()
            pracownicy(records)
            print()
            firmy_zamawiajace(records)
            print()
            klienci_detaliczni(records)
            print()
            produkty(records)
            print()
            zamowienia(records)
            print()
            zamowienia_produkty(records)
            print()
            faktury(records)
            print()
            dostawy(records)
            print()
        elif (choice == 3):
            clear_database()
        elif (choice == 4):
            quit(1)


if __name__ == "__main__":
    print("Symulator aplikacji | ORACLE DB | 'CarParts Opole' | Paweł Siemiginowski")
    print("User: s101450")
    print("Host: 217.173.198.135")
    print("Port: 1521")
    print("Service_name: tpdb")
    user = "s101450"
    password = getpass.getpass("\nWprowadź hasło:\n")
    host = "217.173.198.135"
    port = 1521
    service_name = "tpdb"
    try:
        dsn = oracledb.makedsn(host, port, service_name=service_name)
        connection = oracledb.connect(user=user, password=password, dsn=dsn)
    except Exception as e:
        print("Połączenie nieudane ({0}).".format(e))
        quit(-1)
    print()
    main()
    connection.close()