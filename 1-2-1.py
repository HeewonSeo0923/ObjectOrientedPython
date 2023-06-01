import random
def roll() :
    faces = []
    faces.append(random.randrange(1, 7))
    faces.append(random.randrange(1, 7))
    return faces

def win_lose(faces):
    sum = 0
    for face in faces:
        sum += face
        print(face, end=' ')

    if sum >= 7 :
        print("==> Player Win !")
    else :
        print("==> Player Lose !")

if __name__ == "__main__":
    faces = roll()
    win_lose(faces)