
# from icecream import ic
import numpy as np

file_path = "/home/glados/Documents/AmirAli Toori/Lessons/Python/HWs/AdvancedPrograming-HWs/HW5/Q4/laliga-2023.txt"

def check(table, column):
    max_value = max(table[:,column])
    max_index = np.where(table[:,column] == max_value)
    max_answer = np.squeeze(table[max_index, 0])
    
    min_value = min(table[:,column])
    min_index = np.where(table[:,column] == min_value)
    min_answer = np.squeeze(table[min_index, 0])
    
    return max_answer, min_answer


def convert(table):
    row, column = np.shape(table)
    for r in range(0, row):
        for c in range(1, column):
           temp = np.squeeze(table[r, c])
           temp = int(temp)
           table[r, c] = temp
           
    return table

try:
    with open(file_path, "r") as f:
        
        line_count = len(f.readlines())
        f.seek(0)
        
        text_table = f.readlines()
        table = []
        for line in text_table:
            token_list = line.split()
            
            if len(token_list) == 11:
                token_list [1] = token_list[1] + token_list[2]
                token_list.remove(token_list[2])
            token_list.remove(token_list[0])
            table.append(token_list)
        
            # index 3: Draw
            # index 5: Goals for
            # index 6: Goals Against for
            # index 8: Goal Difference
except:
    raise IOError("The file does not exist.")
else:
    draw_column = 3
    goals_for_column = 5
    goals_againts_column = 6
    goals_difference_column = 8

    table.remove(table[0])
    table = np.array(table, dtype = object)

    print(table)

    table = convert(table)

    max_team, min_team = check(table, goals_for_column)
    print(f"Teams that have the Max and Min GF | MAX: {max_team}, MIN: {min_team}")

    max_team, min_team = check(table, goals_againts_column)
    print(f"Teams that have the Max and Min GA | MAX: {max_team}, MIN: {min_team}")

    max_team, min_team = check(table, goals_difference_column)
    print(f"Teams that have the Max and Min GD | MAX: {max_team}, MIN: {min_team}")

    max_team, min_team = check(table, draw_column)
    print(f"Teams that have the Max and Min Draw | MAX: {max_team}, MIN: {min_team}")




