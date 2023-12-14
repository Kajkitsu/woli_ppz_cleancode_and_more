# Klasy

Klasy w Pythonie to szablony, które definiują cechy i zachowanie obiektów. Obiekty są instancjami klas, a każda instancja ma swoje własne, unikalne wartości dla cech klasy.

Klasa jest definiowana za pomocą słowa kluczowego `class`. Nazwa klasy powinna być napisana dużymi literami i powinna odzwierciedlać cechy i zachowanie obiektów, które będzie reprezentować.

Przykład definicji klasy:

```python
class Person:
    """Klasa reprezentująca osobę."""

    def __init__(self, name, age):
        """Konstruktor klasy Person."""
        self.name = name
        self.age = age

    def say_hello(self):
        """Metoda zwracająca powitanie."""
        return "Cześć, nazywam się {} i mam {} lat.".format(self.name, self.age)
```

Powyższa klasa definiuje dwie cechy: `name` i `age`. Cechy te są dostępne dla każdej instancji klasy Person. Klasa definiuje również metodę `say_hello()`, która zwraca powitanie.

Aby utworzyć instancję klasy, należy użyć słowa kluczowego `()`. Nazwa instancji powinna być pisana małymi literami.

Przykład utworzenia instancji klasy:

```python
person = Person("Jan Kowalski", 30)
```

Powyższy kod tworzy instancję klasy Person o nazwie `person`. Cecha `name` tej instancji jest ustawiona na "Jan Kowalski", a cecha `age` jest ustawiona na 30.

Aby uzyskać dostęp do cech lub metod instancji, należy użyć kropki.

Przykład uzyskania dostępu do cech i metod instancji:

```python
print(person.name)
# Wynik: Jan Kowalski

print(person.age)
# Wynik: 30

print(person.say_hello())
# Wynik: Cześć, nazywam się Jan Kowalski i mam 30 lat.
```

Klasy mogą być dziedziczone od innych klas. Dziedziczenie pozwala na reutilizację kodu i uproszczenie tworzenia nowych klas.

Przykład dziedziczenia:

```python
class Student(Person):
    """Klasa reprezentująca studenta."""

    def __init__(self, name, age, school):
        """Konstruktor klasy Student."""
        super().__init__(name, age)
        self.school = school

    def say_hello(self):
        """Metoda zwracająca powitanie z informacją o szkole."""
        return super().say_hello() + " Studiuję na {}.".format(self.school)
```

Powyższa klasa dziedziczy od klasy Person. Klasa Student dodaje nową cechę `school`. Klasa Student również nadpisuje metodę `say_hello()`, aby dodać informację o szkole.

Aby utworzyć instancję klasy Student, należy użyć słowa kluczowego `()`. Nazwa instancji powinna być pisana małymi literami.

Przykład utworzenia instancji klasy Student:

```python
student = Student("Anna Nowak", 20, "Politechnika Warszawska")
```

Powyższy kod tworzy instancję klasy Student o nazwie `student`. Cecha `name` tej instancji jest ustawiona na "Anna Nowak", cecha `age` jest ustawiona na 20, a cecha `school` jest ustawiona na "Politechnika Warszawska".

Klasy w Pythonie to potężne narzędzie, które można wykorzystać do tworzenia złożonych i elastycznych programów.