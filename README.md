# ***MultiTool***
## *A site that gathers important and multifunctional tools and puts them in one place.*
### Video  :  [YouTube](https://www.youtube.com/watch?v=VYYc3voCKMM)

### Wibsit :  [Live version](https://omarhassouna.pythonanywhere.com/emji)

****

# *About the functionality of the tools*

# **URL Shortener** 
### It is a tool designed to shorten long web addresses and replace them with short ones.

- **of its features**
    - The function of tracking the number of clicks by users on your short link.
    - Create a QR code for the short URL.

# **Currency Converter**
### A tool designed to convert between all currencies, the chosen currency is selected, the currency to which the conversion is chosen, and the amount you want to convert.

- **of its features**
    - Provides additional information about one value of each currency selected for the converted currency and versa.
    
# **Caesar** 
### A tool designed to encrypt text with Caesar Cipher using numeric and alphanumeric keys.

- **of its features**
    - Decrypt any text encrypted with the digital key, using the most widely used language character algorithm.

# **QR Code** 
### A tool designed to convert text and links into a QR code that is easy to read by smartphones and easy to adapt in many areas.

# **Contact** 
### A tool designed to enable the user to send a mail message to the application developer.

***
# ***Explanation of the transactions, structures, and techniques used***
- ## **URL Shortener**  
    - ### **In terms of tasks** :
        - ### *There are 3 main tasks that the tool performs and they are*
            1. **link shortcut**
            2. **Get links when you enter them in the search box**
            3. **Check the number of clicks on links**
            
    ***
    - ### **In terms of design and technology used** :
        - ## *link shortcut* :
            - ### The tool was designed using a database consisting of 2 tables, the
                1. counter manager (id, counter name, counter, counter status)
                2. url (id , URL long, URL short, counter)
            ***
            - ### **process stages**
                - When the user requests to shorten a link, the request is initially processed in terms of errors such as not entering a link
                Or the link is incorrect (where the link is entered into a regular expressions function to verify that the method of writing the link is correct). Then we check the database to see whether the link already exists or not. If it exists, the user is directed to it directly. If it does not exist, we create A new code for the link using Base62 in the hash url function and send it a number from the counter that was saved in the counter manager table and we increase the number of the counter and then add the information to the database,
                The reason for choosing the counter method for creating symbols is that the collision rate is zero. I could have chosen another way, such as taking the first 6 letters of each link, and this collision occurs most of the time because it is possible to enter a link with the same 6 letters in the beginning, but the difference is in the letters Which after it, or it was possible to choose the timing to do it for the first moment, I felt that it was the best way instead of using a counter and consuming memory and time in the counter process, but when I thought about it, I found it crazy because we cannot control the meters such as their size, where they start and where they end and how we will expand Later if we want to put the site on more than one server, and this takes us to the thing that is not done yet, which is expansion, you can quickly expand the site and put other counters for each server or make an algorithm that automates the operations by specifying the number of each counter and so that there is no collision in the counters if it is broken Servant
                At the present time, the matter has been dealt with without expansion and with the closure of data entry operations on the database.
    
            ***
            - ## *Get links when you enter them in the search box*
                - ### When the user searches for the link through the search box, the connection reaches the root
                    `@app.route("/<short_url>")`  the take every operation after the / tag after the site name.
                    ***
                - ### **process stages**
                    - We first search the database for the name of the url long, counter via the short link code, then the number of its counter is updated by 1 increment and the user is converted to url long.
            ***
            - ## *Check the number of clicks on links*
                - When the user searches for their link hit count, enter the short link and the result will appear for them.
                ***
            - ### **process stages**
                - I searched for common errors as before and cut the text after the site name and (/) to find the short link code and searched for its counter in the database and submitted
***

- ## **Currency Converter** 
    - This tool was designed and built using an API
        In the root of ` @app.route("/currency_converter", methods=["GET", "POST"]) ` I check the input as valid and send the input to the function ` def convert(convert_from, to, amount): ` in File `helpers.py`
        Basically, you have defined an environment variable inside the `evn` file that holds the information of the private API key
        The request link for the website used to fetch currency information at its current prices has been defined
        I searched for the currencies by returning the `josn` file with the current currency rates and with a few calculations the desired output was processed
***
- ## **Text encryption**
    - ### **In terms of tasks** :
        - ### *There are 4 main tasks that the tool performs and they are*
            1. **Caesar cipher**
            2. **Substitution cipher**
            3. **Decoding - Caesar cipher**
            4. **Decoding - Substitution cipher**
    ***
    - ### **In terms of design and technology used** :
        - ### *The tool is built using ASCII table information for characters and symbols Where letters were replaced by fetching their numbers from the table and performing various arithmetic operations on them* 
        ***
        - ##  *Caesar cipher*
            - ### **process stages**
                - The encoding process relied on paraphrasing the character back to its number in the ASCII table and performing the calculation 
                `(n - 97 + key) 97 + 26%` , where the number of the first character in the lowercase character string was reduced to determine what the character's order was in the original order and the key number was increased, Then fetch the remainder of dividing the number by 26 in order to locate the new character again after encoding in the original order and add 97 to locate the character in the ASCII table.
        ***
        - ##  *Substitution cipher*
            - ### **process stages**
                - The encoding process relied on reformulating the character to its number in the ASCII table and performing a negative `n - 97` operation in order to locate the character in the original order, but it differs that the replacement is not by the ASCII table, but by the key sent from the user when the character is located in Alphabetical order is replaced by the position of the letter within the key and replaced by it.
        ***
        - ##  *Decoding - Caesar cipher*
            - ### **process stages**
                - The decryption process can be done in two ways, the most common language character in the language (frequency analysis) and brute force attack using all possible possibilities of the key, which is 25 transformation possibilities because the original text is number 26, I used frequency parsing because of the calculation of worst and best case estimates and algorithm speed in Both, where the most popular character counting algorithm parsing is O(n),the tool is designed to extract 200 characters from the text if the text characters size is more than 400 characters to reduce the linear search, and the parsing of the brute force algorithm is `O(n * 26)` which means that even if you extract the text and cut it, it will linearly search for n in 26 attempts, which means `n = 80` characters `(80 * 26) = 2080` characters.
***
- ## **QR Code**
    - ### **In terms of design and technology used** :
        - It is built on the basis of the `flask_qrcode` library, this library takes the data to be converted into a QR image and returns the image in the `JINJA` template inside the `HTML` file, for example `src={{qrcode ( data, box_size = 10)}}` The image upload button is designed
***
- ## **Contact**
    - ### **In terms of design and technology used** :
    - The tool is built with the `flask_mail` library where I specify the server to which it will be sent, specify the port number and save the mail and password information in environmental variables inside the `env` file. When the user sends a message, it calls the `Check_For_Infect_Words` function via the `better_profanity` library if there are inappropriate words, it returns `True` and the message is rejected, the second function `check_email` validates the email entry pattern using a regular expression and returns `True` If there is a typing error in the user's mail
