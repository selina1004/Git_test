#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# manage.py : 스크립트인데, 사이트 관리를 도와주는 역할을 합니다.
# 이 스크립트로 다른 설치 작업 없이, 컴퓨터에서 웹 서버를 시작할 수 있습니다.

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ytc.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
