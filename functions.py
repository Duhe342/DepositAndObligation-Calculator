def onecapit_no_adds_dep(amount: int, months: int, percent: float, percent_added: bool):

    """amount - изначальная сумма вклада
     months - период вклада
     percent - процент
     percent_added - будут ли проценты начисляться на счет вклада
     ф-я высчитывает результат вклада с ежимесячной капитализацией и без довложений 
    """
    res_perc = {}
    period = percent/1200
    payment = amount * period  # здесь считается выплата процента за первый месяц.
    if percent_added is True:
        result = payment + amount  # Здесь к нашей изначальной сумме добавляется процент за первый месяц
    else:
        result = amount

    buf_result = result  # буфер для результата, в случае, если довложений нет
    paid_percent = payment
    res_perc['1'] = [round(result), round(payment)] # задается первый элемент словаря, т.к первая часть вычислений идет до цикла

    for i in range(1, months + 1):
            payment = buf_result * period
            if percent_added is True:
                result = payment + buf_result
            else:
                result = amount
            buf_result = result
            paid_percent += payment
            res_perc[f'{i}'] = [round(result), round(payment)]     
    return {
        "result": round(result),
        "paid_percent": round(paid_percent),
        "dict_(results,paid_percents)": res_perc
    }


def onecapit_adds_dep(amount: int, months: int, percent: float, adds: int, adds_period: int, percent_added: bool):

    """amount - изначальная сумма вклада
     months - период вклада
     percent - процент
     adds - довложения
     adds_period - период довложений
     percent_added - будут ли проценты начисляться на счет вклада
     ф-я высчитывает результат вклада с ежимесячной капитализацией и с довложениями по разным периодам 
    """   
    
    res_perc = {}
    period = percent/1200
    payment = amount * period  # здесь считается выплата процента за первый месяц.
    if percent_added is True:
        result = payment + amount  # Здесь к нашей изначальной сумме добавляется процент за первый месяц
    else: 
        result = amount
    buf_result = result  # буфер для результата, в случае, если довложений нет
    paid_percent = payment
    res_perc['1'] = [round(result), round(payment)] # задается первый элемент словаря, т.к первая часть вычислений идет до цикла

    for i in range(2, months + 1):

        if i % adds_period == 0:
            buf_result = result + adds
        else:
            buf_result = result

        payment = buf_result * period
        if percent_added is True:
            result = payment + buf_result
        result = buf_result
        paid_percent += payment
        res_perc[f'{i}'] = [round(result), round(payment)]

    return {
        "result": round(result),
        "added_amount": round(adds * ((months / adds_period) - 1)),
        "paid_percent": round(paid_percent),
        "dict_(results,paid_percents)": res_perc
    }



def capit_no_adds_dep(amount: int, months: int, percent: float, capit_period: int, percent_added: bool):
    """amount - изначальная сумма вклада
     months - период вклада
     percent - процент
     capit_period - период капитализации 
     percent_added - будут ли проценты начисляться на счет вклада
     ф-я высчитывает результат вклада с капитализацией(разные периоды > 1), без довложений 
    """   

    period = percent / ((12/capit_period) * 100)
    res_perc = {}
    payment = 0
    result = amount
    buf_result = amount
    paid_percent = 0
    res_perc["1"] = [round(result), round(payment)]

    for i in range(1, months+1):

        if i % capit_period == 0:
            payment = buf_result*period
        else:
            payment = 0

        if percent_added is True:
            result = payment + buf_result
        else:
            result = buf_result

        buf_result = result
        paid_percent += payment

        res_perc[f"{i}"] = [round(result), round(payment)]

    
    return {
        "result": round(result),
        "paid_percent": round(paid_percent),
        "dict_(results,paid_percents)": res_perc

    }

    
def capit_adds_dep(amount: int, months: int, percent: float, capit_period: int, adds: int, adds_period: int, percent_added: bool):
    """amount - сумма вклада 
        months - период вклада
        percent - процент
        capit_period - период капитализации 
        percent_added - будут ли проценты начисляться на счет вклада
        ф-я высчитывает результат вклада с капитализацией(разные периоды > 1) и с  довложениями 
    """
   
    period = percent / ((12/capit_period) * 100)
    res_perc = {}
    payment = 0
    result = amount
    buf_result = amount
    paid_percent = 0
    res_perc["1"] = [round(result), round(payment)]
    
    for i in range(2, months+1):

        if i % capit_period == 0:
            payment = buf_result*period
        else:
            payment = 0
        
        
        try:
            if i % adds_period == 0:
                buf_result = result + adds
            else:
                buf_result = result
        except ZeroDivisionError:
            buf_result = result

        if percent_added is True:
            result = buf_result + payment
        else:
            result = buf_result

        buf_result = result
        paid_percent += payment

        res_perc[f"{i}"] = [round(result), round(payment)]

    return {
        "result": round(result),
        "added_amount": round(adds * ((months / adds_period))),
        "paid_percent": round(paid_percent),
        "dict_(results,paid_percents)": res_perc
    }

def dep_comparer(track):
    amount = int(input("Сумма вложения "))
    months = int(input("На какое количество месяцев? "))
    percent = float(input("Какой процент? "))
    percentAdded = bool(input("Проценты начислять на вклад? (1 - да, 0 - нет) "))

    if track == 1:
        func = onecapit_no_adds_dep(amount, months, percent, percentAdded)
        result = func.get("result")
        paidProcent = func.get("paid_percent")
        print(f"Результат {result}, выплаченный процент {paidProcent}")

    elif track == 2:
        adds = int(input("Размер довложения "))
        addsPeriod = int(input("Частота довложений"))
        func = onecapit_adds_dep(amount, months, percent, adds, addsPeriod, percentAdded)
        result = func.get("result")
        paidProcent = func.get("paid_percent")
        print(f"Результат {result}, выплаченный процент {paidProcent}")

    elif track == 3:
        capitPeriod = int(input("Период капитализации "))
        func = capit_no_adds_dep(amount, months, percent, capitPeriod, percentAdded)
        result = func.get("result")
        paidProcent = func.get("paid_percent")
        print(f"Результат {result}, выплаченный процент {paidProcent}")

    elif track == 4:
        adds = int(input("Размер довложения "))
        addsPeriod = int(input("Частота довложений "))
        capitPeriod = int(input("Период капитализации "))
        func = capit_adds_dep(amount, months, percent, capitPeriod, adds, addsPeriod, percentAdded)
        result = func.get("result")
        paidProcent = func.get("paid_percent")
        print(f"Результат {result}, выплаченный процент {paidProcent}")







