Sensor challenge

Create a library/binary/script that will be able to read a list of sensor measurements from stdin and print for each sensor how many values are above provided thresholds.
The input consists of n lines.
The first line of the input represents the number of sensors. 
The second line represents the thresholds the values of each sensor must be above.
The next n-2 lines represent the values of each sensor per minute.
For each sensor, calculate how many values are above each thresholds and print them.

Example

2 9
45 46 47 48 52 60
S1 34 45 18 20 35 40 50 65 75
S2 87 89 80 78 90 38 32 45 58

The first line of the provided input are the numbers 2 and 9. This means that 2 lines of  9 sensor measurements for each line are going to follow.
The second line contains a list of the thresholds that the sensor values should be above.
The next two lines contain the sensors and sensor values.
For each sensor, count how many values are above each threshold value and print them on stdout.

E.g. 

for S1 and the first threshold 45, the count of values of S1 above 45 are 3 (50, 60, 75)
for S1 and the second threshold 46, the count of values of S1 above 46 are 3 (50, 60, 75)
…
for S2 and the last threshold 60, the count of values of S2 above 60 is 1 (75).

For the above example, the output would be the following:

Input
2 9
45 46 47 48 52 60
S1 34 45 18 20 35 40 50 65 75
S2 87 89 80 78 90 38 32 45 58

Output
S1 3 3 3 3 2 2
S2 6 6 6 6 6 5

**NOTE ** Make sure you have covered all edge cases and the code you provide is documented, well tested and (of course) passes tests. Modular and readable code is important too. Upload the sources on a public repository with instructions and give us the link.

**BONUS** As the number of sensors and number of measurements can become too large (E.g. 10000 sensors, 200 values per sensor) find a way to optimize this problem and make it run fast even for 10000 sensors, 200 values per sensor). You can test the performance of your implementation using the file data.txt.
