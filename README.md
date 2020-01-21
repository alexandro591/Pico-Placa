# Pico-Placa
A program build in Python 3 to check if your car can be on the road of Quito, using the the old and new laws of Ecuador for "pico y placa".

## Example of use
You can find the example code inside the repository, but simply the program creates a PlacaEcuador object, which is an Ecuador valid plate in the format ABC0123 or ABC123 (not case sensitive), then it calls the methond of PlacaEcuador called canBeOnTheRoad, which consists of 3 inputs, the date, the time, and the rule "antigua" or "nueva" (optional, not case sensitive). If this rule is not instanced, the default rule is "antigua".

The return of this method is a boolean, on which a true means that you CAN be on the road with the given variables or you CAN'T be on the road if it's false.

## Considerations
- The plate is a string that has to be an Ecuador valid plate which contains only numbers and letters.
    **Example:** _"ABC0123"_
- The date is a string in the format dd-mm-YY.
    **Example:** _"28-02-2016"_
- The time is a string in format of 24h.
    **Example:** _"14:55"_
- The rule and the valid Ecuador plate are NOT case sensitive.
    **Example:** _"nueva"="Nueva", "UKY0652"="uky0652"_
- The valid Ecuador plate can either be in the new format or the old format.
    **Example:** _"UKY0652"="UKY652"_
- The time is inclusive, either if you use the new or old law.
    **Example:** _a car at 19:30 with the new law, in the case that the plate falls inside the date of "pico y placa" can't be on the road, also at 16:00, 9:30 and 7:00_

## Automated testing software
The repository contains an automated testing software for placaEcuador written in python, that creates a random day and time, and a random rule, and tests it an n number of times.

## Instalation
You can clone the repository and use the _placaEcuador.py_ file or you can just simply install it by typing:
```
python3 -m pip install placaEcuador
```
Run the _example.py_ file to test.

### Author
A program created by Andrés Alexandro Tapia Flores<br/>
[package link](https://pypi.org/project/placaEcuador)<br/>
[whatsapp: 0998775709](https://wa.me/593998775709)<br/>
[email: alexandrotapiaflores@gmail.com](mailto:alexandrotapiaflores@gmail.com)<br/>
[website](https://andrestapia.netlify.com)