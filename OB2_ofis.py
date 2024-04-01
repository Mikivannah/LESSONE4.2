# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень
# доступа и могут добавлять или удалять пользователя из системы.
#
# Требования:
#
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень
# доступа ('user' для обычных сотрудников).
#
# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
#
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).


class User:
    def __init__(self, user_id,name):
        self.user_id = user_id            #    ID пользователя
        self.name = name                  #    имя пользователя
        self.__access_level = 'user'      #    уровень доступа /данные приватные/

    def get_user_id(self):
        return self.user_id

    def get_name(self):
        return self.name

    def get_access_level(self):
        return self.__access_level    #   метод приватный

    def __str__(self):
        return (f" Код ID: {self.user_id},"    
                f" Имя: {self.name},"
                f" Access Level: {self.__access_level}")


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'    #  атрибут приватный /уровень доступа/
        self.__user_list = []            #  атрибут приватный /пользовательский список/

    def add_user(self, user):
        self.__user_list.append(user)

    def remove_user(self, user):
        self.__user_list.remove(user)

    def get_user_list(self,):
        return self.__user_list
    def set_user_list(self, value):
        self.__user_list = value  #дополнительная характеристика


    def __str__(self):
        user_list_str = ', '.join([user.name for user in self.__user_list])
        return (f"Код ID: {self.user_id}, Имя: {self.name},"
                f" Уровень доступа: {self.__access_level},"
                f" Список пользовательй: {user_list_str}")


# Пример использования
user1 = User(1, 'Алиса')
user2 = User(2, 'Владимир')
user3 = User(3, 'Игорь')
user4 = User(4, 'Оксана')
admin = Admin(5, 'Admin')

admin.add_user(user1)    # Добавление пользователя Алиса
admin.add_user(user2)    # Добавление пользователя Владимира
admin.add_user(user3)    # Добавление пользователя Игоря
admin.add_user(user4)    # Добавление пользователя Оксана
admin.remove_user(user2) # Удаления пользователя Владимира
print(admin)
print(user1)
print(admin.get_user_list())


