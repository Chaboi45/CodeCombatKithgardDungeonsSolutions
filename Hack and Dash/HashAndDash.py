# You can write code before a loop.
hero.moveRight()
# Break open the "Chest" before using the loop to escape the maze!
hero.moveUp()
hero.attack("Chest")
hero.moveDown()

# Return back back into the main hallway.

while True:
    # Move 3 times.
    hero.moveRight(3)
    # Move 3 times more.
    hero.moveDown(3)
    
    
    
