#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Amtrak Code for Final Project
# Name: James Berardini
# Date: 03/13/2022


# In[ ]:


# pip install hiredis or pip3 install redis
import redis

# Connection string to redislabs.com free 30 mb database.
r_connect = redis.Redis(host='redis-19467.c60.us-west-1-2.ec2.cloud.redislabs.com', port=19467, password='aYK111tVKQBHMF1FdAGBU5v6k5oTee4X')
# Create train stations
r_connect.hmset('BAR', {'name':'Barstow, CA','address':'685 North First Avenue','type': 'Platform with Shelter'})
r_connect.hset('BFD', 'name', 'Bakersfield, CA')
r_connect.hset('BFD', 'address', '601 Truxton Avenue')
r_connect.hset('BFD', 'type', 'Station Building (with waiting room)')
r_connect.hmset('BKY', {'name':'Berkeley, CA','address':'700 University Avenue','type': 'Station Building (with waiting room, wifi and cafe)'})
r_connect.hmset('ANA', {'name':'Anaheim, CA','address':'2626 East Katella Avenue','type': 'Station Building (with waiting room, wifi and cafe)'})
r_connect.hmset('BUR', {'name':'Burbank, CA','address':'3750 Empire Avenue','type': 'Platform with Shelter'})
r_connect.hmset('CIC', {'name':'Chico, CA','address':'450 Orange Street','type': 'Platform only (no shelter)'})
r_connect.hmset('COX', {'name':'Colfax, CA','address':'99 Railroad Street','type': 'Station Building (with waiting room)'})
r_connect.hmset('DAV', {'name':'Davis, CA','address':'840 Second Street','type': 'Station Building (with waiting room, wifi and cafe)'})
r_connect.hmset('FMT', {'name':'Fremont, CA','address':'37260 Fremont Boulevard','type': 'Station Building (with waiting room)'})
r_connect.hmset('FNO', {'name':'Fresno, CA','address':'2650 Tulare Street','type': 'Station Building (with waiting room)'})
r_connect.hmset('FUL', {'name':'Fullerton, CA','address':'120 East Santa Fe Avenue','type': 'Station Building (with waiting room, wifi and cafe)'})
r_connect.hmset('GAC', {'name':'Santa Clara, CA','address':'5099 Stars and Stripes Drive','type': 'Platform only (no shelter)'})
r_connect.hmset('GDL', {'name':'Glendale, CA','address':'400 West Cerritos Avenue','type': 'Platform with Shelter'})
r_connect.hmset('GVB', {'name':'Grover Beach, CA','address':'180 West Grand Avenue','type': 'Platform with Shelter'})
r_connect.hmset('HAY', {'name':'Hayword, CA','address':'22555 Meekland Avenue','type': 'Platform with Shelter'})
r_connect.hmset('HNF', {'name':'Hanford, CA','address':'200 Santa Fe Avenue #A','type': 'Station Building (with waiting room)'})
r_connect.hmset('IRV', {'name':'Irvine, CA','address':'15215 Barranca Parkway','type': 'Station Building (with waiting room, wifi and cafe)'})
r_connect.hmset('LAX', {'name':'Los Angeles, CA','address':'800 North Alameda Street','type': 'Station Building (with waiting room)'})
r_connect.hmset('LPS', {'name':'Lompoc-Surf, CA','address':'Ocean Ave and Park Rd','type': 'Platform with Shelter'})
r_connect.hmset('MPK', {'name':'Moorpark, CA','address':'300 High Street','type': 'Platform only (no shelter)'})
r_connect.hmset('OKJ', {'name':'Oakland, CA','address':'245 Second Street','type': 'Station Building (with waiting room, wifi and cafe)'})
r_connect.hmset('OLT', {'name':'San Diego, CA','address':'4005 Taylor Street','type': 'Platform only (no shelter)'})
r_connect.hmset('ONA', {'name':'Ontario, CA','address':'198 East Emporia Street','type': 'Platform only (no shelter)'})
r_connect.hmset('OSD', {'name':'Oceanside, CA','address':'235 South Tremont Street','type': 'Station Building (with waiting room)'})
r_connect.hmset('OXN', {'name':'Oxnard, CA','address':'201 East Fourth Street','type': 'Station Building (with waiting room)'})
r_connect.hmset('PLS', {'name':'Pleasanton, CA','address':'4950 Pleasanton Avenue','type': 'Platform with Shelter'})
r_connect.hmset('POS', {'name':'Pomona, CA','address':'100 West Commercial Street','type': 'Platform only (no shelter)'})
r_connect.hmset('PRB', {'name':'Paso Robles, CA','address':'800 Pine Street','type': 'Platform only (no shelter)'})
r_connect.hmset('PSN', {'name':'Palm Springs, CA','address':'North Indian Canyon Drive and Palm Springs Station Road','type': 'Platform with Shelter'})
r_connect.hmset('RDD', {'name':'Redding, CA','address':'1620 Yuba Street','type': 'Platform with Shelter'})
r_connect.hmset('RIV', {'name':'Riverside, CA','address':'4066 Vine Street','type': 'Platform with Shelter'})
r_connect.hmset('RLN', {'name':'Rocklin, CA','address':'Rocklin Rd. and Railroad Ave.','type': 'Station Building (with waiting room, wifi and cafe)'})
r_connect.hmset('SAC', {'name':'Sacramento, CA','address':'401 I Street','type': 'Station Building (with waiting room, wifi and cafe)'})
r_connect.hmset('SAN', {'name':'San Diego, CA','address':'1050 Kettner Boulevard','type': 'Station Building (with waiting room)'})
r_connect.hmset('SBA', {'name':'Santa Barbara, CA','address':'209 State Street','type': 'Station Building (with waiting room)'})
r_connect.hmset('SCC', {'name':'Santa Clara, CA','address':'1001 Railroad Avenue','type': 'Platform with Shelter'})
r_connect.hmset('SIM', {'name':'Simi Valley, CA','address':'5050 Los Angeles Avenue','type': 'Platform only (no shelter)'})
r_connect.hmset('SJC', {'name':'Santa Jose, CA','address':'65 Cahill Street','type': 'Station Building (with waiting room)'})
r_connect.hmset('SKN', {'name':'Stockton, CA','address':'735 South San Joaquin Street','type': 'Station Building (with waiting room)'})
r_connect.hmset('SKT', {'name':'Stockton, CA','address':'949 East Channel St.','type': 'Platform with Shelter'})
r_connect.hmset('SNA', {'name':'Santa Ana, CA','address':'1000 East Santa Ana Boulevard','type': 'Station Building (with waiting room, wifi and cafe)'})
r_connect.hmset('SNB', {'name':'San Bernardino, CA','address':'1170 West Third Street','type': 'Station Building (with waiting room)'})
r_connect.hmset('SNC', {'name':'San Juan Capistrano, CA','address':'26701 Verdugo Street','type': 'Station Building (with waiting room)'})
r_connect.hmset('SNP', {'name':'San Clemente Pier, CA','address':'615 Avenida Victoria','type': 'Platform only (no shelter)'})
r_connect.hmset('SNS', {'name':'Salinas, CA','address':'11 Station Place','type': 'Station Building (with waiting room)'})
r_connect.hmset('SOL', {'name':'Solana Beach, CA','address':'105 North Cedros Avenue','type': 'Station Building (with waiting room)'})
r_connect.hmset('VEC', {'name':'Ventura, CA','address':'39 East Harbor Blvd','type': 'Platform with Shelter'})
r_connect.hmset('VNC', {'name':'Ventura, CA','address':'7724 Van Nuys Boulevard','type': 'Station Building (with waiting room)'})
r_connect.hmset('VRV', {'name':'Victorville, CA','address':'16858 South D Street','type': 'Platform only (no shelter)'})
r_connect.hmset('', {'name':', CA','address':'','type': ''})



