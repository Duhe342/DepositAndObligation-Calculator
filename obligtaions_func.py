from random import randrange
from math import trunc, ceil
from ObligationClass import ObligationClass


def obligation_nobuy_noadds_func(amount: int, nominal: float, price_in_percents: float, percent: float, SCI: float, cupn_in_one_year: int, cupn_total: int ):
    """ amount - планируемая сумма вложения
        nominal - номинал облигации
        price_in_percents - цена облигации в процентах
        percent - процент по купону
        SCI - накопленный купонныый доход
        cup_in_one_year -  сколько купонов выплачивается в год
        cupn_total - оставшееся количество купонов к выплате(т.е сколько еще осталось выплат купонов)
        ф-я высчитывает доход с облигации. Без докупания облигаций на довложенные средства и на купоны)
    """
    price_of_one = round(nominal * price_in_percents/100) # цена одной облигации
    price_of_one_w_com = round(price_of_one + price_of_one * 0.0057) # цена одной облигации с коммисией
    lots = trunc(amount/price_of_one_w_com) # количество купленных лотов
    w_is_left = amount - price_of_one_w_com * lots # оставшаяся сумма денег после покупки
    cupn_payment = nominal * (percent / ((cupn_in_one_year * 100))) # один купон на облигацию
    payment = lots * cupn_payment # купон на все облигации
    first_payment = payment - lots * SCI # первый купон на все облигации (тут вычитается наколпенный доход)
    res_payment = round(first_payment * 0.87) # здесь 0.87 - это учет налога 13%
    

    if SCI !=0:
        early_finish = ceil((SCI/cupn_payment) * (12/cupn_in_one_year)) # посленяя выплата будет на н-ное чилсо месяцев раньше
    
    if cupn_total == 1:
        pass
    else:
        for i in range(2, cupn_total + 1):
            res_payment += payment * 0.87
    print(price_of_one_w_com)

    total = round(res_payment + lots * nominal + w_is_left)

    if SCI ==0:
        result = {"result": total, "early_finish": "в тот же месяц"}
    else:
        result = {"result": total, "early_finish": early_finish}
    
    return result



def obligation_nobuy_adds(amount: int, nominal: float, price_in_percents: float, percent: float, SCI: float, adds: int, 
adds_period: int, cupn_in_one_year: int, cupn_total: int):

    price_of_one = round(nominal * price_in_percents/100) # цена одной облигации
    price_of_one_w_com = round(price_of_one + price_of_one * 0.0057) # цена одной облигации с коммисией
    lots = trunc(amount/price_of_one_w_com) # количество купленных лотов
    w_is_left = amount - price_of_one_w_com * lots # оставшаяся сумма денег после покупки
    cupn_payment = nominal * (percent / ((cupn_in_one_year * 100))) # один купон на облигацию
    payment = lots * cupn_payment # купон на все облигации
    first_payment = payment - lots * SCI # первый купон на все облигации (тут вычитается накопленный доход)
    pouch = w_is_left 
    res_payment = round(first_payment * 0.87)
    SCI_list = []
    result = 0
    total = 0
    early_finish = 0
    new_cupn_total = cupn_total
    

    if SCI !=0:
        early_finish = ceil((SCI/cupn_payment) * (12/cupn_in_one_year)) # посленяя выплата будет на н-ное чилсо месяцев раньше 
    
    for i in range(2,cupn_total + 1):
        res_payment += payment * 0.87 # расчет дохода для первых лотов облигаций 

    this_total = res_payment + nominal * lots
      
    e = 1
    while e <= 12/cupn_in_one_year:
        SCI_list.append(round(e*(cupn_payment*cupn_in_one_year/12)))    # список в котором обозначены все возможные нкд за месяцы
        e += 1


    for i in range(len(SCI_list)):
        if SCI < SCI_list[i]:
            position = i       #  определение позиции относительно двух выплат
            break
    

    
    for i in range(1, int((12/cupn_in_one_year * cupn_total)) - early_finish + 1): # цикл с докупкой облигаций

        if i % adds_period == 0:
            position += adds_period
            pouch += adds

        if position >= 12/cupn_in_one_year:  
            
            if position/(12/cupn_in_one_year ) >= 2:
                delta = trunc(position/(12/cupn_in_one_year -1))
                new_cupn_total = new_cupn_total  - delta
                position = position - delta * (12/cupn_in_one_year - 1)

            else:
                position = position - (12/cupn_in_one_year )
                new_cupn_total = new_cupn_total - 1
                
        
        
        if pouch/(nominal * (1 + 0.0057)) >= 1:
            new_lots = trunc(pouch/(nominal * (1 + 0.0057)))
            pouch = pouch - new_lots * (nominal * (1 + 0.0057))
            if position == 0:
                SCI = 0
            else:
                SCI = SCI_list[int(position) - 1]
            obligation = ObligationClass(lots= new_lots, nominal= nominal, percent= percent, SCI= SCI , cupn_in_one_year= cupn_in_one_year , cupn_total= new_cupn_total)
            result += obligation.result_cupn()
            total += obligation.result_cupn() + obligation.lots * obligation.nominal
        
    ova_total = round(this_total + total + pouch)
    
    if SCI ==0:
        result = {"result": ova_total, "early_finish": "в тот же месяц"}
    else:
        result = {"result": ova_total, "early_finish": early_finish}

    return result
    


