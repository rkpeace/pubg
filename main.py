import os, time, random
from replit import db

#NORMAL STUFF
lvl = 1
exp = 0
gold = 200
maxHealth = 100
expNeeded = 100
CurrentPlace = "void"
maxPotions = 30000000000
Potions = 300
PotionsPower = 40
PotionsPriceam = 1500
PotionsPricepo = 1400
maxPotionsAmount = 70000000
maxPotionsPower = 100

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m" 
RESET = "\033[0;0m"
YELLOW = "\033[1;33m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
#NORMAL STUFF

#ARMORY 
def Armory():
    global CurrentPlace
    global gold
    global Current_Armor
    global leatherArmorOwn
    global ironArmorOwn
    global goldenArmorOwn
    global DiamondArmorOwn
    global NetheriteArmorOwn
    global EmeraldArmorOwn
    CurrentPlace = "Armory"
    os.system("clear")
    Info()
    if leatherArmorOwn == True:
        print("1. Equip Leather Armor")
    elif leatherArmor['price'] > gold:
        print(RED + "1. Buy Leather Armor (" + str(leatherArmor['price']) +
              " gold)" + RESET)
    elif leatherArmor['price'] <= gold:
        print(GREEN + "1. Buy Leather Armor (" + str(leatherArmor['price']) +
              " gold)" + RESET)
    if ironArmorOwn == True:
        print("2. Equip Iron Armor")
    elif ironArmor['price'] > gold:
        print(RED + "2. Buy Iron Armor (" + str(ironArmor['price']) +
              " gold)" + RESET)
    elif ironArmor['price'] <= gold:
        print(GREEN + "2. Buy Iron Armor (" + str(ironArmor['price']) +
              " gold)" + RESET)
    if goldenArmorOwn == True:
        print("3. Equip Golden Armor")
    elif goldenArmor['price'] > gold:
        print(RED + "3. Buy Golden Armor (" + str(goldenArmor['price']) +
              " gold)" + RESET)
    elif goldenArmor['price'] <= gold:
        print(GREEN + "3. Buy Golden Armor (" + str(goldenArmor['price']) +
              " gold)" + RESET)
    if DiamondArmorOwn == True:
        print("4. Equip Diamond Armor")
    elif DiamondArmor['price'] > gold:
        print(RED + "4. Buy Diamond Armor (" + str(leatherArmor['price']) +
              " gold)" + RESET)
    elif DiamondArmor['price'] <= gold:
        print(GREEN + "4. Buy Diamond Armor (" + str(leatherArmor['price']) +
              " gold)" + RESET)
    if NetheriteArmorOwn == True:
        print("5. Equip Netherite Armor")
    elif NetheriteArmor['price'] > gold:
        print(RED + "5. Buy Netherite Armor (" + str(leatherArmor['price']) +
              " gold)" + RESET)
    elif NetheriteArmor['price'] <= gold:
        print(GREEN + "5. Buy Netherite Armor (" + str(NetheriteArmor['price']) +
              " gold)" + RESET)
    if EmeraldArmorOwn == True:
        print("6. Equip Emerald Armor")
    elif EmeraldArmor['price'] > gold:
        print(RED + "6. Buy Emerald Armor (" + str(EmeraldArmor['price']) +
              " gold)" + RESET)
    elif leatherArmor['price'] <= gold:
        print(GREEN + "6. Buy Emerald Armor (" + str(EmeraldArmor['price']) +
              " gold)" + RESET)
    print("7. Unequip Armor")
    print("0. back")
    haha = str(input(">"))
    if haha == "1":
        if leatherArmorOwn == True:
            print("You equipied leather Armor!")
            Current_Armor = leatherArmor
            time.sleep(1)
            Armory()
        elif leatherArmor['price'] > gold:
            print("you dont have enough money to buy that!")
            time.sleep(1)
            leatherArmorOwn == True
            Armory()
        elif leatherArmor['price'] <= gold:
            print("You bought Leather Armor!")
            gold -= leatherArmor['price']
            Current_Armor = leatherArmor
            leatherArmorOwn = True
            time.sleep(1)
            Armory()
    elif haha == "2":
        if ironArmorOwn == True:
            print("You equipied iron Armor")
            Current_Armor = ironArmor
            time.sleep(1)
            Armory()
        elif ironArmor['price'] > gold:
            print("you dont have enough gold to buy that!")
            time.sleep(1)
            Armory()
        elif ironArmor['price'] <= gold:
            print("You bought iron Armor!")
            Current_Armor = ironArmor
            ironArmorOwn = True
            gold -= ironArmor['price']
            time.sleep(1)
            Armory()
    elif haha == "3":
        if goldenArmorOwn == True:
            print("you equpied Golden Armor!")
            Current_Armor = goldenArmor
            time.sleep(1)
            Armory()
        elif goldenArmor['price'] > gold:
            print("you dont have enough money to buy that!")
            time.sleep(1)
            Armory()
        elif goldenArmor['price'] <= gold:
            print("You bought Golden Armor!")
            Current_Armor = goldenArmor
            goldenArmorOwn = True
            gold -= goldenArmor['price']
            time.sleep(1)
            Armory()
    if haha == "4":
        if DiamondArmorOwn == True:
            print("You equipied Diamond Armor!")
            Current_Armor = DiamondArmor
            time.sleep(1)
            Armory()
        elif DiamondArmor['price'] > gold:
            print("you dont have enough money to buy that!")
            time.sleep(1)
            Armory()
        elif DiamondArmor['price'] <= gold:
            print("You bought Diamond Armor!")
            gold -= DiamondArmor['price']
            Current_Armor = DiamondArmor
            DiamondArmorOwn = True
            time.sleep(1)
            Armory()
    if haha == "5":
        if NetheriteArmorOwn == True:
            print("You equipied Netherite Armor!")
            Current_Armor = NetheriteArmor
            time.sleep(1)
            Armory()
        elif NetheriteArmor['price'] > gold:
            print("you dont have enough money to buy that!")
            time.sleep(1)
            Armory()
        elif NetheriteArmor['price'] <= gold:
            print("You bought Netherite Armor!")
            gold -= NetheriteArmor['price']
            Current_Armor = NetheriteArmor
            NetheriteArmorOwn = True
            time.sleep(1)
            Armory()
    if haha == "6":
        if EmeraldArmorOwn == True:
            print("You equipied Emerald Armor!")
            Current_Armor = EmeraldArmor
            time.sleep(1)
            Armory()
        elif EmeraldArmor['price'] > gold:
            print("you dont have enough money to buy that!")
            time.sleep(1)
            Armory()
        elif EmeraldArmor['price'] <= gold:
            print("You bought Emerald Armor!")
            gold -= EmeraldArmor['price']
            Current_Armor = EmeraldArmor
            EmeraldArmorOwn = True
            time.sleep(1)
            Armory()
    elif haha == "7":
        print("You unequiped Armor!")
        Current_Armor = noneArmor
        time.sleep(1)
        Armory()
    elif haha == "0":
        Home()
    else:
        print("you can only pick a number from the list!")
        time.sleep(1)
        Armory()

