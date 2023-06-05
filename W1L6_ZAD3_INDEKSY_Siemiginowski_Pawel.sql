-- *******************************************************************************
-- *                                        				 *                                  
-- *       PROJEKTOWANIE BAZ DANYCH - LABORATORIUM 		 * 	 GRUPA: 6		               
-- *                                       					 *                                  
-- *******************************************************************************
-- * 																		     
-- *   Nazwisko i imiê: Siemiginowski Pawe³                                                        
-- * 																		     
-- *******************************************************************************
-- * 																		     
-- *   Nr indeksu: 101450                                                              
-- * 																		     
-- *******************************************************************************
-- *******************************************************************************
-- * 																		     
-- *   Temat projektu: Hurtownia motoryzacyjna „Car Parts Opole”                                                              
-- * 																		     
-- *******************************************************************************


-- ===============================================================================
--   Przygotuj polecenia tworzace poni¿sze indeksy, opisz cel ich u¿ycia,
--   a nastêpnie podaj przyk³ad polecenia SQL, które je wykorzysta                                          
-- ===============================================================================


-- -------------------------------------------------------------------------------
-- POLECENIE  A. (INDEKS Z£O¯ONY)
-- -------------------------------------------------------------------------------
-- Indeks ma pozwoliæ na przyspieszenie wyszukiwania klientów firmy na podstawie nazwiska lub nazwiska i imienia.
-- -------------------------------------------------------------------------------

CREATE INDEX idx_klienci_detaliczni_nazwisko_imie ON klienci_detaliczni (nazwisko, imie);
-- -------------------------------------------------------------------------------


SELECT id_klienta, imie, nazwisko, nr_telefonu FROM klienci_detaliczni WHERE nazwisko = 'Nazwisko_1' AND nr_telefonu LIKE '+484%';

 
 -- -------------------------------------------------------------------------------
-- POLECENIE  B. (INDEKS FUNKCYJNY)
-- -------------------------------------------------------------------------------
-- Indeks sortuj¹cy pracowników wed³ug daty zatrudnienia od najnowszej do najstarszej.
-- -------------------------------------------------------------------------------

CREATE INDEX idx_pracownicy_data_zatrudnienia ON pracownicy (data_zatrudnienia DESC);
-- -------------------------------------------------------------------------------


SELECT id_pracownika, imie, nazwisko, data_zatrudnienia
FROM pracownicy WHERE data_zatrudnienia > TO_DATE('16-01-2020', 'DD-MM-YYYY')
ORDER BY data_zatrudnienia DESC;
 
 -- -------------------------------------------------------------------------------
-- POLECENIE  C. (INDEKS BITMAPOWY)
-- -------------------------------------------------------------------------------
-- Indeks korzystaj¹cy z mapy bitowej dla ka¿dej wartoœci kolumny stanowiska_id_stanowiska. Bêdzie skuteczny w przypadku z góry narzuconej, ma³ej iloœci stanowisk.
-- -------------------------------------------------------------------------------

CREATE BITMAP INDEX idx_pracownicy_stanowiska ON pracownicy(stanowiska_id_stanowiska);
-- -------------------------------------------------------------------------------


SELECT id_pracownika, imie, nazwisko, data_zatrudnienia, nr_tel
FROM pracownicy
WHERE stanowiska_id_stanowiska > 40 AND data_zatrudnienia > TO_DATE('01-02-2020', 'DD-MM-YYYY');
 
 
-- USUWANIE INDEKSÓW
DROP INDEX idx_klienci_detaliczni_nazwisko_imie;
DROP INDEX idx_pracownicy_data_zatrudnienia;
DROP INDEX idx_pracownicy_stanowiska;