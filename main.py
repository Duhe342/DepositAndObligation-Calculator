import functions
import obligtaions_func 

compare = int(input("Хотите сравнить два инструмента? 1- да, 0 - нет "))


if compare == 0:
    whatIns = int(input("Какой инструмент вы хотите изучить? (1- вклад 2 - облигация) "))

    if whatIns == 1:
        trac = int(input("Какая траектория? (1 - вклад без довложений и с ежемесячной капитализацией, "
                         "2 вклад с довложениями и ежемесячной капитализацией, 3 вклад без довложений и любой капитализацией 4 - вклад с довложениями и любой капитализацией) "))
        functions.dep_comparer(trac)

    elif whatIns == 2:
        trac = int(input("Какая траектория? (1 - без докупки и довложений, 2 - без докупки и с довложениями, "
                         "3 - с докупкой и без довложений, 4 - с докупкой и довложениями. Докупка - покупа облигаций на начисленный процент) "))
        obligtaions_func.oblig_comparer(trac)


elif compare == 1:

    #############################################

    first_instrument = int(input("Какой инструмент вы хотите сравнить? (1- вклад 2 - облигация) "))

    if first_instrument == 1:
        track_first = int(input("Какая траектория? (1 - вклад без довложений и с ежемесячной капитализацией, "
                      "2 вклад с довложениями и ежемесячной капитализацией, 3 вклад без довложений и любой капитализацией 4 - вклад с довложениями и любой капитализацией "))

    else:
        track_first = int(input("Какая траектория? (1 - без докупки и довложений, 2 - без докупки и с довложениями, "
                         "3 - с докупкой и без довложений, 4 - с докупкой и довложениями. Докупка - покупа облигаций на начисленный процент) "))


#######################################

    second_instrument = int(input("Какой инструмент вы хотите сравнить? (1- вклад 2 - облигация) "))

    if first_instrument == 1:
        track_second = int(input("Какая траектория? (1 - вклад без довложений и с ежемесячной капитализацией, "
                                "2 вклад с довложениями и ежемесячной капитализацией, 3 вклад без довложений и любой капитализацией 4 - вклад с довложениями и любой капитализацией "))

    else:
        track_second = int(input("Какая траектория? (1 - без докупки и довложений, 2 - без докупки и с довложениями, "
                                 "3 - с докупкой и без довложений, 4 - с докупкой и довложениями. Докупка - покупа облигаций на начисленный процент) "))

#######################################
    print("Первый инструмент")
    if first_instrument == 1:

        functions.dep_comparer(track_first)
    else:
        obligtaions_func.oblig_comparer(track_first)
    print()

    print("Второй инструмент")

    if second_instrument == 1:
        functions.dep_comparer(track_first)
    else:
        obligtaions_func.oblig_comparer(track_first)