from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from db.models import User


def create_user(
        username: str,
        password: str,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
) -> None:
    user = get_user_model()

    if email:
        user.email = email

    if first_name:
        user.first_name = first_name

    if last_name:
        user.last_name = last_name

    user.create_user(
        username=username,
    )

    user.set_password(password)

    user.save()

def get_user(user_id: int) -> User:
    try:
        return get_user_model().objects.get(pk=user_id)
    except ObjectDoesNotExist:
        return None


def update_user(
        user_id: int,
        username: str = None,
        password: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
) -> None:
    user = get_user(user_id)

    if username:
        user.username = username

    if email:
        user.email = email

    if first_name:
        user.first_name = first_name

    if last_name:
        user.lastname = last_name

    if password:
        user.set_password(password)

    user.save()