from models import Player, Labyrinthe, Case

from sys import exit

def resolve(player: Player, lab: Labyrinthe):
    while player.get_coordinates() != lab.get_goal_coordinates():
        try:
            lab.show(player)
            input('Press Enter to continue...\n')

            actual_coordinates = player.get_coordinates()
            if actual_coordinates not in player.visited:
                player.visited.append(actual_coordinates)

            adjacent_cases = player.adjacent_cases(lab)
            if Case.STATUS_GOAL in [case['case'].status for case in adjacent_cases]:
                lab.board[actual_coordinates['x']][actual_coordinates['y']].status = f"{player.steps}"

                player.path.append(actual_coordinates)
                player.move_to(case['coordinates'])
                player.path.append(player.get_coordinates())
            
                lab.show(player)
                print('Finished!')
                print('Path: ' + ', '.join([f"({coords['x']}, {coords['y']})" for coords in player.path]))
                print(f"Path length: {len(player.path)}")
                return input('\nPress Enter to continue...')

            player_moved = False
            for case in adjacent_cases:
                if case['case'].status != Case.STATUS_WALL and case['coordinates'] not in player.visited:
                    player.path.append(actual_coordinates)

                    lab.board[actual_coordinates['x']][actual_coordinates['y']].status = f"{player.steps}"
                    player.move_to(case['coordinates'])
                    player_moved = True
                    break

            if player_moved: continue

            lab.board[actual_coordinates['x']][actual_coordinates['y']].status = f"{player.steps}"
            player.go_backwards()
            player_moved = True
                
        except KeyboardInterrupt:
            exit()