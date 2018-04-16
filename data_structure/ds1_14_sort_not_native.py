# sort a customized class
# lambda or operator.attrgetter
import operator


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=lambda u: u.user_id))

sorted(users, key=operator.attrgetter('user_id'))
