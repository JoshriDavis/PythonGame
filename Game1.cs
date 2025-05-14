using System;
using System.Collections.Generic;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

// TODOs to complete version 0.03:
/*
Make sure the stats + names of the current monsters match the old monsters
Add all the missing monsters
Add to the prints empty prints etc. to show the console in the same way as before
Make sure the game prints the player's stats after each turn
Move classes and so to their separate files
Use exact drop behavior per monster drop table from original game.
Implement "Your stats are:" before printing the stats
Implement and display attack types (critical hits, etc.)
Implement and display training types
Exp seems to be different, fix it
Ensure high scores are saved correctly
It seems like the monsters aren't randomized. Fix it
add all the todos from the original game
 * */

namespace PythonGame
{
    public class Game1: Game
    {
        private readonly GraphicsDeviceManager graphics;
        private readonly SpriteBatch spriteBatch;
        private Player player;
        private readonly Random random = new();
        private int nextLevelExp = 10;
        private int superHit = 0;
        private int superDef = 0;
        private int bestLevel = 0;
        private double bestPower = 0;

        private enum GameState { Menu, Playing, GameOver }

        private GameState currentState = GameState.Menu;

        public Game1()
        {
            graphics = new GraphicsDeviceManager(this);
            Content.RootDirectory = "Content";
            IsMouseVisible = true;
        }

        protected override void Initialize()
        {
            base.Initialize();
            StartGame();
        }

        private void StartGame()
        {
            Console.WriteLine("Welcome to the Console RPG!");
            Console.WriteLine("Choose difficulty: 1-Easy, 2-Medium, 3-Hard");
            string levelInput = Console.ReadLine();

            int firstBoost = levelInput switch
            {
                "1" => 2,
                "2" => 1,
                _ => 0
            };

            Console.WriteLine("Choose speed mode: 1-Regular, 2-Fast");
            string speedInput = Console.ReadLine();

            int maxBoost = 3 + firstBoost;

            player = new Player
            {
                HP = random.Next(10, 21),
                Str = random.Next(1, maxBoost + 1),
                Def = random.Next(1, maxBoost + 1),
                Atk = random.Next(1, maxBoost + 1),
                Level = 1,
                EXP = 0
            };

            player.CurrentHP = player.HP;

            nextLevelExp = 10;
            superHit = 0;
            superDef = 0;

            DisplayStats();
            currentState = GameState.Playing;
        }

        private void DisplayStats()
        {
            Console.WriteLine($"Level: {player.Level}");
            Console.WriteLine($"EXP: {player.EXP:F1}");
            Console.WriteLine($"HP: {player.CurrentHP:F1}/{player.HP:F1}");
            Console.WriteLine($"Str: {player.Str:F1}");
            Console.WriteLine($"Def: {player.Def:F1}");
            Console.WriteLine($"Atk: {player.Atk:F1}");
            Console.WriteLine($"Total Power: {player.TotalPower():F1}");
            Console.WriteLine($"Super Hits: {superHit}");
            Console.WriteLine($"Super Defs: {superDef}");
        }


        protected override void Update(GameTime gameTime)
        {
            if(currentState == GameState.GameOver)
            {
                Console.WriteLine("Do you want to start again? (y/n)");
                string input = Console.ReadLine();
                if(input.Equals("y", StringComparison.CurrentCultureIgnoreCase))
                    StartGame();
                else
                {
                    Console.WriteLine("Goodbye!");
                    Exit();
                }
                return;
            }


            if(currentState != GameState.Playing)
                return;

            Console.WriteLine("What do you want to do? (1. Find monster 2. Training 3. Rest)");
            string choice = Console.ReadLine();

            if(choice == "1")
            {
                Monster monster = MonsterFactory.CreateMonsterByTier(player.Level);
                Console.WriteLine($"A wild {monster.Name} (Level {monster.Level}) appears!");
                FightMonster(monster);
            }
            else if(choice == "2")
            {
                player.Train();
                player.CurrentHP = Math.Min(player.HP, player.CurrentHP + player.HP * 0.2);
                Console.WriteLine("20% HP restored from training.");
                DisplayStats();
            }
            else if(choice == "3")
            {
                player.CurrentHP = Math.Min(player.HP, player.CurrentHP + player.HP * 0.6);
                Console.WriteLine("60% HP restored from rest.");
                DisplayStats();
            }

            base.Update(gameTime);
        }

