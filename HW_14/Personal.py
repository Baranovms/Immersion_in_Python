import json

class OwnBasicException(Exception):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class LevelError(OwnBasicException):
    def __init__(self, me, new):
        super(LevelError, self).__init__(f'Ошибка доступа! Служащий ({me.name}, доступ: {me.lvl_access}) '
                                         f'не имеет права создать служащего ({new.name}, доступ: {new.lvl_access}) '
                                         f'выше собственного уровня доступа')


class AccessError(OwnBasicException):
    def __init__(self, me, Employee):
        super(AccessError, self).__init__(f'Ошибка доступа: Служащий {me.name} ({me.employee_id}) не найден в базе!')


class UniqueID(OwnBasicException):
    def __init__(self, new_id: str):
        super(UniqueID, self).__init__(f'Ошибка доступа: Служащий с таким ID ({new_id}) уже существует')


class UserWorkshop:
    user_list = set()

    def __init__(self):
        UserWorkshop.load_users()
        pass


    @staticmethod
    def load_users(path: str = 'users2.json'):
        with open(path, 'r', encoding='UTF-8') as f:
            user_dict = json.load(f)
        for level, user_list in user_dict.items():
            for id, name in user_list.items():
                UserWorkshop.user_list.add(User(name, str(id), str(level)))


    def login(self, name: str, id: str) -> str:
        login_user = User(name, id)
        for user in UserWorkshop.user_list:
            if login_user == user:                 
                return user.level
        else:
            raise AccessError()

    def create_user(self, name: str, id: str, level: str):                    
        cur_name, cur_id = input("Введите имя авторизированного пользователя и его id через пробел").split()        
        if current_level := self.login(cur_name, cur_id):                      
            if int(current_level) > int(level):
                return User(name, id, level)                           
            else:
                raise LevelError(current_level, level)

class User:
    def __init__(self, name: str, user_id: str,  level: str = '0') -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'User: {self.name}, {self.user_id},  {self.level}'

    def __repr__(self):
        return f'User: {self.name}, {self.user_id},  {self.level}'

    def __hash__(self):
        return hash(self.name) + hash(self.user_id)

    def __eq__(self, other):                                                         
        return self.name == other.name and self.user_id == other.user_id
    
if __name__ == '__main__':
     work_group = set()

     def load_users(path: str = 'users2.json'):
         with open(path, 'r', encoding='UTF-8') as f:
             user_dict = json.load(f)
         for level, user_list in user_dict.items():
             for id, name in user_list.items():
                work_group.add(User(name, id, level))


     load_users()
     print(work_group)