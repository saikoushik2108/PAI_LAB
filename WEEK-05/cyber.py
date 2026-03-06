# Cybersecurity Attack-Defense Simulation using Minimax (with move sequence)

def minimax(state, depth, is_attacker, attacker_moves, defender_moves):
  
    if depth == 0:
        return state, []

    if is_attacker:
        # Attacker tries to minimize system security
        best_score = float('inf')
        best_sequence = []
        for move in attacker_moves:
            new_state = state + move
            score, sequence = minimax(new_state, depth - 1, False, attacker_moves, defender_moves)
            if score < best_score:
                best_score = score
                best_sequence = [("Attacker", move)] + sequence
        return best_score, best_sequence
    else:
        # Defender tries to maximize system security
        best_score = -float('inf')
        best_sequence = []
        for move in defender_moves:
            new_state = state + move
            score, sequence = minimax(new_state, depth - 1, True, attacker_moves, defender_moves)
            if score > best_score:
                best_score = score
                best_sequence = [("Defender", move)] + sequence
        return best_score, best_sequence


def main():
    print("=== Cybersecurity Attack-Defense Simulation Engine ===\n")

    # Input system parameters
    initial_score = int(input("Enter initial system security score (e.g., 0): "))

    attacker_moves = input("Enter attacker move impacts (comma separated, negative numbers): ")
    attacker_moves = [int(x.strip()) for x in attacker_moves.split(",")]

    defender_moves = input("Enter defender move impacts (comma separated, positive numbers): ")
    defender_moves = [int(x.strip()) for x in defender_moves.split(",")]

    depth = int(input("Enter number of turns to simulate (e.g., 2 or 4): "))

    # Run Minimax simulation
    best_score, move_sequence = minimax(initial_score, depth, False, attacker_moves, defender_moves)

    print("\nOptimal system security score:", best_score)
    print("Move sequence (Defender vs AI Attacker):")
    for turn, (player, move) in enumerate(move_sequence, start=1):
        print(f"Turn {turn}: {player} chooses move impact {move}")


if __name__ == "__main__":
    main()