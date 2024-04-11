import pyautogui
import time

def type_string_with_delay(string,):
    """
    Simulate typing a string with a specified delay between key presses.

    Parameters:
    - string: The string to type.
    - delay: The delay between key presses (in seconds).

    Note: Adjust the delay based on your requirements.
    """
    for char in string:
        pyautogui.press(char)


# Example usage:
text_to_type = """"
nav{
width: 100%;
padding: 12px 10px;
background-color: aqua;
display: flex;
justify-content: space-around;
align-items:center;
}

.logo{
width: 300px;
}

.nav-value{

height: 100%;
display: flex;
align-items: center;


}

.nav-value span{
padding: 12px;
}

.nav-value span a{

text-decoration: none;
padding: 12px;

font-size:1.8rem;
}

#hero{
display: flex;
padding:0px 56px;
}

.hero-img{
background-color: rgb(91, 120, 120);
width: 900px;
height: 700px;
}

.textcont{
    width: 40%;
    
    margin: auto;
    display: flex;
    flex-direction: column;
   
}

.textcont h1{
    overflow-x: visible;
    width: 20%;
    font-size: 8rem;
    line-height: 75px;
    margin: 2rem 0rem;

}

.textcont p{
    font-size: 2rem;
}

.btn{
    padding: 9px 19px;
    font-size:1.8rem;
    margin: 18px 0px;
    background-color: white;
    border-radius:2px;
    width: fit-content;
    color: black;

    

}
"""
time.sleep(6)
type_string_with_delay(text_to_type)



