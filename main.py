"""Counter-count"""


class Counter:
    """pass"""
    count = 0

    def __init__(self):
        Counter.count += 1
        self.method_count = 0

    @classmethod
    def get_count(cls):
        """Повертаємо атрибут класу"""
        return cls.count

    def method_called(self):
        """Фіксуємо кількість викликів для кожного екземпляра"""
        self.method_count += 1
        return self.method_count


c1 = Counter()
c2 = Counter()
c3 = Counter()

result = c1.get_count()
print(result)
print(c3.method_called())
