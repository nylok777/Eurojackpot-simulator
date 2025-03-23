import numpy as np
import pandas as pd

def print_win_text(tier: int, week, money: int):
   if tier > 0:
      print(f"You won the {tier}. tier at the {week}. week! Your balance after winning: {money}")
   else:
      print(f"Sadly, you didn't win anything at the {week}. week. Your balance after losing: {money}")

def play(money: int, weeks: int):
   weeks_ar = np.arange(1, weeks+1)
   for week in weeks_ar:
      p_nums = [np.unique(np.random.randint(low=2, high=51, size=(1, 5))), 
               np.unique(np.random.randint(low=2, high=13, size=(1, 2)))]   
      win_nums = [np.unique(np.random.randint(low=2, high=51, size=(1, 5))), 
                  np.unique(np.random.randint(low=2, high=13, size=(1, 2)))]
      money = money - 2
      result_main = np.isin(p_nums[0], win_nums[0])
      result_sup = np.isin(p_nums[1], win_nums[1])
      if result_main.all == True:
         if result_sup.all == True:
            money += 51400000
            print_win_text(1,week=week,money=money)
            return money
         elif result_sup.any == True:
            money += 1330000
            print_win_text(2,week=week,money=money)
            return money
         else:
            money += 196854
            print_win_text(3,week=week,money=money)
            return money
      elif np.sum(result_main) == 4:
         if result_sup.all == True:
            money += 5633
            print_win_text(4,week=week,money=money)
         elif result_sup.any == True:
            money += 325
            print_win_text(5,week=week,money=money)
         else:
            money += 113
            print_win_text(7,week=week,money=money)
      elif np.sum(result_main) == 3:
         if result_sup.all == True:
            money += 164
            print_win_text(6,week=week,money=money)
         elif result_sup.any == True:
            money += 20
            print_win_text(9,week=week,money=money)
         else:
            money += 17
            print_win_text(10,week=week,money=money)
      elif np.sum(result_main) == 2:
         if result_sup.all == True:
            money += 26
            print_win_text(8,week=week,money=money)
         elif result_sup.any == True:
            money += 10
            print_win_text(12,week=week,money=money)
         else:
            print_win_text(0,week=week,money=money)
      elif result_main.any == True and result_sup.all == True:
         money += 13
         print_win_text(11,week=week,money=money)
      else:
         print_win_text(0,week=week,money=money)
   print(f"Your final balance after playing Eurojackpot for {weeks} weeks: {money}")

print("Rules: one line costs 2 euros \nthere are 12 prize tiers, each prize tier contains the average amount won in the "
"tier from March 25 2022 to March 14 2025 \nthe jackpot is 51 million euros\n"
"you only stop playing if you win the jackpot or the 2 tiers below it")
played_weeks = input("How many weeks do you want to play? ")
player_money = input("How much euros do you want to 'invest'? ")
playing = True
while playing == True:
   play(int(player_money), int(played_weeks))
   if input("Type exit to end the game ") == "exit":
      playing = False