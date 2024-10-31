class UserService:
    def __init__(self, user_repo, log_repo):
        self.user_repo = user_repo
        self.log_repo = log_repo


    def get_all(self):
       users = self.user_repo.get_all()
       # self.log_repo.log(users)
       return users