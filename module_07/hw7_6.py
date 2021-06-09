def solve_riddle(riddle, word_length, start_letter, reverse=False):

    if reverse == False:
        index_start_letter = riddle.find(start_letter)

        return riddle[index_start_letter:(index_start_letter + word_length)]

    elif reverse == True:
        index_start_letter = riddle.rfind(start_letter)

        return riddle[index_start_letter:(
            index_start_letter - word_length):-1]