        private void FightMonster(Monster monster)
        {
            while(player.CurrentHP > 0 && monster.HP > 0)
            {
                Console.WriteLine("*** Player Turn ***");
                int atkRoll = random.Next(1, 11);
                double shield = Math.Max(0, monster.Def - player.Atk);
                double damage = atkRoll > 8 ? player.Str * 1.5 : atkRoll > 6 ? player.Str * 1.2 : player.Str;
                damage = Math.Max(1, Math.Round(damage - shield, 1));

                if(superHit > 0)
                {
                    Console.WriteLine("SUPER HIT!");
                    damage = Math.Max(1, Math.Round(player.Str * 2 - shield, 1));
                    superHit--;
                }

                monster.HP -= damage;
                Console.WriteLine($"You dealt {damage} damage. Monster HP left: {Math.Max(monster.HP, 0):F1}");

                if(monster.HP <= 0)
                {
                    double expGain = monster.TotalStats() * (1 + monster.Level * 0.05);
                    player.EXP += Math.Round(expGain, 1);
                    Console.WriteLine($"{monster.Name} is defeated! You earned {expGain:F1} EXP.");

                    int dropRoll = random.Next(1, 276);
                    HandleDrop(dropRoll);

                    if(player.EXP >= nextLevelExp)
                    {
                        player.LevelUp();
                        nextLevelExp = (int)(nextLevelExp * 1.35);
                    }
                    return;
                }

                Console.WriteLine("*** Monster Turn ***");
                int monAtkRoll = random.Next(1, 11);
                double playerShield = Math.Max(0, player.Def - monster.Atk);
                double monDamage = monAtkRoll > 8 ? monster.Str * 1.5 : monAtkRoll > 6 ? monster.Str * 1.2 : monster.Str;
                monDamage = Math.Max(1, Math.Round(monDamage - playerShield, 1));

                if(superDef > 0)
                {
                    Console.WriteLine("SUPER DEF!");
                    monDamage = 1;
                    superDef--;
                }

                player.CurrentHP -= monDamage;
                Console.WriteLine($"{monster.Name} dealt {monDamage} damage. Your HP: {Math.Max(player.CurrentHP, 0):F1}");

                if(player.CurrentHP <= 0)
                {
                    Console.WriteLine("You were defeated. GAME OVER.");
                    Console.WriteLine();
                    Console.WriteLine($"Final Level: {player.Level}");
                    Console.WriteLine($"Total Power: {player.TotalPower():F1}");

                    if(player.Level > bestLevel)
                    {
                        bestLevel = player.Level;
                        Console.WriteLine("*** New record for best level! ***");
                    }
                    else
                    {
                        Console.WriteLine($"Best level: {bestLevel}");
                    }

                    if(player.TotalPower() > bestPower)
                    {
                        bestPower = player.TotalPower();
                        Console.WriteLine("*** New record for best power! ***");
                    }
                    else
                    {
                        Console.WriteLine($"Best power: {bestPower:F1}");
                    }

                    currentState = GameState.GameOver;
                    return;
                }
            }
        }

        private static void HandleDrop(int roll) { /* existing unchanged */ }
        protected override void Draw(GameTime gameTime) { GraphicsDevice.Clear(Color.Black); base.Draw(gameTime); }
        private static void Main() { using Game1 game = new(); game.Run(); }

    }

    public class Player
    {
        public double HP;
        public double CurrentHP;
        public double Str;
        public double Def;
        public double Atk;
        public int Level;
        public double EXP;

        public double TotalPower() => Math.Round(HP + Str + Def + Atk, 1);

        public void Train()
        {
            Random rand = new();
            int skill = rand.Next(1, 5);
            double multiplier = rand.NextDouble() * 0.5 + 1.2;

            switch(skill)
            {
                case 1: HP += HP * multiplier / 10; break;
                case 2: Str += Str * multiplier / 10; break;
                case 3: Def += Def * multiplier / 10; break;
                case 4: Atk += Atk * multiplier / 10; break;
            }
        }

        public void LevelUp()
        {
            Level++;
            Random rand = new();
            HP += rand.Next(0, 2) == 0 ? HP * 0.25 : HP * 0.5;
            Str += rand.Next(0, 2) == 0 ? Str * 0.25 : Str * 0.5;
            Def += rand.Next(0, 2) == 0 ? Def * 0.25 : Def * 0.5;
            Atk += rand.Next(0, 2) == 0 ? Atk * 0.25 : Atk * 0.5;
        }
    }

    public class Monster
    {
        public string Name;
        public int Level;
        public double HP;
        public double Str;
        public double Def;
        public double Atk;
        public double TotalStats() => Math.Round(HP + Str + Def + Atk, 1);
    }

    public static class MonsterFactory
    {
        public static Monster CreateMonsterByTier(int playerLevel)
        {
            //Random rand = new();
            List<(string name, int level, double hp, double atk, double def, double str)> monsters =
            [
                ("Rat", 1, 5, 1.4, 1, 1),
                ("Fat Rat", 3, 22, 1, 2, 2),
                ("Goblin", 5, 32, 6, 6, 6),
                ("Elite Goblin", 7, 52, 8, 8, 8),
                ("Giant", 9, 64.4, 16, 9, 15),
                ("Dragon Warrior", 85, 300, 165, 50, 165),
                ("Goku SSJ1", 2100, 12800, 4200, 4000, 4200),
                ("God Super Titan", 4000, 10000, 10000, 10000, 10000),
                ("Gotenks SSJ3", 9000, 60000, 18000, 13500, 16500)
            ];
            var tier = Math.Min(monsters.Count - 1, playerLevel / 3);
            return new Monster
            {
                Name = monsters[tier].name,
                Level = monsters[tier].level,
                HP = monsters[tier].hp,
                Atk = monsters[tier].atk,
                Def = monsters[tier].def,
                Str = monsters[tier].str
            };
        }
    }
}
