# def tower_of_hanoi(n, source='A', auxiliary='B', destination='C'):
#     """Solve Tower of Hanoi puzzle with n disks."""
#     moves = []
    
#     def solve(n, src, aux, dst):
#         if n == 1:
#             moves.append(f"Move disk 1 from {src} → {dst}")
#         else:
#             solve(n-1, src, dst, aux)
#             moves.append(f"Move disk {n} from {src} → {dst}")
#             solve(n-1, aux, src, dst)
    
#     solve(n, source, auxiliary, destination)
#     return moves

# def tower_of_hanoi(n, source='A', auxiliary='B', destination='C'):
#     moves = []
#     def solve(n, src, aux, dst):
#         if n:
#             solve(n-1, src, dst, aux)
#             moves.append(f"Move disk {n} from {src} → {dst}")
#             solve(n-1, aux, src, dst)
#     solve(n, source, auxiliary, destination)
#     return moves

# num_disks = 3
# moves = tower_of_hanoi(num_disks)
# print("\n".join(moves))
# print(f"\nTotal Moves: {len(moves)}")

def twh(n,source = "A",auxilary = "B",destination = "C"):
    moves = []
    def solve(n,src,aux,dest):
        if n == 1:
            moves.append(f"Move disk 1 from {src} -> {dest}")
        else:
            solve(n-1,src,dest,aux)
            moves.append(f"Move disk {n} from {src} -> {dest}")
            solve(n-1,aux,src,dest)
    
    solve(n,source,auxilary,destination)
    return moves

no = 3
moves = twh(no)
print(f"\n".join(moves))
print(f"\nTotsl moves: {len(moves)}")
