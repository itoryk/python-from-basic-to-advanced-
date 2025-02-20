from typing import Callable


def check_permission(user: str) -> Callable:
    def decorator(func: Callable):
        def wrapped_func(*args, **kwargs):
            if user in user_permissions:
                func(*args, **kwargs)
            else:
                raise PermissionError(f'У пользователя {user} недостаточно прав, '
                                      f'чтобы выполнить функцию {func.__name__}')

        return wrapped_func

    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


try:
    delete_site()
    add_comment()
except PermissionError as error:
    print(error)
