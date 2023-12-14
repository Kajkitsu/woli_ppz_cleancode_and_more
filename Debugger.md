# Debuger
Debugger to narzędzie programistyczne używane do debugowania, czyli procesu znajdowania, analizowania i usuwania błędów w kodzie źródłowym programu komputerowego. Debugger umożliwia programiście monitorowanie wykonywania programu, analizowanie zmiennych, śledzenie ścieżki wykonania kodu, a także zatrzymywanie wykonania programu w określonych miejscach, aby dokładnie zbadać stan aplikacji.

## Przykład 1

```python
def modify_list(my_list):
    my_list = [10, 20, 30]
    # my_list.clear()
    # my_list.append(12)

# Przykładowa lista
numbers = [1, 2, 3, 4, 5]

# Wywołanie funkcji do modyfikacji listy
modify_list(numbers)

# Próba dostępu do zmodyfikowanej listy
print(numbers)
```


## Przykład 2
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Zamień elementy, jeśli są w złej kolejności
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Przykładowa lista
numbers = [64, 34, 25, 12, 22, 11, 90]

# Wywołanie funkcji do sortowania listy
bubble_sort(numbers)

# Wydrukowanie posortowanej listy
print("Posortowana lista:", numbers)
```

## Przykład 3
```python
def outer_method():
    matrix = generate_matrix(3, 3)
    element = get_element(matrix, 2, 3)
    return element

def generate_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(i * j)
        matrix.append(row)
    return matrix

def get_element(matrix, row, col):
    return matrix[row][col]

print(outer_method())
```


## Przykład 4
```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        # Błąd: nie sprawdzana jest dostępność środków na koncie
        self.balance += amount

    def withdraw(self, amount):
        # Błąd: nie sprawdzana jest dostępność środków na koncie
        self.balance -= amount
        
    def get_balance(self):
        return self.balance

def main():
    account = BankAccount("1234-5678-9012-3456", 1000)
    account.deposit(1000)
    account.withdraw(3000)
    print("Balance:", account.get_balance())

if __name__ == "__main__":
    main()
```

## Przykład 5
```python
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class OnlineStore:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price):
        self.products[product_id] = Product(product_id, name, price)
    
    def get_product(self, product_id):
        return self.products[product_id]
    
def main():
    store = OnlineStore()
    store.add_product(1, "Komputer", 1000)
    store.add_product(1, "Telewizor", 2000)
    print(store.get_product(1))
if __name__ == "__main__":
    main()
```