# Inserting schedule data from sheets:
r_connect.zadd("BFD:594", {"07:08A": 0, "09:04A": 1, "02:03P": 2, "07:20P": 3})
r_connect.zadd('BKY:588', {'08:10A':0,'10:09A':1,'03:09P':2,'08:18P':3})
r_connect.zadd('BUR:784', {'09:17A':0,'11:15A':1,'04:21P':2,'09:27P':3})
r_connect.zadd('FUL:794', {'06:41A':0,'07:41A':1,'10:41A':2,'11:41A':3,'12:41P':4,'03:41P':5,'05:41P':6,'06:41P':7,'07:41P':8,'10:51P':9})
r_connect.zadd('GDL:794',{'09:29A':0,'11:26A':1,'04:34P':2,'09:38P':3})
r_connect.zadd('GVB:594', {'04:25A':0,'06:31A':1,'11:05A':2,'04:42P':3})
r_connect.zadd('IRV:770', {'07:12A':0,'08:12A':1,'11:12A':2,'12:12P':3,'01:12P':4,'04:12P':5,'06:12P':6,'07:12P':7,'08:12P':8,'11:22P':9})
r_connect.zadd('LAX:770', {'09:46A':0,'11:43A':1,'04:48P':2,'06:40P':3,'09:56P':4})
r_connect.zadd('LPS:794',{'07:21A':0,'05:31P':1})
r_connect.zadd('MPK:794',{'08:24A':0,'10:23A':1,'03:23P':2,'08:34P':3})
r_connect.zadd('OLT:588',{'08:50A':0,'09:50A':1,'12:53P':2,'01:53P':3,'02:50P':4,'05:50P':5,'07:50P':6,'08:50P':7,'09:50P':8,'01:00A':9})
r_connect.zadd('OSD:770',{'08:05A':0,'09:05A':1,'12:08P':2,'01:08P':3,'02:05P':4,'05:05P':5,'07:05P':6,'08:05P':7,'09:05P':8,'12:15A':9})
r_connect.zadd('OXN:784',{'07:57A':0,'09:55A':1,'02:53P':2,'04:35P':3,'08:05P':4})
r_connect.zadd('RLN:594',{'05:25A':0,'12:10P':1})
r_connect.zadd('SAN:794',{'09:04A':0,'10:04A':1,'01:07P':2,'02:07P':3,'03:04P':4,'06:04P':5,'08:04P':6,'09:04P':7,'10:04P':8,'01:14A':9})
r_connect.zadd('SBA:588',{'06:30A':0,'08:46A':1,'01:25P':2,'07:01P':3})
r_connect.zadd('SIM:588',{'08:41A':0,'10:39A':1,'03:39P':2,'08:51P':3})
r_connect.zadd('SNA:770',{'07:01A':0,'08:01A':1,'11:01A':2,'12:01P':3,'01:01P':4,'04:01P':5,'06:01P':6,'07:01P':7,'08:01P':8,'11:11P':9})
r_connect.zadd('SNC:594',{'07:26A':0,'08:26A':1,'11:25A':2,'12:25P':3,'01:26P':4,'04:26P':5,'06:26P':6,'07:26P':7,'08:26P':8,'11:36P':9})
r_connect.zadd('SNP:770',{'06:39A':0,'08:31A':1,'01:31P':2,'06:44P':3})
r_connect.zadd('SOL:770',{'08:20A':0,'09:20A':1,'12:23P':2,'01:23P':3,'02:20P':4,'05:20P':5,'07:20P':6,'08:20P':7,'09:20P':8,'12:30A':9})
r_connect.zadd('VNC:784',{'07:39A':0,'09:38A':1,'02:34P':2,'04:10P':3,'07:45P':4})
r_connect.zadd('HNF:770',{'08:53A':0,'10:52A':1,'03:52P':2,'09:08P':3})
r_connect.zadd('DAV:588',{'08:59A':0,'04:05P':1})
r_connect.zadd('RDD:594',{'09:09A':0,'11:07A':1,'04:13P':2,'09:19P':3})
r_connect.zadd('POS:588',{'11:38A':0,'12:38P':1})
r_connect.hmset('770', {'type':'Pacific Surfliner','region':'Southern California'})
r_connect.hmset('588', {'type':'California Zephyr','region':'Northern California'})
r_connect.hmset('594', {'type':'Pacific Surfliner','region':'Southern California'})
r_connect.hmset('770', {'type':'Pacific Surfliner','region':'Southern California'})
r_connect.hmset('794', {'type':'Pacific Surfliner','region':'Southern California'})
r_connect.hmset('784', {'type':'California Zephyr','region':'Central California and Chicago'})


