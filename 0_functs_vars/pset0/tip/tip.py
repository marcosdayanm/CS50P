def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    ds = d.strip("$")
    return float(ds)


def percent_to_float(p):
    ps = p.strip("%")
    pf = float(ps)
    return pf/100


main()