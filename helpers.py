import requests
import re
import os
from dotenv import load_dotenv
from better_profanity import profanity

def CheckForInappropriateWords(msg, name, email, sub ,country):
    txt = msg + " " + name + " " + email + " " + sub + " " + country
    result = profanity.contains_profanity(txt)
    if result == True:
        return True
    else:
        return False

def CheckEmail(email):
    # format name@gmail.com
    if re.findall(r"^[A-z0-9\.]+@[A-z0-9]+\.\w{,5}$", email) == []:
        return True
    else:
        return False

def CheckCounterURL(counter, bool):
    if counter ==  4294967295 or bool == 0:
        return False
    return True

def CheckURL(url):
    # format www.name.com or name.com or https://www.name.com/ or http://www.name.com/
    if re.findall(r"(https?)?:?/?/?(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", url) != []:
        return True
    else:
        return False

def HashURL(id):
    letter = "abcdefghijklmnopqrstuvwxyz123456789GHIJKLMNOPQRSTUVWXYZ0123456789"
    short_URL = ''
    while id > 0:
        short_URL = letter[id % 62] + short_URL
        id //= 62
    return short_URL

def CaesarDigital(key, text):
    cipher_text = ""
    for letter in text:
        try:
            if letter.isupper():
                cipher_text += chr((ord(letter) - 65 + int(key)) %26 + 65)

            elif letter.islower():
                cipher_text += chr((ord(letter) - 97 + int(key)) %26 + 97)
            else:
                cipher_text += letter
        except:
            return "Operation denied: Unsupported languages entered"
    return cipher_text

def CheckLetterKeys(key):
    if not key or not key.isalpha() or len(key) > 26 or len(key) < 26:
        return True

    for sum in range(len(key)):
        for num in range(sum+1, len(key)):
            if key[sum] == key[num]:
                return True
    return False

def CaesarLetters(key, text, cipher_decrypt):
    cipher_text = ""
    if cipher_decrypt == 'cipher':
        for letter in text:
            try:
                if letter.isupper():
                    cipher_text += key[(ord(letter) - 65)].upper()

                elif letter.islower():
                    cipher_text += key[(ord(letter) - 97)].lower()
                elif not letter.isalpha():
                    cipher_text += letter
            except:
                return "Operation denied: Unsupported languages entered"
        return cipher_text

    else:
        original_letter_order = "ABCDEFGHIJKLMNOPQRSTYVWXYZ"
        for letter in text:
            for sum in range(25):
                try:
                    if letter.isupper() and key[sum].upper() == letter:
                        cipher_text += original_letter_order[sum]
                        break
                    elif letter.islower() and key[sum].lower() == letter:
                        cipher_text += original_letter_order[sum].lower()
                        break
                    elif not letter.isalpha():
                        cipher_text += letter
                        break
                except:
                        return "Operation denied: Unsupported languages entered"
        return cipher_text

def CaeserDigitalDecoding(text):
    Letter = 'a'
    MaxCounterChar = 0
    MaxLetter = 'a'

    for x in range(26):
        Counter = 0
        CountChar = 0
        for letters in text:
            CountChar += 1
            if Letter == letters.lower():
                Counter += 1

            if Counter > MaxCounterChar:
                MaxCounterChar = Counter
                MaxLetter = Letter

            if CountChar >= 300:
                break
        Letter = chr(ord(Letter) + 1)

    Key = 0
    if int(ord(MaxLetter) - ord('e')) > 0:
        Key = 26 - int(ord(MaxLetter) - ord('e'))
    else:
        Key = 26 - int(ord(MaxLetter) - ord('e')) + 26

    return Key

def ConvertCurrencies(convert_from, to, amount):

    # Load environment variables for API KEY information.
    load_dotenv()

    url = f"https://v6.exchangerate-api.com/v6/{os.getenv('API_KEY')}/latest/{convert_from}"

    response = requests.request("GET", url)

    result = response.json()

    if result['result'] == "success":
        return {
            "from": float(result['conversion_rates'][convert_from]),
            "to": float(result['conversion_rates'][to]),
            "amount_total": float(result['conversion_rates'][to]*float(amount)),
            "amount": float(amount)
        }
    else:
        return None

def CurrencySupplyChangeToUsd(value):
    # Format value as USD
    return f"${value:,.2f}"
