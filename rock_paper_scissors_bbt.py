def rps():
    import time
    import random
    from datetime import date
    from datetime import datetime
                                                                    #USER Inputs for the intro section.
    try:
        user_name = input('Please enter your full name: ')
        age = int(input('Please enter your age: '))
    except:
        print('Ehhh I just got an error.\nPlease make sure you enter the data correctly.')
        user_name = input('Please eneter your full name: ')
        age = int(input('Please enter your age: '))

                                                                    #Game Intro
    def intro():
        print(f'Hello {user_name}! Welcome to the best game ever invented since Bar wrote it.\n')
        print('We are going to play 5 rounds\n'
              '\nThe game rules:\n'
              '\t 1. Rock beats scissors and lizard\n'
              '\t 2. Paper beats rock and spock\n'
              '\t 3. Scissors beats paper and lizard\n'
              '\t 4. Lizard beats spock and paper\n'
              '\t 8. Spock beats scissors and rock\n'
              '\t 5. Who ever has the most points, wins.\n'
              '\t 6. PG-18, do not play if you are underage.\n')
    intro()

    def game():

        # Score_board
        the_date = date.today()
        today_date = the_date.strftime("%d/%m/%Y")
        the_time = datetime.now()
        today_time = the_time.strftime("%H:%M")
        pc_wins = 0
        player_wins = 0
        sivuv = 0

        if age > 18:
            while True:
                            # LIST OF WEAPONS
                weapons = ['rock', 'paper', 'scissors', 'lizard', 'spock']

                            # Element = [WHO GETS KILLED]
                rock_losers = ['scissors','lizard']
                paper_losers = ['spock','rock']
                scissors_losers = ['lizard','paper']
                lizard_losers = ['spock','paper']
                spock_losers = ['rock','scissors']

                            # Winners lists - ELEMENT = [WHO CAN KILL]
                rock_winers = ['paper','spock']
                paper_winers = ['lizard','scissors']
                scissors_winers = ['spock','rock']
                lizard_winers = ['scissors','rock']
                spock_winers = ['lizard','paper']

                            # Random choice for PC --> pc_choice
                _pc_choice = random.randint(0,4)
                pc_choice = weapons[_pc_choice]

                            # Letting the user choose --> player_choice
                please_pick = (f'This is your arsenal for today, choose carefully.\n'
                      f'{weapons}')
                top = f'-----------------------------------------------\n'
                bot = f'\n-----------------------------------------------'
                score_board_tie = f'{top}\tIts a tie\n\tSTATS:\n\tROUNDS: {sivuv}/5\nPC: {pc_wins}\t\t{user_name}: {player_wins}\n\t{today_time}\n\t{today_date}{bot}'
                score_board_lost = f'{top}\tYou lost\n\tSTATS:\n\tROUNDS: {sivuv}/5\nPC: {pc_wins}\t\t{user_name}: {player_wins}\n\t{today_time}\n\t{today_date}{bot}'
                score_board_won = f'{top}\tYou won\n\tSTATS:\n\tROUNDS: {sivuv}/5\nPC: {pc_wins}\t\t{user_name}: {player_wins}\n\t{today_time}\n\t{today_date}{bot}'
                            # Check if we reached 5 rounds
                if sivuv >= 5:
                    # ITS A TIE
                    if pc_wins == player_wins:
                        print('its a tie')
                        print(score_board_tie)
                        again = input('Do you want to save the results of the last match? ')
                        if again.lower() == 'yes':
                            print('Saving the last match results.')
                            results_file = open('Results.txt', 'a')
                            results_file.write(f'{score_board_tie}\n')
                            results_file.close()
                            x = input('do you want to keep playing?: ')
                            if x == 'yes':
                                sivuv = 0
                                game()
                            else:
                                exit()
                        else:
                            x = input('do you want to keep playing?: ')
                            if x == 'yes':
                                sivuv = 0
                                game()
                            else:
                                exit()
                    # USER WON
                    elif player_wins > pc_wins:
                        print(score_board_won)
                        again = input('Do you want to save the results of the last match? ')
                        if again.lower() == 'yes':
                            print('Saving the last match results.')
                            results_file = open('Results.txt', 'a')
                            results_file.write(f'{score_board_won}\n')
                            results_file.close()
                            x = input('do you want to keep playing?: ')
                            if x == 'yes':
                                sivuv = 0
                                game()
                            else:
                                exit()
                        else:
                            x = input('do you want to keep playing?: ')
                            if x == 'yes':
                                sivuv = 0
                                game()
                            else:
                                exit()
                    # USER LOST
                    elif pc_wins > player_wins:
                        print(score_board_lost)
                        again = input('Do you want to save the results of the last match? ')
                        if again.lower() == 'yes':
                            print('Saving the last match results.')
                            results_file = open('Results.txt', 'a')
                            results_file.write(f'{score_board_lost}\n')
                            results_file.close()
                            x = input('do you want to keep playing?: ')
                            if x == 'yes':
                                sivuv = 0
                                game()
                            else:
                                exit()
                        else:
                            x = input('do you want to keep playing?: ')
                            if x == 'yes':
                                sivuv = 0
                                game()
                            else:
                                exit()
    # USER PICK & CHECKS FOR WINNER
                else:
                    print(please_pick)
                    player_choice = input('Chooce your weapon: ')

                    if player_choice.lower() == pc_choice.lower():
                        sivuv = sivuv + 1
                        print(f'-----------------ROUND:{sivuv}---------------------')
                        print(f'{user_name} chose {player_choice}!')
                        print(f'The computer chose {pc_choice}')
                        print('its a tie.')
                    elif player_choice.lower() == 'rock':
                        if pc_choice in rock_losers:
                            player_wins += 1
                            sivuv = sivuv+1
                            print(f'-----------------ROUND:{sivuv}---------------------')
                            print(f'{user_name} chose {player_choice}!')
                            print(f'The computer chose {pc_choice}')
                            print('you win')
                        elif pc_choice in rock_winers:
                            pc_wins += 1
                            sivuv = sivuv+1
                            print(f'-----------------ROUND:{sivuv}---------------------')
                            print(f'{user_name} chose {player_choice}!')
                            print(f'The computer chose {pc_choice}')
                            print('you lose')
                    elif player_choice.lower() == 'paper':
                        if pc_choice in paper_losers:
                            player_wins += 1
                            sivuv = sivuv+1
                            print(f'-----------------ROUND:{sivuv}---------------------')
                            print(f'{user_name} chose {player_choice}!')
                            print(f'The computer chose {pc_choice}')
                            print('you win')
                        elif pc_choice in paper_winers:
                            pc_wins += 1
                            sivuv = sivuv+1
                            print(f'-----------------ROUND:{sivuv}---------------------')
                            print(f'{user_name} chose {player_choice}!')
                            print(f'The computer chose {pc_choice}')
                            print('you lose')
                    elif player_choice.lower() == 'scissors':
                        if pc_choice in scissors_losers:
                            player_wins += 1
                            sivuv = sivuv+1
                            print(f'-----------------ROUND:{sivuv}---------------------')
                            print(f'{user_name} chose {player_choice}!')
                            print(f'The computer chose {pc_choice}')
                            print('you win')
                        elif pc_choice in scissors_winers:
                            pc_wins += 1
                            sivuv = sivuv+1
                            print(f'-----------------ROUND:{sivuv}---------------------')
                            print(f'{user_name} chose {player_choice}!')
                            print(f'The computer chose {pc_choice}')
                            print('you lose')
                    elif player_choice.lower() == 'lizard':
                        if pc_choice in lizard_losers:
                            player_wins += 1
                            sivuv = sivuv+1
                            print(f'-----------------ROUND:{sivuv}---------------------')
                            print(f'{user_name} chose {player_choice}!')
                            print(f'The computer chose {pc_choice}')
                            print('you win')
                        elif pc_choice in lizard_winers:
                            pc_wins += 1
                            sivuv = sivuv+1
                            print(f'-----------------ROUND:{sivuv}---------------------')
                            print(f'{user_name} chose {player_choice}!')
                            print(f'The computer chose {pc_choice}')
                            print('you lose')
                    elif player_choice.lower() == 'spock':
                        if pc_choice in spock_losers:
                            player_wins += 1
                            sivuv = sivuv+1
                            print(f'-----------------ROUND:{sivuv}---------------------')
                            print(f'{user_name} chose {player_choice}!')
                            print(f'The computer chose {pc_choice}')
                            print('you win')
                        elif pc_choice in spock_winers:
                            pc_wins += 1
                            sivuv = sivuv+1
                            print(f'-----------------ROUND:{sivuv}---------------------')
                            print(f'{user_name} chose {player_choice}!')
                            print(f'The computer chose {pc_choice}')
                            print('you lose')
                    else:
                        print('Please make sure that you are entering a proper weapon name.\n'
                              'This will not affect the point & rounds system.')
    game()
rps()
