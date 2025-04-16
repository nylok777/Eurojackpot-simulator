import numpy as np
import keyboard as kb
from numpy.random import Generator, PCG64

generator = Generator(PCG64())

def print_win_text(tier: int, week, money: int):
   if tier > 0:
      print(f"You won the {tier}. tier on the {week}. week! Your balance after winning: {money}")
   else:
      print(f"Sadly, you didn't win anything on the {week}. week. Your balance after losing: {money}")

def play(money: int, weeks: int, often, tables):
   weeks_ar = np.arange(1, weeks+1)
   for week in weeks_ar:
      if money < 2:
         print("You ran out of money!")
         break
      for i in range(often):
         p_tables = []
         for _ in range(tables[i]):
            p_nums = [generator.choice(np.arange(1, 51), (5, 1), replace=False),
                      generator.choice(np.arange(1, 13), (2, 1), replace=False)]
            p_tables.append(p_nums)
            money -= 2
         win_nums = [generator.choice(np.arange(1, 51), (5, 1), replace=False),
                     generator.choice(np.arange(1, 13), (2, 1), replace=False)]
         for t in range(tables[i]):
            result_main = np.isin(p_tables[t][0], win_nums[0])
            result_sup = np.isin(p_tables[t][1], win_nums[1])
            if result_main.all():
               if result_sup.all():
                  money += 51400000
                  print_win_text(1,week, money)
                  return money
               elif result_sup.any():
                  money += 1330000
                  print_win_text(2,week, money)
                  return money
               else:
                  money += 196854
                  print_win_text(3,week, money)
                  return money
            elif np.sum(result_main) == 4:
               if result_sup.all():
                  money += 5633
                  print_win_text(4,week, money)
               elif result_sup.any():
                  money += 325
                  print_win_text(5,week, money)
               else:
                  money += 113
                  print_win_text(7,week, money)
            elif np.sum(result_main) == 3:
               if result_sup.all():
                  money += 164
                  print_win_text(6,week, money)
               elif result_sup.any():
                  money += 20
                  print_win_text(9,week, money)
               else:
                  money += 17
                  print_win_text(10,week, money)
            elif np.sum(result_main) == 2:
               if result_sup.all():
                  money += 26
                  print_win_text(8,week, money)
               elif result_sup.any():
                  money += 10
                  print_win_text(12,week, money)
               else:
                  print_win_text(0,week, money)
            elif result_main.any() and result_sup.all():
               money += 13
               print_win_text(11,week, money)
            else:
               print_win_text(0,week, money)
   print(f"Your final balance after playing Eurojackpot for {weeks} weeks: {money}")

def tables_per_week(often: int):
   if often > 1:
      first_draw = input("how many tables do you want to play per week in the first drawing? (max 5) ")
      sec_draw = input("how many tables do you want to play per week in the second drawing? (max 5) ")
      return np.array([int(first_draw), int(sec_draw)])
   else:
      first_draw = input("how many tables do you want to play per week? (max 5) ")
      return np.array([int(first_draw)])
   
text_dict = {
   1 : "How many weeks do you want to play? ",
   2 : "How much euros do you want to 'invest'? ",
   3 : "How often do you want to play per week? type 1 or 2 ",
   4 : ""
}

def input_check(key: int):
   if key == 4:
      return tables_per_week(how_often)
   user_in_casted = 0
   while True:
      user_in = input(text_dict[key])
      try:
         user_in_casted = int(user_in)
      except ValueError:
         print("Error! Incorrect input")
         continue
      break
   return user_in_casted

print("Rules: one ticket costs 2 euros\nthere are 12 prize tiers, each prize tier contains the average amount won in the "
"tier from March 25 2022 to March 14 2025\nthe jackpot is 51 million euros\n"
"you only stop playing if you win the jackpot or the 2 tiers below it")

playing = True
while playing == True:
   weeks = input_check(1)
   money = input_check(2)
   how_often = input_check(3)
   tables_num = input_check(4)

   play(money, weeks, how_often, tables_num)
   print("Press escape to exit, or any other key to play again (EXCEPT ENTER :( )")

   event = kb.read_event()
   if event.event_type == kb.KEY_DOWN and event.name == 'esc':
      playing = False