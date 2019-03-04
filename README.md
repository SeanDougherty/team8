How to operate this simulator:

This simulator is operated from the command line using python3

An example execution is shown below

```
$ python3 main.py TestData_2_19_2019_proprietary-e.csv 50000 25000 1000
```


Further details on the command line arguments are as follows

```
$ python3 main.py {csvDataFilePath} {ProcessingRate aka PacketsProcessedPerSecond} {desiredBufferSize} {desiredRunTime in seconds}
```

{csvDataFilePath}

Currently there is not support for pulling live data from the web. In order to test data not included in the repository, visit www.marketdatapeaks.net and download a csv of their market data.

{ProcessingRate}

For this iteration of the program, we concern ourselves with how many packets a single processing unit can process in 1 given second. 
In future iterations we will take Processing Rate as a function of nanoseconds per packet.

{desiredMaxBufferSize}

In future iterations we will report the number of packets lost when a buffer overflow occurs.

{desiredRunTime}

This is how many seconds you would like to simulate. Currently, the max # of seconds is 60 x (# of data rows). This doesn't allow for the program to run until the buffer is cleared and is most definitely a bug noted by the developers. This bug is of high priority and will be addressed during the next sprint.