#SMALL GOBLIN
SmallGoblin = "Small Goblin"
SmallGoblin_attack = random.randint(3, 10)
SmallGoblin_Health = 40
#BIG GOBLIN
BigGoblin = "Big Goblin"
BigGoblin_attack = random.randint(5, 15)
BigGoblin_Health = 60
#Goblin Boss
GoblinBoss = "Big Goblin"
GoblinBoss_attack = random.randint(10, 20)
GoblinBoss_Health = 100
#FOREST MOBS
ForestMobs = [SmallGoblin, BigGoblin, GoblinBoss]

#MONSTER WORM
MonsterWorm = "Monster Worm"
MonsterWorm_attack = random.randint(15, 30)
MonsterWorm_Health = 120
#MONSTER SKELETON
MonsterSkeleton = "Monster Skeleton"
MonsterSkeleton_attack = random.randint(20, 30)
MonsterSkeleton_Health = 110
#Monster Spider
MonsterSpider = "Monster Spider"
MonsterSpider_attack = random.randint(25, 30)
MonsterSpider_Health = 130
#UNDERGROUND MOBS
Umobs = [MonsterWorm, MonsterSkeleton, MonsterSpider]

#MONSTER TURTLE
MonsterTurtle = "Monster Turtle"
MonsterTurtle_attack = random.randint(15, 30)
MonsterTurtle_Health = 300
#MonsterPiranha
MonsterPiranha = "Monster Piranha"
MonsterPiranha_attack = random.randint(30, 50)
MonsterPiranha_Health = 75
#MonsterCroc
MonsterCroc = "Monster Croc"
MonsterCroc_attack = random.randint(25, 40)
MonsterCroc_Health = 175
Uwater = [MonsterTurtle, MonsterPiranha, MonsterCroc]

#DUNGEONS
Forest = "Forest"
Underground = "UnderGround"
Underwater = "UnderWater"

