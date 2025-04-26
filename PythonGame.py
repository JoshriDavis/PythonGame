###  Need to develop:
# All DB Heroes V
# All DB Vilans
# Option to miss the HIT
# Drops V
# Option to save the game
# option for choosing the hard Level V
# Option for a slow mod and fast mod WORKING ON IT
# From level X you became super
# Cheats
# fix the bug of wrong stats after starting again the game after losing V
###

# ### Monsters ###:
# Normal monster(N) = 8 points for each Level
# Half Boss monster (HB) = 10 points for each level
# Boss monster (B) = 12 points for each level
# Each monster get bonus EXP this way = total points *1+(monster level*0.05)

# ### Levels ###:
# * for each level, each skills will improved by 1.2-1.5
# for next level needs *1.35 exp
'''
1 - 0
2 - 6
3 - 7.2
4 - 8.64
5 - 10.36
6 - 12.44
and so
'''

import random
import time

# Object = the player
class Player(object):
 userLevel = 1
 enviromentLevel = 1
 userHP = 0
 userStr = 0
 userDef = 0
 userAtt = 0
 userEXP = 0

# Constractor for calculate the total power
 def TotalPower(self):
  userTotalPower = self.userHP+self.userStr+self.userDef+self.userAtt
  userTotalPower = float(round(userTotalPower,1))
  return userTotalPower

# Time create for each action
def TimeCreate(timer):
# DELETE IT!!!
   return 0
   if timer=="FineTraning":
     time.sleep(1)
   elif timer=="GoodTraning":
     time.sleep(1.5)
   elif timer=="AwsomeTraning":
     time.sleep(2)
   elif timer=="NormalAttack":
     time.sleep(1)
   elif timer=="StrongAttack":
     time.sleep(1.5)
   elif timer=="CriAttack":
     time.sleep(2)
   elif timer=="Rest":
     time.sleep(3)

# Creat Monster object
class Monster(object):
 MonName = "Monster"
 MonLevel = 1
 MonHP = 1
 MonAtk = 1
 MonDef = 1
 MonStr = 1

# Function that definding monster stats
def MonsterStats(MonObject, hp, atk, deff, strr):
 MonObject.MonHP = hp
 MonObject.MonAtk = atk
 MonObject.MonDef = deff
 MonObject.MonStr = strr

# Function that definding monster name and level
def MonsterStats2(MonObject, name, lvl):
 MonObject.MonName = name
 MonObject.MonLevel = lvl

BestLevel = 0
BestPower = 0
SuperHit = 0
SuperDef = 0

# ############# Main starts from here ############
NextLevel = 10 #Shows the next exp you need for the next level

print ("Hello there and welcome to the game!")
print()
print("Please choose the game level: (1 = Easy, 2 = Medium, 3 = Hard)")
GameLevel = input()
if GameLevel=="1":
 FirstBoost=2
elif GameLevel=="2":
 FirstBoost=1
elif GameLevel=="3":
 FirstBoost=0

print()
print("And do you prefer regular of fast mode? (1 = regular, 2 = fast)")
print()
SpeedMode = input()

print ("Your stats are:")

# This is the chance to get stronger monsters
MonsterBuilderLevel = 1
MonsterTempMonsterNum = 0

MaxBoost = 3+FirstBoost

# Creating the user and his first stats
player = Player()
player.userHP = random.randint(10, 20)
player.userStr = random.randint(1, MaxBoost)
player.userDef = random.randint(1, MaxBoost)
player.userAtt = random.randint(1, MaxBoost)
TempUserHP = player.userHP

print ("Level:", player.userLevel)
print ("EXP:", player.userEXP)
print ("HP:",TempUserHP,"/", player.userHP)
print ("Str:", player.userStr)
print ("Def:", player.userDef)
print ("Atk:", player.userAtt)
print ("Total Power:", player.TotalPower())
print ("Super Hits: ", SuperHit)
print ("Super Defs: ", SuperDef)

MonsterTempMonsterNumMIN = 1

