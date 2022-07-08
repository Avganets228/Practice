
import smtplib

from password import password



addresses = []

my_filet = '/home/priceman/priceDil.txt';
with open(my_filet) as f:
    for line in f:
        addresses.append([line for line in line.split()])


def send_mail(addresses):
    email_getter = ''
    if addresses = []:
        return 0
    for i in range(len(addresses) + 1):
        email_getter = addresses[i]
    return email_getter




email_sender = 'priceman@tayle.ru'
email_getter = send_mail(addresses)


smtp_server = smtplib.SMTP(smtp.tayle.ru, 465)
smtp_server.starttls()

smtp_server.login(email_sender, password)



my $message = Mail::Internet -> new([ <>]);  # Получение письма

exit 69 if ($message->get(From) !~ /\@tayle\.com |\@tayle\.ru /);  # service unavailable if sent not from test.net domain

my $filet = '/home/priceman/priceDil.txt';  # файл со списком адресов

open(RCPT,, $filet)

or die "File not '$filet' found $!";  # get recipients from file which name based on Subject string



# Не понял часть, которая закоментирована, как связать получение и отправку письма

while mail in RCPT:
    message.replace('To', "$bcc");  # empty To field
    message.replace('Cc', "");  # empty Cc field
    message.replace('From', "Tayle <priceman\@tayle.ru>")
    message.replace('Sender', "Tayle <priceman\@tayle.ru>")
    message.replace('Bcc', "");  # put all recipients to Bcc field
    message.replace('Subject', message.get(Subject))  # replace Subject field
    message.replace('X-Original-To', "priceman\@tayle.ru")
    message.replace('Delivered-To', "priceman\@tayle.ru")
    message.smtpsend()  # send this shit

sleep(5)

close(RCPT)
