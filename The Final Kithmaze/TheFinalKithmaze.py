# Use a while-true loop to both move and attack.

while True:
    hero.moveRight()
    hero.moveUp()
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    hero.moveRight()
    hero.moveDown(2)
    hero.moveUp()
    
    pass
