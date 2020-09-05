import os
from os.path import join, dirname
from dotenv import load_dotenv

# .enfファイルのパスを指定
dotenv_path = join(dirname(__file__), '.env')
# ファイルの中身を読み込み
load_dotenv(verbose=True)
load_dotenv(dotenv_path)


BASEKEY = os.environ.get("BASEKEY")
TABLENAME = os.environ.get("TABLENAME")
APIKEY = os.environ.get("APIKEY")
