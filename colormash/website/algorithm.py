def convert_hex_to_rgb(hex_name):
    string = str(hex_name)
    rgb = [0,0,0]
    rgb[0] = int("0x" + string[0].lower() + string[1].lower(),0)
    rgb[1] = int("0x" + string[2].lower() + string[3].lower(),0)
    rgb[2] = int("0x" + string[4].lower() + string[5].lower(),0)
    return rgb

def elo(eloA, eloB, score_A):
    K = 32
    expected_A = 1/(1 + 10**((eloB - eloA)/400))
    expected_B = 1 - expected_A
    score_B = 1 - score_A
    new_eloA = eloA + K*(score_A - expected_A)
    new_eloB = eloB + K*(score_B - expected_B)

    elo = [new_eloA , new_eloB]
    return elo