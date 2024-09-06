class Calculator:

    def __init__(self, number_1, number_2):
        '''конструктор, который выполняется при создании объекта'''
        self.number_1 = number_1
        self.number_2 = number_2

    def add(self):
        return self.number_1 + self.number_2
    def subtract(self):
        return self.number_1 - self.number_2
    def divide(self):
        if number_2 != 0:
            return self.number_1 / self.number_2

class Logger:
    def __init__(self, filename):
        self.filename = filename

    def lod_to_file(self, number_1, number_2, action):
        with open(self.filename, 'a', encoding='utf-8') as f:
            log_string = f'{number_1} {number_2}: {action} = {res}\n'
            f.write(log_string)
    def read_logs(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            print(f.read())

print('Введите два числа: ')
number_1 = int(input('Первое число: '))
number_2 = int(input('Второе число: '))
print('1-сложить')
print('2-вычесть')
print('3-делить')
print('4-прочитать логи')

ans = input('Выберите операцию: ')

calculator = Calculator(number_1, number_2)
logger = Logger('logs.txt')
logger_new = Logger('logs_new.txt')
if ans == '1':
    res = calculator.add()
    print(res)
    logger.lod_to_file(number_1, number_2, 'сложение')
    logger_new.lod_to_file(number_1, number_2, 'сложение')
elif ans == '2':
    res = calculator.subtract()
    print(res)
    logger.lod_to_file(number_1, number_2, 'вычитание')
elif ans == '3':
    res = calculator.divide()
    print(res)
    logger.lod_to_file(number_1, number_2, 'деление')
elif ans == '4':
    logger.read_logs()
else:
    print('Неверная операция')