#DUNGEON
def Dungeon():
    global exp
    global CurrentPlace
    CurrentPlace = "Dungeoun"
    os.system("clear")
    Info()
    print(GREEN + "1. Forest" + RESET)
    if lvl >= 5:
        print(GREEN + "2. Underground" + RESET)
    else:
        print(RED + "2. Underground (+5 lvl)" + RESET)
    if lvl >= 10:
        print(GREEN + "3. UnderWater" + RESET)
    else:
        print(RED + "2. UnderWater (+10 lvl)" + RESET)
    print("0. back")
    move = str(input(">"))
    if move == "1":
        CurrentPlace = Forest
        Fight()
    elif move == "2":
        if lvl < 5:
            print("Your level is too low!")
            time.sleep(1)
            os.system("clear")
            Dungeon()
        else:
            CurrentPlace = Underground
            Fight()
    elif move == "3":
        if lvl < 10:
            print("Your level is too low!")
            time.sleep(1)
            os.system("clear")
            Dungeon()
        else:
            CurrentPlace = Underwater
            Fight()
    elif move == "0":
        Home()
    else:
        print("you can pick a number from the list!")
        time.sleep(1)
        Dungeon()

def Fight():
    #getting ready to fight system (some borning stuff)
    global Enermy
    global Enermy_attack
    global Enermy_Health
    global Current_Sword_sharp
    global maxHealth
    global Health
    global Potions

    #REFRESHING STUFF
    Health = maxHealth
    Health += Current_Armor['Health']
    Potions = maxPotions

    if CurrentPlace == Forest:
        Enermy = random.choice(ForestMobs)
        if Enermy == BigGoblin:
            Enermy_Health = BigGoblin_Health
            Enermy_attack = BigGoblin_attack
        elif Enermy == SmallGoblin:
            Enermy_Health = SmallGoblin_Health
            Enermy_attack = SmallGoblin_attack
        elif Enermy == GoblinBoss:
            Enermy_Health = GoblinBoss_Health
            Enermy_attack = GoblinBoss_attack
    elif CurrentPlace == Underground:
        Enermy = random.choice(Umobs)
        if Enermy == MonsterSkeleton:
            Enermy_Health = MonsterSkeleton_Health
            Enermy_attack = MonsterSkeleton_attack
        elif Enermy == MonsterWorm:
            Enermy_attack = MonsterWorm_attack
            Enermy_Health = MonsterWorm_Health
        elif Enermy == MonsterSpider:
            Enermy_attack = MonsterSpider_attack
            Enermy_Health = MonsterSpider_Health
    if CurrentPlace == Underwater:
        Enermy = random.choice(Uwater)
        if Enermy == MonsterTurtle:
            Enermy_Health = MonsterTurtle_Health
            Enermy_attack = MonsterTurtle_attack
        elif Enermy == MonsterPiranha:
            Enermy_Health = MonsterPiranha_Health
            Enermy_attack = MonsterPiranha_attack
        elif Enermy == MonsterCroc:
            Enermy_Health = MonsterCroc_Health
            Enermy_attack = MonsterCroc_attack
    if Current_Sword == Wooden_Sword:
        Current_Sword_sharp = Wooden_Sword_sharp
    if Current_Sword == Stone_Sword:
        Current_Sword_sharp = Wooden_Sword_sharp
    if Current_Sword == Golden_Sword:
        Current_Sword_sharp = Golden_Sword_sharp
    if Current_Sword == Iron_Sword:
        Current_Sword_sharp = Iron_Sword_sharp
    if Current_Sword == Diamond_Sword:
        Current_Sword_sharp = Diamond_Sword_sharp
    if Current_Sword == Netherite_Sword:
        Current_Sword_sharp = Netherite_Sword_sharp
    if Current_Sword == Emerald_Sword:
        Current_Sword_sharp = Emerald_Sword_sharp
    os.system("clear")
    FInfo()
    Fsys()


def IsDead():
    if Enermy_Health <= 0 and Health <= 0:
        ForestDraw()
    if Enermy_Health <= 0:
        ForestWin()
    if Health <= 0:
        ForestLose()


def ForestLose():
    global gold
    global exp
    gold += random.randint(10, 30)
    exp += random.randint(10, 60)
    print("you noob lose")
    input("yes >")
    Home()


