from security.model.model import Users


class UserRepository:

    @staticmethod
    async def save_users(engine, users: Users):
        return await engine.save(users)

    @staticmethod
    async def find_users(engine, users: Users):
        return await engine.find_one(Users, Users.name == users.first_name)

    @staticmethod
    async def get_user(engine, username):
        return await engine.find_one(Users, Users.username == username)

    @staticmethod
    async def get_user_by_email(engine, email):
        return await engine.find_one(Users,
                                     Users.email == email)

    @staticmethod
    async def create_user(engine, users):
        return await engine.save(users)
