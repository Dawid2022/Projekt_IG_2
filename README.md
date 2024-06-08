# IG_projekt_2

IG_projekt_2 to wtyczka zaprojektowana do obliczania różnic wysokości między dwoma punktami oraz obliczanie powierzchni wielokąta utworzonego z punktów za pomocą metody Gaussa.

### Minimalne wymagania:

Aby korzystać z IG_projekt_2, upewnij się, że masz następujące minimalne wymagania sprzętowe i programowe:

-System operacyjny: Windows 10

-Wersja QGIS: 3.0

### Funkcjonalności wtyczki:

IG_projekt_2 oferuje następujące funkcje:

#### Obliczanie powierzchni:

Funkcja "area" oblicza powierzchnię wielokąta utworzonego z wybranych punktów za pomocą metody Gaussa. Aby użyć tej funkcji, wykonaj następujące kroki:

-Wybierz minimum trzy punkty na warstwie.

-Otwórz wtyczkę, i kliknij przycisk "Oblicz pole powierzchni".

-Wtyczka wyświetli obliczoną powierzchnię wielokąta w metrach kwadratowych.

#### Obliczanie różnic wysokości:

Funkcja "calcuate_dh" oblicza różnicę wysokości między dwoma wybranymi punktami. Aby użyć tej funkcji, wykonaj następujące kroki:

-Wybierz dwa punkty na warstwie.

-Otwórz wtyczkę, kliknij przycisk "Oblicz różnicę wysokości".

-Wtyczka wyświetli obliczoną różnicę wysokości między dwoma punktami.

### Dodatkowe uwagi:

Użytkownik powinnen wybrać z jakiej warstwy chce korzystać. Przycisk znajduje się na górze okna.

### Możliwe błędy:

-Jeśli użytkownik będzie chciał obliczyć różnicę wysokości i poda za mało punktów to wyświetli się komunikat: "Wybrano zbyt mało punktów", a w przypadku wybrania zbyt wielu punktów: "Wybrano zbyt dużo punktów",

-Jeśli użytkownik będzie chciał obliczyć pole powierzchni  i poda za mało punktów to wyświetli się komunikat: "Wybrano zbyt mało punktów",

-Jeżeli punkty pomiędzy którymi użytkownik będzie chciał obliczyć różnicę wysokości nie będą miały atrybutu 'wysokosci', wtyczka nie poda wyniku.
