import os
import gettext

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCALE_DIR = os.path.join(BASE_DIR, "locale")

translate = gettext.translation('messages', localedir=LOCALE_DIR, fallback=True)
_ = translate.gettext