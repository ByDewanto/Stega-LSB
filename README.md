# README

this repository contains code and resources for steganography and setaganalysis. to put it simply to hide secret messages in images.

to extract the hidden message on pictures you used to save messages, you could use code from setganalysis folder.

to put it simply, steganography is to hide messages in pictures and steganalysis to extract it.

please note:

1. that this code is for educational purposes only. do not use it for illegal activities.
2. steganalysis code only works for pictures that were used to hide messages using the steganography code in this repository.

### Requirements

- python
- pillow

```bash
        pip install pillow
```

- docx

```bash
        pip install python-docx
```

## Steganografi

steganography code is in the steganography folder (/steganografi/steganography.py). is program to hide messages in pictures.

### How it works?

the program will change the least significant bit (LSB) of each pixel in the image to hide the message. since the LSB is the least significant bit, changing it will not significantly affect the appearance of the image.

### algortihm

1. open the image and convert it to RGB mode.
2. convert the message to binary.
3. the program will check if the message can fit in the image. if not, it will raise an error.
4. if the message can fit, it will proceed to hide the message in the image.
5. for each pixel in the image, change the LSB of each color channel (R, G, B) to the next bit of the message.
6. save the modified image.

## Staganalysis

### How it works?

the program will read the LSB of each pixel in the image to extract the hidden message. since the LSB is the least significant bit, it will contain the hidden message. may I remind you again that this code only works for images that were used to hide messages using the steganography code in this repository.

### algortihm

1. open the image and convert it to RGB mode.
2. read the LSB of each color channel (R, G, B) of each pixel in the image.
3. combine the LSBs to form the binary message.
4. convert the binary message to text.
5. save the extracted message to a text file or docx file.