import redis
# Connection string to redislabs.com free 30 mb database.
r_connect = redis.Redis(host='redis-19467.c60.us-west-1-2.ec2.cloud.redislabs.com', port=19467, password='aYK111tVKQBHMF1FdAGBU5v6k5oTee4X')


# Business Problem #1 addressed:
# For a station, what departure times are available and what train number do I take?
print ("Lookup Departure Times and Train Number.")
station_code = input ("Enter Station Code :")

# lookup station name in redis with station code, convert to upper case.
station_name = r_connect.hget(station_code.upper(), 'name')
if station_name:
    # convert redis byte type to utf character set.
    station_name = station_name.decode('utf-8')
    print(station_name)
    
    # Query by key name for existence of a train schedule.  Format is Station code:train number (IRV:770)
    key_code_train = (r_connect.keys (station_code.upper() + ':*'))
    # if they're no available times then go to else.
    if len(key_code_train) > 0:
        # for each found train code with train number:
        for item in key_code_train:
            # Query for all arrival times in sorted set.  
            l_arrival_times = r_connect.zrange(item.decode('utf-8'),0,-1)
    
            train_key = item.decode('utf-8')
            # Split the key to get the train number and print it.
            train_key = train_key.split(":")
            print ("Train Number " + str(train_key[1]))
   
            # Loop and print each arrival time.
            for item in l_arrival_times:
                print (item.decode('utf-8'))
    else:
        print ("There are no available train times for " + str(station_name) + ".")