while(1):
 while(1):
  print ("********************************************")
  print ("What do you want to do? (1. Find monster 2. Traning 3. Rest)")
  choise = input()
  # Find Monster+fight
  if choise=="1":
      # Choose the monster you will found
      MonsterTempMonsterNum = random.randint(MonsterTempMonsterNumMIN, MonsterBuilderLevel)
      MaxDrop = 1001-MonsterBuilderLevel
      DropChange = random.randint(1,MaxDrop)
      if MonsterTempMonsterNum>245 and MonsterTempMonsterNum<247:
          Rat = Monster()
          MonsterStats(Rat, 60000, 18000, 13500, 16500) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Gotenks SSJ3 ♛",9000)
      elif MonsterTempMonsterNum>244 and MonsterTempMonsterNum<246:
          Rat = Monster()
          MonsterStats(Rat, 38400, 12600, 12000, 12600) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Goku SSJ3 ♛",6300)
      elif MonsterTempMonsterNum>241 and MonsterTempMonsterNum<245:
          Rat = Monster()
          MonsterStats(Rat, 10000, 10000, 10000, 10000) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♦ God Super Titan ♦",4000)
      elif MonsterTempMonsterNum>240 and MonsterTempMonsterNum<242:
          Rat = Monster()
          MonsterStats(Rat, 33120, 9000, 9000, 9000) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Ultimate Gohan ♛",5010)
      elif MonsterTempMonsterNum>239 and MonsterTempMonsterNum<241:
          Rat = Monster()
          MonsterStats(Rat, 40000, 12000, 9000, 11000) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Gotenks SSJ2 ♛",6000)
      elif MonsterTempMonsterNum>234 and MonsterTempMonsterNum<240:
          Rat = Monster()
          MonsterStats(Rat, 2000, 11000, 1000, 11000) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♦ God Attaker Titan ♦",2500)
      elif MonsterTempMonsterNum>229 and MonsterTempMonsterNum<235:
          Rat = Monster()
          MonsterStats(Rat, 2000, 500, 20000, 500) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♦ God Defender Titan ♦",2300)
      elif MonsterTempMonsterNum>226 and MonsterTempMonsterNum<230:
          Rat = Monster()
          MonsterStats(Rat, 18000, 500, 1000, 500) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♦ God Lifer Titan ♦",2000)
      elif MonsterTempMonsterNum>225 and MonsterTempMonsterNum<227:
          Rat = Monster()
          MonsterStats(Rat, 25600, 8400, 8000, 8400) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Goku SSJ2 ♛",4200)
      elif MonsterTempMonsterNum>224 and MonsterTempMonsterNum<226:
          Rat = Monster()
          MonsterStats(Rat, 24000, 9000, 6000, 9000) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Vegeta SSJ2 ♛",4000)
      elif MonsterTempMonsterNum>223 and MonsterTempMonsterNum<225:
          Rat = Monster()
          MonsterStats(Rat, 22080, 6000, 6000, 6000) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Gohan SSJ2 ♛",3340)
      elif MonsterTempMonsterNum>222 and MonsterTempMonsterNum<224:
          Rat = Monster()
          MonsterStats(Rat, 19000, 5560, 4760, 5000) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Trunks SSJ2 ♛",2860)
      elif MonsterTempMonsterNum>221 and MonsterTempMonsterNum<223:
          Rat = Monster()
          MonsterStats(Rat, 20000, 6000, 4500, 5500) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Gotenks SSJ1 ♛",3000)
      elif MonsterTempMonsterNum>220 and MonsterTempMonsterNum<222:
          Rat = Monster()
          MonsterStats(Rat, 12800, 4200, 4000, 4200) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Goku SSJ1 ♛",2100)
      elif MonsterTempMonsterNum>219 and MonsterTempMonsterNum<221:
          Rat = Monster()
          MonsterStats(Rat, 12000, 4500, 3000, 4500) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Vegeta SSJ1 ♛",2000)
      elif MonsterTempMonsterNum>213 and MonsterTempMonsterNum<220:
          Rat = Monster()
          MonsterStats(Rat, 500, 3000, 500, 3000) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♦ Super Android Damager ♦",700)
      elif MonsterTempMonsterNum>212 and MonsterTempMonsterNum<214:
          Rat = Monster()
          MonsterStats(Rat, 10000, 2500, 3000, 2500) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Gohan SSJ1 ♛",1670)
      elif MonsterTempMonsterNum>211 and MonsterTempMonsterNum<213:
          Rat = Monster()
          MonsterStats(Rat, 9500, 2780, 2380, 2500) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Super Picolo ♛",1500)
      elif MonsterTempMonsterNum>210 and MonsterTempMonsterNum<212:
          Rat = Monster()
          MonsterStats(Rat, 8500, 2700, 2380, 2500) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Trunks SSJ1 ♛",1430)
      elif MonsterTempMonsterNum>209 and MonsterTempMonsterNum<211:
          Rat = Monster()
          MonsterStats(Rat, 8500, 2700, 2380, 2500) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Goten SSJ1 ♛",1340)
      elif MonsterTempMonsterNum>161 and MonsterTempMonsterNum<210:
          Rat = Monster()
          MonsterStats(Rat, 1080, 450, 100, 450) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"Kai Warrior",260)
      elif MonsterTempMonsterNum>160 and MonsterTempMonsterNum<162:
          Rat = Monster()
          MonsterStats(Rat, 2000, 600, 450, 550) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Gotenks ♛",300)
      elif MonsterTempMonsterNum>160 and MonsterTempMonsterNum<162:
          Rat = Monster()
          MonsterStats(Rat, 1280, 420, 400, 420) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Goku ♛",210)
      elif MonsterTempMonsterNum>159 and MonsterTempMonsterNum<161:
          Rat = Monster()
          MonsterStats(Rat, 1200, 450, 300, 450) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Vegeta ♛",200)
      elif MonsterTempMonsterNum>143 and MonsterTempMonsterNum<160:
          Rat = Monster()
          MonsterStats(Rat, 1100, 160, 180, 160) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"Ultimate Dragonsnake",200)
      elif MonsterTempMonsterNum>142 and MonsterTempMonsterNum<144:
          Rat = Monster()
          MonsterStats(Rat, 1104, 300, 300, 300) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Gohan ♛",167)
      elif MonsterTempMonsterNum>141 and MonsterTempMonsterNum<143:
          Rat = Monster()
          MonsterStats(Rat, 1000, 250, 300, 250) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Picolo ♛",150)
      elif MonsterTempMonsterNum>140 and MonsterTempMonsterNum<142:
          Rat = Monster()
          MonsterStats(Rat, 950, 278, 238, 250) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Trunks ♛",143)
      elif MonsterTempMonsterNum>139 and MonsterTempMonsterNum<141:
          Rat = Monster()
          MonsterStats(Rat, 850, 270, 238, 250) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Goten ♛",134)
      elif MonsterTempMonsterNum>131 and MonsterTempMonsterNum<140:
          Rat = Monster()
          MonsterStats(Rat, 1000, 140, 160, 140) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"Dragonsnake",180)
      elif MonsterTempMonsterNum>130 and MonsterTempMonsterNum<132:
          Rat = Monster()
          MonsterStats(Rat, 800, 305, 150, 305) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♣♣♣ Dragon King ♣♣♣",130)
      elif MonsterTempMonsterNum>129 and MonsterTempMonsterNum<131:
          Rat = Monster()
          MonsterStats(Rat, 800, 290, 140, 270) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Krilin ♛",125)
      elif MonsterTempMonsterNum>115 and MonsterTempMonsterNum<130:
          Rat = Monster()
          MonsterStats(Rat, 500, 200, 100, 200) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♦ Dragon Elite Warrior ♦",100)
      elif MonsterTempMonsterNum>102 and MonsterTempMonsterNum<116:
          Rat = Monster()
          MonsterStats(Rat, 300, 165, 50, 165) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"Dragon Warrior",85)
      elif MonsterTempMonsterNum>101 and MonsterTempMonsterNum<103:
          Rat = Monster()
          MonsterStats(Rat, 500, 135, 135, 130) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Tien Shinhan♛",75)
      elif MonsterTempMonsterNum>100 and MonsterTempMonsterNum<102:
          Rat = Monster()
          MonsterStats(Rat, 402, 146, 146, 146) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♣♣ Rune Titan ♣♣",70)
      elif MonsterTempMonsterNum>90 and MonsterTempMonsterNum<101:
          Rat = Monster()
          MonsterStats(Rat, 150, 110, 110, 110) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"Rune Warrior",60)
      elif MonsterTempMonsterNum>89 and MonsterTempMonsterNum<91:
          Rat = Monster()
          MonsterStats(Rat, 280, 200, 60, 60) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♣ Abyssal Titan ♣",52)
      elif MonsterTempMonsterNum>81 and MonsterTempMonsterNum<90:
          Rat = Monster()
          MonsterStats(Rat, 230, 150, 50, 50) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♦ Abyssal Greater Demon ♦",48)
      elif MonsterTempMonsterNum>80 and MonsterTempMonsterNum<82:
          Rat = Monster()
          MonsterStats(Rat, 250, 100, 86, 80) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Yamcha ♛",43)
      elif MonsterTempMonsterNum>75 and MonsterTempMonsterNum<81:
          Rat = Monster()
          MonsterStats(Rat, 160, 110, 30, 36) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"Abyssal Demon",42)
      elif MonsterTempMonsterNum>71 and MonsterTempMonsterNum<76:
          Rat = Monster()
          MonsterStats(Rat, 130, 90, 30, 30) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"Abyssal Imp",35)
      elif MonsterTempMonsterNum>70 and MonsterTempMonsterNum<72:
          Rat = Monster()
          MonsterStats(Rat, 260, 65, 90, 65) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♣ Zombie Master ♣",40)
      elif MonsterTempMonsterNum>60 and MonsterTempMonsterNum<71:
          Rat = Monster()
          MonsterStats(Rat, 120, 30, 60, 30) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"Zombie",30)
      elif MonsterTempMonsterNum>51 and MonsterTempMonsterNum<61:
          Rat = Monster()
          MonsterStats(Rat, 100, 25, 50, 25) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"Mummy",25)
      elif MonsterTempMonsterNum>50 and MonsterTempMonsterNum<52:
          Rat = Monster()
          MonsterStats(Rat, 120, 40, 30, 60) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♦ Adamant Giant ♦",25)
      elif MonsterTempMonsterNum>45 and MonsterTempMonsterNum<51:
          Rat = Monster()
          MonsterStats(Rat, 100, 20, 10, 30) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"Mithril Giant",20)
      elif MonsterTempMonsterNum>41 and MonsterTempMonsterNum<46:
          Rat = Monster()
          MonsterStats(Rat, 75, 15, 10, 20) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"Steel Giant",15)
      elif MonsterTempMonsterNum>40 and MonsterTempMonsterNum<42:
          Rat = Monster()
          MonsterStats(Rat, 79, 18, 18, 17) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♛ Master Roshi ♛",11)
      elif MonsterTempMonsterNum>32 and MonsterTempMonsterNum<41:
          Rat = Monster()
          MonsterStats(Rat, 64.4, 15, 9, 16) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"Giant",9)
      elif MonsterTempMonsterNum>30 and MonsterTempMonsterNum<33:
          Rat = Monster()
          MonsterStats(Rat, 101.4, 11, 11, 11) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♣ Goblin King ♣",8)
      elif MonsterTempMonsterNum>20 and MonsterTempMonsterNum<31:
          Rat = Monster()
          MonsterStats(Rat, 51.6, 8, 8, 8) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"Elite Goblin",7)
      elif MonsterTempMonsterNum>12 and MonsterTempMonsterNum<21:
          Rat = Monster()
          MonsterStats(Rat, 32, 6, 6, 6) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"Goblin",5)
      elif MonsterTempMonsterNum>11 and MonsterTempMonsterNum<13:
          Rat = Monster()
          MonsterStats(Rat, 50, 9, 6, 10) #MonObject, hp, atk, deff, strr
          MonsterStats2(Rat,"♣ Rat King ♣",5)
      elif MonsterTempMonsterNum>6 and MonsterTempMonsterNum<11:
          Rat = Monster()
          MonsterStats(Rat, 22, 2, 2, 1)
          MonsterStats2(Rat,"Fat Rat",3)
      elif MonsterTempMonsterNum>5 and MonsterTempMonsterNum<7:
          Rat = Monster()
          MonsterStats(Rat, 11, 3, 3, 2.6)
          MonsterStats2(Rat,"Big Rat",2)
      else:
          Rat = Monster()
          MonsterStats(Rat, 5, 1, 1, 1.4)
          MonsterStats2(Rat,"Rat",1)
      TempMonHP = Rat.MonHP
      print ()
      print ("A level",Rat.MonLevel," ",Rat.MonName," appears!")
      print ()
      TempPlayerMAXspeed = player.userLevel+1
      TempPlayerSpeed = random.randint(1, TempPlayerMAXspeed)
      TempMonsterMAXspeed = Rat.MonLevel+1
      TempMonserSpeed = random.randint(1, TempMonsterMAXspeed)
      # Fight The Monster
      while(TempUserHP>0 or Rat.MonHP>0):
          MonsterAtkPower = random.randint(1, 10)
          UserAtkPower = random.randint(1, 10)
          if TempPlayerSpeed>=TempMonserSpeed:
              if  TempPlayerSpeed==TempMonserSpeed:
                  TempMonserSpeed-=1
              TempMaxSpeed = TempPlayerSpeed
              TempPlayerSpeed = TempMonserSpeed
              TempMonserSpeed = TempMaxSpeed
              print()
              # PLAYER TURN
              print ("*** Player Turn ***")
              if SuperHit>0:
                  TimeCreate("CriAttack")
                  print ("! ! ! S U P E R    H I T ! ! !")
                  MonsterShield = Rat.MonDef- player.userAtt
                  if MonsterShield<0:
                      MonsterShield = 0
                  Damage = player.userStr*2 - MonsterShield
                  Damage = float(round(Damage,1))
                  if Damage<1:
                      Damage = 1
                  Rat.MonHP-=Damage
                  print ("You deal ",Damage," damage")
                  SuperHit-=1
              elif UserAtkPower>8:
                  TimeCreate("CriAttack")
                  print ("CRITICAL HIT!!!")
                  MonsterShield = Rat.MonDef- player.userAtt
                  if MonsterShield<0:
                      MonsterShield = 0
                  Damage = player.userStr*1.5 - MonsterShield
                  Damage = float(round(Damage,1))
                  if Damage<1:
                      Damage = 1
                  Rat.MonHP-=Damage
                  print ("You deal ",Damage," damage")
              elif UserAtkPower>6:
                  TimeCreate("StrongAttack")
                  print ("Strong hit!")
                  MonsterShield = Rat.MonDef- player.userAtt
                  if MonsterShield<0:
                      MonsterShield = 0
                  Damage = player.userStr*1.2 - MonsterShield
                  Damage = float(round(Damage,1))
                  if Damage<1:
                      Damage = 1
                  Rat.MonHP-=Damage
                  print ("You deal ",Damage," damage")
              else:
                  TimeCreate("NormalAttack")
                  print ("Regular hit.")
                  MonsterShield = Rat.MonDef- player.userAtt
                  if MonsterShield<0:
                      MonsterShield = 0
                  Damage = player.userStr - MonsterShield
                  Damage = float(round(Damage,1))
                  if Damage<1:
                      Damage = 1
                  Rat.MonHP-=Damage
                  print ("You deal ",Damage," damage")
             
              Rat.MonHP = float(round(Rat.MonHP,1))
              print("HP left to the Monster: ",Rat.MonHP)

              if Rat.MonHP<=0:
                  tempEXP = TempMonHP+Rat.MonAtk+Rat.MonStr+Rat.MonDef
                  tempEXP = float(round(tempEXP,1))
                  player.userEXP+=tempEXP
                  player.userEXP = float(round(player.userEXP,1))
                  print ()
                  print (Rat.MonName," Is Dead!")
                  print ()
                  print  ("You earned ",tempEXP," EXP!")
                  print ()
                  print ()
             
                  # DROPS!
                  if DropChange>0 and DropChange<50:
                    print ("You found an apple!")
                    print ("You ate the apple")
                    if TempUserHP<player.userHP:
                       TempUserHP = TempUserHP+player.userHP*0.05
                       TempUserHP = float(round(TempUserHP,1))
                       print ("5% of your HP has restored!")
                       print ()
                       if TempUserHP>player.userHP:
                         TempUserHP = player.userHP
                    else:
                           print ()
                           print ("Nothing happened.")
                           print ()
                  elif DropChange>50 and DropChange<88:
                       print ("You found an cake!")
                       print ("You ate the cake")
                       if TempUserHP<player.userHP:
                          TempUserHP = TempUserHP+player.userHP*0.1
                          TempUserHP = float(round(TempUserHP,1))
                          print ("10% of your HP has restored!")
                          print ()
                          if TempUserHP>player.userHP:
                            TempUserHP = player.userHP
                       else:
                           print ()
                           print ("Nothing happened.")
                           print ()
                  elif DropChange>88 and DropChange<113:
                       print ("You found an tuna!")
                       print ("You ate the tuna")
                       if TempUserHP<player.userHP:
                          TempUserHP = TempUserHP+player.userHP*0.15
                          TempUserHP = float(round(TempUserHP,1))
                          print ("15% of your HP has restored!")
                          print ()
                          if TempUserHP>player.userHP:
                            TempUserHP = player.userHP
                       else:
                           print ()
                           print ("Nothing happened.")
                           print ()
                  elif DropChange>113 and DropChange<133:
                        print ("You found Super Hit x1!")
                        SuperHit+=1
                        print ()
                  elif DropChange>133 and DropChange<149:
                        print ("You found Super Def x1!")
                        SuperDef+=1
                        print ()
                  elif DropChange>149 and DropChange<163:
                        print ("You found Small Easier Game package!")
                        print ()
                        print ("The game became little bit Easier.")
                        if MonsterBuilderLevel>3:
                          MonsterBuilderLevel-=3
                        if MonsterTempMonsterNumMIN>3:
                          MonsterTempMonsterNumMIN-=3
                        print ()
                  elif DropChange>163 and DropChange<175:
                      print ("You found an lobster!")
                      print ("You ate the lobster")
                      if TempUserHP<player.userHP:
                         TempUserHP = TempUserHP+player.userHP*0.2
                         TempUserHP = float(round(TempUserHP,1))
                         print ("20% of your HP has restored!")
                         print ()
                         if TempUserHP>player.userHP:
                           TempUserHP = player.userHP
                      else:
                          print ()
                          print ("Nothing happened.")
                          print ()
                  elif DropChange>175 and DropChange<186:
                      print ("You found an swordfish!")
                      print ("You ate the swordfish")
                      if TempUserHP<player.userHP:
                         TempUserHP = TempUserHP+player.userHP*0.25
                         TempUserHP = float(round(TempUserHP,1))
                         print ("25% of your HP has restored!")
                         print ()
                         if TempUserHP>player.userHP:
                           TempUserHP = player.userHP
                      else:
                          print ()
                          print ("Nothing happened.")
                          print ()
                  elif DropChange>186 and DropChange<196:
                      print ("You found an EXP Package 1!")
                      print ("Your exp raised by 1.1!")
                      player.userEXP = player.userEXP*1.1
                      player.userEXP = float(round(player.userEXP,1))
                      print ()
                  elif DropChange>196 and DropChange<205:
                        print ("You found Super Hit x2!")
                        SuperHit+=2
                        print ()
                  elif DropChange>205 and DropChange<213:
                        print ("You found Super Def x2!")
                        SuperDef+=2
                        print ()
                  elif DropChange>213 and DropChange<220:
                        print ("You found Medium Easier Game package!")
                        print ()
                        print ("The game became Easier.")
                        if MonsterBuilderLevel>6:
                          MonsterBuilderLevel-=6
                        if MonsterTempMonsterNumMIN>6:
                          MonsterTempMonsterNumMIN-=6
                        print ()
                  elif DropChange>220 and DropChange<227:
                      print ("You found an EXP Package 2!")
                      print ("Your exp raised by 1.25!")
                      player.userEXP = player.userEXP*1.25
                      player.userEXP = float(round(player.userEXP,1))
                      print ()
                  elif DropChange>227 and DropChange<233:
                      print ("You found an shark!")
                      print ("You ate the shark")
                      if TempUserHP<player.userHP:
                         TempUserHP = TempUserHP+player.userHP*0.30
                         TempUserHP = float(round(TempUserHP,1))
                         print ("30% of your HP has restored!")
                         print ()
                         if TempUserHP>player.userHP:
                           TempUserHP = player.userHP
                      else:
                          print ()
                          print ("Nothing happened.")
                          print ()
                  elif DropChange>233 and DropChange<239:
                        print ("You found Super Hit x3!")
                        SuperHit+=3
                        print ()
                  elif DropChange>239 and DropChange<244:
                        print ("You found Super Def x2!")
                        SuperDef+=2
                        print ()
                  elif DropChange>244 and DropChange<249:
                        print ("You found Medium Easier Game package!")
                        print ()
                        print ("The game became much more Easier!")
                        if MonsterBuilderLevel>9:
                          MonsterBuilderLevel-=9
                        if MonsterTempMonsterNumMIN>9:
                          MonsterTempMonsterNumMIN-=9
                        print ()
                  elif DropChange>249 and DropChange<254:
                      print ("You found an EXP Package 3!")
                      print ("Your exp raised by 1.5!")
                      player.userEXP = player.userEXP*1.5
                      player.userEXP = float(round(player.userEXP,1))
                      print ()
                  elif DropChange>254 and DropChange<258:
                      print ("You found an Food Warehouse!")
                      print ("You ate from the Food Warehouse")
                      if TempUserHP<player.userHP:
                         TempUserHP = TempUserHP+player.userHP
                         TempUserHP = float(round(TempUserHP,1))
                         print ("100% of your HP has restored!")
                         print ()
                         if TempUserHP>player.userHP:
                           TempUserHP = player.userHP
                      else:
                          print ()
                          print ("Nothing happened.")
                          print ()
                  elif DropChange>258 and DropChange<262:
                        print ("You found Ulimited Power Aura!")
                        SuperHit+=10
                        print ()
                  elif DropChange>262 and DropChange<266:
                        print ("You found Unbreakeable Shield Aura")
                        SuperDef+=10
                        print ()
                  elif DropChange>266 and DropChange<269:
                        print ("You found Huge Easier Game package!")
                        print ()
                        print ("The game became MUCH MUCH more Easier!")
                        if MonsterBuilderLevel>15:
                          MonsterBuilderLevel-=15
                        if MonsterTempMonsterNumMIN>15:
                          MonsterTempMonsterNumMIN-=15
                        print ()
                  elif DropChange>269 and DropChange<271:
                        print ("*** You Powered up to maximum power! ***")
                        SuperHit+=30
                        print ()
                  elif DropChange>271 and DropChange<273:
                        print ("*** You Powered up to maximum defence! ***")
                        SuperDef+=30
                        print ()
                  elif DropChange>273 and DropChange<275:
                        print ("*** You found a time machine! ***")
                        print ()
                        print ("The game became TOO MUCH  Easier!")
                        if MonsterBuilderLevel>30:
                          MonsterBuilderLevel-=30
                        if MonsterTempMonsterNumMIN>30:
                          MonsterTempMonsterNumMIN-=30
                        print ()

                  else:
                    print ("You found nothing.")
                    print ()
             
          # Check Level Up:
              if player.userEXP>= NextLevel and Rat.MonHP<=0:
                  player.userLevel+=1
                  print ("Congratulations! you have level up!")
                  print ("Your new level: ",player.userLevel)
                  NextLevel*=2.5
                  chance = random.randint(1, 10)
                  if chance>7:
                      plus = player.userHP*0.5
                  else:
                      plus = player.userHP*0.25
                  plus = float(round(plus,1))
                  player.userHP+=plus
                  print ("+ ",plus," HP!")
                  chance = random.randint(1, 10)
                  if chance>7:
                      plus = player.userStr*0.5
                  else:
                      plus = player.userStr*0.25
                  plus = float(round(plus,1))
                  player.userStr+=plus
                  print ("+ ",plus," Str!")
                  chance = random.randint(1, 10)
                  if chance>7:
                      plus = player.userAtt*0.5
                  else:
                      plus = player.userAtt*0.25
                  plus = float(round(plus,1))
                  player.userAtt+=plus
                  print ("+ ",plus," Atk!")
                  chance = random.randint(1, 10)
                  if chance>7:
                      plus = player.userDef*0.5
                  else:
                      plus = player.userDef*0.25
                  plus = float(round(plus,1))
                  player.userDef+=plus
                  print ("+ ",plus," Def!")
                  print ()
                  player.userHP = float(round(player.userHP,1))
                  player.userStr = float(round(player.userStr,1))
                  player.userAtt = float(round(player.userAtt,1))
                  player.userDef = float(round(player.userDef,1))
                  TempUserHP = float(round(TempUserHP,1))
                  break
              elif Rat.MonHP<=0:
                  break
          else:
              print()
              # MONSTER TURN
              if  TempPlayerSpeed==TempMonserSpeed:
                  TempPlayerSpeed-=1
              TempMaxSpeed = TempMonserSpeed
              TempMonserSpeed = TempPlayerSpeed
              TempPlayerSpeed = TempMaxSpeed
              print ("*** Monster Turn ***")
              if MonsterAtkPower>8:
                  TimeCreate("CriAttack")
                  print ("CRITICAL HIT!!!")
                  PlayerShield = player.userDef- Rat.MonAtk
                  if PlayerShield<0:
                      PlayerShield = 0
                  if SuperDef>0:
                    print("Super Def Activate!")
                    Damage = 1
                    SuperDef-=1
                  else:
                    Damage = Rat.MonStr*1.5 - PlayerShield
                  Damage = float(round(Damage,1))
                  if Damage<1:
                      Damage = 1
                  TempUserHP-=Damage
                  TempUserHP = float(round(TempUserHP,1))
                  print ("Monster deal ",Damage," damage")
              elif MonsterAtkPower>6:
                  TimeCreate("StrongAttack")
                  print ("Strong hit!")
                  PlayerShield = player.userDef- Rat.MonAtk
                  if PlayerShield<0:
                      PlayerShield = 0
                  if SuperDef>0:
                    print("Super Def Activate!")
                    Damage = 1
                    SuperDef-=1
                  else:
                    Damage = Rat.MonStr*1.2 - PlayerShield
                  Damage = float(round(Damage,1))
                  if Damage<1:
                      Damage = 1
                  TempUserHP-=Damage
                  TempUserHP = float(round(TempUserHP,1))
                  print ("Monster deal ",Damage," damage")
              else:
                  TimeCreate("NormalAttack")
                  print ("Regular hit.")
                  PlayerShield = player.userDef- Rat.MonAtk
                  if PlayerShield<0:
                      PlayerShield = 0
                  if SuperDef>0:
                    print("Super Def Activate!")
                    Damage = 1
                    SuperDef-=1
                  else:
                    Damage = Rat.MonStr - PlayerShield
                  Damage = float(round(Damage,1))
                  if Damage<1:
                      Damage = 1
                  TempUserHP-=Damage
                  TempUserHP = float(round(TempUserHP,1))
                  print ("Monster deal ",Damage," damage")
              print("HP left to the Player: ",TempUserHP)
              if TempUserHP<=0:
                  TempUserHP = 0
                  print ()                      
                  print ("Player Is Dead!")
                  print ()
                  print(Rat.MonName," has won!")
                  print ()
                  print ("*** GAME OVER! ***")
                  print ()
             
                  print ("Level:", player.userLevel)
                  print ("EXP:", player.userEXP)
                  print ("HP:",TempUserHP,"/", player.userHP)
                  print ("Str:", player.userStr)
                  print ("Def:", player.userDef)
                  print ("Atk:", player.userAtt)
                  print ("Total Power:", player.TotalPower())
                  print ("Super Hits: ", SuperHit)
                  print ("Super Defs: ", SuperDef)

                  print ()
                  if player.userLevel>BestLevel:
                      BestLevel = player.userLevel
                      print("*** You break a record! ***")
                      print("The best User level you have reach to is: ",BestLevel)
                      print()
                  else:
                      print("The best User level you have reach to is: ",BestLevel)
                      print()
                 
                  if player.TotalPower()>BestPower:
                      BestPower = player.TotalPower()      
                      print("*** You break a record! ***")
                      print("The best Power Level you have reach to is: ",BestPower)
                      print()
                  else:
                      print("The best Power Level you have reach to is: ",BestPower)  
                      print()
             
                  print ("Do you want to start again? (y/n):")
                  a = input()
                  if a=="y":
                      # ############# Main starts from here ############
                      NextLevel = 10 #Shows the next exp you need for the next level
                      print()
                      print ("********************************************")
                      print()
                      print ("Hello there and welcome to the game!")
                      print ("Your stats are:")
                 
                      # This is the chance to get stronger monsters
                      MonsterBuilderLevel = 1
                      MonsterTempMonsterNum = 0
                 
                      if GameLevel=="1":
                          FirstBoost=2
                      elif GameLevel=="2":
                          FirstBoost=1
                      elif GameLevel=="3":
                          FirstBoost=0

                      MaxBoost = 3+FirstBoost

                      # Creating the user and his first stats
                      player = Player()
                      player.userHP = random.randint(10, 20)
                      player.userStr = random.randint(1, MaxBoost)
                      player.userDef = random.randint(1, MaxBoost)
                      player.userAtt = random.randint(1, MaxBoost)
                      TempUserHP = player.userHP
                 
                      break
                  else:
                      print("Goodbay!")
                      exit()

      print ("Level:", player.userLevel)
      print ("EXP:", player.userEXP)
      print ("HP:",TempUserHP,"/", player.userHP)
      print ("Str:", player.userStr)
      print ("Def:", player.userDef)
      print ("Atk:", player.userAtt)
      print ("Total Power:", player.TotalPower())
      print ("Super Hits: ", SuperHit)
      print ("Super Defs: ", SuperDef)
      print ()
  # Traning
  elif choise=="2":
      TrainingEffectivity = random.randint(1, 100)
      SkillLevelUpMulty = 1
      print("Traning...")
      if TrainingEffectivity<60:
          TimeCreate("FineTraning")
          print ("You had a fine traning")
          SkillLevelUpMulty = 1.2
      elif TrainingEffectivity>60 and TrainingEffectivity<90:
          TimeCreate("GoodTraning")
          print ("You had a great traning!")
          SkillLevelUpMulty = 1.6
      else:
          TimeCreate("AwsomeTraning")
          print ("You had a AWSOME traning!!!")
          SkillLevelUpMulty = 2
      ChosenSkill = random.randint(1, 4)
      if ChosenSkill==1:
          plus = (SkillLevelUpMulty*player.userHP)/10
          plus = float(round(plus,1))
          player.userHP=player.userHP+((SkillLevelUpMulty/10)*player.userHP)
          print ("Your HP skill improved!")
          print ("+",plus)
      elif ChosenSkill==2:
          plus = (SkillLevelUpMulty*player.userStr)/10
          plus = float(round(plus,1))
          player.userStr=player.userStr+((SkillLevelUpMulty/10)*player.userStr)
          print ("Your Str skill improved!")
          print ("+",plus)
      elif ChosenSkill==3:
          plus = (SkillLevelUpMulty*player.userDef)/10
          plus = float(round(plus,1))
          player.userDef=player.userDef+((SkillLevelUpMulty/10)*player.userDef)
          print ("Your Def skill improved!")
          print ("+",plus)
      elif ChosenSkill==4:
          plus = (SkillLevelUpMulty*player.userAtt)/10
          plus = float(round(plus,1))
          player.userAtt=player.userAtt+((SkillLevelUpMulty/10)*player.userAtt)
          print ("Your Atk skill improved!")
          print ("+",plus)
      player.userHP = float(round(player.userHP,1))
      player.userStr = float(round(player.userStr,1))
      player.userAtt = float(round(player.userAtt,1))
      player.userDef = float(round(player.userDef,1))
      if TempUserHP<player.userHP:
          TempUserHP = TempUserHP+player.userHP*0.20
          TempUserHP = float(round(TempUserHP,1))
          print ()
          print ("20% of your HP has restored!")
          if TempUserHP>player.userHP:
              TempUserHP = player.userHP
      print ()
      print ("Level:", player.userLevel)
      print ("EXP:", player.userEXP)
      print ("HP:",TempUserHP,"/", player.userHP)
      print ("Str:", player.userStr)
      print ("Def:", player.userDef)
      print ("Atk:", player.userAtt)
      print ("Total Power:", player.TotalPower())
      print ("Super Hits: ", SuperHit)
      print ("Super Defs: ", SuperDef)
      print ()
  elif choise=="3":
      if TempUserHP<player.userHP:
          TempUserHP = TempUserHP+player.userHP*0.60
          TempUserHP = float(round(TempUserHP,1))
          print ()
          print("Resting...")
          TimeCreate("Rest")
          print ("You have rested")
          print ("60% of your HP has restored!")
          if TempUserHP>player.userHP:
              TempUserHP = player.userHP
      else:
          print ()
          print ("You have rested")
          print ("Nothing happened.")
      print ()
      print ("Level:", player.userLevel)
      print ("EXP:", player.userEXP)
      print ("HP:",TempUserHP,"/", player.userHP)
      print ("Str:", player.userStr)
      print ("Def:", player.userDef)
      print ("Atk:", player.userAtt)
      print ("Total Power:", player.TotalPower())
      print ("Super Hits: ", SuperHit)
      print ("Super Defs: ", SuperDef)
      print ()
  MonsterBuilderLevel+=1
  if MonsterBuilderLevel>50:
    MonsterTempMonsterNumMIN+=1
    if GameLevel=="2":
      MonsterTempMonsterNumMIN+=1
    elif GameLevel=="3":
      MonsterTempMonsterNumMIN+=2
  if MonsterBuilderLevel>246:
    MonsterBuilderLevel-=1
    MonsterTempMonsterNumMIN-=1










