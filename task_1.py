class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    # 1. Напиши геттеры
    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    # 2. Добавь товар в чек
    def add_item_to_cheque(self, name):
        try:
            if len(name) > 40 or len(name) < 1:
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
            elif name not in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')

            self.__name_items.append(name)
            self.__number_items += 1

        except ValueError as v:
            print(v)
        except NameError as n:
            print(n)

    # 3. Удали товар из чека
    def delete_item_from_check(self, name):
        try:
            if name not in self.__name_items:
                raise NameError('Позиция отсутствует в чеке')

            self.__name_items.remove(name)
            self.__number_items -= 1

        except NameError as n:
            print(n)

    # 4. Посчитай общую стоимость товаров
    def check_amount(self):
        total = []
        for a in self.__name_items:
            if a in self.__item_price:
                total.append(self.__item_price[a])

        if len(total) > 10:
            discount = sum(total) * 0.1
            return sum(total) - int(discount)
        else:
            return sum(total)

    # 5. Вычисли НДС для товаров со ставкой 20%
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        for b in self.__name_items:
            for keys, values in self.__tax_rate.items():
                if values == 20 and keys == b:
                    twenty_percent_tax.append(b)

        total = []
        for c in twenty_percent_tax:
            item_price = self.__item_price[c]
            price_nds_twenty = item_price * 0.2
            nds_twenty = price_nds_twenty + item_price
            total.append(int(nds_twenty))

        if len(total) > 10:
            discount = sum(total) * 0.1
            return sum(total) - int(discount)
        else:
            return sum(total)

    # 6. Вычисли НДС для товаров со ставкой 10%
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        for d in self.__name_items:
            for keys, values in self.__tax_rate.items():
                if values == 10 and keys == d:
                    ten_percent_tax.append(d)

        total = []
        for e in ten_percent_tax:
            item_price = self.__item_price[e]
            price_nds_ten = item_price * 0.1
            nds_ten = price_nds_ten + item_price
            total.append(int(nds_ten))

        if len(total) > 10:
            discount = sum(total) * 0.1
            return sum(total) - int(discount)
        else:
            return sum(total)

    # 7. Посчитай общую сумму налогов
    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    # 8. Верни номер телефона покупателя
    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            if telephone_number is not int(telephone_number):
                raise ValueError('Необходимо ввести цифры')
            elif len(str(telephone_number)) > 10:
                raise ValueError('Необходимо ввести 10 цифр после "+7"')

            return f'+7{telephone_number}'

        except ValueError as v:
            print(v)