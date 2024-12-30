import hashlib

def calculate_md5(file_path):
    """تحسب MD5 checksum لملف"""
    md5_hash = hashlib.md5()
    try:
        with open(file_path, "rb") as file:
            # قراءة الملف على دفعات لتجنب استهلاك الذاكرة
            for chunk in iter(lambda: file.read(4096), b""):
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
    except FileNotFoundError:
        print(f"الملف غير موجود: {file_path}")
        return None

def verify_md5(file_path, expected_md5):
    """التحقق مما إذا كانت MD5 checksum تطابق القيمة المتوقعة"""
    calculated_md5 = calculate_md5(file_path)
    if calculated_md5 is None:
        return False
    print(f"MD5 المحسوبة: {calculated_md5}")
    print(f"MD5 المتوقعة: {expected_md5}")
    return calculated_md5 == expected_md5

# المدخلات
file_path = input("أدخل مسار الملف: ").strip()
expected_md5 = input("أدخل قيمة MD5 المتوقعة: ").strip()

# التحقق
if verify_md5(file_path, expected_md5):
    print("✅ تطابق MD5 checksum مع القيمة المتوقعة.")
else:
    print("❌ MD5 checksum لا تطابق القيمة المتوقعة.")
