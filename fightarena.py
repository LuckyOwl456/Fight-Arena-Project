
##What to work on next:
#Items, Abilities, (Abilities are finished for mage ONLY)
#More fights
#Armor
#Inventory
#Save system
#PvP

import random
import time

#Gamestates
chosenfight = 0
freetime = 0
doing = 0
shoptutorialstate = 1
enemycanmove = 1
#Rewards

fpgain = {"Goblin" : 1, "Dwarf" : 3}
fpcost = {"Fireball" : 1, "Shortsword" : 1, "Potion" : 1}

#Shop

shopprices = {"Potion" : 1, "Shortsword" : 1, "Fireball Tome" : 1}

#Passive Ability List

enemypassive = {"Rage" : 0, "Rock Solid" : 0}

#Player character

canusespec = 1
specials = {"Freeze" : 0, "Backstab" : 0, "Hack and Slash" : 0}
spellbookcontents = {"Spark" : 1}
spellbookdamage = {"Spark" : 2, "Fireball Tome" : 4}
inventory = {"Dagger" : 1}
weapon =  "Dagger"
stats = {"Health" : 1, "Strength" : 1, "Speed" : 1, "Defense" : 1, "Ranged" : 1, "Magic" : 1}
mweaponbns = {"Dagger" : 1, "Shortsword" : 3, "None" : 0}
rweaponbns = {"Shortbow" : 2, "Crossbow" : 3}
print("Character Creation")
playername = input("What is your name, adventurer?")
print("Alright", playername +", what class do you specialize in?")
playerclass = input("(Your choices are Knight, Magician or Bandit)")
if "andit" in playerclass:
    stats["Health"] = 15
    stats["Strength"] = 5
    stats["Ranged"] = 10
    stats["Speed"] = 10
    stats["Defense"] = 4
    stats["Magic"] = 2
    specials["Backstab"] = 1
    
if "night" in playerclass:
    stats["Health"] = 20
    stats["Strength"] = 10
    stats["Ranged"] = 3
    stats["Speed"] = 2
    stats["Defense"] = 9
    stats["Magic"] = 1
    specials["Hack and Slash"] = 1

if "agician" in playerclass:
    stats["Health"] = 10
    stats["Strength"] = 3
    stats["Ranged"] = 5
    stats["Speed"] = 3
    stats["Defense"] = 2
    stats["Magic"] = 15
    specials["Freeze"] = 1

hitpoints = stats["Health"]
fightpoints = 0
print("Perfect! As a", playerclass, "your stats will be:")
print(stats)

time.sleep(2)

print("Welcome to the text fight arena, where you will face off against dangerous enemies in search of fame and treasure!")
time.sleep(1)
print("Your first opponent will be a goblin!")

#Enemystats

opponentstat = {"Health" : 1, "Strength" : 1, "Speed" : 1, "Defense" : 1, "Ranged" : 1, "Magic" : 1}

#First fight
print("[Quick Tutorial]")
time.sleep(1)
print("On your turn, you will be asked to complete an action. You can use an item a special ability, a spell, or attack! After your turn, your opponent will be presented with the same opportunity. The goal is to lower your opponent's health points to 0 before they do the same to you. For your first fight, you'll only have a dagger if you are a Bandit or Knight, you can access your spellbook if you are a mage with 'Cast'")
opponentstat["Health"] = 10
opponentstat["Defense"] = 2
opponentstat["Strength"] = 3
opponentstat["Speed"] = 1
enemy = "Goblin"
enemyweapon = "None"

