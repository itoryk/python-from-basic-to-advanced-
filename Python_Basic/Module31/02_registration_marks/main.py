import re


catalogue = input('Введите регистрационные знаки: ')  #А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

print('Список номеров частных автомобилей:', re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b', catalogue))
print('Список номеров такси:', re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}\b', catalogue))
