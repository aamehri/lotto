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

def save(num, pr):
    try:
        f = open("lotto_results.ext", "a")
    except:
        print("Error with file handling")
    else:
        f.writelines(str(num) + " " + str(pr) + "\n")
        f.close()
def view():
    try:
        f = open("lotto_results.ext", "r")
    except:
        print("File not found")
    else:
        print(f.read())
        f.close()

def main():
    powerBallTicket = list()
    powerBallTicket = fill_ticket(powerBallTicket)
    print("The Power Ball Winning Numbers:")
    print("Play: ", powerBallTicket[:5], " Power Ball: ", powerBallTicket[-1])
    choice = input("Do you want to save this result?")
    choice.lower()
    if choice =="yes" or choice =="y":
        save(powerBallTicket[:5], powerBallTicket[-1])

    choice = input("Do you want to see previous results?")
    choice.lower()
    if choice == "yes" or choice == "y":
        view()

main()