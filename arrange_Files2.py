import os
import shutil

# Define file extensions for different categories
FILE_CATEGORIES = {
    "Images": ("gif", "jfif", "jpg", "jpeg", "webp"),
    "Text_Files": (".txt", ".lst", ".pdf"),
    "Videos": ("mp4", "mp3"),
}

def make_new_folder(folder_name):
    """Create a new folder if it doesn't already exist."""
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")

def move_file_to_folder(source, destination):
    """Move a file to a destination folder, avoiding duplicates."""
    if not os.path.exists(destination):
        shutil.copy(source, destination)
        print(f"Copied '{os.path.basename(source)}' to '{destination}'")
        os.remove(source)
        return True
    else:
        print(f"File already exists: '{os.path.basename(source)}'")
        return False

def process_files_by_category(directory, categories):
    """
    تصنيف الملفات الموجودة في دليل معين وتنظيمها في مجلدات حسب الفئات.

    Args:
        directory (str): المسار إلى الدليل المراد تنظيمه.
        categories (dict): قاموس يحتوي على أسماء الفئات كالمفاتيح والامتدادات كقيم.
    """
    # إنشاء عداد لتخزين عدد الملفات التي تم نقلها لكل فئة
    total_counters = {category: 0 for category in categories}

    # استعراض جميع الملفات والمجلدات في الدليل
    for file_name in os.listdir(directory): #لوب علي كل الملفات في المسار
        file_path = os.path.join(directory, file_name)  # المسار الكامل للملف/المجلد

        # التأكد أن العنصر الحالي هو ملف فقط
        if os.path.isfile(file_path):
            # استعراض الفئات والامتدادات المرتبطة بها
            for category, extensions in categories.items():
                # التحقق مما إذا كان اسم الملف ينتهي بأي امتداد من الفئة
                if file_name.endswith(extensions):
                    # تحديد مسار المجلد الخاص بالفئة وإنشاؤه إذا لم يكن موجودًا
                    folder_path = os.path.join(directory, category)
                    make_new_folder(folder_path)

                    # تحديد مسار الوجهة داخل مجلد الفئة
                    destination = os.path.join(folder_path, file_name)

                    # نقل الملف إلى الوجهة وزيادة العداد إذا تم النقل بنجاح
                    if move_file_to_folder(file_path, destination):
                        total_counters[category] += 1

    # عرض ملخص الملفات التي تم نقلها
    print("\nملخص الملفات التي تم نقلها:")
    for category, count in total_counters.items():
        print(f"{category}: {count} ملف/ملفات")




def main():
    """Main function to organize files."""
    current_directory = os.path.realpath(".")
    process_files_by_category(current_directory, FILE_CATEGORIES)

if __name__ == "__main__":
    main()
