import sys
import io
from contextlib import redirect_stdout

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

with redirect_stdout(io.StringIO()):
    import solver as sv
    import cubie as cb


def main():
    if len(sys.argv) != 2:
        print('Usage: ./nissy2x2 "scramble"')
        sys.exit(1)

    cube = cb.CubieCube()

    for move in sys.argv[1].split():
        face = move[0]

        if face not in "URF":
            print(f"Error: invalid move: {move}")
            sys.exit(1)

        base = {"U": 0, "R": 3, "F": 6}

        if len(move) == 1:
            turns = 1
        elif move[1] == "2":
            turns = 2
        elif move[1] == "'":
            turns = 3
        else:
            print(f"Error: invalid move: {move}")
            sys.exit(1)

        for _ in range(turns):
            cube.multiply(cb.moveCube[base[face]])

    solution = sv.solve(cube.to_facelet_cube().to_string())

    moves = solution.split("(")[0].split()
    output = []

    for move in moves:
        face = move[0]
        turn = move[1]

        if turn == "1":
            output.append(face)
        elif turn == "2":
            output.append(face + "2")
        elif turn == "3":
            output.append(face + "'")

    print(f"{' '.join(output)} ({len(output)})")


if __name__ == "__main__":
    main()