def obligation_buy_noadds(amount: int, nominal: float, price_in_percents: float, percent: float, SCI: float, cupn_in_one_year: int, cupn_total: int ):
    price_of_one = round(nominal * price_in_percents/100) # цена одной облигации
    price_of_one_w_com = round(price_of_one + price_of_one * 0.0057) # цена одной облигации с коммисией
    lots = trunc(amount/price_of_one_w_com) # количество купленных лотов
    pouch = amount - price_of_one_w_com * lots # оставшаяся сумма денег после покупки
    cupn_payment = nominal * (percent / ((cupn_in_one_year * 100))) # один купон на облигацию
    payment = lots * cupn_payment # купон на все облигации
    res_payment = round((payment - lots * SCI) * 0.87) # здесь 0.87 - это учет налога 13%
    early_finish = 0

    if SCI !=0:
        early_finish = ceil((SCI/cupn_payment) * (12/cupn_in_one_year)) # посленяя выплата будет на н-ное чилсо месяцев раньше 
    
    
    for i in range(1, cupn_total + 1):

        if i == 1:
            pouch += res_payment

        else:   
            pouch += lots * cupn_payment * 0.87

        if pouch/(nominal*1.057) >= 1:
            new_lots = trunc(pouch/(nominal * 1.057))
            lots += new_lots
            pouch = pouch - new_lots * nominal * 1.057
    if early_finish != 0:
      resultat = {"result": lots * nominal + pouch, "early_finish": early_finish}
    else:
        resultat = {"result": lots * nominal + pouch, "early_finish": "в тот же месяц"}


    return resultat    

    

