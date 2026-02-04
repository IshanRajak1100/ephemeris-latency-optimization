# STEP: README finalization
WHAT I DID: Finished a scoped, honest README covering problem, metrics, baselines, safety, and limitations.
WHY I DID IT: To lock scope and prevent feature creep before coding.
WHAT I LEARNED: Clear writing exposed design gaps early and simplified future implementation.

# STEP 1

I tried to make timestamps using loop 

so that i can save them in a new file in raw folder

i tried to make start_date = "2014-01-01" it failed becuase it is a string not a date

so  i import datetime and did datetime(2014,01,01) , it will also note the hours and seconds , i made a gap of 6 but later changed it to 3 hours because 6hour gap was too wide,but agin changed to 6 since 3 hours everything changes lesss according to panatery relativiy , so even dumb ml will learn it 

made a loop and using with open i made a file and saved it in there usinf a new func timedelta

 current_date += timedelta(hours=gap)
 from this we can do diffrence in time

 # stpe-2

 made a exampletimeframe to check baselien 2 if it can see the recent previous timestamp from it , firstt added all the timestamps into a timestamp list and then made a past list and looped through the timestamp list and added those timestamps to the past which were earlier than the example one, them just print the latest one

 # step-3
 we will make a csv file and store the positions there along with timestamps , so first we read the timestamps file and put all timestamps in a list