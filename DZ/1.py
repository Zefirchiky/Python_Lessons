def month_to_season(nomer_mesaca):
    if nomer_mesaca==12 or 1<=nomer_mesaca <=2:
             print("Зима")
    elif 3<=nomer_mesaca <=5:
             print("Весна")
    elif 6<=nomer_mesaca <=8:
             print("Лето")
    elif 9<=nomer_mesaca <=11:
             print("Осень")
    else:
        print("error")
nomer=int(input("Ведите номер месяца -->"))
month_to_season(nomer)
