import re

def validate_email(email: str) -> bool:
    check=re.search('^(\w+[.|\w])*@(\w{2,}[.])*\w{2,}$', email)
    return True if check is not None else False

if __name__ == '__main__':
    print(validate_email('santa.banta.manta@gmail.co.in.xv.fg.gh'))
    print(validate_email('somethingthatisnotvalid'))
    print(validate_email('someone@abv'))
    print(validate_email('someone@abv.a'))
