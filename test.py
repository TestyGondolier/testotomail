import smtplib
from email.mime.text \
import MIMEText

smtpadresi = "smtp.google.com"
smtpport = 587
kullaniciadi = "live.instagramcenter@gmail.com"
sifre = "fros3131"

gonderilecekadres = ["eneskaym34@gmail.com"]
konu = ("Verify Badges")
icerik = C:\Users\Testy\Desktop\testt.html
mail = MIMEText(icerik, "html", "utf-8")
mail["From"] = "Instagram"
mail["Subject"] = "Verify Badges"
mail["To"] = ",".join(gonderilecekadres)

mail = mail.as_string()

print("Lütfen bekleyiniz. Mail gönderiliyor..")

s = smtplib.SMTP(smtp.google.com,587)
s.starttls()
s.login(kullaniciadi, sifre)
s.sendmail(kullaniciadi, gonderilecekadres, mail)
print("Mail gönderildi.")
