-- *******************************************************************************
-- *                                        				 *                                  
-- *       PROJEKTOWANIE BAZ DANYCH - LABORATORIUM 		 * 	 GRUPA: 6		               
-- *                                       					 *                                  
-- *******************************************************************************
-- * 																		     
-- *   Nazwisko i imi�: Siemiginowski Pawe�                                                        
-- * 																		     
-- *******************************************************************************
-- * 																		     
-- *   Nr indeksu: 101450                                                              
-- * 																		     
-- *******************************************************************************
-- *******************************************************************************
-- * 																		     
-- *   Temat projektu: Hurtownia motoryzacyjna �Car Parts Opole�                                                              
-- * 																		     
-- *******************************************************************************


-- ===============================================================================
--   Przygotuj polecenia tworzace poni�sze indeksy, opisz cel ich u�ycia,
--   a nast�pnie podaj przyk�ad polecenia SQL, kt�re je wykorzysta                                          
-- ===============================================================================


-- -------------------------------------------------------------------------------
-- POLECENIE  A. (INDEKS Z�O�ONY)
-- -------------------------------------------------------------------------------
-- Indeks ma pozwoli� na przyspieszenie wyszukiwania klient�w firmy na podstawie nazwiska lub nazwiska i imienia.
-- -------------------------------------------------------------------------------

CREATE INDEX idx_klienci_detaliczni_nazwisko_imie ON klienci_detaliczni (nazwisko, imie);
-- -------------------------------------------------------------------------------


SELECT id_klienta, imie, nazwisko, nr_telefonu FROM klienci_detaliczni WHERE nazwisko = 'Nazwisko_1' AND nr_telefonu LIKE '+484%';

 
 -- -------------------------------------------------------------------------------
-- POLECENIE  B. (INDEKS FUNKCYJNY)
-- -------------------------------------------------------------------------------
-- Indeks sortuj�cy pracownik�w wed�ug daty zatrudnienia od najnowszej do najstarszej.
-- -------------------------------------------------------------------------------

CREATE INDEX idx_pracownicy_data_zatrudnienia ON pracownicy (data_zatrudnienia DESC);
-- -------------------------------------------------------------------------------


SELECT id_pracownika, imie, nazwisko, data_zatrudnienia
FROM pracownicy WHERE data_zatrudnienia > TO_DATE('16-01-2020', 'DD-MM-YYYY')
ORDER BY data_zatrudnienia DESC;
 
 -- -------------------------------------------------------------------------------
-- POLECENIE  C. (INDEKS BITMAPOWY)
-- -------------------------------------------------------------------------------
-- Indeks korzystaj�cy z mapy bitowej dla ka�dej warto�ci kolumny stanowiska_id_stanowiska. B�dzie skuteczny w przypadku z g�ry narzuconej, ma�ej ilo�ci stanowisk.
-- -------------------------------------------------------------------------------

CREATE BITMAP INDEX idx_pracownicy_stanowiska ON pracownicy(stanowiska_id_stanowiska);
-- -------------------------------------------------------------------------------


SELECT id_pracownika, imie, nazwisko, data_zatrudnienia, nr_tel
FROM pracownicy
WHERE stanowiska_id_stanowiska > 40 AND data_zatrudnienia > TO_DATE('01-02-2020', 'DD-MM-YYYY');
 
 
-- USUWANIE INDEKS�W
DROP INDEX idx_klienci_detaliczni_nazwisko_imie;
DROP INDEX idx_pracownicy_data_zatrudnienia;
DROP INDEX idx_pracownicy_stanowiska;