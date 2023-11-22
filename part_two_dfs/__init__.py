from models import Player, Labyrinthe, Case

from sys import exit

def resolve(player: Player, lab: Labyrinthe):
    tries = 0
    while player.get_coordinates() != lab.get_goal_coordinates():
        try:
            lab.show(player)
            input('Press Enter to continue...\n')

            actual_coordinates = player.get_coordinates()
            forward_case = player.forward_case(lab)
            adjacent_cases = player.adjacent_cases(lab)
            for case in adjacent_cases:
                if case['case'].status == Case.STATUS_GOAL:
                    lab.board[actual_coordinates['x']][actual_coordinates['y']].status = f"{player.steps}"

                    player.path.append(actual_coordinates)
                    player.move_to(case['coordinates'])
                    player.path.append(player.get_coordinates())
                
                    lab.show(player)
                    print('Finished!')
                    print('Path: ' + ', '.join([f"({coords['x']}, {coords['y']})" for coords in player.path]))
                    return input('Press Enter to continue...\n')
            
            if forward_case['case'].status != Case.STATUS_WALL and forward_case['coordinates'] not in player.visited:
                player.visited.append(actual_coordinates)
                player.path.append(actual_coordinates)
                tries = 0

                lab.board[actual_coordinates['x']][actual_coordinates['y']].status = f"{player.steps}"
                player.move_to(forward_case['coordinates'])
            elif tries != 3:
                    player.change_direction()

                    tries += 1
            else:
                if actual_coordinates not in player.visited:
                    player.visited.append(actual_coordinates)

                lab.board[actual_coordinates['x']][actual_coordinates['y']].status = f"{player.steps}"
                player.go_backwards()
                tries = 0
                
        except KeyboardInterrupt:
            exit()