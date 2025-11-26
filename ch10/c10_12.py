"""c10_12.py"""

S = "user_account"
print(S, S.isidentifier())

S = "user_100"
print(S, S.isidentifier())

S = "100_user"
print(S, S.isidentifier())