#Basic Fights (This may require a rewrite or modification for special fights)
enemyhitpoints = opponentstat["Health"]
def fight(fightpoints):
 canusespec = 1
 hitpoints = stats["Health"]
 enemyhitpoints = opponentstat["Health"]
 while (enemyhitpoints > 0) and (hitpoints > 0):
    enemycanmove = 1
    #Missing Calculation
    if (stats["Speed"] == opponentstat["Speed"]):
        missrate = random.randint(1, 10)
    if (stats["Speed"] < opponentstat["Speed"]):
        missrate = random.randint(1, (10 - (opponentstat["Speed"] - stats["Speed"])))
    if (stats["Speed"] > opponentstat["Speed"]):
        missrate = random.randint(1, (10 + (stats["Speed"] - opponentstat["Speed"])))
    #Dodging Calculation
    if (stats["Speed"] == opponentstat["Speed"]):
        hit = random.randint(0, 9)
    if (stats["Speed"] < opponentstat["Speed"]):
        hit = random.randint(0, (9 - (opponentstat["Speed"] - stats["Speed"])))
    if (stats["Speed"] > opponentstat["Speed"]):
        hit = random.randint(0, (9 + (stats["Speed"] - opponentstat["Speed"])))
    #Player Turn
    print("your turn")
    time.sleep(1)
    act = input("What would you like to do?")
    if "ttack" in act:
        time.sleep(0.5)
        print("You attack the", enemy +"!")
        #Damage Calc
        damage = round((stats["Strength"] / 2) + mweaponbns[weapon]) - round(opponentstat["Defense"] / 3)
        time.sleep(0.5)
        print("It deals", damage, "damage!")
        enemyhitpoints = enemyhitpoints - damage
    if "ast" in act:
        #Spell Selection
        for k in spellbookcontents.keys():
            print(k)
        #Damage calculation
        chosenspell = input("Which spell do you cast?")
        if chosenspell in spellbookdamage.keys() and chosenspell in spellbookcontents.keys():
         damage = round((spellbookdamage[chosenspell] + stats["Magic"] / 3) - ((opponentstat["Defense"] / 5) + (opponentstat["Magic"] / 4)))
         time.sleep(0.5)
         print("You cast", chosenspell, "on the", enemy + "!")
         time.sleep(0.5)
         print("It deals", damage, "damage!")
         enemyhitpoints = enemyhitpoints - damage
        #Special attacks
    if "pecial" in act:
        if canusespec == 0:
            print("your special has already been used")
        if canusespec == 1:
            
         for key, value in specials.items():
           if 1 == value:
            print(key)
            usedspec = input("Which special?")
            if usedspec in specials.keys():
            #Detect if player has the special
              if (specials[usedspec] == 1):
                #Backstab
                if "ackstab" in usedspec:
                    spechit = random.randint(1,4)
                    if (spechit < 4):
                        time.sleep(0.7)
                        print("You successfully backstab the", enemy)
                        damage = (stats["Strength"] + (mweaponbns[weapon]* 2))
                        enemyhitpoints = enemyhitpoints - damage
                        print("It deals", damage,"damage!")
                    else:
                        time.sleep(0.7)
                        print("The backstab was unsuccessful!")
                #Freeze
                if "reeze" in usedspec:
                    enemycanmove = 0
                    time.sleep(1)
                    print("The",enemy, "is frozen!")
                    time.sleep(1)
                    damage = (round(stats["Magic"] / 2))
                    enemyhitpoints = enemyhitpoints - damage
                    canusespec = 0
                    time.sleep(0.5)
                    print("The enemy takes", damage, "damage from your attack!")

                #Hack And Slash
                if "Hack" in usedspec:
                    time.sleep(1)
                    print("You hit the",enemy +"... Then hit it again!")
                    damage = round((stats["Strength"] / 2) + mweaponbns[weapon]) - round(opponentstat["Defense"] / 3)
                    print("The first strike deals", damage, "damage...")
                    enemyhitpoints = enemyhitpoints - damage
                    damage2 = round((stats["Strength"] / 3) + mweaponbns[weapon])
                    enemyhitpoints = enemyhitpoints - damage
                    time.sleep(0.5)
                    print("and the second deals", damage, "damage!")
        #Enemy Passive Abilities
    if (enemypassive["Rage"] == 1) and (enemyhitpoints < (opponentstat["Health"] / 2)):
        time.sleep(0.5)
        print("The",enemy, "is incredibly angry! It's strength increases drastically!")
        opponentstat["Strength"] = opponentstat["Strength"] + 5
        enemypassive["Rage"] = 0
    if (enemyhitpoints < 1):
        #Enemy Death and Rewards
        fightpoints = fightpoints + fpgain[enemy]
        print("The", enemy,"Has been slain!")
        time.sleep(1)
        hitpoints = stats["Health"]
        print("You have obtained", fpgain[enemy], "fightpoint(s) from slaying the", enemy)
    if (enemyhitpoints > 0) and (enemycanmove == 1):
     if (hit == 0):
        print("the enemy",enemy, "misses!")
     if (hit > 0):
         #Enemy Damage
        damage = round(opponentstat["Strength"] / 2 + mweaponbns[enemyweapon]) - round(stats["Defense"] / 3)
        if (damage < 1):
            damage = 1
        time.sleep(0.5)
        print("The enemy hits you for", damage, "damage!")
        hitpoints = hitpoints - damage
        time.sleep(0.5)
        print("You have", hitpoints, "hitpoints left!")
    if hitpoints < 1:
        print("You have died, and lost all your fight points, what a shame!")
        fightpoints = 0
 return fightpoints
