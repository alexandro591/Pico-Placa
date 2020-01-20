# Pico-Placa
A program build in Python 3 to check if your car can be on the road of Quito, using the the old and new laws of Ecuador for "pico y placa".

## Example of use
You can find the example code inside the repository, but simply the program creates a PlacaEcuador object, which is a valid Ecuador plate in the format ABC0123 or ABC123 (not case sensitive), then it calls the methond of PlacaEcuador called canBeOnTheRoad, which consists of 3 inputs, the date, the time, and the rule "antigua" or "nueva" (optional). If this rule is not instanced, the default rule is "antigua".

The return of this method is a boolean, on which a true means that you CAN be on the road with the given variables or you CAN'T be on the road if it's false.