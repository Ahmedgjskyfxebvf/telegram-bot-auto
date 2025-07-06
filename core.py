# core.py
import os
import importlib

bots_folder = 'bots'

for filename in os.listdir(bots_folder):
    if filename.endswith('.py'):
        module_name = f"{bots_folder}.{filename[:-3]}"
        try:
            importlib.import_module(module_name)
            print(f"✅ تم تشغيل {filename}")
        except Exception as e:
            print(f"❌ فشل تشغيل {filename}: {e}")
