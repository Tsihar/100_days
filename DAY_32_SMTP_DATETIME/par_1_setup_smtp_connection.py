import smtplib

gmail_login = "appbrewery87@gmail.com"
gmail_password = "746681app"
gmail_app_password = "rtqw vcqi bxbn ebvr"

yahoo_mail = "app_brewery@yahoo.com"
yahoo_password = "7789987798"


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # работаем через with, чтобы закрывать соединение сразу после отправки сообщения
    connection.starttls()  # tls используется, чтобы секьюрно 1(шифрованно отправляются сообщения) установить соединением с smtp сервером
    connection.login(user=gmail_login, password=gmail_app_password)
    connection.sendmail(
        from_addr=gmail_login,
        to_addrs=yahoo_mail,
        msg="Subject:My subject\n\nMy mail body.")  # формат сообщения с темой и телом сообщения

