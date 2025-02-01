import openpyxl
from lunarcalendar import Converter, Solar
from datetime import date, timedelta

# 엑셀 파일을 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Lunar Calendar Data"

# 첫 번째 행에 양력, 음력, 요일 제목을 설정
ws.append(["양력", "음력", "요일"])

# 1900년 1월 1일부터 2100년 1월 1일까지 모든 날짜 계산
start_date = date(1900, 1, 1)
end_date = date(2100, 1, 1)
current_date = start_date

while current_date < end_date:
    # 양력 날짜로부터 음력 날짜를 구하기
    solar = Solar(current_date.year, current_date.month, current_date.day)
    lunar = Converter().Solar2Lunar(solar)

    # 음력 날짜 형식 (음력 연도, 월, 일)
    lunar_date_str = f"{lunar.year}-{lunar.month:02d}-{lunar.day:02d}"

    # 요일 계산 (0: 월요일, 1: 화요일, ..., 6: 일요일)
    weekday = current_date.weekday()

    # 요일을 한글로 변환
    days_of_week = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    weekday_str = days_of_week[weekday]

    # 양력, 음력, 요일을 한 행에 추가
    ws.append([current_date, lunar_date_str, weekday_str])

    # 다음 날짜로 이동
    current_date += timedelta(days=1)

# 파일 저장
wb.save("lunar_calendar_with_weekdays.xlsx")

print("엑셀 파일 생성 완료!")
