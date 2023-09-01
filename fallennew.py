import telebot
import random
import json
import telegram
import requests
from telebot import TeleBot
import time
from telebot import types
import os
from enum import Enum
import uuid
from datetime import datetime, timedelta


 
bot = telebot.TeleBot("6086089724:AAEOShd8YmARkpjgJcelI1GKSxgpXlprR3A")




print("BOT ÇALIŞIYOR"
print("Fallen PROJECT 2.5 </>;")


destek_ID = 5638708289

# Bot sahibinin keyi
bot_password = "adm1nfallen"

#logged_in_users = [1288968123, 6109533276, 1820192566, 6273291829, 2082436453, 5131340769, 5145867434, 1591960734, 5569718615] # Giriş yapmış kullanıcıların ID Listesi


def load_logged_in_users():
    with open("logged_in_users.txt", "r") as file:
        logged_in_users = [int(line.strip()) for line in file]
    return logged_in_users




@bot.message_handler(commands=['info'])
def user_info(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    lastname = message.from_user.last_name
    is_bot = message.from_user.is_bot
    username = message.from_user.username
    kullanici = message.from_user.first_name
    
    # /info komutunu yanıt aldığında
    if message.reply_to_message:
        replied_user_id = message.reply_to_message.from_user.id
        replied_user_firstname = message.reply_to_message.from_user.first_name
        replied_user_lastname = message.reply_to_message.from_user.last_name
        replied_user_username = message.reply_to_message.from_user.username
        replied_user_is_bot = message.reply_to_message.from_user.is_bot
        
        bot.reply_to(message, f"*Kullanıcı bilgisi:*\n\n*Kimlik:* `{replied_user_id}`\n*Adı: {replied_user_firstname}*\n*Soyadı: {replied_user_lastname}*\n*Kullanıcı Adı:* @{replied_user_username}\n*Bot mu?:* `{replied_user_is_bot}`", parse_mode="Markdown")
    # /info <ID> veya /info <Kullanıcı-Adı> komutunu aldığında
    elif len(message.text.split()) > 1:
        user_id_or_username = message.text.split()[1]
        
        # /info <ID> komutunu aldığında
        if user_id_or_username.isdigit():
            try:
                user = bot.get_chat_member(chat_id, int(user_id_or_username)).user
                user_id = user.id
                user_firstname = user.first_name
                user_lastname = user.last_name
                user_username = user.username
                user_is_bot = user.is_bot
                
                bot.reply_to(message, f"*Kullanıcı bilgisi:*\n\n*Kimlik:* `{user_id}`\n*Adı: {user_firstname}*\n*Soyadı: {user_lastname}*\n*Kullanıcı Adı:* @{user_username}\n*Bot mu?:* `{user_is_bot}`", parse_mode="Markdown")
            except Exception as e:
                bot.reply_to(message, "Geçersiz kullanıcı kimliği!")
        
        # /info <Kullanıcı-Adı> komutunu aldığında
        else:
            try:
                user = bot.get_chat_member(chat_id, user_id_or_username).user
                user_id = user.id
                user_firstname = user.first_name
                user_lastname = user.last_name
                user_username = user.username
                user_is_bot = user.is_bot
                
                bot.reply_to(message, f"*Kullanıcı bilgisi:*\n\n*Kimlik:* `{user_id}`\n*Adı: {user_firstname}*\n*Soyadı: {user_lastname}*\n*Kullanıcı Adı:* @{user_username}\n*Bot mu?:* `{user_is_bot}`", parse_mode="Markdown")
            except Exception as e:
                bot.reply_to(message, "Geçersiz bir kullanıcı adı!")
    # /info komutunu aldığında
    else:
        bot.reply_to(message, f"*Kullanıcı bilgisi:*\n\n*Kimlik:* `{user_id}`\n*Adı: {kullanici}*\n*Soyadı: {lastname}*\n*Kullanıcı Adı:* @{username}\n*Bot mu?:* `{is_bot}`\n*Chat ID:* `{chat_id}`", parse_mode="Markdown")
        



@bot.message_handler(commands=['id'])
def chat_info(message):
    chat_id = message.chat.id
    username = message.from_user.username
    
    # /id komutunu yanıt aldığında
    if message.reply_to_message:
        replied_user_id = message.reply_to_message.from_user.id
        bot.reply_to(message, f"Kullanıcı ID'si: `{replied_user_id}`", parse_mode="Markdown")
    
    # /id <Kullanıcı-Adı> komutunu aldığında
    elif len(message.text.split()) > 1:
        user_username = message.text.split()[1]
        
        try:
            user = bot.get_chat_member(chat_id, user_username).user
            user_id = user.id
            bot.reply_to(message, f"{user_username} kullanıcısının ID'si: `{user_id}`", parse_mode="Markdown")
        except Exception as e:
            bot.reply_to(message, "Geçersiz bir kullanıcı adı!")
    
    # /id komutunu aldığında
    else:
        bot.reply_to(message, f"Bu grubun ID'si: `{chat_id}`", parse_mode="Markdown")
        

    

@bot.message_handler(commands=['cevap'])
def handle_cevap(message):
    chat_type = message.chat.type
    if chat_type == "private": # Sadece özel sohbetlerde geçerli
        user_id = message.from_user.id
        kullanici = f"[{message.from_user.first_name}](tg://user?id={user_id})" # Kullanıcı profili

        # Hata formatını kontrol etmek için gerekli kodu buraya ekleyin
        hata_formati = message.text.split()[1:]

        if len(hata_formati) < 1: # En az 1 parametre gerekiyor
            bot.reply_to(message, "Hatalı format girdiniz. Lütfen /cevap <Mesaj> şeklinde kullanın.")
            return

        hata_mesaji = ' '.join(hata_formati) # Hata mesajını bir metin haline getirin

        # Hata mesajını bizim_IDmiz'e gönderin
        bot.send_message(destek_ID, f"Kullanıcı Adı: {kullanici}\nID : `{user_id}`\nHata Mesajı: {hata_mesaji}", parse_mode="Markdown")

        bot.reply_to(message, "Hata mesajınız gönderildi.") # Kullanıcıya geri bildirim gönderin
        


# Sorgu mesajı
sorgu_text = "Lütfen Bağış Yöntemini Seçin!"
markup = types.InlineKeyboardMarkup()
adsoyad_button = types.InlineKeyboardButton("İninal", callback_data="adsoyad")
markup.row(adsoyad_button)

@bot.message_handler(commands=['odeme'])
def handle_sorgu(message):
    bot.send_message(message.chat.id, sorgu_text, reply_markup=markup)


# butonlara yetki verelim 
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "adsoyad":
            # random Şifre oluştursun
            new_password = ''.join(random.choice('QWqwErRTyUiİOPpASsDfGMYHKZCBhJkLzXcVbNm29427389') for i in range(8))
            global bot_password
            bot_password = new_password
            bot.send_message(call.message.chat.id, f"*1445155626379 İninal Adresine Bağış Yapabilirsiniz!*", parse_mode="Markdown")	          


premium_users_file = 'logged_in_users.txt'


@bot.message_handler(commands=['start'])
def check_membership(message):
    user_id = message.from_user.id
    if is_premium_user(user_id):
        kullanici = f"{message.from_user.first_name}"
        markup = telebot.types.InlineKeyboardMarkup(row_width=3)
        btn_chat = telebot.types.InlineKeyboardButton('Sohbet-e Git  🔎', url='https://t.me/PrimordialTr')
        btn_kanal = telebot.types.InlineKeyboardButton('Kanal-a Git  🚀', url='https://t.me/JazeProject')
        btn_destek = telebot.types.InlineKeyboardButton('Destek  🧑‍💻', url='https://t.me/Yakupisyanedior')    	
        btn_grub = telebot.types.InlineKeyboardButton('➕ Gruba Ekle ➕', url='http://t.me/FallenSorguBot?startgroup=start')
        markup.add(btn_chat, btn_kanal, btn_grub, btn_destek)
        bot.reply_to(message, f"╠══════════════╣\n║*Merhaba: {kullanici}* \n║(`{user_id}`) *Nasılsın?*\n╠══════════════╣\n║*Üyelik:* `Premium`\n╠══════════════╣\n║*Premium Özelikler 👇*\n╠══════════════╣\n║/sorgu *-isim Roket -soyisim Atar -il \n║Bursa -ilce OsmanGazi*\n╠══════════════╣\n║/aile *T.C'den Aile Sorgu Atar*\n╠══════════════╣\n║/tckn *T.C Sorgu Yapar*\n╠══════════════╣\n║/gsmtc *GSM'den T.C Çıkarır*\n╠══════════════╣\n║/tcgsm *T.C'den GSM Çıkarır*\n╠══════════════╣\n║/plaka *Plaka'dan Kişi Bilgileri Arac Bilgileri Verir*\n╠══════════════╣\n║/index *<URL>'dan Sitenin indexini \n║Çeker*\n╠══════════════╣\n║/hava *<Şehir> İL'e Göre Hava \n║Sıcaklığı verir*\n╠══════════════╣\n║/tgsorgu *<ID> ID'den Numara \n║Çıkarır*\n╠══════════════╣\n║/adres *T.C'den 2015 Adres Çıkarır*\n╠══════════════╣\n║/ip *IP'den IP Bilgileri Çıkarır*\n╠══════════════╣\n║/ddos *-host https://example.com \n║-port 443*\n╠══════════════╣\n║/sms *GSM'ye Sms Saldırısı Yapar*\n╠══════════════╣\n\n*Yardım Ve Destek Ekibi İle görüşmek istiyorsan /cevap <Mesaj> Girebilirsin\n\nKomutlar Hakkında Yardım almak istiyorsan\n/yardim <Komut> Girin\n\nBağış Yapmak için\n/odeme Komutunu Kullanabilirsiniz!*", reply_markup=markup, parse_mode="Markdown")
    else:
        kullanici = f"{message.from_user.first_name}"
        markup = telebot.types.InlineKeyboardMarkup(row_width=3)
        btn_chat = telebot.types.InlineKeyboardButton('Sohbet-e Git  🔎', url='https://t.me/PrimordialTr')
        btn_kanal = telebot.types.InlineKeyboardButton('Kanal-a Git  🚀', url='https://t.me/JazeProject')
        btn_destek = telebot.types.InlineKeyboardButton('Destek  🧑‍💻', url='https://t.me/Yakupisyanedior')    	
        btn_grub = telebot.types.InlineKeyboardButton('➕ Gruba Ekle ➕', url='http://t.me/FallenSorguBot?startgroup=start')
        markup.add(btn_chat, btn_kanal, btn_grub, btn_destek)
        bot.reply_to(message, f"╠══════════════╣\n║*Merhaba: {kullanici}* \n║(`{user_id}`) *Nasılsın?*\n╠══════════════╣\n║*Üyelik:* `Freemium`\n╠══════════════╣\n║*Freemium Özelikler 👇*\n╠══════════════╣\n║/sorgu *-isim Roket -soyisim Atar -il \n║Bursa -ilce OsmanGazi*\n╠══════════════╣\n║/aile *T.C'den Aile Sorgu Atar*\n╠══════════════╣\n║/tckn *T.C Sorgu Yapar*\n╠══════════════╣\n║/gsmtc *GSM'den T.C Çıkarır*\n╠══════════════╣\n║/tcgsm *T.C'den GSM Çıkarır*\n╠══════════════╣\n║/plaka *Plaka'dan Kişi Bilgileri Arac Bilgileri Verir*\n╠══════════════╣\n║/index *<URL>'dan Sitenin indexini \n║Çeker*\n╠══════════════╣\n║/hava *<Şehir> İL'e Göre Hava \n║Sıcaklığı verir*\n╠══════════════╣\n║/tgsorgu *<ID> ID'den Numara \n║Çıkarır*\n╠══════════════╣\n║/iban *İban'dan Adres Vb Bilgiler Çıkarır*\n╠══════════════╣\n║/ip *IP'den IP Bilgileri Çıkarır*\n╠══════════════╣\n║/ddos *-host https://example.com \n║-port 443*\n╠══════════════╣\n║/sms *GSM'ye Sms Saldırısı Yapar*\n╠══════════════╣\n\n*Yardım Ve Destek Ekibi İle görüşmek istiyorsan /cevap <Mesaj> Girebilirsin\n\nKomutlar Hakkında Yardım almak istiyorsan\n/yardim <Komut> Girin\n\nBağış Yapmak için\n/odeme Komutunu Kullanabilirsiniz!*", reply_markup=markup, parse_mode="Markdown")
        

def is_premium_user(user_id):
    with open(premium_users_file, 'r+') as file:
        premium_users = [line.strip() for line in file.readlines()]
        if str(user_id) in premium_users:
            return True
        else:
            return False





from bs4 import BeautifulSoup


@bot.message_handler(commands=['site'])
def check_xss(message):
    blocked_users = load_blocked_users()  # is_user_blocked.txt dosyasından engellenen kullanıcı kimliklerini al

    # Engellenmiş kullanıcı kontrolü sağlar
    if message.from_user.id in blocked_users:
        bot.reply_to(message, "╠══════════════╣\n║ Ban_v2.2 ║ Sowix-Yasaklı-Üyesiniz.\n╠══════════════╣\n\n╠══════════════╣\n║ Tebrikler, Yasaklandınız.\n╟ Ödül Olarak: Kendinizi;\n║ Sowix Sisteminden Banlandınız.\n╠══════════════╣")
        return
    try:
        # Bot komutundan URL al
        url = message.text.split(' ')[1]
        
        # HTTP başlıklarını ayarla
        headers = {
            'User-Agent': 'Mozilla',
            'Referer': 'https://www.google.com'
        }
        
        # Web sitesini iste ve HTML'yi analiz et
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # XSS açığı tespit etmek için HTML etiketlerini kontrol et
        dangerous_tags = ['script', 'img', 'iframe', 'a']
        xss_vulnerabilities = []
        for tag in soup.find_all(dangerous_tags):
            xss_vulnerabilities.append(tag)
        
        if len(xss_vulnerabilities) > 0:
            vulnerabilities_message = 'XSS açığı tespit edildi Tespit edilen Yer:\n\n'
            for vuln in xss_vulnerabilities:
                vulnerabilities_message += '\n- ' + str(vuln)
            bot.reply_to(message, vulnerabilities_message)
        else:
            bot.reply_to(message, 'XSS açığı Bulunamadı!.')
    
    except IndexError:
        bot.reply_to(message, 'Geçerli bir web sitesi URL\'si girmelisiniz.')
    
    except Exception as e:
        bot.reply_to(message, 'Bir hata oluştu: {}'.format(str(e)))
        


@bot.message_handler(commands=['penis'])
def penis_size(message):
    
    blocked_users = load_blocked_users()  # is_user_blocked.txt dosyasından engellenen kullanıcı kimliklerini al

    # Engellenmiş kullanıcı kontrolü sağlar
    if message.from_user.id in blocked_users:
        bot.reply_to(message, "╠══════════════╣\n║ Ban_v2.2 ║ Fallen-Yasaklı-Üyesiniz.\n╠══════════════╣\n\n╠══════════════╣\n║ Tebrikler, Yasaklandınız.\n╟ Ödül Olarak: Kendinizi;\n║ Fallen Sisteminden Banlandınız.\n╠══════════════╣")
        return
        
    try:
        query = message.text.strip().split(' ')
        if len(query) != 2 or len(query[1]) != 11:
            bot.reply_to(message, "Geçersiz format! Lütfen 11 haneli bir T.C. numarası girerek tekrar deneyin.")
            return
        penis_length = random.choice([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44])
        penis_unit = 'CM'
        bot.reply_to(message, f"T.C {query[1]}\n\nPenis Boyu: {penis_length}{penis_unit}")
    except IndexError:
        bot.reply_to(message, "Hatalı format! Doğru şekilde kullanın: /penis T.C")
    except Exception as e:
        bot.reply_to(message, f"Bir hata oluştu: {str(e)}")
        




@bot.message_handler(commands=['yardim'])
def help_message(message):
    blocked_users = load_blocked_users()  # is_user_blocked.txt dosyasından engellenen kullanıcı kimliklerini al

    # Engellenmiş kullanıcı kontrolü sağlar
    if message.from_user.id in blocked_users:
        bot.reply_to(message, "╠══════════════╣\n║ Ban_v2.2 ║ Fallen-Yasaklı-Üyesiniz.\n╠══════════════╣\n\n╠══════════════╣\n║ Tebrikler, Yasaklandınız.\n╟ Ödül Olarak: Kendinizi;\n║ Fallen Sisteminden Banlandınız.\n╠══════════════╣")
        return
        
    try:
        command = message.text.split(' ', 1)[1]
    except IndexError:
        bot.reply_to(message, "Hatalı format girdiniz. Lütfen /yardim <Komut> şeklinde girin.\n\nÖrnek: /yardim sorgu")
        return

    help_message = ""
    if command == "sorgu":
        help_message = "/sorgu *-isim * -soyisim * -il * -ilce *\n\n * Simgeli Yerlere Bilgileri Girin.*"
    elif command == "gsmtc":
        help_message = "/gsmtc *Numara Giriniz!.\n\nÖrnek: /gsmtc 5553723339*"
    elif command == "tcgsm":
        help_message = "/tcgsm *T.C Giriniz!.\n\nÖrnek: /tcgsm 11111111110*"
    elif command == "ddos":
        help_message = "/ddos *-host * -port *\n\n* Simgeli Yerlere Bilgileri Girin!.*"
    elif command == "tckn":
        help_message = "/tckn *T.C Giriniz\nT.C yazan yere kişinin T.C Kimlik Numarasını Girin!.*"
    else:
        bot.reply_to(message, f"(`{command}`) için yardım mesajı bulunamadı.", parse_mode="Markdown")
        return

    bot.reply_to(message, help_message, parse_mode="Markdown")
    print(str(e))

admins = [5638708289]
admin_file = "admins.txt"

# Admin listesini bir dosyadan yükleme
def load_admins():
    with open(admin_file, "r") as file:
        for line in file:
            admins.append(int(line.strip()))

# Admin listesini bir dosyaya kaydetme
def save_admins():
    with open(admin_file, "w") as file:
        for admin in admins:
            file.write(str(admin) + "\n")

# Yeni admin ekleme komutu

import datetime



@bot.message_handler(commands=['adminekle'])
def add_admin(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    command_parts = message.text.split(" ")

    # Sadece mevcut adminler yeni admin ekleyebilir
    if user_id in admins:
        if len(command_parts) == 3:
            admin_to_add = int(command_parts[1])
            admin_duration = int(command_parts[2])
            
            # Yeni admini eklemek için kullanıcı kimliğini ve bitiş süresini kaydet
            admins.append(admin_to_add)
            save_admins()  # Yeni admini dosyaya kaydet
            
            bot.send_message(chat_id, f"*Yeni admin eklendi! Admin süresi: {admin_duration} gün*", parse_mode="Markdown")
            
            # Belirtilen gün sayısını datetime.timedelta ile hesaplayın
            admin_end_date = datetime.datetime.now() + datetime.timedelta(days=admin_duration)
            
            # Admin süresi sonunda admini kaldır
            def remove_admin():
                admins.remove(admin_to_add)
                save_admins()
                bot.send_message(chat_id, "*Admin süresi sona erdi. Admin yetkileri kaldırıldı.*", parse_mode="Markdown")
            
            timer = threading.Timer(admin_duration * 24 * 60 * 60, remove_admin)
            timer.start()
        else:
            bot.send_message(chat_id, "*Yanlış komut formatı. Doğru kullanım: /adminekle <ID> <Süre>*", parse_mode="Markdown")
    else:
        bot.send_message(chat_id, "*Bu komutu kullanmaya yetkiniz yok! ⛔*", parse_mode="Markdown") 
        

@bot.message_handler(commands=['adminsil'])
def remove_admin(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    command_parts = message.text.split(" ")

    # Sadece mevcut adminler admini kaldırabilir
    if user_id in admins:
        if len(command_parts) == 2:
            admin_to_remove = command_parts[1]

            # Admini listeden kaldır
            if admin_to_remove in admins:
                admins.remove(admin_to_remove)
                save_admins()
                bot.send_message(chat_id, "*Adminlik Silindi!*", parse_mode="Markdown")
            else:
                bot.send_message(chat_id, "*Böyle bir admin bulunamadı!*", parse_mode="Markdown")
                
            return  # Komut işlendikten sonra fonksiyondan çık
        else:
            bot.send_message(chat_id, "*Yanlış komut formatı. Doğru kullanım: /adminsil <ID>*", parse_mode="Markdown")
    else:
        bot.send_message(chat_id, "*Bu komutu kullanmaya yetkiniz yok! ⛔*", parse_mode="Markdown")
        

# Komutlara genel erişimi kontrol etmek için decorator
def admin_only(func):
    def wrapper(message):
        user_id = message.from_user.id
        
        # Sadece adminlere erişime izin ver
        if user_id in admins:
            func(message)
        else:
            bot.send_message(message.chat.id, "*Bu komutu kullanmaya yetkiniz yok! ⛔*", parse_mode="Markdown")
            
    return wrapper
    
        


@bot.message_handler(commands=['admin'])
@admin_only
def test_command(message):
    user_id = message.from_user.id
    kullanici = f"{message.from_user.first_name}"
    bot.send_message(message.chat.id, f"Merhaba, *Admin {kullanici}* (`{message.from_user.id}`)\n\n*Admin Komutları 👇*\n\n/format Tüm Kullanıcıları Siler\n/uyekle Üyelik Tanımlar\n/liste Kullanıcı Listesi Verir\n/uyesil Üyelik Siler\n/uzaban Kullanıcı Yasaklar\n/uzban Kullanıcı Yasağı Kaldırır", parse_mode="Markdown")
    


@bot.message_handler(commands=['cevapla'])
@admin_only
def cevapla(message):
    user_id = message.from_user.id

    if int(user_id) == destek_ID:
        message_params = message.text.split()

        if len(message_params) < 3: # En az 3 parametre gerekiyor
            bot.reply_to(message, "*Hatalı format girdiniz. Lütfen /cevapla <ID> <Mesaj> şeklinde kullanın.*", parse_mode="Markdown")
            return

        gonderliecek_kisi = message_params[1]
        gonderilecek_mesaj = " ".join(message_params[2:])

        try:
            bot.send_message(gonderliecek_kisi, f"Cevap: {gonderilecek_mesaj}")
            bot.reply_to(message, "Mesaj gönderildi. ✅")
        except:
            bot.reply_to(message, "Mesaj gönderilemedi. ❌")
            



@bot.message_handler(commands=['plaka'])
def handle_plaka(message):
    blocked_users = load_blocked_users()  # is_user_blocked.txt dosyasından engellenen kullanıcı kimliklerini al

    # Engellenmiş kullanıcı kontrolü sağlar
    if message.from_user.id in blocked_users:
        bot.reply_to(message, "╠══════════════╣\n║ Ban_v2.2 ║ Fallen-Yasaklı-Üyesiniz.\n╠══════════════╣\n\n╠══════════════╣\n║ Tebrikler, Yasaklandınız.\n╟ Ödül Olarak: Kendinizi;\n║ Fallen Sisteminden Banlandınız.\n╠══════════════╣")
        return
    try:
        plaka = message.text.split()[1]

        response = requests.get(f"APİ GİR!")

        if response.status_code == 200:
            data = response.json()

            mukellef = data['data']['mukellef_bilgileri']
            arac = data['data']['arac_bilgileri']
            tescil_vd = data['data']['tescil_vd_bilgileri']

            result = f"╭─━━━━━━━━━━━━━─╮\n┃Plaka: {arac['plaka']}\n"
            result += f"┃Marka: {arac['marka']}\n"
            result += f"┃Model: {arac['model']}\n"
            result += f"┃Tip: {arac['tip']}\n"
            result += f"┃Sahip Bilgileri:\n"
            result += f"┃Ad: {mukellef['ad']}\n"
            result += f"┃Soyad: {mukellef['soyad']}\n"
            result += f"┃TCKNO: {mukellef['tckno']}\n"
            result += f"┃Şirket Türü: {mukellef['sirketturu']}\n"
            result += f"┃Şirket Unvanı: {mukellef['unvan']}\n"
            result += f"┃Baba Adı: {mukellef['babaadi']}\n"
            result += f"┃Vergi No: {mukellef['vergino']}\n"
            result += f"┃Vergi Dairesi Adı: {tescil_vd['vdadi']}\n"
            result += f"┃Vergi Dairesi Telefon: {tescil_vd['vdtelno1']}\n"
            result += f"┃Vergi Dairesi Fax: {tescil_vd['vdfaxno1']}\n╰─━━━━━━━━━━━━━─╯"

            bot.reply_to(message, result)
        else:
            bot.reply_to(message, "API'den geçerli bir yanıt alınamadı.")
    except IndexError:
        bot.reply_to(message, "Geçerli bir plaka numarası girin\n\nÖrnek: /plaka <Plaka> Giriniz")
    except Exception as e:
        bot.reply_to(message, f"Plaka Ait Bir bilgi Bulunamadı")




@bot.message_handler(commands=['uzaban'])
@admin_only
def ban_user(message):
    parameters = message.text.split()
    if len(parameters) >= 3:
        user_id = parameters[1]
        mesaj = ' '.join(parameters[2:]) # Mesajdaki tüm boşlukları korumak için
        try:
            with open("is_user_blocked.txt", "a") as file:
                file.write(str(user_id) + "\n")
            
            # logged_in_users.txt dosyasından ID'yi sil
            with open("logged_in_users.txt", "r") as file:
                lines = file.readlines()
            with open("logged_in_users.txt", "w") as file:
                for line in lines:
                    if line.strip() != str(user_id):
                        file.write(line)
            
            bot.reply_to(message, f"(`Uza_BAN`) *Başarıyla 7 Kahinatının amına postalandı:*\n*ID:* `{user_id}`\n( *Sebep:* `{mesaj}` )", parse_mode="Markdown")
            
            # Banlanan kullanıcıya bildirim gönder
            bot.send_message(user_id, f"(`Uza_BAN`) *Ban Yedin Oruspu Çocuğu*\n( *Sebep:* `{mesaj}` )", parse_mode="Markdown")
        except:
            bot.reply_to(message, "Engelleme işlemi sırasında bir hata oluştu.")
    else:
        bot.reply_to(message, "*Geçersiz komut formatı. /uzaban <kullanıcı_ID> <Sebep>*", parse_mode="Markdown")
        bot.reply_to(message, "*Hatalı Format. <mesaj> girmediniz.*", parse_mode="Markdown")
        



@bot.message_handler(commands=['uzban'])
@admin_only
def unban_user(message): 
    parameters = message.text.split()
    if len(parameters) >= 2:
        user_id = parameters[1]       
        try:
            with open("is_user_blocked.txt", "r") as file:
                lines = file.readlines()
            with open("is_user_blocked.txt", "w") as file:
                found = False
                for line in lines:
                    if line.strip() != str(user_id):
                        file.write(line)
                    else:
                        found = True
            if found:
                bot.reply_to(message, f"( *Kullanıcının Engeli Kaldırıldı* )\n( *ID:* `{user_id}` )", parse_mode="Markdown")
                bot.send_message(user_id, "*Engeliniz kaldırıldı. Artık Komutları Kulanbilirsiniz!.*", parse_mode="Markdown")
            else:
                bot.reply_to(message, "*Bu kullanıcının engeli zaten kaldırılmış.*", parse_mode="Markdown")
        except:
            bot.reply_to(message, "*Engel kaldırma işlemi sırasında bir hata oluştu.*", parse_mode="Markdown")
    else:
        bot.reply_to(message, "*Geçersiz komut formatı. /unban <kullanıcı_ID>*", parse_mode="Markdown")
        bot.reply_to(message, "*Lütfen geçerli bir <ID> giriniz.*", parse_mode="Markdown")
        




from threading import Timer
from datetime import datetime, timedelta


@bot.message_handler(commands=['uyekle'])
@admin_only
def handle_uyeekle(message):
    # Sadece bot sahibi tarafından kullanılabilir

    # ID ve süre bilgisini alalım
    command_parts = message.text.split()
    if len(command_parts) != 3:
        bot.reply_to(message, "Geçersiz komut formatı. Örnek: /uyekle <kullanıcı_ID> <süre>")
        return

    user_id = command_parts[1]
    duration = command_parts[2]

    # logged_in_users.txt dosyasına ID'yi ekle
    with open("logged_in_users.txt", "a") as file:
        file.write(str(user_id) + "\n")

    # Süreyi kontrol et ve süre sonunda listeden kaldır
    if duration.isdigit():
        duration_days = int(duration)
        expiration_date = datetime.now() + timedelta(days=duration_days)

        def remove_user_from_list():
            with open("logged_in_users.txt", "r") as file:
                lines = file.readlines()
            with open("logged_in_users.txt", "w") as file:
                for line in lines:
                    if line.strip() != str(user_id):
                        file.write(line)

        Timer(duration_days * 24 * 60 * 60, remove_user_from_list).start()

        # Kullanıcıya bildirim gönder
        bot.send_message(user_id, f"*Sizin hesabınız {duration} gün boyunca erişime açılmıştır.\nBitiş Tarihi:* `{expiration_date}`", parse_mode="Markdown")

        bot.reply_to(message, f"*Kullanıcı Başarıyla eklendi.\nBitiş Tarihi:* `{expiration_date}`", parse_mode="Markdown")
    else:
        bot.reply_to(message, "*Geçersiz komut formatı.\nLütfen geçerli bir süre giriniz.*", parse_mode="Markdown")
        



@bot.message_handler(commands=['uyesil'])
@admin_only
def uye_sil(message):
    
    parameters = message.text.split()
    if len(parameters) >= 2:
        user_id = parameters[1]
        try:
            with open("logged_in_users.txt", "r") as file:
                lines = file.readlines()
            with open("logged_in_users.txt", "w") as file:
                for line in lines:
                    if line.strip() != str(user_id):
                        file.write(line)
            bot.reply_to(message, f"*Kullanıcı* `{user_id}` *Başarıyla silindi.*", parse_mode="Markdown")
            bot.send_message(user_id, "*Üyeliğiniz silindi. Artık bot'daki Premium Özelikleri Kullanmasınız!.*", parse_mode="Markdown")
        except:
            bot.reply_to(message, "*Kullanıcı silme işlemi sırasında bir hata oluştu.*", parse_mode="Markdown")
    else:
        bot.reply_to(message, "*Geçersiz komut formatı. /uyesil <kullanıcı_ID>*", parse_mode="Markdown")
        bot.reply_to(message, "*Lütfen geçerli bir <ID> giriniz.*", parse_mode="Markdown")




@bot.message_handler(commands=['format'])
@admin_only
def format_files(message):
    
    try:
        # logged_in_users.txt dosyasını temizle
        with open("logged_in_users.txt", "w") as file:
            file.write("")
        
        # is_user_blocked.txt dosyasını temizle
        with open("blocked_users.txt", "w") as file:
            file.write("")
            
        with open("admins.txt", "w") as file:
            file.write("")
        
        bot.reply_to(message, "*Bot Sıfırlandı 🚀*\n*Tüm Üyelikler Silindi 🛡*\n*Tüm Banlılar Silindi ⛔*", parse_mode="Markdown")
    except:
        bot.reply_to(message, "Dosyaların içeriği temizlenirken bir hata oluştu.")
        


# Admin listesini başlat
load_admins()



# OpenWeatherMap API anahtarını buraya girin
API_KEY = "0db3f8408b136206ce52409d715437e8"


@bot.message_handler(commands=['hava'])
def weather(message):
    blocked_users = load_blocked_users()  # is_user_blocked.txt dosyasından engellenen kullanıcı kimliklerini al

    # Engellenmiş kullanıcı kontrolü sağlar
    if message.from_user.id in blocked_users:
        bot.reply_to(message, "╠══════════════╣\n║ Ban_v2.2 ║ Fallen-Yasaklı-Üyesiniz.\n╠══════════════╣\n\n╠══════════════╣\n║ Tebrikler, Yasaklandınız.\n╟ Ödül Olarak: Kendinizi;\n║ Fallen Sisteminden Banlandınız.\n╠══════════════╣")
        return
    
    # Kullanıcının istediği şehir adını alın
    try:
        city = message.text.split(' ', 1)[1]
    except IndexError:
        bot.reply_to(message, "Üzgünüm, hatalı bir format girdiniz. Lütfen /hava <Şehir> şeklinde girin.")
        return

    # Hava durumu API'sini çağır ve verileri al
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        # Hava durumu verilerini al
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        
        # Kullanıcıya hava durumu bilgilerini gönder
        bot.reply_to(message, f"*{city} şehrinde hava durumu: {weather_desc.capitalize()}\nSıcaklık: {temp}°C*", parse_mode="Markdown")
    except:
        bot.reply_to(message, "Hava durumu bilgileri bulunamadı. Lütfen geçerli bir şehir adı girin.")
        
                


def load_blocked_users():
    with open("is_user_blocked.txt", "r") as file:
        blocked_users = [int(line.strip()) for line in file]
    return blocked_users

def is_user_blocked(user_id, blocked_users):
    return user_id in blocked_users

blocked_users = load_blocked_users()
user_id = 123456
is_blocked = is_user_blocked(user_id, blocked_users)




import logging


@bot.message_handler(commands=['index'])
def index(message):
    try:
        site_url = message.text.split(maxsplit=1)[1]
    except IndexError:
        bot.reply_to(message, "Üzgünüm, hatalı bir format girdiniz. Lütfen doğru bir şekilde kullanın.\n\nÖrnek kullanım: /index <site_url>")
        return
    
    if not site_url.startswith("http://") and not site_url.startswith("https://"):
        bot.reply_to(message, "Üzgünüm, hatalı bir format girdiniz.\nLütfen doğru bir şekilde kullanın.\n\nÖrnek kullanım: /index <site_url>")
        return
    
    response = requests.get(site_url)
    
    if response.status_code == 200:
        file_name = "Sowix.php"
        file_content = response.text
        
        with open(file_name, 'w') as file:
            file.write(file_content)
        
        with open(file_name, 'rb') as file:
            bot.send_document(message.chat.id, file)
        
        os.remove(file_name)
    else:
        bot.reply_to(message, "Üzgünüm, bu siteye ait bir index çekilemiyor!")
        


@bot.message_handler(commands=['ip'])
def handle_ip(message):
    blocked_users = load_blocked_users()  # is_user_blocked.txt dosyasından engellenen kullanıcı kimliklerini al

    # Engellenmiş kullanıcı kontrolü sağlar
    if message.from_user.id in blocked_users:
        bot.reply_to(message, "╠══════════════╣\n║ Ban_v2.2 ║ Fallen-Yasaklı-Üyesiniz.\n╠══════════════╣\n\n╠══════════════╣\n║ Tebrikler, Yasaklandınız.\n╟ Ödül Olarak: Kendinizi;\n║ Fallen Sisteminden Banlandınız.\n╠══════════════╣")
        return
    
    # Diğer işlemler devam etsin
    try:
        ip = message.text.split()[1]
        

        response = requests.get(f"http://ip-api.com/json/{ip}").json()

        if response['status'] == 'success':
            result = f"╠══════════════╣\n║ IP Adresi: {response['query']}\n"
            result += f"║ Ülke: {response['country']}\n"
            result += f"║ Ülke Kodu: {response['countryCode']}\n"
            result += f"║ Bölge: {response['regionName']}\n"
            result += f"║ Şehir: {response['city']}\n"
            result += f"║ Posta Kodu: {response['zip']}\n"
            result += f"║ Koordinatlar: ({response['lat']}, {response['lon']})\n"
            result += f"║ Zaman Dilimi: {response['timezone']}\n"
            result += f"║ İnternet Sağlayıcı: {response['isp']}\n"
            result += f"║ Organizasyon: {response['org']}\n"
            result += f"║ AS: {response['as']}\n╠══════════════╣"
            
            bot.reply_to(message, result)
                      
        else:
            bot.reply_to(message, f"╠══════════════╣\n║Girdiğiniz Bilgiler ile Eşleşen Biri ║Bulunamadı! ❌\n╠══════════════╣")
    except IndexError:
        bot.reply_to(message, "╠══════════════╣\n║❌ İşlem Başarısız\n╠══════════════╣\n║❗Lütfen, Geçerli Bir IP Adresi Giriniz!\n╠══════════════╣\n\n╠══════════════╣\n║Örnek: /ip 45.155.125.209\n╠══════════════╣")
        print(str(e))


@bot.message_handler(commands=['iban'])
def handle_iban(message):
    blocked_users = load_blocked_users()  # is_user_blocked.txt dosyasından engellenen kullanıcı kimliklerini al

    # Engellenmiş kullanıcı kontrolü sağlar
    if message.from_user.id in blocked_users:
        bot.reply_to(message, "╠══════════════╣\n║ Ban_v2.2 ║ Fallen-Yasaklı-Üyesiniz.\n╠══════════════╣\n\n╠══════════════╣\n║ Tebrikler, Yasaklandınız.\n╟ Ödül Olarak: Kendinizi;\n║ Fallen Sisteminden Banlandınız.\n╠══════════════╣")
        return
    try:
        iban = message.text.split()[1]

        response = requests.get(f"APİ GİR !")

        if response.status_code == 200:
            data = response.json()

            bank = data['BANKA']
            sube = data['ŞUBE']

            result = f"╭─━━━━━━━━━━━━─╮\n┃Banka Adı: {bank['Adı']}\n"
            result += f"┃Banka Kodu: {bank['Kod']}\n"
            result += f"┃Swift: {bank['Swift']}\n"
            result += f"┃Hesap No: {bank['Hesap No']}\n"
            result += f"┃Şube Adı: {sube['Ad']}\n"
            result += f"┃Şube Kodu: {sube['Kod']}\n"
            result += f"┃İl: {sube['İl']}\n"
            result += f"┃İlçe: {sube['İlçe']}\n"
            result += f"┃Telefon: {sube['Tel']}\n"
            result += f"┃Fax: {sube['Fax']}\n"
            result += f"┃Adres: {sube['Adres']}\n╰─━━━━━━━━━━━━─╯"

            bot.reply_to(message, result)
        else:
            bot.reply_to(message, "API'den geçerli bir yanıt alınamadı.")
    except IndexError:
        bot.reply_to(message, "Geçerli bir IBAN numarası girin.")
    except Exception as e:
        bot.reply_to(message, f"Bir hata oluştu: {str(e)}")
        




@bot.message_handler(commands=['sms'])
def handle_sms_command(message):
    blocked_users = load_blocked_users()  # is_user_blocked.txt dosyasından engellenen kullanıcı kimliklerini al

    # Engellenmiş kullanıcı kontrolü sağlar
    if message.from_user.id in blocked_users:
        bot.reply_to(message, "╠══════════════╣\n║ Ban_v2.2 ║ Fallen-Yasaklı-Üyesiniz.\n╠══════════════╣\n\n╠══════════════╣\n║ Tebrikler, Yasaklandınız.\n╟ Ödül Olarak: Kendinizi;\n║ Fallen Sisteminden Banlandınız.\n╠══════════════╣")
        return

    try:
        command_parts = message.text.split()

        if len(command_parts) == 4 and command_parts[0] == '/sms' and command_parts[2] == '-adet':
            numara = command_parts[1]
            adet = int(command_parts[3])

            api_url = f"APİ GİR!"
            response = requests.get(api_url)
            response_data = json.loads(response.text)

            if "message" in response_data:
                reply_message = response_data["message"]
            else:
                reply_message = f"Sms Saldırısı Gönderildi!\nGSMN: {numara}\nAdet: {adet}"

        else:
            reply_message = "Hatalı komut kullanım\n\nÖrnek: /sms 5555555555 -adet 10"

    except Exception as e:
        numara = command_parts[1]
        adet = int(command_parts[3])
        reply_message = f"Sms Saldırısı Gönderildi!\nGSMN: {numara}\nAdet: {adet}"

    bot.reply_to(message, reply_message)
    




@bot.message_handler(commands=['tckn'])
def handle_tckn(message):
    blocked_users = load_blocked_users()  # is_user_blocked.txt dosyasından engellenen kullanıcı kimliklerini al

    # Engellenmiş kullanıcı kontrolü sağlar
    if message.from_user.id in blocked_users:
        bot.reply_to(message, "╠══════════════╣\n║ Ban_v2.2 ║ Fallen-Yasaklı-Üyesiniz.\n╠══════════════╣\n\n╠══════════════╣\n║ Tebrikler, Yasaklandınız.\n╟ Ödül Olarak: Kendinizi;\n║ Fallen Sisteminden Banlandınız.\n╠══════════════╣")
        return


    # Diğer işlemler devam etirir
    try:
        tc = message.text.split()[1]
        
        response = requests.get(f"APİ GİR!").json()
        if response:
            result = response[0]
            response_text = f"╠══════════════╣\n║ TCKN: {result['TC']}\n║ Adı: {result['ADI']}\n║ Soyadı: {result['SOYADI']}\n║ Doğum Tarihi: {result['DOGUMTARIHI']}\n║ Nüfus İli: {result['NUFUSIL']}\n║ Nüfus İlçesi: {result['NUFUSILCE']}\n║ Anne Adı: {result['ANNEADI']}\n║ Anne TC: {result['ANNETC']}\n║ Baba Adı: {result['BABAADI']}\n║ Baba TC: {result['BABATC']}\n║ Uyruk: {result['UYRUK'] or 'TR'}"
            bot.reply_to(message, response_text)
        else:
            bot.reply_to(message, "╠══════════════╣\n║Girdiğiniz Bilgiler ile Eşleşen Biri ║Bulunamadı! ❌\n╠══════════════╣")
    except IndexError:
        bot.reply_to(message, "╠══════════════╣\n║❌ İşlem Başarısız\n╠══════════════╣\n║❗Lütfen, Geçerli Bir T.C Giriniz!\n╠══════════════╣\n\n╠══════════════╣\n║Örnek: /tckn 11111111110\n╠══════════════╣")
    except Exception as e:
        bot.reply_to(message, "╠══════════════╣\n║Bir Hata oluştu ❌\n╠══════════════╣\n╠══════════════╣\n║Lütfen daha sonra tekrar deneyin. . .⏳\n╠══════════════╣")
        print(str(e))



API_BASE_URL = "APİ GİR ADSOYAD"


@bot.message_handler(commands=['sorgu'])
def handle_sorgu(message):
    blocked_users = load_blocked_users()  # is_user_blocked.txt dosyasından engellenen kullanıcı kimliklerini al

    # Engellenmiş kullanıcı kontrolü sağlar
    if message.from_user.id in blocked_users:
        bot.reply_to(message, "╠══════════════╣\n║ Ban_v2.2 ║ Fallen-Yasaklı-Üyesiniz.\n╠══════════════╣\n\n╠══════════════╣\n║ Tebrikler, Yasaklandınız.\n╟ Ödül Olarak: Kendinizi;\n║ Fallen Sisteminden Banlandınız.\n╠══════════════╣")
        return
        
    try:
        parameters = message.text.split()[1:]
        if len(parameters) < 4 or parameters[0] != '-isim' or parameters[2] != '-soyisim':
            raise IndexError
        isim = parameters[1]
        soyisim = parameters[3]
        il = parameters[5] if len(parameters) > 5 and parameters[4] == '-il' else ''
        ilce = parameters[7] if len(parameters) > 7 and parameters[6] == '-ilce' else ''

        session = requests.Session()
        session.headers = {
            'User-Agent': 'Your User Agent String',
            'Authorization': 'Your Authorization Token',
        }

        response = session.get(f"{API_BASE_URL}?ad={isim}&soyad={soyisim}&il={il}&ilce={ilce}").json()
        if response:
            formatted_result = ""
            kayit_sayisi = 0  # Kayıt sayısını tutmak için sayaç
            
            for person in response:
                kayit_sayisi += 1                                
                
                formatted_result += f"\n╠══════════════╣\n║ Kayıt sayısı: {kayit_sayisi}\n╠══════════════╣"
                formatted_result += f"\n║ TCKN: {person['TC']}\n"
                formatted_result += f"║ Adı: {person['ADI']}\n"
                formatted_result += f"║ Soyadı: {person['SOYADI']}\n"
                formatted_result += f"║ Doğum Tarihi: {person['DOGUMTARIHI']}\n"
                formatted_result += f"║ GSMN: {person['GSM']}\n╠══════════════╣\n"
                
                # formatted_result'in uzunluğunu kontrol et
                if len(formatted_result) > 3500:
                    # Eğer fazla uzunsa, mesajı gönder
                    bot.send_message(message.chat.id, formatted_result)
                    # formatted_result'i sıfırla
                    formatted_result = ""
            
            # formatted_result boş değilse, son mesajı gönder
            if formatted_result:
                bot.send_message(message.chat.id, formatted_result)
                
                bot.send_message(message.chat.id, f"Toplam Kayıt Sayısı: {kayit_sayisi} Adet")
            
            
        else:
            bot.send_message(message.chat.id, "╠══════════════╣\n║Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı! ❌\n╠══════════════╣")
    except IndexError:
        bot.send_message(message.chat.id, "╠══════════════╣\n║❌ İşlem Başarısız\n╠══════════════╣\n║❗ Lütfen Geçerli Parametreleri Giriniz!\n╠══════════════╣\n\n╠══════════════╣\n║Örnek: /sorgu -isim Mehmet \n║-soyisim Yılmaz -il Diyarbakır -ilce \n║Baglar\n╠══════════════╣")
    except Exception as e:
        bot.send_message(message.chat.id, f"Hata Lütfen daha sonra Tekrar deneyiniz!.")
        print(str(e))  

                

@bot.message_handler(commands=['gsmtc'])
def handle_gsmtc(message):
    blocked_users = load_blocked_users()  # is_user_blocked.txt dosyasından engellenen kullanıcı kimliklerini al

    # Engellenmiş kullanıcı kontrolü sağlar
    if message.from_user.id in blocked_users:
        bot.reply_to(message, "╠══════════════╣\n║ Ban_v2.2 ║ Fallen-Yasaklı-Üyesiniz.\n╠══════════════╣\n\n╠══════════════╣\n║ Tebrikler, Yasaklandınız.\n╟ Ödül Olarak: Kendinizi;\n║ Fallen Sisteminden Banlandınız.\n╠══════════════╣")
        return

    # Diğer işlemler devam etsin
    try:
        gsm = message.text.split()[1]
        
        response = requests.get(f"APİ GİR").json()
        if response:
            tc = response[0]['TC']
            bot.reply_to(message, f"╠══════════════╣\n║ *TCKN*: `{tc}`\n╠══════════════╣", parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "╠══════════════╣\n║Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı! ❌\n╠══════════════╣")
    except IndexError:
        bot.reply_to(message, "╠══════════════╣\n║❌ İşlem Başarısız\n╠══════════════╣\n║Lütfen, Geçerli Bir GSM Giriniz!\n╠══════════════╣\n\n╠══════════════╣\n║Örnek: /gsmtc 5551234567\n╠══════════════╣")
    except Exception as e:
        bot.reply_to(message, "╠══════════════╣\n║Bir Hata oluştu ❌\n╠══════════════╣\n╠══════════════╣\n║Lütfen daha sonra tekrar deneyin. . .⏳\n╠══════════════╣")
        print(str(e))
        
                           
@bot.message_handler(commands=['aile'])
def handle_aile(message):
    blocked_users = load_blocked_users()  # is_user_blocked.txt dosyasından engellenen kullanıcı kimliklerini al

    # Engellenmiş kullanıcı kontrolü sağlar
    if message.from_user.id in blocked_users:
        bot.reply_to(message, "╠══════════════╣\n║ Ban_v2.2 ║ Fallen-Yasaklı-Üyesiniz.\n╠══════════════╣\n\n╠══════════════╣\n║ Tebrikler, Yasaklandınız.\n╟ Ödül Olarak: Kendinizi;\n║ Fallen Sisteminden Banlandınız.\n╠══════════════╣")
        return

    # Diğer işlemler devam etsin
    try:
        tc = message.text.split()[1]
        response = requests.get(f"APİ GİR").json()
        if response:
            formatted_result = ""
            for person in response:
                formatted_result += f"\n╠══════════════╣\n║ Yakınlık: {person['Yakınlık']}\n"
                formatted_result += f"║ TCKN: {person['TcKm']}\n"
                formatted_result += f"║ Adı: {person['Adı']}\n"
                formatted_result += f"║ Soyadı: {person['Soyadı']}\n"
                formatted_result += f"║ Doğum Tarihi: {person['DoğumGünü']}\n"
                formatted_result += f"║ Nufüs İL: {person['Nufüsil']}\n"
                formatted_result += f"║ Nufüs İLÇE: {person['Nufüsilçe']}\n"
                formatted_result += f"║ GSM: +90{person['Gsm']}\n╠══════════════╣\n"
                

            bot.reply_to(message, formatted_result)
        else:
            bot.send_message(message.chat.id, "╠══════════════╣\n║Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı! ❌\n╠══════════════╣")
    except IndexError:
        bot.reply_to(message, "╠══════════════╣\n║❌ İşlem Başarısız\n╠══════════════╣\n║❗Lütfen, Geçerli Bir T.C Giriniz!\n╠══════════════╣\n\n╠══════════════╣\n║Örnek: /aile 11111111110\n╠══════════════╣")
    except Exception as e:
        bot.reply_to(message, "╠══════════════╣\n║Bir Hata oluştu ❌\n╠══════════════╣\n╠══════════════╣\n║Lütfen daha sonra tekrar deneyin. . .⏳\n╠══════════════╣")
        print(str(e))




@bot.message_handler(commands=['tcgsm'])
def handle_tcpro(message):
    blocked_users = load_blocked_users()  # is_user_blocked.txt dosyasından engellenen kullanıcı kimliklerini al

    # Engellenmiş kullanıcı kontrolü sağlar
    if message.from_user.id in blocked_users:
        bot.reply_to(message, "╠══════════════╣\n║ Ban_v2.2 ║ Fallen-Yasaklı-Üyesiniz.\n╠══════════════╣\n\n╠══════════════╣\n║ Tebrikler, Yasaklandınız.\n╟ Ödül Olarak: Kendinizi;\n║ Fallen Sisteminden Banlandınız.\n╠══════════════╣")
        return

    # Diğer işlemler devam etsin
    try:
        tc = message.text.split()[1]
        response = requests.get(f"APİ GİR!").json()
        if response:
            formatted_result = ""
            for person in response:
                formatted_result += f"\n╠══════════════╣\n║ GSMN: +90{person['GSM']}\n╠══════════════╣\n"
                

            bot.reply_to(message, formatted_result)
        else:
            bot.send_message(message.chat.id, "╠══════════════╣\n║Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı! ❌\n╠══════════════╣")
    except IndexError:
        bot.reply_to(message, "╠══════════════╣\n║❌ İşlem Başarısız\n╠══════════════╣\n║❗Lütfen, Geçerli Bir T.C Giriniz!\n╠══════════════╣\n\n╠══════════════╣\n║Örnek: /tcgsm 11111111110\n╠══════════════╣")
    except Exception as e:
        bot.reply_to(message, "╠══════════════╣\n║Bir Hata oluştu ❌\n╠══════════════╣\n╠══════════════╣\n║Lütfen daha sonra tekrar deneyin. . .⏳\n╠══════════════╣")
        print(str(e))




@bot.message_handler(commands=['ddos'])
def handle_ddos(message):
    blocked_users = load_blocked_users()  # is_user_blocked.txt dosyasından engellenen kullanıcı kimliklerini al

    # Engellenmiş kullanıcı kontrolü sağlar
    if message.from_user.id in blocked_users:
        bot.reply_to(message, "╠══════════════╣\n║ Ban_v2.2 ║ Fallen-Yasaklı-Üyesiniz.\n╠══════════════╣\n\n╠══════════════╣\n║ Tebrikler, Yasaklandınız.\n╟ Ödül Olarak: Kendinizi;\n║ Fallen Sisteminden Banlandınız.\n╠══════════════╣")
        return
        
    # Diğer işlemler devam etsin
    try:
        parameters = message.text.split()[1:]
        if len(parameters) < 4 or parameters[0] != '-host' or parameters[2] != '-port':
            raise IndexError
        host = parameters[1]
        port = parameters[3]               

        response = requests.get(f"APİ GİR").json()

        if response['status'] == 'success':
            result = f"╠══════════════╣\n║ Saldırı Başarıyla Gönderildi!\n║Sunucu: Ücretsiz\n║(Saldırının Başlaması İçin 20 Saniye Bekleyin)\n╠══════════════╣"

            bot.reply_to(message, result)
        else:
            bot.reply_to(message, f"╠══════════════╣\n║Hata Lütfen 30 saniye Bekleyin!.\n╠══════════════╣")
    except IndexError:
        bot.reply_to(message, "╠══════════════╣\n║Lütfen Geçerli Parametreleri Girin\n╠══════════════╣\n║Örnek: /ddos -host [URL] -port [PORT]\n╠══════════════╣")
        




bot.polling()