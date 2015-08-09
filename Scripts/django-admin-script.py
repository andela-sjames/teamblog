#!C:\Users\Administrator\Desktop\Tlog\Team\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'django==1.8.2','console_scripts','django-admin'
__requires__ = 'django==1.8.2'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('django==1.8.2', 'console_scripts', 'django-admin')()
    )
