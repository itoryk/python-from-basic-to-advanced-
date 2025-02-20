import random

enlightenment = 500


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    day = 0
    total_karma = 0
    while total_karma < enlightenment:
        day += 1

        if random.randint(1, 10) == 1:
            dice = random.choice(['IamGodError', 'DrunkError', 'CarCrashError',
                                  'GluttonyError', 'DepressionError', 'SuicideError'])
            with open('karma.log', 'a', encoding='utf-8') as file:
                file.write(f'День: {day} Исключение: {dice}\n')
                try:
                    if dice == 'DrunkError':
                        raise DrunkError
                    elif dice == 'CarCrashError':
                        raise CarCrashError
                    elif dice == 'GluttonyError':
                        raise GluttonyError
                    elif dice == 'DepressionError':
                        raise DepressionError
                except DrunkError:
                    print(f'День: {day} Исключение: {dice}')
                except CarCrashError:
                    print(f'День: {day} Исключение: {dice}')
                except GluttonyError:
                    print(f'День: {day} Исключение: {dice}')
                except DepressionError:
                    print(f'День: {day} Исключение: {dice}')

        else:
            karma = random.randint(1, 7)
            total_karma += karma
            print(f'День: {day} Выпало кармы: {karma} Всего кармы: {total_karma}')


one_day()