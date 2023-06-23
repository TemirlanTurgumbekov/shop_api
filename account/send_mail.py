from django.core.mail import send_mail


HOST = '127.0.0.1:8000'


def send_confirmation_email(user, code):
    link = f'http://{HOST}/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт!',
        f'Чтобы активировать ваш аккаунт нужно перейти по ссылке ниже: '
        f'\n{link}'
        f'\nСсылка работает один раз!',
        'tturgum5ekov@gmail.com',
        [user],
        fail_silently=False,
    )
