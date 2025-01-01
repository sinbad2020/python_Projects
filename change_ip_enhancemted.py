import os
import random
import time
import sys
import threading

# دالة لطلب إدخال رقم الراوتر من المستخدم
def get_router_number():
    while True:
        router_number = input('Enter router number (192.168.__.1): ')
        if router_number.isdigit() and 0 <= int(router_number) <= 255:
            return router_number
        else:
            print("Invalid input. Please enter a valid number between 0 and 255.")


# دالة لتوليد عنوان IP عشوائي بين 90 و 200
def generate_random_ip():
    return random.randint(90, 200)

# دالة لتغيير إعدادات الـ IP باستخدام أمر netsh في Windows
def change_ip(router_number, random_ip):
    os.system(f"netsh interface ipv4 set address wi-fi static 192.168.{router_number}.{random_ip} 255.255.255.0 192.168.{router_number}.1 > NUL 2>&1")

# دالة لتغيير إعدادات الـ DNS باستخدام أمر netsh في Windows
def change_dns():
    os.system("netsh interface ipv4 set dnsserver name=wi-fi static 8.8.8.8 > NUL 2>&1")

# دالة لعرض عداد نصي أثناء تنفيذ عملية معينة
def show_timer(message, stop_event, interval=0.1):
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\r{message} {i:2}")
        sys.stdout.flush()
        time.sleep(interval)
        i += 1

# الدالة الرئيسية التي تدير عملية تغيير الـ IP والـ DNS
def main():
    router_number = get_router_number()  # طلب إدخال رقم الراوتر من المستخدم
    random_ip = generate_random_ip()     # توليد عنوان IP عشوائي

    stop_event = threading.Event()       # إنشاء حدث للتحكم في المؤقت

    # تغيير الـ IP أولاً مع عرض المؤقت
    ip_thread = threading.Thread(target=change_ip, args=(router_number, random_ip))
    ip_timer_thread = threading.Thread(target=show_timer, args=("Changing IP...", stop_event, 0.1))

    ip_timer_thread.start()
    ip_thread.start()

    ip_thread.join()
    stop_event.set()  # إيقاف المؤقت بعد انتهاء تغيير الـ IP
    ip_timer_thread.join()

    print("\nIP changed successfully.")

    # إعادة تعيين الحدث لتغيير الـ DNS
    stop_event.clear()

    # تغيير الـ DNS مع عرض المؤقت
    dns_thread = threading.Thread(target=change_dns)
    dns_timer_thread = threading.Thread(target=show_timer, args=("Changing DNS...", stop_event, 0.1))

    dns_timer_thread.start()
    dns_thread.start()

    dns_thread.join()
    stop_event.set()  # إيقاف المؤقت بعد انتهاء تغيير الـ DNS
    dns_timer_thread.join()

    print("\nDNS changed successfully.")

if __name__ == "__main__":
    main()
