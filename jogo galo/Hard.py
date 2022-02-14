def main():
    try:
        cenario = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


        def printcenario(cenario):
            print("\n" * 1000 + f"{cenario[0]}|{cenario[1]}|{cenario[2]}\n-+-+-\n{cenario[3]}|{cenario[4]}|{cenario[5]}\n-+-+-\n{cenario[6]}|{cenario[7]}|{cenario[8]}")


        def ganhou(cenario):
            pos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
            for a in pos:
                if cenario[a[0]] == cenario[a[1]] and cenario[a[1]] == cenario[a[2]] and cenario[a[0]] != " ":
                    return cenario[a[0]]
            return False


        while True:
            printcenario(cenario)
            if ganhou(cenario) == "X":
                printcenario(cenario)
                print("Player venceu")
                break
            if ganhou(cenario) == "O":
                printcenario(cenario)
                print("Bot venceu")
                break
            x = int(input(""))
            y = int(input(""))
            if not 0 < x and x < 4:
                0 / 0
            if not 0 < y and y < 4:
                0 / 0
            pos = (x - 1) + (y - 1) * 3
            while cenario[pos] != " ":
                print("[ERROR] 404")
                printcenario(cenario)
                x = int(input(""))
                y = int(input(""))
                if not 0 < x and x < 4:
                    0 / 0
                if not 0 < y and y < 4:
                    0 / 0
                pos = (x - 1) + (y - 1) * 3
            cenario[pos] = "X"
            if ganhou(cenario) == "X":
                printcenario(cenario)
                print("Player venceu")
                break
            if ganhou(cenario) == "O":
                printcenario(cenario)
                print("Bot venceu")
                break
            bot = -1
            for a in range(9):
                if cenario[a] == " ":
                    cenario[a] = "X"
                    if ganhou(cenario) == "X":
                        bot = a
                    cenario[a] = " "
            for a in range(9):
                if cenario[a] == " ":
                    cenario[a] = "O"
                    if ganhou(cenario) == "O":
                        bot = a
                    cenario[a] = " "
            if bot == -1:
                for a in [4, 2, 0, 1, 3, 5, 6, 7, 8]:
                    if cenario[a] == " ":
                        bot = a
                        break
            if bot == -1:
                printcenario(cenario)
                print("EMPATE")
                break
            cenario[bot] = "O"
    except:
        print("\n" * 1000 + "1 1|2 1|3 1\n---+---+---\n1 2|2 2|3 2\n---+---+---\n1 3|2 3|3 3")
if __name__=='__main__':
    main()