import os
import shutil
import argparse


def copy_files_recursive(src, dst):
    try:
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            if os.path.isdir(src_path):
                copy_files_recursive(src_path, dst)
            else:
                ext = os.path.splitext(item)[1][1:] or "no_extension"
                target_dir = os.path.join(dst, ext)
                os.makedirs(target_dir, exist_ok=True)
                shutil.copy2(src_path, target_dir)
    except Exception as e:
        print(f"Помилка при обробці {src}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Копіювання і сортування файлів за розширенням")
    parser.add_argument("src", help="Шлях до вихідної директорії")
    parser.add_argument("dst", nargs="?", default="dist", help="Шлях до директорії призначення")
    args = parser.parse_args()

    os.makedirs(args.dst, exist_ok=True)
    copy_files_recursive(args.src, args.dst)
    print(f"✅ Файли скопійовано та відсортовано у {args.dst}")


if __name__ == "__main__":
    main()
