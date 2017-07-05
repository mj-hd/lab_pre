#!/usr/bin/python
# -*- coding: utf-8 -*-

# 日付を表すクラス
class Date:

    # 月ごとの日数
    DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 曜日を求め、文字列で返す
    def get_day_of_week(self):
        year  = self.year
        month = self.month
        day   = self.day

        # Zellerの公式を使用して、曜日を求める
        # 参考: http://edu.clipper.co.jp/pg-2-47.html
        if month < 3:
            year -= 1
            month += 12

        dow = (year + year/4 - year/100 + year/400 + (13 * month + 8) / 5 + day) % 7

        return ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"][dow]

    # 日付を加算する
    def increment_day(self):
        self.day += 1
        self._normalize()

    # 日付を正規化する
    def _normalize(self):
        # 日数が超えていた場合、月へ繰り上げる
        if self.day > Date.DAYS[self.month - 1]:
            self.day = self.day % Date.DAYS[self.month - 1]
            self.month += 1

        # 月が12を超えていた場合、年へ繰り上げる
        if self.month > 12:
            self.year += 1
            self.month = self.month % 12 + 1

    # 日付比較
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.year == other.year and self.month == other.month and self.day == other.day
        raise NotImplemented()

    def __ne__(self, other):
        return not(self.__eq__(other))

    # 文字列へ変換する
    def __repr__(self):
        return str(self.year) + "/" + str(self.month) + "/" + str(self.day) + "(" + str(self.get_day_of_week()) + ")"


start = Date(1900, 1, 1)   # 開始する日付
end   = Date(2000, 12, 31) # 終了する日付

# 開始日から終了日まで走査する
current = start
count = 0
while current != end:
    current.increment_day() # 日付を加算
    if current.day == 1 and current.get_day_of_week() == "SUN": # 月初で、日曜日
        print(current) # 出力
        count += 1     # カウントアップ

print "TOTAL: " + str(count)

