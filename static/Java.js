import Country from ".//CountriesNamesAndCurrencies.json" assert {type: 'json'};

function GetNameCountries () {
    let CountriesName = document.querySelector("#CountriesName");
    console.log(CountriesName);
    for (const [key, value] of Object.entries(Country.CountriesName)) {

        let Element = document.createElement("option");
        let Attr = document.createAttribute(`value`);
        let Text = document.createTextNode(`${ key } - ${ value }`);

        Element.setAttributeNode(Attr);
        Element.setAttribute("value", value);
        Element.appendChild(Text);

        CountriesName.appendChild(Element);
        
    }
}

function GetNameCurrencies () {
    let CurrenciesName = document.querySelectorAll("#CurrenciesName");

    for (const [key, value] of Object.entries(Country.CurrenciesName)) {

        let Element = document.createElement("option");

        let Attr = document.createAttribute(`value`);
        let Text = document.createTextNode(`${ key } - ${ value }`);

        Element.setAttributeNode(Attr);
        Element.setAttribute("value", key);
        Element.appendChild(Text);

        CurrenciesName[0].appendChild(Element);
        let Element2 = Element.cloneNode(true);
        CurrenciesName[1].appendChild(Element2);
    }
}

function Caesar () {
    let key = document.querySelector("#key");
    let select = document.querySelector("#select");
    let cipher_decrypt = document.querySelector("#cipher_decrypt");
    
    cipher_decrypt.style.display='none';
    select.addEventListener('click', function() { 
        if (select.value == "digital") {
            document.querySelector('#feedback1').innerHTML = '&#9989;  You must enter a text and a numeric key.';
            document.querySelector('#feedback2').innerHTML = '&#9989;  To decrypt the text with the key, enter the ciphertext and the key preceded by a negative sign (-).';
            key.style.display='block';
            cipher_decrypt.style.display='none';
        }

        else if (select.value == "letters") {
            document.querySelector('#feedback1').innerHTML = '&#9989;  You must enter text and a key of 26 uppercase or lowercase characters must be entered without repetition.';
            document.querySelector('#feedback2').innerHTML = '';
            key.style.display='block';
            cipher_decrypt.style.display='block';
        }

        else if (select.value == "digital_decoding") {
            document.querySelector('#feedback1').innerHTML = '&#9888;  Decryption only if the cipher used was Caesar digital cipher.';
            document.querySelector('#feedback2').innerHTML = '&#9888;  Text less than 140 characters, 23 words or close to two sentences is difficult to decipher, it depends on the context and the length of the words.';
            key.style.display='none';
            cipher_decrypt.style.display='none';
        }

        else {
            document.querySelector('#feedback1').innerHTML = '';
            document.querySelector('#feedback2').innerHTML = '';
            key.style.display='block';
            cipher_decrypt.style.display='none';
        }
    });
}

function CopyText () {

const CopyButton = document.getElementById("CopyButton");

if (CopyButton != null) {
    CopyButton.addEventListener("click", () =>  {
    const copyText = document.getElementById("Text");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyText.value);
    ("Copied the text: " + copyText.value);
    });
}
}

const Page = document.body.className;

window.addEventListener("load", _ => {
switch (Page) {
    case "currency":
        GetNameCurrencies();
        break;
    case "contact":
        GetNameCountries();
        break;
    case "caesar":
        Caesar();
        CopyText();
        break;
    case "url_shortener":
        CopyText();
        break;
}
})

let Text = document.querySelector("#writing");
let TextArray = ["We care about the customer", "We care about product quality",
 "We are trustworthy", "All rights are save", "Do not hesitate to contact us"];

let TextIndex = 0;
let CharIndex = 0;

function Typing() {
    if (CharIndex < TextArray[TextIndex].length) {
        Text.textContent += TextArray[TextIndex].charAt(CharIndex);
        CharIndex++;
        setTimeout(Typing, 200);
    }
    else {
        setTimeout(Erasing, 2000);
    }
}

function Erasing() {
    if (CharIndex > 0)
    {
        Text.textContent = TextArray[TextIndex].substring(0, CharIndex -1);
        CharIndex--;
        setTimeout(Erasing, 100);
    }
    else
    {
        TextIndex++;
        if (TextIndex >= TextArray.length)
        {
            TextIndex = 0;
        }
        setTimeout(Typing, 1500);
    }
}

setTimeout(Typing, 2000);

let loader = document.getElementById("Page_loader");

window.addEventListener("load", _ => {
    loader.style.display = "none";
})
 
