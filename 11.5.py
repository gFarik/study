def quarter(xcoord, ycoord):
    if xcoord > 0 and ycoord > 0:
        print("1 четверть")
    elif xcoord < 0 and ycoord > 0:
        print("2 четверть")
    elif xcoord < 0 and ycoord < 0:
        print("3 четверть")
    elif xcoord > 0 and ycoord < 0:
        print("4 четверть")


quarter(xcoord= 3, ycoord= 4)
quarter(-3.5, ycoord= 8)