# inheritance and polymorphism
# 1- inheritance


class UserActions:
    userName = ''
    password = ''

    def __init__(self, uname, password):
        self.userName = uname
        self.password = password

    def login(self):
        print('login with cradentials ', self.userName + ', ', self.password)


class FbUserAction(UserActions):

    def login(self):
        print('login with FB cradentials ', self.userName + ', ', self.password)

"""
# uncomment these lines to execute the example
u1 = UserActions('amr', '123')
u1.login()
print('\n')
u2 = FbUserAction('amrfb', 'fb123')
u2.login()
"""

# 2- polymorphism
# the fblogin function expecting a FBUserAction object and a UserAction object
# was passed


def fblogin(FbUserAction):
    FbUserAction.login()

u = UserActions('amr', 'mohamed')
fblogin(u)
