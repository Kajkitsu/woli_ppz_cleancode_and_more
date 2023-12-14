### Klasy w Pythonie

W Pythonie, **klasa** to struktura umożliwiająca tworzenie obiektów, które łączą dane (atrybuty) i funkcje (metody) operujące na tych danych. Klasy są podstawowym mechanizmem programowania obiektowego w Pythonie.

```python
class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def opis(self):
        return f"{self.marka} {self.model}"
```

#### Kluczowe Pojęcia:

1. **Klasa:** Klasa to szablon, na podstawie którego tworzone są obiekty. Definiuje ona atrybuty (cechy) i metody (funkcje) obiektów.

2. **Obiekt:** Obiekt to instancja klasy. Tworzenie obiektu nazywane jest inicjalizacją. Obiekty zawierają unikalne kopie atrybutów klasy.

3. **Atrybuty:** Atrybuty to zmienne przechowywane w obiekcie.

4. **Metody:** Metody to funkcje zdefiniowane wewnątrz klasy, które działają na obiektach danej klasy.

5. **Konstruktor (`__init__`):** Specjalna metoda wywoływana podczas tworzenia obiektu. Inicjalizuje atrybuty obiektu.

   ```python
   def __init__(self, marka, model):
       self.marka = marka
       self.model = model
   ```

6. **Self:** Pierwszy parametr w definicji każdej metody klasy. Oznacza obiekt, na którym metoda jest wywoływana.

Klasy pozwalają na tworzenie strukturalnych i czytelnych struktur kodu, wspierają dziedziczenie, polimorfizm i hermetyzację, co jest charakterystyczne dla programowania obiektowego. Klasy są ważnym elementem wielu zaawansowanych projektów w Pythonie.