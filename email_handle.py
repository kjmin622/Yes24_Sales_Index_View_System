import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime, timedelta
import pytz


def get_password():
    with open("password", "r", newline="", encoding="utf-8") as file:
        password = file.readline()
    return str(password)


def email_send(html_data):
    # 발신자, 수신자 이메일 주소
    sender_email = "kjmin622@hanyang.ac.kr"
    receiver_email = "kjmin622@hanyang.ac.kr"

    # 이메일 서버 로그인 정보
    smtp_server = "smtp.gmail.com"  # 사용하는 이메일 서비스의 SMTP 서버 주소
    smtp_port = 587  # 대부분의 이메일 서비스에서 사용하는 SMTP 포트
    smtp_user = "kjmin622@hanyang.ac.kr"
    smtp_password = get_password()

    # 이메일 내용 생성

    # 한국 시간대 설정
    korea_timezone = pytz.timezone("Asia/Seoul")

    # 현재 날짜와 시간 (한국 시간대 기준)
    now_korea = datetime.now(korea_timezone)

    # 현재 날짜 (한국 시간대 기준)
    today_date_korea = now_korea.strftime("%Y-%m-%d")

    subject = f"{today_date_korea} Yes24 판매지수 통계"
    body = html_data

    # MIMEMultipart 객체 생성 및 세부 정보 설정
    msg = MIMEMultipart("alternative")
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # MIMEText 객체를 HTML 본문으로 추가
    msg.attach(MIMEText(body, "html"))

    try:
        # SMTP 서버에 연결
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # TLS 보안 시작
        server.login(smtp_user, smtp_password)  # 로그인

        # 이메일 전송
        server.sendmail(sender_email, receiver_email, msg.as_string())

    finally:

        server.quit()  # SMTP 세션 종료
