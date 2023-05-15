from django.core.mail import send_mail 

def send_activation_code(email, activation_code):
    message = f'Вы зарегистрировались на нашем сайте. Пройдите активацию аккаунта \n Код активации: {activation_code}'
    send_mail('Активация аккаунта', message, 'AKA@gmail.com', [email])

def send_change_code(email, activation_code):
    message = f'Для того что бы сбросить пароль, введите этот код \n Код активации: {activation_code}'
    send_mail('Сброс пароля', message, 'aka@gmail.com', [email])