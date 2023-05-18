from typing import NamedTuple

from django.http import QueryDict


class DataForRegisterUser(NamedTuple):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.username} {self.email} {self.password}'


class DataForLoginUser(NamedTuple):
    username: str
    password: str

    def __str__(self):
        return f'{self.username} {self.password}'


def get_data_for_register(data: QueryDict) -> DataForRegisterUser:
    """
    Function for getting data from QueryDict and return DataForRegisterUser

    :param data: QueryDict
    :return: DataForRegisterUser
    """

    return DataForRegisterUser(
        first_name=data.get('full_user_name').split(' ')[0],
        last_name=data.get('full_user_name').split(' ')[1],
        username=data.get('username'),
        email=data.get('email_user'),
        password=data.get('password_user')
    )


def get_data_for_login(data: QueryDict) -> DataForLoginUser:
    """
    Function for getting data from QueryDict and return DataForLoginUser

    :param data: QueryDict
    :return: DataForLoginUser
    """

    return DataForLoginUser(
        username=data.get('username'),
        password=data.get('password')
    )
