"""c5_9.py"""

FLAG = False
STATUS = (10, 20)
match STATUS:
    case (10, 30):
        print('case 1')
    case (10, 20) if FLAG:
        print('case 2')
    case (10, y):
        print('case 3', y)
    case (x, 20):
        print('case 4', x)
    case _:
        print('case 5')