def ForestWin():
    global gold
    global exp
    global emermy
    print("You won!")
    if Enermy == SmallGoblin:
        expReceived = random.randint(250, 500)
        goldreceived = random.randint(100, 250)
    elif Enermy == BigGoblin:
        expReceived = random.randint(350, 600)
        goldreceived = random.randint(250, 400)
    elif Enermy == GoblinBoss:
        expReceived = random.randint(450, 700)
        goldreceived = random.randint(400, 550)
    elif Enermy == MonsterSkeleton:
        expReceived = random.randint(550, 800)
        goldreceived = random.randint(550, 700)
    elif Enermy == MonsterWorm:
        expReceived = random.randint(650, 900)
        goldreceived = random.randint(700, 850)
    elif Enermy == MonsterSpider:
        expReceived = random.randint(750, 1000)
        goldreceived = random.randint(850, 1000)
    elif Enermy == MonsterTurtle:
        expReceived = random.randint(850, 1100)
        goldreceived = random.randint(1000, 1150)
    elif Enermy == MonsterPiranha:
        expReceived = random.randint(1100, 1250)
        goldreceived = random.randint(1150, 1300)
    elif Enermy == MonsterCroc:
        expReceived = random.randint(1250, 1400)
        goldreceived = random.randint(1300, 1450)
    exp += expReceived
    gold += goldreceived
    print("You received " + str(goldreceived) + " gold and " +
          str(expReceived) + " exp !")
    input("Click Enter To Continue >")
    Home()


def ForestDraw():
    global gold
    print("HOW DID YOU DRAW THIS LOOOL")
    print("FOR THIS YOU RECIVE INFINITE GOLD")
    gold += 100000000000
    input("Click Enter To Continue >")
    Home()


#FIGHT SYSTEM
def Fsys():
    global Enermy_Health
    global Wooden_Sword_sharp
    global Stone_Sword_sharp
    global Golden_Sword_sharp
    global Iron_Sword_sharp
    global Diamond_Sword_sharp
    global Netherite_Sword_sharp
    global Emerald_Sword_sharp
    global Current_Sword_sharp
    global Potions
    global Health
    global Current_Armor


    print("1. Attack")
    print("2. Use Potion")
    print("3. Wait")
    print("4. Give Up")
    de = str(input(">"))
    if de == "1":
        #SWORD SHARP REFRESHING
        Wooden_Sword_sharp = random.randint(5, 11)
        Stone_Sword_sharp = random.randint(10, 16)
        Golden_Sword_sharp = random.randint(15, 21)
        Iron_Sword_sharp = random.randint(20, 26)
        Diamond_Sword_sharp = random.randint(25, 31)
        Netherite_Sword_sharp = random.randint(30, 36)
        Emerald_Sword_sharp = random.randint(40, 46)
        if Current_Sword == Wooden_Sword:
            Current_Sword_sharp = Wooden_Sword_sharp
        if Current_Sword == Stone_Sword:
            Current_Sword_sharp = Stone_Sword_sharp
        if Current_Sword == Golden_Sword:
            Current_Sword_sharp = Golden_Sword_sharp
        if Current_Sword == Iron_Sword:
            Current_Sword_sharp = Iron_Sword_sharp
        if Current_Sword == Diamond_Sword:
            Current_Sword_sharp = Diamond_Sword_sharp
        if Current_Sword == Netherite_Sword:
            Current_Sword_sharp = Netherite_Sword_sharp
        if Current_Sword == Emerald_Sword:
            Current_Sword_sharp = Emerald_Sword_sharp

        Enermy_Health -= Current_Sword_sharp
        os.system("clear")
        FInfo()
        print("You attacked Enermy with " + str(Current_Sword_sharp) +
              " damage!")
        time.sleep(2)
        os.system("clear")
        FInfo()
        IsDead()
    elif de == "2":
        if Health == maxHealth:
            print("You cant Use Potion Now!")
            time.sleep(1)
            os.system("clear")
            FInfo()
            Fsys()
        elif Potions == 0:
            print("You dont have more potions!")
            time.sleep(1)
            os.system("clear")
            FInfo()
            Fsys()
        else:
            Potions -= 1
            if Health >= maxHealth - PotionsPower:
                Health = maxHealth
            else:
                Health += PotionsPower
            os.system("clear")
            FInfo()
            print("You used Health Potion!")
            time.sleep(1.5)
    elif de == "3":
        os.system("clear")
        FInfo()
        print("You are waiting for Enermy's move!")
        time.sleep(2)
        os.system("clear")
        FInfo()
    elif de == "4":
        print("You gived up!")
        ForestLose()
    else:
        print("You can only pick a number from the list!")
        time.sleep(1)
        os.system("clear")
        FInfo()
        Fsys()
    print("Wait for Enermy move..")
    time.sleep(1)
    os.system("clear")
    FInfo()
    Enermyturn()
    Fsys()


