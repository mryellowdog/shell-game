string = "nothing"
character = "#"
w = 10
h = 10
x = 0
y = 0
global iterations
iterations = 0

global score
score = 0

global apple
apple = True

def generate_random_number(seed):
    """Generates a pseudorandom number from a seed."""
    #if seed is None:
        #seed = int(time.time())

    x = seed
    for _ in range(1000):
        x = (x * 1103515245 + 12345) % 2**31

    return x % 100

seedstart = 1
enemyseed = 43


def clear_shell():
    """Clears the shell."""

    print("\x1b[2J\x1b[H")
#desiredX = 5
#desiredY = 5
#for x in range(h):
def render(desiredX, desiredY):
    global iterations
    global apple
    global score
    clear_shell()
    
    string = "#"
    x = 0
    y = 0
    for i in range(h):
        appleX = round(generate_random_number(seedstart + iterations) * 0.1)     
        appleY = round(generate_random_number(seedstart * 500 + iterations) * 0.1)
        enemyX = round(generate_random_number(enemyseed + iterations) * 0.1)
        enemyY = round(generate_random_number(enemyseed * 500 + iterations) * 0.1)
        string = ""
        y += 1
        x = 0
        for ii in range(w):
            if appleX == desiredX and appleY == desiredY:
                iterations += 1
                appleX = round(generate_random_number(seedstart + iterations) * 0.1)
                appleY = round(generate_random_number(seedstart * 500 + iterations) * 0.1)
                score += 1
            if enemyX == desiredX and enemyY == desiredY:
                print("GAME OVER!")
                q = input()
                if q == "q":
                    quit()
                else:
                    quit()
            if x  == desiredX and y == desiredY:
                string = string + character
            else:
                string = string + " "
            if x == appleX and y == appleY:
                string = string + "o"
                apple = False
            if x == enemyX and y == enemyY:
                string = string + "%"
            x += 1
        print(string)
        #print(appleX)
        #print(appleY)
    print(score)
#print("X: " + str(x) + " Y: " + str(y))
mx = 5
my = 5

render(mx, my)

while True:
    key = input()
    if key == "w":
        my -= 1
        render(mx, my)
    if key == "s":
        my += 1
        render(mx, my)
    if key == "a":
        mx -= 1
        render(mx, my)
    if key == "d":
        mx += 1
        render(mx, my)

