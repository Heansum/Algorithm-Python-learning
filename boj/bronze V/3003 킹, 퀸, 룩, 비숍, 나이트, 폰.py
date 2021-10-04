king, queen, rook, bishop, knight, pawn = input().split(' ')

king = int(king)
queen = int(queen)
rook = int(rook)
bishop = int(bishop)
knight = int(knight)
pawn = int(pawn)

king = 1 - king
queen = 1 - queen
rook = 2 - rook
bishop = 2 - bishop
knight = 2 - knight
pawn = 8 - pawn

print(king, queen, rook, bishop, knight, pawn, sep=' ')