def Enermyturn():
    global Health
    global Enermy_attack
    #changing enemys attack dmg lol
    if Enermy == SmallGoblin:
        Enermy_attack = random.randint(3, 10)
    if Enermy == BigGoblin:
        Enermy_attack = random.randint(5, 15)
    if Enermy == GoblinBoss:
        Enermy_attack = random.randint(10, 20)
    if Enermy == MonsterSkeleton:
        Enermy_attack = random.randint(15, 25)
    if Enermy == MonsterWorm:
        Enermy_attack = random.randint(20, 30)
    if Enermy == MonsterSpider:
        Enermy_attack = random.randint(25, 35)
    if Enermy == MonsterTurtle:
        Enermy_attack = random.randint(15, 30)
    if Enermy == MonsterPiranha:
        Enermy_attack = random.randint(30, 50)
    if Enermy == MonsterCroc:
        Enermy_attack = random.randint(25, 40)

    Health -= Enermy_attack
    os.system("clear")
    FInfo()
    print("Enermy attacked You with " + str(Enermy_attack) + " damage!")
    time.sleep(1)
    IsDead()


def Home():
    #TODO:
    # Load And Save functions the game in replit DataBase
    global CurrentPlace
    CurrentPlace = "Home"
    os.system("clear")
    Info()
    print("1. Enter the Dungeon")
    print("2. Go to Shop")
    print("3. Go to Armory")
    print("4. Load Game")
    print("5. Save Game")
    Move = str(input(">"))
    if Move == "1":
        Dungeon()
    elif Move == "2":
        Shop()
    elif Move == "3":
        Armory()
    elif Move == "4":
        Load()
    elif Move == "5":
        Save()
    else:
        print("You can pick a number from the list!")
        time.sleep(1)
        Home()


def Uptade():
    global lvl
    global exp
    global expNeeded
    while exp > expNeeded:
        exp = exp - expNeeded
        expNeeded = int(expNeeded * 1.5)
        lvl += 1


#NORMAL INFO
def Info():
    Uptade()
    print(BLUE + CurrentPlace + RESET)
    print("-----------------")
    print(CYAN + "exp: " + str(exp) + "/" + str(expNeeded) + RESET)
    print(BLUE + "lvl: " + str(lvl) + RESET)
    print(YELLOW + "gold: " + str(gold) + RESET)
    print("Weapon: " + Current_Sword)
    print("Armor: " + Current_Armor['name'])
    print("Potions: " + str(maxPotions))
    print("Potions Power: " + str(PotionsPower))
    print("-----------------\n\n")


#INFO IN FIGHT
def FInfo():
    Uptade()
    print("-----------------")
    print(BLUE + Enermy + RESET)
    print(RED + str(Enermy_Health) + " HP" + RESET)
    print("-----------------")
    print(BLUE + "YOU" + RESET)
    print(RED + str(Health) + " HP" + RESET)
    print("Weapon: " + Current_Sword)
    print("Armor: " + Current_Armor['name'])
    print("Potions: " + str(Potions))
    print("Potions Power: " + str(PotionsPower))
    print("-----------------\n\n")

#ITEMS
Wooden_Sword = "Wooden sword"
Wooden_Sword_sharp = 5
Stone_Sword = BOLD + "Stone sword" + RESET
Stone_Sword_sharp = 10
StoneSwordOwn = False
Golden_Sword = YELLOW + "Golden Sword" + RESET
Golden_Sword_sharp = 15
GoldenSwordOwn = False
Iron_Sword = BOLD + "Iron Sword" + RESET
Iron_Sword_sharp = 20
IronSwordOwn = False
Diamond_Sword = BLUE + "Diamond Sword" + RESET
Diamond_Sword_sharp = 25
DiamondSwordOwn = False
Netherite_Sword = RED+"Netherite Sword"+RESET
Netherite_Sword_sharp = 30
NetheriteSwordOwn = False
Emerald_Sword = GREEN+"Emerald Sword"+RESET
Emerald_Sword_sharp = 40
EmeraldSwordOwn = False
Current_Sword = Wooden_Sword

noneArmor = {'Health': 0, 'name': 'none'}
leatherArmor = {'Health': 20, 'name': 'Leather Armor', 'price': 1300}
leatherArmorOwn = False
ironArmor = {'Health': 50, 'name': BOLD + 'Iron Armor' + RESET, 'price': 2300}
ironArmorOwn = False
goldenArmor = {
    'Health': 100,
    'name': YELLOW + 'Golden Armor' + RESET,
    'price': 5500
}
goldenArmorOwn = False
DiamondArmor = {
    'Health': 200,
    'name': BLUE + 'Diamond Armor' + RESET,
    'price': 15000
}
DiamondArmorOwn = False
NetheriteArmor = {
    'Health': 350,
    'name': RED+"Netherite Armor"+RESET,
    'price': 30000
}
NetheriteArmorOwn = False
EmeraldArmor = {
  'Health': 500,
  'name': GREEN+"Emerald Armor"+RESET,
  'price': 50000
}
EmeraldArmorOwn = False
Current_Armor = noneArmor

