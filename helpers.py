import requests
import re
import os
from dotenv import load_dotenv
from better_profanity import profanity

def Check_For_Inappropriate_Words(msg, name, email, sub ,country):
    txt = msg + " " + name + " " + email + " " + sub + " " + country
    result = profanity.contains_profanity(txt)
    if result == True:
        return True
    else:
        return False

def check_email(email):
    # format name@gmail.com
    if re.findall(r"^[A-z0-9\.]+@[A-z0-9]+\.\w{,5}$", email) == []:
        return True
    else:
        return False

def check_counter(counter, bool):
    if counter ==  4294967295 or bool == 0:
        return False
    return True

def check_url(url):
    # format www.name.com or name.com or https://www.name.com/ or http://www.name.com/
    if re.findall(r"(https?)?:?/?/?(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", url) != []:
        return True
    else:
        return False

def hash_URL(id):
    letter = "abcdefghijklmnopqrstuvwxyz123456789GHIJKLMNOPQRSTUVWXYZ0123456789"
    short_URL = ''
    while id > 0:
        short_URL = letter[id % 62] + short_URL
        id //= 62
    return short_URL

def caesar_digital(key, text):
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

def check_letter_keys(key):
    if not key or not key.isalpha() or len(key) > 26 or len(key) < 26:
        return True

    for sum in range(len(key)):
        for num in range(sum+1, len(key)):
            if key[sum] == key[num]:
                return True
    return False

def caesar_letters(key, text, cipher_decrypt):
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

