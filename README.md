# Pico-Placa
A program build in Python 3 to check if your car can be on the road of Quito, using the the old and new laws of Ecuador for "pico y placa".

## Example of use
You can find the example code inside the repository, but simply the program creates a PlacaEcuador object, which is a valid Ecuador plate in the format ABC0123 or ABC123 (not case sensitive), then it calls the methond of PlacaEcuador called canBeOnTheRoad, which consists of 3 inputs, the date, the time, and the rule "antigua" or "nueva" (optional, not case sensitive). If this rule is not instanced, the default rule is "antigua".

The return of this method is a boolean, on which a true means that you CAN be on the road with the given variables or you CAN'T be on the road if it's false.

## Considerations
- The date is a string in the format dd-mm-YY
    **Example:** _"28-02-2016"_
- The time is a string in format of 24h
    **Example:** _"14:55"_
- The rule and the valid Ecuador plate are NOT case sensitive.
    **Example:** _"nueva"="Nueva", "UKY0652"="uky0652"_
- The valid Ecuador plate can be in the old format or the new format.
    **Example:** _"UKY0652"="UKY652"_

The program can achive a 