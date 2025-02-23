#Task1
import re
text = "Here are some examples: Rbbbr, Rb, rb, Rbb, Rbrr, RbbrB."
pattern = r'[Rr]b+r'
matches = re.findall(pattern, text)
print(matches)

#Task2
import re
def validate_card_number(card_number):
    pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
    if re.match(pattern, card_number):
        return True
    return False
if __name__=="__main__":
    cart1 = "1452-4656-4866-4986"
    cart2 = "5456-8466-4856-566"
    print(f'The card {cart1} is valid: {validate_card_number(cart1)}')
    print(f'The card {cart2} is not valid: {validate_card_number(cart2)}')

#Task3
import re
def validate_email(email):
    pattern = r'^[a-zA-Z][a-zA-Z0-9]*(?:[-][a-zA-Z0-9]+)*@([a-zA-Z0-9]+(?:[._][a-zA-Z0-9]+)*)+$'
    if re.match(pattern, email):
        return True
    return False
if __name__=="__main__":
    emails = [
        "my_email@example.com",
        "my-email@example.com",
        "my--email@example.com",
        "-myemail@example.com",
        "myemail@ex-ample.com",
        "myemail@example-.com",
        "myemail@.com",
        "my_email123@example.com",
        "my_email@example..com",
        "my_email@example_com"]
    for email in emails:
        print(f'{email}:{validate_email(email)}')

#Task4
import re
def validate_login(login):
    pattern = r'^[a-zA-Z0-9]{2,10}$'
    if re.match(pattern, login):
        return True
    return False
if __name__=="__main__":
    logins = [
        "user",
        "u1",
        "user123456",
        "a",
        "username_too_long",
        "user@name",
        "user name"
    ]
    for login in logins:
        print(f"{login}: {validate_login(login)}")