fightpoints = fight(fightpoints)
#Post-Goblin Gameplay
time.sleep(1)
print("Congratulations! You have won your first fight! Once you win fights, you earn fight points, which can be redeemed for rewards at the fight shop, to access it, once you have free time, simply enter 'Shop' as your command.")
time.sleep(2)
print("In the shop, you can redeem items such as potions that provide stat buffs, powerfull new equipment, spells, and other goodies!")
time.sleep(1)
print("By killing the goblin, you've only obtained one fight point, but that is enough to get you a starter weapon. Why don't you take a look and see what all you can buy?")
time.sleep(1.5)
freetime  = 1
print("Now that you have slain your first enemy, you can access all available fights at any time, though some fights may be locked behind certain items or require completion of other fights to start. To open the menu of which fights are available, type 'Arena' during free time.")
time.sleep(2)


#Fight Data

opponentstat = {"Health" : 1, "Strength" : 1, "Speed" : 1, "Defense" : 1, "Ranged" : 1, "Magic" : 1}
enemies = {"Goblin" : 1,"Dwarf" : 2, "Bear" : 3}


#Free Time
while (freetime == 1):
    #Choosing
     doing = input("You have free time now, what would you like to do?")

     #Equipment

     if "Equip" in doing:
         
         chosenweap = input("What would you like to equip? (You may only equip melee weapons)")
         if chosenweap in inventory.keys():
             weapon = chosenweap
         time.sleep(1)
         print("successfully equipped",weapon)
     #Fights
     if "Arena" in doing:
        print("Which fight would you like to begin?")
        chosenfight = input("1-Goblin, 2-Dwarf, 3- Bear")
        #Goblin refight
        if "oblin" in chosenfight:
            enemy = "Goblin"
            opponentstat["Health"] = 10
            opponentstat["Strength"] = 3
            opponentstat["Defense"] = 2
            enemyweapon = "None"
            fightpoints = fight(fightpoints)

        if "Dwarf" in chosenfight:
            enemy = "Dwarf"
            
            opponentstat["Health"] = 20
            opponentstat["Strength"] = 8
            opponentstat["Defense"] = 6
            opponentstat["Magic"] = 7
            opponentstat["Speed"] = 5
            enemyweapon = "Shortsword"
            enemypassive["Rage"] = 1
            fightpoints = fight(fightpoints)
     #SHOP
     if "Shop" in doing:
         print("You have", fightpoints, "Fight Points.")
         time.sleep(1.4)
         print("What would you like?")
         print("1-Potion (1FP)")
         print("2-Shortsword (1FP)")
         purchase = input("3-Fireball Tome (1FP)")
         if purchase in shopprices.keys():
          if (shopprices[purchase] < (fightpoints + 1)):
            if ("Fireball" in purchase):
                spellbookcontents[purchase] = 1
            fightpoints = fightpoints - shopprices[purchase]
            if purchase in inventory.keys():
                inventory[purchase] = inventory[purchase] + 1
            else:
                inventory[purchase] = 1
            
            print("your inventory now contains",inventory)
            if shoptutorialstate == 1:
                print("You can equip purchased melee weapons with the 'Equip' command, try it out!")
                shoptutorialstate = 2
                
