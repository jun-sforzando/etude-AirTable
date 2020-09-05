from airtable import Airtable
import settings


class AirtableOperation:
    def __init__(self, basekey, table_name, api_key):
        # 初期化
        self.basekey = basekey
        self.table_name = table_name
        self.api_key = api_key

        # Airtable Python Wrapperを使うための設定
        self.airtable_set = Airtable(
            self.basekey, self.table_name, self.api_key)

    # データを追加する
    # 他のテーブルとリンクしている”Register"はRecord IDをリストで入力しなくてはいけない
    def insert_data(self, name, image, url, date, register, types):
        # キーと内容をそれぞれリストに登録
        asset_key = ["Name", "URL", "Image URL", "Date", "Register", "Type"]
        asset_value = [name, image, url, date, register, types]
        # 挿入したいデータを辞書で設定する
        asset_data = {key: val for key, val in zip(asset_key, asset_value)}

        # 接続セット
        set_data = self.airtable_set

        set_data.insert(asset_data)


if __name__ == "__main__":
    # キーやテーブル名をsettings.pyから設定
    basekey = settings.BASEKEY
    table_name = settings.TABLENAME
    api_key = settings.APIKEY
    # インスタンス化
    asset_airtable = AirtableOperation(basekey, table_name, api_key)
    # # データを追加する
    # asset_airtable.insert_data(
    #     "テスト", "https://test.jp", "https://test.jp/test.jpg",
    #     "2020-09-03", ['receN9Pqw5cwwqkoQ'], "red"
    # )
    # print(asset_airtable.all_data())
    print(api_key)
