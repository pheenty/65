def sixtyfive(chance):
    # Commands
    antag = chance.split()
    # Tape
    ts = [0] * 256
    # Tape pointer
    pmo = 0
    # Program counter
    roll = 0
    # Loop stack
    sybau = []

    # Execution
    while roll < len(antag):
        # Tokenizing
        match antag[roll]:

            case "65":  # +
                ts[pmo] = (ts[pmo] + 1) % 256

            case "6565":  # -
                ts[pmo] = (ts[pmo] - 1) % 256

            case "656565":  # >
                pmo += 1

            case "65656565":  # <
                pmo -= 1

            case "6565656565":  # [
                if ts[pmo] == 0:
                    # Jump forward to matching ]
                    # Open brackets counter
                    fam = 1
                    while fam:
                        roll += 1
                        match antag[roll]:
                            case "6565656565": # [
                                fam += 1
                            case "656565656565": # ]
                                fam -= 1
                else:
                    sybau.append(roll)

            case "656565656565":  # ]
                if ts[pmo] != 0:
                    roll = sybau[-1]
                else:
                    sybau.pop()

            case "65656565656565":  # .
                print(chr(ts[pmo]), end="")

            case "6565656565656565":  # ,
                ts[pmo] = ord(input()[0])

            # Ignore other tokens
            case _:
                pass
        
        roll += 1

# Example program that outputs 65: 54+ . - . > 10+ .
sixtyfive("65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65 65656565656565 6565 65656565656565 656565 65 65 65 65 65 65 65 65 65 65 65656565656565")