#ITEMS
def Load():
    global gold
    global lvl
    global exp
    global expNeeded
    global maxPotions
    global PotionsPower
    global PotionsPriceam
    global PotionsPricepo
    global Current_Sword
    global Current_Armor
    global StoneSwordOwn
    global GoldenSwordOwn
    global leatherArmorOwn
    global ironArmorOwn
    global goldenArmorOwn
    global IronSwordOwn
    global DiamondSwordOwn
    global DiamondArmorOwn
    global NetheriteArmorOwn
    global EmeraldArmorOwn
    global NetheriteSwordOwn
    global EmeraldSwordOwn
    gold = db["gold"]
    lvl = db["lvl"]
    exp = db["exp"]
    expNeeded = db["expNeeded"]
    maxPotions = db["maxPotions"]
    PotionsPower = db["PotionsPower"]
    PotionsPriceam = db["PotionsPriceam"]
    PotionsPricepo = db["PotionsPricepo"]
    Current_Sword = db["Current_Sword"]
    Current_Armor = db["Current_Armor"]
    StoneSwordOwn = db["StoneSwordOwn"]
    GoldenSwordOwn = db["GoldenSwordOwn"]
    leatherArmorOwn = db["leatherArmorOwn"]
    ironArmorOwn = db["ironArmorOwn"]
    goldenArmorOwn = db["goldenArmorOwn"]
    IronSwordOwn = db["IronSwordOwn"]
    DiamondSwordOwn = db["DiamondSwordOwn"]
    DiamondArmorOwn = db["DiamondArmorOwn"]
    NetheriteSwordOwn = db["NetheriteSwordOwn"]
    EmeraldSwordOwn = db["EmeraldSwordOwn"]
    NetheriteArmorOwn = db["NetheriteArmorOwn"]
    EmeraldArmorOwn = db["EmeraldArmorOwn"]
    print(GREEN + "Game has been loaded!" + RESET)
    time.sleep(1)
    Home()


def Save():
    global gold
    global lvl
    global exp
    global expNeeded
    global maxPotions
    global PotionsPower
    global PotionsPriceam
    global PotionsPricepo
    global Current_Sword
    global Current_Armor
    global StoneSwordOwn
    global GoldenSwordOwn
    global leatherArmorOwn
    global ironArmorOwn
    global goldenArmorOwn

    db["gold"] = gold
    db["lvl"] = lvl
    db["exp"] = exp
    db["expNeeded"] = expNeeded
    db["maxPotions"] = maxPotions
    db["PotionsPower"] = PotionsPower
    db["PotionsPriceam"] = PotionsPriceam
    db["PotionsPricepo"] = PotionsPricepo
    db["Current_Sword"] = Current_Sword
    db["Current_Armor"] = Current_Armor
    db["StoneSwordOwn"] = StoneSwordOwn
    db["GoldenSwordOwn"] = GoldenSwordOwn
    db["leatherArmorOwn"] = leatherArmorOwn
    db["ironArmorOwn"] = ironArmorOwn
    db["goldenArmorOwn"] = goldenArmorOwn
    db["IronSwordOwn"] = IronSwordOwn
    db["DiamondSwordOwn"] = DiamondSwordOwn
    db["DiamondArmorOwn"] = DiamondArmorOwn
    db["NetheriteArmorOwn"] = NetheriteArmorOwn
    db["EmeraldArmorOwn"] = EmeraldArmorOwn
    db["NetheriteSwordOwn"] = NetheriteSwordOwn
    db["EmeraldSwordOwn"] = EmeraldSwordOwn
    print(GREEN + "Game has been saved!" + RESET)
    time.sleep(1)
    Home()

#SHOP
def Shop():
    global CurrentPlace
    CurrentPlace = "Shop"
    os.system("clear")
    Info()
    print("1. Swords")
    print("2. Potions")
    print("0 to back")
    hm = str(input(">"))
    if hm == "1":
        os.system("clear")
        Info()
        ShopSwords()
    elif hm == "2":
        os.system("clear")
        Info()
        ShopPotions()
    elif hm == "0":
        Home()
    else:
        print("You can only pick a number from the list!")
        time.sleep(1)
        Shop()