def obligationBuyAdds(amount: int, nominal: float, price_in_percents: float, percent: float, SCI: float, adds: int, 
adds_period: int, cupn_in_one_year: int, cupn_total: int):

    price_of_one = round(nominal * price_in_percents/100) # цена одной облигации
    price_of_one_w_com = round(price_of_one + price_of_one * 0.0057) # цена одной облигации с коммисией
    lots = trunc(amount/price_of_one_w_com) # количество купленных лотов
    w_is_left = amount - price_of_one_w_com * lots # оставшаяся сумма денег после покупки
    cupn_payment = nominal * (percent / ((cupn_in_one_year * 100))) # один купон на облигацию
    payment = lots * cupn_payment # купон на все облигации
    first_payment = payment - lots * SCI # первый купон на все облигации (тут вычитается накопленный доход)
    pouch = w_is_left 
    res_payment = round(first_payment * 0.87)
    lottings = 0
    SCI_list = []
    newObligFirstPay = 0
    early_finish = 0
    new_cupn_total = cupn_total
    cupnsPaid = 0
    paying = False

    if SCI !=0:
        early_finish = ceil((SCI/cupn_payment) * (12/cupn_in_one_year)) # посленяя выплата будет на н-ное чилсо месяцев раньше 

    e = 1
    while e <= 12/cupn_in_one_year:
        SCI_list.append(round(e*(cupn_payment*cupn_in_one_year/12)))    # список в котором обозначены все возможные нкд за месяцы
        e += 1
    

    for i in range(len(SCI_list)): 
        if SCI < SCI_list[i]:
            position = i
            break
    
    position2 = position
    
    for i in range(1, int((12/cupn_in_one_year * cupn_total)) - early_finish + 1):
            payment = lots * cupn_payment * 0.87
            
            if i % adds_period == 0:
                position += adds_period
                pouch += adds

            position2 += 1

            if position >= 12/cupn_in_one_year:

                if position/(12/cupn_in_one_year ) >= 2:
                    delta = trunc(position/(12/cupn_in_one_year -1))
                    new_cupn_total = new_cupn_total  - delta
                    position = position - delta * (12/cupn_in_one_year - 1)
                   
                else:
                    position = position - (12/cupn_in_one_year )
                    new_cupn_total = new_cupn_total - 1
            
            if pouch/(nominal * 1.057) >= 1:
                new_lots = trunc(pouch/(nominal * 1.057))
                pouch = pouch - new_lots * (nominal * 1.057)
                if position == 0:
                    SCI = 0
                else:
                    SCI = SCI_list[int(position) - 1]
                obligation = ObligationClass(lots= new_lots, nominal= nominal, percent= percent, SCI= SCI , cupn_in_one_year= cupn_in_one_year , cupn_total= new_cupn_total)
                newObligFirstPay += obligation.cupnAndLots()
                lottings += new_lots
            

            if position2 == 12/cupn_in_one_year - 1:
                paying = True
                cupnsPaid += 1
                position2 = 0
            else:
                paying = False
            
            if paying is True:

                if cupnsPaid == 1:
                    pouch += res_payment + newObligFirstPay
                    lots += lottings
                    lottings = 0
                    newObligFirstPay = 0

                pouch += payment + newObligFirstPay
                lots += lottings
                lottings = 0
                newObligFirstPay = 0

    total = round(lots * nominal + pouch)

    if early_finish ==0:
        resultat = {"result": total, "early_finish": "в тот же месяц"}
    else:
        resultat = {"result": total, "early_finish": early_finish}

    return resultat


def oblig_comparer(track):
    amount = int(input("Сумма вложения "))
    nominal = float(input("Номинал облигации "))
    priceInPrecent = float(input("Цена облигации в процентах "))
    percent = float(input("Какой процент? "))
    SCI = float(input("Какой НКД "))
    cupnsInOneYear = int(input("Сколько купонов в году "))
    cupnsLeft = int(input("Сколько купонов осталось "))

    if track == 1:
        oblig = obligation_nobuy_noadds_func(amount, nominal, priceInPrecent, percent, SCI,
                                                              cupnsInOneYear, cupnsLeft)
        result = oblig.get("result")
        early_finish = oblig.get("early_finish")
        print(f"Результат {result}, раннее завершение {early_finish}")

    elif track == 2:
        adds = int(input("Размер довложения"))
        addsPeriod = int(input("Частота довложений "))
        oblig = obligation_nobuy_adds(amount, nominal, priceInPrecent, percent, SCI, adds, addsPeriod,
                                                       cupnsInOneYear, cupnsLeft)
        result = oblig.get("result")
        early_finish = oblig.get("early_finish")
        print(f"Результат {result}, раннее завершение {early_finish}")
    elif track == 3:
        oblig = obligation_buy_noadds(amount, nominal, priceInPrecent, percent, SCI, cupnsInOneYear,
                                                       cupnsLeft)
        result = oblig.get("result")
        early_finish = oblig.get("early_finish")
        print(f"Результат {result}, раннее завершение {early_finish}")
    elif track == 4:
        adds = int(input("Размер довложения "))
        addsPeriod = int(input("Частота довложений "))
        oblig = obligationBuyAdds(amount, nominal, priceInPrecent, percent, SCI, adds, addsPeriod,
                                                   cupnsInOneYear, cupnsLeft)
        result = oblig.get("result")
        early_finish = oblig.get("early_finish")
        print(f"Результат {result}, раннее завершение {early_finish}")




            
