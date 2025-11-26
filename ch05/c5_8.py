"""c5_8.py"""

STATUS = 401
match STATUS:
    case 400:
        print("Bad request")
    case 401:
        print("Unauthorized")
    case 403:
        print("Forbidden")
    case 404:
        print("Not found")
    case _:
        print("Something is wrong")
