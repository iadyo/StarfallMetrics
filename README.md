# StarfallMetrics (wstępna wersja prezentująca koncepcję działania)
StarfallMetrics to program, który analizuje dane dotyczące meteorytów. Program przyjmuje różne parametry wejściowe, które pozwalają użytkownikowi wyszukiwać i analizować dane dotyczące meteorytów. Możliwe parametry wejściowe to:

<b>-id:</b> ID meteorytu<br>
<b>-name:</b> nazwa meteorytu<br>
<b>-date:</b> data upadku meteorytu (w formacie RRRR-MM-DD)<br>
<b>-type:</b> metoda wizualizacji danych (plot, bar, console, loc)<br>
<b>-savetopdf:</b> nazwa pliku PDF, do którego dane zostaną zapisane<br>

Program wczytuje dane dotyczące meteorytów, które mogą pochodzić z lokalnego pliku CSV lub są pobierane z bazy danych NASA, jeśli plik lokalny nie istnieje.
Po przetworzeniu danych, program wyszukuje meteoryty na podstawie podanych parametrów. Wyniki wyszukiwania mogą być wyświetlane w różny sposób, zależnie od wybranej metody wizualizacji danych. Opcje obejmują wyświetlanie wyników w konsoli, lokalizacji geograficznej meteorytów oraz generowanie wykresów.

Program daje również możliwość zapisania wyników do pliku PDF o podanej nazwie.