def caeser_digital_decoding(text):
    letter = 'a'
    maxcounter = 0
    maxletter = 'a'

    if len(text) > 400:
        text = text[len(text)//2:]

    for x in range(26):
        counter = 0
        for letters in text:
            if letter == letters.lower():
                counter += 1

            if counter > maxcounter:
                maxcounter = counter
                maxletter = letter

        letter = chr(ord(letter) + 1)

    key = 0
    if int(ord(maxletter) - ord('e')) > 0:
        key = 26 - (ord(maxletter) - ord('e'))

    key = 26 - int(ord(maxletter) - ord('e')) + 26

    return key

def convert(convert_from, to, amount):

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

def usd(value):
    # Format value as USD
    return f"${value:,.2f}"

def currency_names(kye):
    if kye == "country":
        return {
             'Afghanistan': 'AF',
             'Åland Islands': 'AX', 
             'Albania': 'AL',
             'Algeria': 'DZ', 
             'American Samoa': 'AS', 
             'AndorrA': 'AD',
             'Angola': 'AO',
             'Anguilla': 'AI', 
             'Antarctica': 'AQ', 
             'Antigua and Barbuda': 'AG', 
             'Argentina': 'AR',
             'Armenia': 'AM',
             'Aruba': 'AW',
             'Australia': 'AU', 
             'Austria': 'AT',
             'Azerbaijan': 'AZ', 
             'Bahamas': 'BS',
             'Bahrain': 'BH', 
             'Bangladesh': 'BD', 
             'Barbados': 'BB', 
             'Belarus': 'BY',
             'Belgium': 'BE', 
             'Belize': 'BZ',
             'Benin': 'BJ',
             'Bermuda': 'BM', 
             'Bhutan': 'BT',
             'Bolivia': 'BO', 
             'Bosnia and Herzegovina': 'BA',
             'Botswana': 'BW',
             'Bouvet Island': 'BV', 
             'Brazil': 'BR',
             'British Indian Ocean Territory': 'IO', 
             'Brunei Darussalam': 'BN',
             'Bulgaria': 'BG',
             'Burkina Faso': 'BF', 
             'Burundi': 'BI',
             'Cambodia': 'KH', 
             'Cameroon': 'CM', 
             'Canada': 'CA',
             'Cape Verde': 'CV', 
             'Cayman Islands': 'KY', 
             'Central African Republic': 'CF', 
             'Chad': 'TD',
             'Chile': 'CL', 
             'China': 'CN', 
             'Christmas Island': 'CX', 
             'Cocos (Keeling) Islands': 'CC', 
             'Colombia': 'CO', 
             'Comoros': 'KM', 
             'Congo': 'CG', 
             'Congo: The Democratic Republic of the': 'CD', 
             'Cook Islands': 'CK', 
             'Costa Rica': 'CR', 
             'Cote D\'Ivoire': 'CI', 
             'Croatia': 'HR', 
             'Cuba': 'CU', 
             'Cyprus': 'CY', 
             'Czech Republic': 'CZ', 
             'Denmark': 'DK',
             'Djibouti': 'DJ',
             'Dominica': 'DM', 
             'Dominican Republic': 'DO', 
             'Ecuador': 'EC', 
             'Egypt': 'EG', 
             'El Salvador': 'SV', 
             'Equatorial Guinea': 'GQ', 
             'Eritrea': 'ER', 
             'Estonia': 'EE', 
             'Ethiopia': 'ET', 
             'Falkland Islands (Malvinas)': 'FK', 
             'Faroe Islands': 'FO', 
             'Fiji': 'FJ', 
             'Finland': 'FI', 
             'France': 'FR', 
             'French Guiana': 'GF', 
             'French Polynesia': 'PF', 
             'French Southern Territories': 'TF', 
             'Gabon': 'GA', 
             'Gambia': 'GM', 
             'Georgia': 'GE', 
             'Germany': 'DE', 
             'Ghana': 'GH', 
             'Gibraltar': 'GI', 
             'Greece': 'GR', 
             'Greenland': 'GL', 
             'Grenada': 'GD', 
             'Guadeloupe': 'GP', 
             'Guam': 'GU',
             'Guatemala': 'GT', 
             'Guernsey': 'GG', 
             'Guinea': 'GN',
             'Guinea-Bissau': 'GW', 
             'Guyana': 'GY', 
             'Haiti': 'HT',
             'Heard Island and Mcdonald Islands': 'HM', 
             'Holy See (Vatican City State)': 'VA',
             'Honduras': 'HN',
             'Hong Kong': 'HK', 
             'Hungary': 'HU', 
             'Iceland': 'IS', 
             'India': 'IN',
             'Indonesia': 'ID', 
             'Iran: Islamic Republic Of': 'IR', 
             'Iraq': 'IQ', 
             'Ireland': 'IE', 
             'Isle of Man': 'IM', 
             'Italy': 'IT',
             'Jamaica': 'JM', 
             'Japan': 'JP', 
             'Jersey': 'JE', 
             'Jordan': 'JO', 
             'Kazakhstan': 'KZ', 
             'Kenya': 'KE',
             'Kiribati': 'KI', 
             'Korea: Democratic People\'S Republic of': 'KP', 
             'Korea: Republic of': 'KR', 
             'Kuwait': 'KW',
             'Kyrgyzstan': 'KG', 
             'Lao People\'S Democratic Republic': 'LA', 
             'Latvia': 'LV', 
             'Lebanon': 'LB', 
             'Lesotho': 'LS', 
             'Liberia': 'LR', 
             'Libyan Arab Jamahiriya': 'LY', 
             'Liechtenstein': 'LI', 
             'Lithuania': 'LT', 
             'Luxembourg': 'LU', 
             'Macao': 'MO', 
             'Macedonia: The Former Yugoslav Republic of': 'MK', 
             'Madagascar': 'MG',
             'Malawi': 'MW',
             'Malaysia': 'MY', 
             'Maldives': 'MV', 
             'Mali': 'ML',
             'Malta': 'MT', 
             'Marshall Islands': 'MH', 
             'Martinique': 'MQ',
             'Mauritania': 'MR', 
             'Mauritius': 'MU',
             'Mayotte': 'YT',
             'Mexico': 'MX', 
             'Micronesia: Federated States of': 'FM', 
             'Moldova: Republic of': 'MD', 
             'Monaco': 'MC',
             'Mongolia': 'MN', 
             'Montserrat': 'MS', 
             'Morocco': 'MA', 
             'Mozambique': 'MZ', 
             'Myanmar': 'MM',
             'Namibia': 'NA', 
             'Nauru': 'NR',
             'Nepal': 'NP', 
             'Netherlands': 'NL', 
             'Netherlands Antilles': 'AN', 
             'New Caledonia': 'NC', 
             'New Zealand': 'NZ', 
             'Nicaragua': 'NI', 
             'Niger': 'NE', 
             'Nigeria': 'NG', 
             'Niue': 'NU', 
             'Norfolk Island': 'NF', 
             'Northern Mariana Islands': 'MP', 
             'Norway': 'NO', 
             'Oman': 'OM', 
             'Pakistan': 'PK', 
             'Palau': 'PW',
             'Palestine': 'PS', 
             'Panama': 'PA', 
             'Papua New Guinea': 'PG', 
             'Paraguay': 'PY', 
             'Peru': 'PE', 
             'Philippines': 'PH', 
             'Pitcairn': 'PN', 
             'Poland': 'PL',
             'Portugal': 'PT', 
             'Puerto Rico': 'PR', 
             'Qatar': 'QA', 
             'Reunion': 'RE',
             'Romania': 'RO', 
             'Russian Federation': 'RU',
             'RWANDA': 'RW',
             'Saint Helena': 'SH', 
             'Saint Kitts and Nevis': 'KN', 
             'Saint Lucia': 'LC', 
             'Saint Pierre and Miquelon': 'PM', 
             'Saint Vincent and the Grenadines': 'VC', 
             'Samoa': 'WS',
             'San Marino': 'SM', 
             'Sao Tome and Principe': 'ST', 
             'Saudi Arabia': 'SA', 
             'Senegal': 'SN', 
             'Serbia and Montenegro': 'CS', 
             'Seychelles': 'SC', 
             'Sierra Leone': 'SL', 
             'Singapore': 'SG', 
             'Slovakia': 'SK', 
             'Slovenia': 'SI', 
             'Solomon Islands': 'SB', 
             'Somalia': 'SO', 
             'South Africa': 'ZA', 
             'South Georgia and the South Sandwich Islands': 'GS', 
             'Spain': 'ES', 
             'Sri Lanka': 'LK', 
             'Sudan': 'SD', 
             'Suri': 'SR', 
             'Svalbard and Jan Mayen': 'SJ', 
             'Swaziland': 'SZ', 
             'Sweden': 'SE', 
             'Switzerland': 'CH', 
             'Syrian Arab Republic': 'SY', 
             'Taiwan: Province of China': 'TW', 
             'Tajikistan': 'TJ',
             'Tanzania: United Republic of': 'TZ', 
             'Thailand': 'TH', 
             'Timor-Leste': 'TL', 
             'Togo': 'TG',
             'Tokelau': 'TK', 
             'Tonga': 'TO', 
             'Trinidad and Tobago': 'TT', 
             'Tunisia': 'TN', 
             'Turkey': 'TR', 
             'Turkmenistan': 'TM', 
             'Turks and Caicos Islands': 'TC', 
             'Tuvalu': 'TV', 
             'Uganda': 'UG', 
             'Ukraine': 'UA', 
             'United Arab Emirates': 'AE', 
             'United Kingdom': 'GB', 
             'United States': 'US', 
             'United States Minor Outlying Islands': 'UM', 
             'Uruguay': 'UY', 
             'Uzbekistan': 'UZ', 
             'Vanuatu': 'VU', 
             'Venezuela': 'VE', 
             'Viet Nam': 'VN', 
             'Virgin Islands: British': 'VG', 
             'Virgin Islands: U.S.': 'VI', 
             'Wallis and Futuna': 'WF', 
             'Western Sahara': 'EH', 
             'Yemen': 'YE', 
             'Zambia': 'ZM', 
             'Zimbabwe': 'ZW' 
        }
    return {
        "AED": "United Arab Emirates Dirham",
        "AFN": "Afghan Afghani",
        "ALL": "Albanian Lek",
        "AMD": "Armenian Dram",
        "ANG": "Netherlands Antillean Guilder",
        "AOA": "Angolan Kwanza",
        "ARS": "Argentine Peso",
        "AUD": "Australian Dollar",
        "AWG": "Aruban Florin",
        "AZN": "Azerbaijani Manat",
        "BAM": "Bosnia-Herzegovina Convertible Mark",
        "BBD": "Barbadian Dollar",
        "BDT": "Bangladeshi Taka",
        "BGN": "Bulgarian Lev",
        "BHD": "Bahraini Dinar",
        "BIF": "Burundian Franc",
        "BMD": "Bermudan Dollar",
        "BND": "Brunei Dollar",
        "BOB": "Bolivian Boliviano",
        "BRL": "Brazilian Real",
        "BSD": "Bahamian Dollar",
        "BTC": "Bitcoin",
        "BTN": "Bhutanese Ngultrum",
        "BWP": "Botswanan Pula",
        "BYN": "New Belarusian Ruble",
        "BYR": "Belarusian Ruble",
        "BZD": "Belize Dollar",
        "CAD": "Canadian Dollar",
        "CDF": "Congolese Franc",
        "CHF": "Swiss Franc",
        "CLF": "Chilean Unit of Account (UF)",
        "CLP": "Chilean Peso",
        "CNY": "Chinese Yuan",
        "COP": "Colombian Peso",
        "CRC": "Costa Rican Col\u00f3n",
        "CUC": "Cuban Convertible Peso",
        "CUP": "Cuban Peso",
        "CVE": "Cape Verdean Escudo",
        "CZK": "Czech Republic Koruna",
        "DJF": "Djiboutian Franc",
        "DKK": "Danish Krone",
        "DOP": "Dominican Peso",
        "DZD": "Algerian Dinar",
        "EGP": "Egyptian Pound",
        "ERN": "Eritrean Nakfa",
        "ETB": "Ethiopian Birr",
        "EUR": "Euro",
        "FJD": "Fijian Dollar",
        "FKP": "Falkland Islands Pound",
        "GBP": "British Pound Sterling",
        "GEL": "Georgian Lari",
        "GGP": "Guernsey Pound",
        "GHS": "Ghanaian Cedi",
        "GIP": "Gibraltar Pound",
        "GMD": "Gambian Dalasi",
        "GNF": "Guinean Franc",
        "GTQ": "Guatemalan Quetzal",
        "GYD": "Guyanaese Dollar",
        "HKD": "Hong Kong Dollar",
        "HNL": "Honduran Lempira",
        "HRK": "Croatian Kuna",
        "HTG": "Haitian Gourde",
        "HUF": "Hungarian Forint",
        "IDR": "Indonesian Rupiah",
        "ILS": "Palestinian New Sheqel",
        "IMP": "Manx pound",
        "INR": "Indian Rupee",
        "IQD": "Iraqi Dinar",
        "IRR": "Iranian Rial",
        "ISK": "Icelandic Kr\u00f3na",
        "JEP": "Jersey Pound",
        "JMD": "Jamaican Dollar",
        "JOD": "Jordanian Dinar",
        "JPY": "Japanese Yen",
        "KES": "Kenyan Shilling",
        "KGS": "Kyrgystani Som",
        "KHR": "Cambodian Riel",
        "KMF": "Comorian Franc",
        "KPW": "North Korean Won",
        "KRW": "South Korean Won",
        "KWD": "Kuwaiti Dinar",
        "KYD": "Cayman Islands Dollar",
        "KZT": "Kazakhstani Tenge",
        "LAK": "Laotian Kip",
        "LBP": "Lebanese Pound",
        "LKR": "Sri Lankan Rupee",
        "LRD": "Liberian Dollar",
        "LSL": "Lesotho Loti",
        "LTL": "Lithuanian Litas",
        "LVL": "Latvian Lats",
        "LYD": "Libyan Dinar",
        "MAD": "Moroccan Dirham",
        "MDL": "Moldovan Leu",
        "MGA": "Malagasy Ariary",
        "MKD": "Macedonian Denar",
        "MMK": "Myanma Kyat",
        "MNT": "Mongolian Tugrik",
        "MOP": "Macanese Pataca",
        "MRO": "Mauritanian Ouguiya",
        "MUR": "Mauritian Rupee",
        "MVR": "Maldivian Rufiyaa",
        "MWK": "Malawian Kwacha",
        "MXN": "Mexican Peso",
        "MYR": "Malaysian Ringgit",
        "MZN": "Mozambican Metical",
        "NAD": "Namibian Dollar",
        "NGN": "Nigerian Naira",
        "NIO": "Nicaraguan C\u00f3rdoba",
        "NOK": "Norwegian Krone",
        "NPR": "Nepalese Rupee",
        "NZD": "New Zealand Dollar",
        "OMR": "Omani Rial",
        "PAB": "Panamanian Balboa",
        "PEN": "Peruvian Nuevo Sol",
        "PGK": "Papua New Guinean Kina",
        "PHP": "Philippine Peso",
        "PKR": "Pakistani Rupee",
        "PLN": "Polish Zloty",
        "PYG": "Paraguayan Guarani",
        "QAR": "Qatari Rial",
        "RON": "Romanian Leu",
        "RSD": "Serbian Dinar",
        "RUB": "Russian Ruble",
        "RWF": "Rwandan Franc",
        "SAR": "Saudi Riyal",
        "SBD": "Solomon Islands Dollar",
        "SCR": "Seychellois Rupee",
        "SDG": "Sudanese Pound",
        "SEK": "Swedish Krona",
        "SGD": "Singapore Dollar",
        "SHP": "Saint Helena Pound",
        "SLL": "Sierra Leonean Leone",
        "SOS": "Somali Shilling",
        "SRD": "Surinamese Dollar",
        "STD": "S\u00e3o Tom\u00e9 and Pr\u00edncipe Dobra",
        "SVC": "Salvadoran Col\u00f3n",
        "SYP": "Syrian Pound",
        "SZL": "Swazi Lilangeni",
        "THB": "Thai Baht",
        "TJS": "Tajikistani Somoni",
        "TMT": "Turkmenistani Manat",
        "TND": "Tunisian Dinar",
        "TOP": "Tongan Pa\u02bbanga",
        "TRY": "Turkish Lira",
        "TTD": "Trinidad and Tobago Dollar",
        "TWD": "New Taiwan Dollar",
        "TZS": "Tanzanian Shilling",
        "UAH": "Ukrainian Hryvnia",
        "UGX": "Ugandan Shilling",
        "USD": "United States Dollar",
        "UYU": "Uruguayan Peso",
        "UZS": "Uzbekistan Som",
        "VEF": "Venezuelan Bol\u00edvar Fuerte",
        "VND": "Vietnamese Dong",
        "VUV": "Vanuatu Vatu",
        "WST": "Samoan Tala",
        "XAF": "CFA Franc BEAC",
        "XAG": "Silver (troy ounce)",
        "XAU": "Gold (troy ounce)",
        "XCD": "East Caribbean Dollar",
        "XDR": "Special Drawing Rights",
        "XOF": "CFA Franc BCEAO",
        "XPF": "CFP Franc",
        "YER": "Yemeni Rial",
        "ZAR": "South African Rand",
        "ZMK": "Zambian Kwacha (pre-2013)",
        "ZMW": "Zambian Kwacha",
        "ZWL": "Zimbabwean Dollar"
    }