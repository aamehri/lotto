import random

def gen_nums():
    play = list()
    power = list()
    tkt_ply = list()
    for num in range(1, 70):
        play.append(num)
    for num in range(1, 27):
        power.append(num)
    random.shuffle(play)
    random.shuffle(power)

    tkt_ply= play[:5]
    tkt_ply.sort()
    tkt_ply.append(power[0])

    return tkt_ply


def fill_ticket(tkt):
    tkt = gen_nums()
    return tkt

def main():
    powerBallTicket = list()
    powerBallTicket = fill_ticket(powerBallTicket)
    print("The Power Ball Winning Numbers:")
    print("Play: ", powerBallTicket[:5], " Power Ball: ", powerBallTicket[-1])

main()