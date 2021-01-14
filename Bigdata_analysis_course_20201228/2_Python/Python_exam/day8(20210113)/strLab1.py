# 2021-01-13 실습()
def myemail_info(email):
    if '@' in email:
        ad = tuple(email.split('@'))
        return ad
    else:
        return None



# @ 기준으로 쪼개는 방법은?
# 2개의 원소를 갖는 튜플을 리턴하는 방법은?