else:
    print ("Invalid train station code.")


# Business Problem #2 addressed:
# Whats the address for a station?
print ("Address Lookup for a Station.")
station_code_input = input ("Enter Station Code :")
station_code = station_code_input.upper()
station_name = r_connect.hget(station_code, 'name')
if station_name:
    print ("The address for " + str(station_code) + " station is:")
    
    address =  r_connect.hget(station_code,'address')
    
    address = address.decode('utf-8')
    print (address)
    
    station_name = station_name.decode('utf-8')
    print(station_name)
      
else:
    print ("Invalid train station code.")


# Business Problem #3 addressed:
# Find all available times for a given hour by train number. Dispalay station names with times:

# Scan the keys for any key with a colon and iterate through.
l_train_schedules = []
s_train_number = {''}
for redis_key in r_connect.scan_iter("*:*"):
    # Loading all train schedule keys for processing.
    
    l_train_schedules.append(str(redis_key.decode('utf-8')))
    # convert to string or correct character set
    train_number = redis_key.decode('utf-8')
    # split the key to get the train number.
    train_number = train_number.split(":")[1]
    # Create a set of unique train numbers.
    s_train_number.add(str(train_number))

# Display all unique train numbers.
print ("Available train numbers are the following:")
for train_number in s_train_number:
    print (train_number)
    
# prompt for a train number
train_number_input = input ("Enter a train number:")
hour_input = input ("Enter an hour (1-12) in 2 digit format: (Example: 08):")
ampm_input = input ("Enter A (AM) or P (PM):")

print ("")
print ("Train Station Code          Train Number         Departure Time")
    
# iterate through all train schedules - Example IRV:770 
for schedule in l_train_schedules:

    # If we find a matching train number  
    if schedule.split(":")[1] == train_number_input:
       
        # From Redis database get all of the departure times.
        l_departure_times = r_connect.zrange(schedule,0,-1)
       
        # For each dpearture time match the time and am or pm.
        for depart_time in l_departure_times:
            
            # item.decode('utf-8'))[:2] is the first two digits of the time
            # item.decode('utf-8')[-1] is the am or pm of the time.        
            # If the first 2 digits match the time and the am or pm match then print it.
            if str(depart_time.decode('utf-8'))[:2] == hour_input and depart_time.decode('utf-8')[-1] == ampm_input.upper(): 
                print ("        " + str(schedule.split(":")[0]) + "                    " +                                      str(schedule.split(":")[1]) +  "                  " +                                      str(depart_time.decode('utf-8')))
                

# Pseduo code:   
# Ask for a train number
# Enter hour: Ask for departure time in Hours and Am or PM.
# find all train stations with that number
# Get all times for each train code and matching number.
# search times for given hour.
# Print Station, times and train number




# Business Problem #4 addressed:
# Whatare the station amenities for various stations?
print ("Station Amenities:")

s_station_type = {''}
l_station_code = []

for redis_key in r_connect.scan_iter():
    # Loading all train schedule keys for processing.
    if redis_key.isalpha():
        
        # appending station codes to a list for later lookups below 
        l_station_code.append(redis_key)
        # get station types by station code 
        station_type = r_connect.hget(redis_key.upper(), 'type')
        # Create a set of unique station types for displaying to the user.
        s_station_type.add(str(station_type.decode('utf-8')))
    
# counter is used to assign a number for each unique type
counter = 0
# were printing a selection of station type for the user.
for amenity in s_station_type:
    if counter > 0:
        print (str(counter) + ".)  " + str(amenity))
    counter += 1
    
print ("")
# Ask the user to pick one of the station types.
station_type_number = input ("Enter a number for the station type:")
# convert station_type_number to int so we can use it as a subscript.
station_type_number = int(station_type_number)

# Sets can't be accessed with a subscript so I'm assigning to a list to grab the user's selection of 1 through 4.
l_station_type = list(s_station_type)

print #
# printing station types for the user.
print ( "For " + "\"" + str(l_station_type[station_type_number]) + "\"" + " the following stations are available:" )
 
# sorting stations codes so they print out sorted.
l_station_code.sort()    
# for each station code look up type
for station_code in l_station_code:
   
    # In redis lookup the station type by the station code. Stored as hash table
    station_type = r_connect.hget(station_code.upper(), 'type')
    # if the selected station type is equal to the sorted list of station types.
    if station_type.decode('utf-8') ==  l_station_type[station_type_number]:
        station_name = r_connect.hget(station_code.upper(), 'name')
        station_code = station_code.decode('utf-8')
        print (str(station_code.upper()) + "   " + str(station_name.decode('utf-8')))
       

