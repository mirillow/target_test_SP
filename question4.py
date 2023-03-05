SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53

def main():
    total = SP + RJ + MG + ES + OUTROS
    print(f"SP representa {SP/total * 100}% do faturamento mensal")
    print(f"RJ representa {RJ/total * 100}% do faturamento mensal")
    print(f"MG representa {MG/total * 100}% do faturamento mensal")
    print(f"ES representa {ES/total * 100}% do faturamento mensal")
    print(f"Outros estados representam {OUTROS/total * 100}% do faturamento mensal")

if __name__ == '__main__':
    main()