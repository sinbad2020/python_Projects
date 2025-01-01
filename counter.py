"""
import time
import sys

# function to count as timer

def timer(massag="changing Dns now: "):
    for i in range(71):
        # كتابة الرقم على سطر الأوامر
        sys.stdout.write(f'\r{massag}{i:3}')  # عرض الرقم مع تنسيق مكون من 3 أرقام
        sys.stdout.flush()  # التأكد من أن الكتابة تتم فوراً
        time.sleep(0.1)  # الانتظار قليلاً قبل كتابة الرقم التالي

# استدعاء الدالة لطباعة الأرقام
timer()

#function to count the time of process

import time
import os

def measure_execution_time():
    start_time = time.time()  # بدء التوقيت
    # تنفيذ الأمر
    #result = os.system('netsh interface ipv4 set dnsserver name="wi-fi" static 8.8.8.8')
    result = os.system(f"netsh interface ipv4 set address wi-fi static 192.168.10.11 255.255.255.0 192.168.10.1")
    end_time = time.time()  # انتهاء التوقيت
    
    # حساب الوقت المستغرق
    elapsed_time = end_time - start_time
    
    # طباعة الوقت المستغرق
    print(f"الوقت المستغرق لتنفيذ الأمر: {elapsed_time:.2f} ثانية")
    
    # العودة لحالة التنفيذ (صفر يعني نجاح)
    return result

# استدعاء الدالة لقياس الوقت
measure_execution_time()
"""

import time
import sys

#function to change case of chars

def toggle_case_per_character():
    message = "i love my python projects"
    message_length = len(message)

    for _ in range(10):  # تكرار التغيير 10 مرات كمثال
        for i in range(message_length):
            # الحصول على الحرف الحالي
            char = message[i]
            
            # تغيير الحالة
            if char.islower():
                char = char.upper()
            else:
                char = char.lower()
            
            # بناء الرسالة الجديدة مع الحرف المعدل
            new_message = message[:i] + char + message[i+1:]
            
            # طباعة الرسالة المحدثة
            sys.stdout.write(f'\r{new_message}')
            sys.stdout.flush()  # التأكد من أن الكتابة تتم فوراً
            time.sleep(0.2)  # الانتظار قليلاً قبل تحديث الحرف التالي

        # الانتظار قليلاً بعد تغيير جميع الأحرف
        time.sleep(1)

# استدعاء الدالة لتغيير حالة الأحرف
toggle_case_per_character()


