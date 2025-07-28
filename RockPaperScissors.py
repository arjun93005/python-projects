import random

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None 
class RockPaperScissors:

    @staticmethod
    def play():
        user = input("enter a choice between rock, paper and scissors \
                    \nr : rock\
                    \np : paper\
                    \ns : scissors\nEnter your choice: ")
        user = user.lower()
        computer = random.choice(['r', 'p', 's'])
        """
        circular linked list
        r -> p -> s -> r

        the next one is greater that the previous one
        """
        print("Computer chose:", computer)

        rock = Node('r')
        paper = Node('p')
        rock.next = paper
        scissors = Node('s')
        paper.next = scissors 
        scissors.next = rock
  
        abbreviations = {'r': rock, 'p': paper, 's': scissors}

        temp1 = abbreviations[computer]
        temp2 = abbreviations[user]

        if user == computer:
            print("It's a tie!")
        elif (temp1.next == temp2):
            print("You win!")
        else:
            print("You lose!")


if __name__ == "__main__":
    RockPaperScissors.play()