def ShopSwords():
    global gold
    global Current_Sword
    global GoldenSwordOwn
    global StoneSwordOwn
    global IronSwordOwn
    global DiamondSwordOwn
    global NetheriteSwordOwn
    global EmeraldSwordOwn
    if StoneSwordOwn == True:
        print("1. Equip Stone Sword")
    elif gold >= 1500:
        print(GREEN + "1. Buy Stone Sword (1500 gold)" + RESET)
    elif gold < 1500:
        print(RED + "1. Buy Stone Sword (1500 gold)" + RESET)
    if GoldenSwordOwn == True:
        print("2. Equip Golden Sword")
    elif gold >= 5000:
        print(GREEN + "2. Buy Golden Sword (5000 gold)" + RESET)
    elif gold < 5000:
        print(RED + "2. Buy Golden Sword (5000 gold)" + RESET)
    if IronSwordOwn == True:
        print("3. Equip Iron Sword")
    elif gold >= 10000:
        print(GREEN + "3. Buy Iron Sword (10000 gold)" + RESET)
    elif gold < 10000:
        print(RED + "3. Buy Iron Sword (10000 gold)" + RESET)
    if DiamondSwordOwn == True:
        print("4. Equip Diamond Sword")
    elif gold >= 10000:
        print(GREEN + "4. Buy Diamond Sword (20000 gold)" + RESET)
    elif gold < 10000:
        print(RED + "4. Buy Diamond Sword (20000 gold)" + RESET)
    if NetheriteSwordOwn == True:
        print("5. Equip Netherite Sword")
    elif gold >= 40000:
        print(GREEN + "5. Buy Netherite Sword (40000 gold)" + RESET)
    elif gold < 40000:
        print(RED + "5. Buy Netherite Sword (40000 gold)" + RESET)
    if EmeraldSwordOwn == True:
        print("6. Equip Emerald Sword")
    elif gold >= 60000:
        print(GREEN + "6. Buy Emerald Sword (60000 gold)" + RESET)
    elif gold < 60000:
        print(RED + "6. Buy Emerald Sword (60000 gold)" + RESET)
    print("7. Equip Wooden Sword")
    print("0. back")
    a = str(input(">"))
    if a == "1":
        if StoneSwordOwn == True:
            print("You equipied Stone Sword!")
            Current_Sword = Stone_Sword
            time.sleep(1)
            os.system("clear")
            Info()
            ShopSwords()
        else:
            if gold >= 1500:
                print("You bought Stone Sword! for 1500 gold")
                gold -= 1500
                Current_Sword = Stone_Sword
                StoneSwordOwn = True
                time.sleep(1)
                os.system("clear")
                Info()
                ShopSwords()
            else:
                print("You dont have enough money to buy that!")
                time.sleep(1)
                os.system("clear")
                Info()
                ShopSwords()
    elif a == "2":
        if GoldenSwordOwn == True:
            print("You equpied Golden Sword!")
            Current_Sword = Golden_Sword
            time.sleep(1)
            os.system("clear")
            Info()
            ShopSwords()
        else:
            if gold >= 5000:
                print("You bought Golden Sword for 5000 gold")
                gold -= 5000
                GoldenSwordOwn = True
                Current_Sword = Golden_Sword
                time.sleep(1)
                os.system("clear")
                Info()
                ShopSwords()
            elif gold < 5000:
                print("you dont have enought money to buy that!")
                os.system("clear")
                Info()
                ShopSwords()
    if a == "3":
        if IronSwordOwn == True:
            print("You equipied Iron Sword!")
            Current_Sword = Iron_Sword
            time.sleep(1)
            os.system("clear")
            Info()
            ShopSwords()
        else:
            if gold >= 10000:
                print("You bought Iron Sword! for 10000 gold")
                gold -= 10000
                Current_Sword = Iron_Sword
                IronSwordOwn = True
                time.sleep(1)
                os.system("clear")
                Info()
                ShopSwords()
            else:
                print("You dont have enough money to buy that!")
                time.sleep(1)
                os.system("clear")
                Info()
                ShopSwords()
    if a == "4":
        if DiamondSwordOwn == True:
            print("You equipied Diamond Sword!")
            Current_Sword = Diamond_Sword
            time.sleep(1)
            os.system("clear")
            Info()
            ShopSwords()
        else:
            if gold >= 20000:
                print("You bought Diamond Sword! for 20000 gold")
                gold -= 20000
                Current_Sword = Diamond_Sword
                DiamondSwordOwn = True
                time.sleep(1)
                os.system("clear")
                Info()
                ShopSwords()
            else:
                print("You dont have enough money to buy that!")
                time.sleep(1)
                os.system("clear")
                Info()
                ShopSwords()
    if a == "5":
        if NetheriteSwordOwn == True:
            print("You equipied Netherite Sword!")
            Current_Sword =  Netherite_Sword
            time.sleep(1)
            os.system("clear")
            Info()
            ShopSwords()
        else:
            if gold >= 40000:
                print("You bought Netherite Sword! for 40000 gold")
                gold -= 40000
                Current_Sword = Netherite_Sword
                NetheriteSwordOwn = True
                time.sleep(1)
                os.system("clear")
                Info()
                ShopSwords()
            else:
                print("You dont have enough money to buy that!")
                time.sleep(1)
                os.system("clear")
                Info()
                ShopSwords()
    if a == "6":
        if EmeraldSwordOwn == True:
            print("You equipied Emerald Sword!")
            Current_Sword = Emerald_Sword
            time.sleep(1)
            os.system("clear")
            Info()
            ShopSwords()
        else:
            if gold >= 60000:
                print("You bought Emerald Sword! for 60000 gold")
                gold -= 60000
                Current_Sword = Emerald_Sword
                EmeraldSwordOwn = True
                time.sleep(1)
                os.system("clear")
                Info()
                ShopSwords()
            else:
                print("You dont have enough money to buy that!")
                time.sleep(1)
                os.system("clear")
                Info()
                ShopSwords()
    elif a == "7":
        print("You equpied Wooden Sword!")
        Current_Sword = Wooden_Sword
        time.sleep(1)
        os.system("clear")
        Info()
        ShopSwords()
    elif a == "0":
        Shop()
    else:
        print("You can only pick a number from the list!")
        time.sleep(1)
        os.system("clear")
        Info()
        ShopSwords()


