# Font_Extractor
Really simple python script to extract every character of a monospace font from an image


## How to make the script work ? 

### What is the use of the script

From an image of the characters of a font, **which has to be monospace**, it will automatically create a folder with an image for each character. 
Input image exemple :

![image Char Screen](https://github.com/AxelThevenot/Font_Extractor/blob/master/font_images/%7BCourier%20Prime%7D_%7BABCDEFGHIJKLMNOPQRSTUVWXYZ.-()0123456789_%7D.png)

Output images exemple :

![char A](https://github.com/AxelThevenot/Font_Extractor/blob/master/font_extracted/Courier%20Prime/%5BA%5D.png)

![char B](https://github.com/AxelThevenot/Font_Extractor/blob/master/font_extracted/Courier%20Prime/%5BB%5D.png)

![char C](https://github.com/AxelThevenot/Font_Extractor/blob/master/font_extracted/Courier%20Prime/%5BC%5D.png)

![char _](https://github.com/AxelThevenot/Font_Extractor/blob/master/font_extracted/Courier%20Prime/%5B_%5D.png)

### How to use it 
#### Google Slide or whatever to create an image

First we need to know exactly what are height dimension in pixel we want for each character's image. For exemple let's say we want images with 128 pixels height and make it very long. 

Go to google slide or equivalent.

Then change the dimension of the page as I made for exemple on [this slide](https://docs.google.com/presentation/d/1MTCx6Kiezsvf7npga9RZpKJuVV9khNg-E8gGzddzc_Q/edit?usp=sharing).

![Google Slide Screen](https://github.com/AxelThevenot/Font_Extractor/blob/master/google_slide_scren.png)

Be sure the font you choose is a monospace one

Then write all the characters you can as above 

![image Char Screen](https://github.com/AxelThevenot/Font_Extractor/blob/master/image_char_screen.png)

Be sure the starting block of the first character is bordered the slide and the last character is taking all the horizontal block (for exemple the _ char on the the image)

Then export it to .png image with the `{Font Name}_{ALL_THE_CHARS}.png` as instance: `{Courier Prime}_{ABCDEFG_}.png` by copy pasting the char written in the slide. 

And finally move the image into the `font_images/` folder and run the python script.

```
python3 font_extractor.py
```

You can change the parameter on the top of the script for example for the `SIZE = (64, 128)` by default. 
