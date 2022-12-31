# ***MultiTool***
## *A site that gathers important and multifunctional tools and puts them in one place.*
### Video   : [YouTube](https://www.youtube.com/watch?v=VYYc3voCKMM)

### Website : [Live version](https://omarhassouna.pythonanywhere.com/emji)

****

# *About the functionality of the tools*

# **URL Shortener** 
### It is a tool designed to shorten long web addresses and replace them with short ones.

- **Features**
    - The function of tracking the number of clicks by users on your short link.
    - Create a QR code for the short URL.

# **Currency Converter**
### A tool designed to convert between all currencies, the chosen currency is selected, the currency to which the conversion is chosen, and the amount you want to convert.

- **Features**
    - Provides additional information about one value of each currency selected for the converted currency and vice versa.
    
# **Caesar Cipher** 
### A tool designed to encrypt text with Caesar Cipher using numeric and alphanumeric keys.

- **Features**
    - Decrypt any text encrypted with the digital key, using the most widely used language character algorithm.

# **QR Code Generator** 
### A tool designed to convert text and links into a QR code that is easy to read by smartphones and easy to adapt in many areas.

# **Contact Form** 
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
        - ## *Link shortening* :
            - ### The tool was designed using a database consisting of 2 tables, the
                1. counter manager (id, counter name, counter, counter status)
                2. url (id , URL long, URL short, counter)
            ***
            - ### **Process stages**
            - When a user requests a link shortening, the request is initially handled for errors such as no link entered or the link being incorrect (where the link is entered into the function of the regular expression to verify that the way the link is written is correct). Then we check against the database to see if the link already exists. If it exists, the user is directed directly to it. if it doesn't exist then we create a new link token using Base62 in the hash URL function and send a number from the counter which is saved in the counter manager table we increment the counter number and then add the information to the database the reason we choose the counter method to generate the tokens is that the collision rate is zero. I could have chosen another way, such as taking the first six characters of each link, and this conflict happens most of the time because it is possible to enter a link with the same six characters at the beginning, but the difference in the characters after that, or it could have chosen the timing to do it in the first moment , I felt it's the best way instead of using the counter and consuming memory and time in the counter process but when I thought about it I found it crazy because we can't control the counters like how big they are, where they start and where they end and how we will expand later if we want to put the site on more than one server One, and this takes us to the thing that is not done yet, which is expansion, you can quickly expand the site and put other counters for each server or make an algorithm that automates the processes by limiting the number of each counter so there is no collision in the counters if the server is broken,now it's done Without taking into account the issue of expanding the site in more than one server, where only one counter was defined in the database.
    
            ***
            - ## *Retrieving links when you enter them in the search box*
                - ### When the user searches for the link through the search box, the connection reaches the root
                    `@app.route("/<short_url>")`  the take every operation after the / tag after the site name.
                    ***
                - ### **Process stages**
                    - We first search the database for the name of the url long, counter via the short link code, then the number of its counter is updated by 1 increment and the user is converted to url long.
            ***
            - ## *Check the number of clicks on links*
                - When the user searches for their link hit count, enter the short link and the result will appear for them.
                ***
            - ### **Process stages**
                - I searched for common errors as before and cut the text after the site name and (/) to find the short link code and searched for its counter in the database and submitted.
***

- ## **Currency Converter** 
    - This tool was designed and built using an API
        In the root of ` @app.route("/currency_converter", methods=["GET", "POST"]) ` I check the input as valid and send the input to the function ` def convert(convert_from, to, amount): ` in File `helpers.py`
        Basically, you have defined an environment variable inside the `env` file that holds the information of the private API key
        The request link for the website used to fetch currency information at its current prices has been defined
        I searched for the currencies by returning the `json` file with the current currency rates and with a few calculations the desired output was processed.
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
        - ### *The tool is built using ASCII table information for characters and symbols. Letters were replaced by fetching their numbers from the table and performing various arithmetic operations on them.* 
        ***
        - ##  *Caesar cipher*
            - ### **Process stages**
                - The encoding process relied on paraphrasing the character back to its number in the ASCII table and performing the calculation 
                `(n - 97 + key) 26% + 97`, where the number of the first character in the lowercase character string was reduced to determine what the character's order was in the original order and the key number was increased, Then fetch the remainder of dividing the number by 26 in order to locate the new character again after encoding in the original order and add 97 to locate the character in the ASCII table.
        ***
        - ##  *Substitution cipher*
            - ### **Process stages**
                - The encoding process relied on reformulating the character to its number in the ASCII table and performing a negative `n - 97` operation in order to locate the character in the original order, but it differs that the replacement is not by the ASCII table, but by the key sent from the user when the character is located in Alphabetical order is replaced by the position of the letter within the key and replaced by it.
        ***
        - ##  *Decoding - Caesar cipher*
            - ### **Process stages**
                - Decoding process: the most common linguistic adjective in a language (Frequency analysis)
                The complexity and cost of the algorithm for analyzing the most common character counting algorithm is `O(n)`. The tool is designed and optimized to take the first 300 characters of text if it is greater than it to reach the lowest cost, which is a sufficient number to find the most common character, where the complexity and cost of the algorithm is `O(1)` because the numbers are fixed and there are no variables where the whole process is `(26 * 300)` is equivalent to searching in 7800 characters in linear search.
***
- ## **QR Code Generator**
    - ### **In terms of design and technology used** :
        - It is built on the basis of the `flask_qrcode` library, this library takes the data to be converted into a QR image and returns the image in the `JINJA` template inside the `HTML` file, for example `src={{qrcode ( data, box_size = 10)}}` The image upload button is designed.
***
- ## **Contact Form**
    - ### **In terms of design and technology used** :
    - The tool is built with the `flask_mail` library where I specify the server to which it will be sent, specify the port number and save the mail and password information in environmental variables inside the `env` file. When the user sends a message, it calls the `Check_For_Infect_Words` function via the `better_profanity` library if there are inappropriate words, it returns `True` and the message is rejected, the second function `check_email` validates the email entry pattern using a regular expression and returns `True` If there is a typing error in the user's mail.