def ShopPotions():
    global maxPotions
    global PotionsPower
    global gold
    global PotionsPriceam
    global PotionsPricepo
    global maxPotionsAmount
    global maxPotionsPower
    if maxPotionsAmount == maxPotions:
        print("1. Buy more Potions (cant buy)")
    elif PotionsPriceam <= gold:
        print(GREEN + "1. Buy more Potions (" + str(PotionsPriceam) +
              " gold)" + RESET)
    else:
        print(RED + "1. Buy more Potions (" + str(PotionsPriceam) + " gold)" +
              RESET)
    if maxPotionsPower == PotionsPower:
        print("2. Buy +10 Health to Potions Power (cant buy)")
    elif PotionsPricepo <= gold:
        print(GREEN + "2. Buy +10 Health to Potions Power (" +
              str(PotionsPricepo) + " gold)" + RESET)
    elif PotionsPricepo > gold:
        print(RED + "2. Buy +10 Health to Potions Power (" +
              str(PotionsPricepo) + " gold)" + RESET)
    print("0. back")
    abc = str(input(">"))
    if abc == "1":
        if maxPotionsAmount == maxPotions:
            print("You have max amount (" + str(maxPotionsAmount) +
                  ") of Potions")
            time.sleep(1)
            os.system("clear")
            Info()
            ShopPotions()
        elif PotionsPriceam <= gold:
            gold -= PotionsPriceam
            PotionsPriceam *= 2
            maxPotions += 1
            print("You bought 1 potion!")
            time.sleep(1)
            os.system("clear")
            Info()
            ShopPotions()
        elif PotionsPriceam > gold:
            print("You dont have enough gold to buy that!")
            time.sleep(1)
            os.system("clear")
            Info()
            ShopPotions()
        else:
            os.system("clear")
            print("Game crashed bc of really wierd glitch lol")
            input("Close game >")
            exit(0)
    elif abc == "2":
        if maxPotionsPower == PotionsPower:
            print("You have max amount (" + str(maxPotionsPower) +
                  ") of Potions Power")
            time.sleep(1)
            os.system("clear")
            Info()
            ShopPotions()
        elif PotionsPricepo <= gold:
            gold -= PotionsPricepo
            PotionsPricepo *= 2
            PotionsPower += 10
            print("You Bought +10 Health to Potions Power!")
            time.sleep(1)
            os.system("clear")
            Info()
            ShopPotions()
        elif PotionsPricepo > gold:
            print("You dont have enough gold to buy that!")
            time.sleep(1)
            os.system("clear")
            ShopPotions()
    elif abc == "0":
        os.system("clear")
        Info()
        Shop()

def Start():
    input(
        "Welcome To freefight By Me rkpeace. Potions are bugged whereby if u drink it with more than 100hp it sets ur hp at 100 hps\n>"
    )
    Game()


#GAME LOOP
def Game():
    global GameLoop
    GameLoop = True
    os.system("clear")
    while GameLoop == True:
        Home()
        os.system("cls")
        print(RED + "The Game Crashed!" + RESET)
        print(BLUE + "Reason: " + RESET + "unfortunately left the game loop")
        input("Click Enter to Close the game >")
        GameLoop = False

Start()
