
Practical OSINT Investigation - Airplanes, Airspace Monitoring
Veda Prakash Chintha; SRH University of Berlin for Applied Sciences; Berlin, Germany
 
Abstract
The dawn of Information Technology (IT) led to ever-increasing exchange of information/data between people publicly. This data is stored in repositories around the world, and anyone is free to access it as and when one desired to do so. 
Here lies an opportunity to analyze this publicly available information to gather insights such as patterns or sentiments etc. These insights can be used to satisfy particular requirements by implementing targeted actions. 
One such opportunity in the aviation sector is to monitor the airspace i.e., the number, type, flight and carrier information of aircraft flying over a specific geo-space and identify patterns. This is useful to air traffic controllers, for example, to efficiently guide the traffic. This paper focuses on monitoring the airspace around Ukraine between November 2022 and January 2023 and understanding the air activity of various air forces that were active in the region. The outcome of the study is that the United States Air Force (USAF) was the most active, followed by the Royal / British Air Force.
Keywords: OSINT, Airspace, Monitoring, ADS-B, Satellite Tracking.
OSINT
Open Source Intelligence (OSINT), is the collection, analysis, and dissemination of information that is available to the general public or can be obtained through open sources. These sources can include publicly available information from news articles, social media, government reports, academic research, and other publicly available sources. OSINT is often used by government agencies, law enforcement, private investigators, and security professionals to gather intelligence on individuals, groups, or activities of interest. However, OSINT is also increasingly used by businesses, journalists, and researchers to gain insights into competitors, market trends, and public sentiment. OSINT can be used to identify potential threats, assess risk, and make informed decisions. It is an important tool for intelligence gathering and analysis in the digital age, where information is readily available online and can be leveraged for a variety of purposes.
Types of Data for OSINT [1]
As the OSINT is performed on data available in public domains, the data sources are divided into six major categories:
A.	Media
The Information available in newspapers, magazines, television and radio, which can be accessed throughout the world [1].
B.	Internet
Any information that can be accessed using the internet falls under this category. These include online media, publications, news channels, blogs, and social media (Facebook, Instagram, Twitter, YouTube, Reddit etc.). Information gathered by individuals in the form of pictures, videos and voice notes that are posted on social media websites also fall under this category [].
Due to its ease of accessibility and facility for quick uploads, the internet gathers data at a faster pace than other information repositories/sources as the contribution comes from everyone that can access the internet [1].
C.	State Data
Information released by government organizations for the public such as NASA releasing mission reports, the central government releasing national yearly budgets, courts publishing hearings on national matters, telecom organizations issuing telephone directories, the government issuing information in press conferences etc. This can also include the information made available in the internet, election campaign or speeches [1]. 
D.	Scientific Publications
Professional and educational organizations generate a lot of intellectual information from their respective scientific research. Most of this information is published publicly in the form of scientific publications, papers, theses etc., [1].
E.	Commercial Data
Companies specialized in gathering information for commercial purposes, such as satellite imagery, newsletters, financial reports etc. This information can be used to estimate the direction of industries [1].
F.	Grey Information
Information that does not fall into any above-mentioned categories such as non-scientific technical reports, unfinished informatics, technologically controlled patents, any business-related documents etc., [1].
History of OSNIT
William Donovan, a reputed lawyer, and a veteran of the American armed forces was generally credited with the creation of an intelligence department in the American government in 1941. This department served as a precursor to the Central Intelligence Agency (CIA). With the rapid advent of the IT sector, there was a need to dedicate specific resources to monitoring the data from open sources and interpreting hidden intelligence information. This led to the creation of the Directorate of National Intelligence’s Open-Source Center (OSC) [2].
OSINT is mainly used to serve a nation’s security, however, national security must be seen as a ‘public good’, i.e., to serve non-state security interests such business or competitive intelligence. Therefore, private non-state organizations, under government supervision, perform such tasks [7].
One example of the tasks is to predict market behavior based on user and provider sentiment.
Advantages of OSINT
•	Timely and Fast [4]: 

As per ‘worldpolulationreview’, over 69% of the world’s population or 4.9 billion people have access to the internet. This number is set to grow by 4% or 196 million every year. In addition, it is expected that by the end of 2023, 6.8 billion unique smartphone users to exist.

Search engines like Google and Bing and social media platforms like Twitter, Facebook and Reddit have made any information accessible worldwide within seconds of being posted. This has enabled anyone with a smartphone and an internet connection to send real-time information.

This becomes a valuable source of information for the OSINT community.

•	Cheap [4]:

Open sources are often free to use. However, the collection of information from the sources could be an expensive affair. For example, Flightrdar24 website is free for anyone who visits the website, however, for the website, it costs millions of dollars to make the information available on the website. This can limit the amount of information that can be available for free.

•	Shareable [4]:

The intelligence obtained from open sources are shareable with coalition partners, for example, the USA and British intelligence department can share information with each other acquired from open sources.
Types of OSINT
•	Imagery Intelligence (IMINT) [4]: 

Planet Labs, Sentinel Hub and Google Earth are a few examples of commercial geographic information systems (GIS) providers, which provide satellite imagery of the planet.

These provide geo-images for free or for a price that can contain detailed topographic information and the artefacts placed on them. There have been instances in the past where an entire air defense network deployment of the USA in the Middle east was identified from the images released by these GIS companies (see Figure 1).

These images were of such high quality that the type of equipment and their make were also identifiable from those images.

 
Figure 1: Patriot Air Defense Systems Located using IMINT. [Image source: Ref. [4]]

•	Signals Intelligence (SIGINT) [4]:

This is the intelligence acquired from communication interception, such as Automatic Information System (AIS) and Automatic Dependent Surveillance-Broadcast (ADS-B, discussed below).

AIS is a system that has been created to track and monitor shipping vessels using their AIS transponders’ broadcasting. This information is freely made available to the public by websites such as Marine Traffic, Vessel Finder etc. However, the AIS system’s reliability has always been debatable, because, the identity of vessels could be easily manipulated or simply switched off (military). However, the majority of the information available from AIS is a valuable resource for OSINT collectors,

 
Figure 2: AIS Vessel Tracking [Image source: [9]]
•	Human Intelligence (HUMINT) and Social Media Intelligence (SOCMINT) [4]:

This is the intelligence gathered from information that the general public publish/post on social media websites such as Twitter and Facebook.
For example, it is possible to identify the geolocation based on just the image by analyzing the surroundings from the image This method is being extensively used by both Ukrainian and Russian forces to locate their targets, in the ongoing war.
By collecting and analyzing the tweets, images and videos posted by people in the vicinity of the conflicts, it is possible to understand the situation on ground in the areas of conflicts, which greatly benefits the rescue/supply missions (see Figure 3).

  
Figure 3: Conflict Areas Identified Using SCOMINT [Image Source: Eyes on Russia Map]
OSINT Challenges [4]:
Even though OSINT seem to be a simple concept, implementation requires analysts to be proficient in computer skills and also possess a knack for searching for information online. Additionally, it is simply not possible for individual analysts to gather and mine the information alone and requires a team of greatly skilled, invested and motivated personnel. 
With the amount of information available on the internet, it is also a daunting task for individuals and teams to collect, store and manage the information/data. Therefore, OSINT demands a well-organized system.
OSINT Limitations [4]:
As the information is attained from open sources, mostly free and from the general public, OSINT becomes very difficult to validate. Anyone can target anyone by spreading misinformation and intelligence obtained from such sources is useless to the analysts or even worse, could misguide them.
One of the ways to navigate around this issue is to conduct cross-validation of the information with other sources. Even though this cannot mitigate the issue, it would reduce the misinformation. Additionally, this is not always possible under OSINT.
OSINT Ethics [4]:
OSINT is probably one the most ethical ways of collecting and propagating information. However, OSINT can potentially breach the privacy of people when used in combination with malpractices like hacking and information theft.
Air-Space Monitoring

Mid-air collision is an accident occurring between two aircraft with intruding flight paths. This can lead to heavy loss of life, equipment and/or reputation. Accidents like the 2002 Überlingen mid-air collision, which killed 71 people (mostly children), the 1976 Anapa mid-air collision, which killed 70 people and the Tenerife airport disaster, which is the deadliest aircraft crashes in history with 583 fatalities occurred due to improper/insufficient monitoring of airspace and shortage of respective actions.
Therefore, the ability to track all flights in the air and in airports is quintessential to maintaining safe operation of the aviation sector. The positional information of an aircraft is used in efficient routing, controlling and managing the airspace.
The requirement of this project is to monitor the airspace around Europe in order to understand the response of NATO (NAT), United States Airforce (RCH), Royal Airforce (RFR), Belgium - Air Force (BAF), Turkish Airforce (HVK) and Italian Air Force (IAM) to the ongoing Russo – Ukrainian war. In order to achieve this, the following methods, tools and practices were used.
Data Source
Tracking an aircraft is a complex and expensive process and requires complex mathematical computation, specialized personnel and equipment to achieve this. This potentially makes the acquisition of the airspace data by the individual who wants to gather the data very complicated. Therefore, the website Flightradar24 is used for this purpose.
Flightradar24 is a flight tracking website that gathers information about flights around the world and shows it interactively on a map. The data for the website itself comes from a combination of ADS-B, MLAT/WAL, radar and satellites. This data is then aggregated together with scheduled and actual flight data published by the operators in advance and creates a unique interactive flight tracking experience [8]. 
 
Figure 4: Flightradar24 website
These methods of monitoring flight data are discussed below:
Radar
Most of the North American continent’s airspace is covered using Radars. This technology works on the principle of Radio waves that are reflected off of an aircraft.
 
Figure 5: RADAR Illustrated [Britannica]
RADAR stands for Radio Detection and Ranging and contains a transmitter and a receiver. The transmitter emits a radio signal towards the anticipated direction of the aircraft. If there is an aircraft, the waves hit and reflect off it (called echo) and are detected by the receiver. The time taken for the waves to reach the receiver will determine the location of the aircraft [8].
ADS-B
ADS-B is the primary technology that Flightradar24 uses to receive flight information. ADS-B can be explained as follows [8]:
1.	Modern aircraft are constantly connected to GPS navigation satellites and calculate their location information. This is used in aircraft navigation and getting situational awareness.
2.	This location information, along with other data such as altitude, speed, heading and other flight data is then transmitted out in the open air, without a destination by the ADS-B transponder.
3.	This signal can be received by any compatible receiver. Flightradar24 has these receivers placed all over the world are specific locations to optimize the receiving. The signal is then processed and converted into data.
4.	The converted data is then fed to the website.
5.	This data is then displayed on an interactive map on the website
 
Figure 6: ADS-B working
Even though ADS-B is reliable, versatile and able t transmit around the world, it is a relatively new technology. Therefore, this is not the only technology that Air Traffic Controllers (ATC) rely upon and indeed rarely used. It is estimated that ~70% of all commercial passenger aircraft (0% in Europe, 60% in the US) are equipped with an ADS-B transponder [8]. 
However, for general aviation (private carriers, drones, flying schools, etc.) the adoption of the technology is below 20%. Recently, the trend of adoption of ADS-B technology has been steadily and steeply increasing in both commercial and general aviation. It is estimated that by the mid of the current decade, ADS-B will replace other primary surveillance methods (radar,  etc.) used by ATC. 
The ADS-B operates on 1090 MHz and therefore, the coverage is limited to about 250-450 km diameter for the receiver, depending on location. If an aircraft flies farther, a greater number of receivers are required to track it seamlessly. This limitation makes flight tracking challenging over oceans. Flightradar24 receives flight data from ADS-B transponders from all the aircraft in the vicinity of over 20000 receivers (FR24) around the world [8].
For Flightradar24, ADS-B receivers are placed in Canada, Mexico, the Caribbean, Venezuela, Colombia, Ecuador, Peru, Brazil, South Africa, Russia, the Middle East, Pakistan, India, China, Taiwan, Japan, Thailand, Malaysia, Indonesia, Australia and New Zealand. The website is adding the receivers to its network [8].
MLAT/WAM

Multi-Lateration/Wide Area Multi-Lateration (MLAT/WAM) is used to track flights that are equipped with older or non-ADS-B type transponders. In addition, this can also be used concurrently with ADS-B method to improve accuracy. MLAT works on the principle of the time taken for the signals from aircraft to reach a pre-set number of receivers. This is called the Time Difference of Arrival (TDOA) [8]. 

 
Figure 7: MLAT [ResearchGate]
In this setup, there is an aircraft that constantly emits signals and there are four or more receivers. The time taken by the signal to reach each receiver is measured and then the distance from each receiver is calculated. Then by calculating the distance of the aircraft from each receiver, it is possible to accurately measure the location, altitude and speed of an aircraft [8]. 

As the MLAT coverage increases with the increase in altitude with four or more receivers, it can only be achieved above about 3,000-10,000 feet. Most parts of the world where are more than or equal to four FR24 receivers are covered by MLAT (Europe, North America, Mexico, Brazil, South Africa, India, China, Japan, Taiwan, Thailand, Malaysia, Indonesia, Australia and New Zealand). The MLAT coverage area is set to increase as the website is adding FR24 receivers to its worldwide network [8]. 
Satellite
Satellite-based flight tracking is identical to that of ADS-B, with the only exception that the receivers are satellites. This is the latest technology in flight tracking. The signals emitted by the ADS-B transponders are detected by the satellites instead if land-based receivers and the information is then passed onto Flightradar24 website. This is most useful where there is no provision for equipping ground-based receivers, such as over the oceans [8].

 
Figure 8: Satellite based ADSB [Aviation Today]
Estimations

It’s not always possible to receive signals from aircraft throughout the world, therefore, Flightradar24 cannot track some flights during their entire legs. Therefore, the flight path and location are estimated based on previously known locations [8].

 
Figure 9: Estimated Location [Image Source  [8]]
Blocking
Illegal tracking of flights is a big threat to privacy and security. Therefore, it is strictly governed and regulated. Not only Flightradar24, but also any other flight tracking websites are legally bound to not track a small number of flights based on the people travelling in the flight and/or upon request from the carrier/owner [8]. 
There is a restriction on some specific types of aircraft that are not allowed to be tracked and/or displayed, such as Air Force One. Other aircraft that are not allowed to be displayed are tracked as anonymous type flights [8].
Methodology
For the purpose of the project, Python was chosen as the preferred language owing to its simple syntax and preferred libraries – Requests, Pandas, Json and Matplotlib. A summary of these libraries is discussed below:
Requests
The Requests library is created to allow users to send HTTP requests using Python. There are multiple methods in the requests like requests.delete(), requests.get() etc., however, for the purpose of this project, requests.get() method was used [10]. 
 
Figure 10: Response Get
This method returns a Response object which can then be accessed using response methods such as Response.text, which in turn returns its content in Unicode [10].
 
Figure 11: Response Text
Pandas
The Pandas library is a primary, quick and easy method of cleaning and analyzing heterogeneous data using Python. This library contains data structures and data manipulation tools, that lets users arrange data in rows and columns and access them using indexes or location–array-based computing. This allows to manipulation of the data at multiple locations without the use of loops [11].
 
Figure 12: Pandas example
Generally, Pandas is often used alongside of other data science libraries such as NumPy, SciPy, statsmodels, scikit-learn, matplotlib. 
JSON
This library parses the response text into a dictionary, which can be then be used to create a pandas Dataframe [13].
 
Figure 13:JSON Parsing
Matplotlib
Plotting helps visualize data to understand the distribution and patterns. Matplotlib is one of the most used Python libraries for visualization [12].
For the purpose of this project, Matplotlib is used to plot various views of the data as shown below. Each of these views is discussed in the following sections [12].
 
Figure 14: Plots Created using Matplotlib
Scientific Research
Analysis Of the ADS-B Airspace Monitoring System
As established in this report, the awareness of the whereabouts of any aircraft is one of the most important aspects of flight safety. This report also discusses the methods implemented to track flights such as ADS-B, Multilateration and RADAR-based approaches. However, the paper is focused on ADS-B for general aviation helicopters in Russia, especially for those operated by special emergency services [6]. 
As Russia is seeing increasing air traffic in the general aviation sector, especially in homegrown helicopters, the research paper focuses on the need to modernize the infrastructure related to flight tracking and navigation [6]. This is imperative considering the fact that the increasing traffic needs much closer and more accurate tracking and monitoring [6].
It was identified that the locally made general-purpose civil helicopters are not equipped with ADS-B transponders, and are dependent on ‘transmit-receive’ / RADAR type surveillance systems, and are not widely used. In order to improve the way these helicopters are tracked and thus, improve air safety, the paper emphasizes on the adoption of ADS-B transponders for all flying equipment [6].
The paper also identifies that, for Russia, it is very important to adopt ADS-B transponders for helicopters of the Ministry of Emergency Situations. This will not only improve the safety of the airspace during emergency situations, but also improve the efficiency of deployment of search and rescue flights, even in the remotest of areas. Canadian and American off-shore oil companies use helicopters that are equipped with and actively in use of ADS-B transponders. This is to improve the safety and efficiency of helicopter operations to-and-from the off-shore rigs. Adoption of an identical set-up is very much needed for Russian distant oil platforms [6]. 

The paper further adds to ADS-B argument by comparing the accuracies of the Radar based and ADS-B based systems, as shown in Figure 15 [6]. 

 
Figure 15: Radar vs ADS-B Accuracies [Image Source: [6]]
The error packets (i.e., information error in information received) are on the x-axis and the percentages of messages are on the y-axis. The comparative study showed that the error packets are much lower for a large percent of messages received in ADS-B data against Radar data [6].

Therefore, the comparative analysis also substantiates the need to employ ADS-B transmitters on general aviation aircraft in Russia, also, supported by the fact that installing these transmitters in helicopters is not difficult, as most of these transmitters are plug-and-play type [6]. 

Additionally, ADS-B system will greatly increase coverage for a fraction of the cost of deploying Radar-based systems. 

Generic Airspace Research
Over the years of evolution of navigation in the aviation sector, each sector of the current airspace/traffic management system has its own unique designs, labelling and management procedures [5]. This uniqueness is due to each sector starting off as a separate, isolated entity and evolving to accommodate more global management and safety requirements [5].
This results in crew transfer management as a hassle as it requires unique and extensive training for deployment across sectors. As part of the generalization of some parts/sectors in order to reduce training efforts, Federal Aviation Administration (FAA) and the National Aeronautics and Space Administration (NASA) have assessed multiple approaches and have created a Controller Information Tool (CIT) that displays sector-specific information and traffic flow details. This greatly reduces the necessity to memorize information as part of training [5]. 
Preliminary assessments have shown that the CIT is preferred by the test participants when working in unfamiliar sectors [5].
Tracking the Flow of Military Assets and Logistics for OSINT: The Case of the Syrian Civil War [4]
The Primary objective of any state intelligence department was to gather information related to the activities of adversaries and understand their motives. This intelligence helps the state to come up with countermeasures or actions to safeguard the country and its inhabitants. In the pre-IT age, this information was gathered by people with specific skill sets and located inside the enemy territory. This intelligence was kept highly guarded, oblivious to the general public [4]. 
This ‘we know what you are up to’ situation gives an edge to the state during conflicts and the counteractions were mostly a surprise to the adversaries [4]. 
With the advancement of the IT age these counter- and/or pre-emptive actions have been made conspicuous by the general public due to the availability of the internet, mobile devices and social media platforms and OSINT techniques. Even though this does not hamper or undermine the work or intelligence department, OSINT potentially can track military deployments and defensive infrastructure and make them public. This can seriously impact the safety of personnel and hinder objective of such military strategies [4]. 
This research paper strives to achieve a better understanding of the potential impact of the process and consequences of OSINT among military strategists. The paper details the methods and tools of OSINT that are used by general public to identify military assets, track them and make public the activities those assets are performing during conflicts [4]. 
This paper discusses the basic concept of OSINT, its advantages, limitations, and then explores how historically military logistics have been performed during conflicts and then fuses it with the OSINT. With this fusion as the core concept, the paper methodologically understands the impact of OSINT on such deployments, with the Syrian Civil War case study [4].
An example of such understanding is shown in Figure 16. With pictures of a cargo aircraft at an airport, the public traced its presence in Syria within the timeframe of an attack by Israel Air Force [4].
 
Figure 16: Tweet Showing Tracked Military Logistic Movement
Website Network and Data
The Flightradar24 website is built with JavaScript at the back end, HTTPS in the front end and CSS for design elements. The website ‘Request method’ is ‘GET’, therefore, the website calls ‘feed.js’ file, which is located in its ‘data cloud’ at approximately every 10 seconds as shown in Figure 17 [8]. 
 
Figure 17: Feed File [Image Source: [8]]
Along with the request to run ‘feed.js’ file, the website also sends some parameters to limit the fetching of information to specific requested geo-space/bounds (see Figure 18). These parameters also include the Boolean value for selecting various tracking methodologies, as discussed above [8].

 
Figure 18: Parameters for Feed.js [Image Source: [8]]
This feed.js file returns a JASON file (see Figure 19) that is read by the website and the HTTPS parses the information into an overlayed interactive map, as shown in Figure 20 [8].

 
Figure 19: Response in JSON From Flightradar24 cloud
 
Figure 20: Interactive Flightradar24 Website  [Image Source: [8]]
This interactive map does not contain all the information on the displayed airspace. Therefore, a user needs to click on a specific flight to know the information about that flight. When a flight is selected, the website makes another call to the data cloud, however, this time to ‘clickhandler’, to fetch the required information, as shown in Figure 21. The response is again a JSON file as shown in Figure 19.

 
Figure 21: Specific Flight Data [Image Source: [8]]
This completes one cycle of data fetching. For the purpose of this project, this cycle is run multiple times to gather information related to all the required flights.
Code Structure
In order to be able to build a complex software project, it is necessary to implement an architecture and write code using Classes and Methods. The architecture for the Airspace monitoring project is shown in Figure 22.
The different classes and methods created for the project are discussed below: 
 
Figure 22: Software Architecture for Airspace Monitoring
FetchAirspace:
This class is created to send HTTP queries to the Frightradar24 website and then receive, parse and convert the information into a pandas Dataframe. This is achieved by a series of methods that utilize ‘Requests’, ‘json’ and ‘Pandas’ libraries.
‘current_space’ method:
This method sends HTTP queries to the Frightradar24 website to fetch current airspace i.e., all the flights in a given territory by passing the parameters, and headers (including bounds) as follows:
 
 
Figure 23: Query for Airspace to the Website Using Requests
The response is an object, that contains all the necessary information about the current airspace in selected bounds.
‘selected_flights’ method:
This method sends HTTP queries to the Frightradar24 website to fetch airspace occupied by specific carriers by passing the parameters (flight ID), and headers as follows:
 
Figure 24: Query for Carrier Data to the Website Using Requests
The response is an object, that contains all the necessary information about the current airspace in selected bounds.

Both these methods then convert the response’s text to a dictionary using ‘Json’ library. This is an intermediate step in converting the response text into Dataframe using ‘Pandas’ library.
SelectClean:
This class is created to:
•	call FetchAirspace class
•	get the current airspace
•	Filter the current airspace against ‘selected’ carriers i.e, loop through each of the selected air forces as listed under ‘Air-Space Monitoring’ section in this document
•	call FetchAirspace class again 
•	get ‘selected’ carrier flight details
•	merge the flights data in current airspace and specific flight data using pandas Dataframe.
•	Pass this merged data to ‘build_database’ method to build a carrier-specific database.
‘flightdata’ method:
This method creates a FetchAirspace.current_space object and calls the method. The returned Dataframe is then saved in a variable. The Dataframe is then used to clean and transform data, i.e., assign user specific column names, and delete irrelevant columns (see Figure 25).
 
Figure 25: Manipulating Current Airspace
This data frame is then returned to ‘save_flights’ method (discussed below), which saves the ‘current’ airspace in a database, as shown in Figure 26.
 
Figure 26: Saved Current Airspace
As discussed, this data does not contain enough information to assess the airspace occupancy by the selected air forces. Therefore, another call needs to be made by the code, just as the website would in case of a click on the interactive map.

Therefore, another method ‘carrierdata’ has been created for the purpose.

‘carrierdata’ method:
This method creates a FetchAirspace.selected_flights object and calls the method. This method passes the flight ids form filtered airspace (for carriers called carrier frame) and receives a Dataframe with specific flight information. This Dataframe is then merged with the carrier frame and a final, carrier specific database is created. This is now saved in a data, as shown in Figure 27, Figure 28 and Figure 29. These databases are then used to plot data and extract information.
 
Figure 27: Manipulating Selected Flights
 
Figure 28: Final Carrier Space
 
Figure 29: All Carriers' Data Saved in a Database
Windows task Scheduler:

It is not possible to monitor the airspace for an extended period of time using loops in python code. In addition, one flight can span over many hours, therefore, frequent extraction of data has a potential to create duplicates and saturate the database and render the extracted data useless.

Therefore, an innovative way was needed to overcome this. Firstly, for the purpose of this project, the flights that take place for at least an hour were decided to be tracked as less than an hour flights were mostly considered not to be on a mission.

Next, a ‘windows task scheduler’ task was created to run the python code every one hour for at least a week, as shown in Figure 30. This gathered enough relevant data for the purpose of the project.

 
Figure 30: Windows Task Scheduler
Plotting:
The final carrier specific data contains the following information:
•	Unique Flight ID – the count of these gives number of flights occurred per carrier in a given day
•	Carrier /Air force 
•	Aircraft type
•	Altitude
•	Flight date
•	Origin and 
•	Destination
Therefore, plotting of multiple combinations of these types information is possible, however, analyzing the information form these plots would become cumbersome. Therefore, as per the objective of this project, only three types of plots were selected.
Type vs Altitude:

This plot provides the information of an aircraft type against the altitude at which it was flown. This is a vital piece of information as this gives an idea of the mission profile i.e., air to air refueling, meaning the aircraft is planned to be operated for long time/ranges etc. This plot is shown for RFR in Figure 31.

 
Figure 31: RFR Type vs Altitude
Date vs Flight Count:
This plot provides the information of number of flights per day for a specific carrier as well as for all the carriers combined. This is also a vital piece of information as this gives an idea of number of sorties carried out by a a given carrier. This in turn shows the active involvement of countries in the war efforts. This plot is shown for RFR in Figure 32.
 
Figure 32: RFR Flights in a Day

Flight Type vs Flight Count:
This plot provides the information of number of flights carried out by type of aircraft. This is perhaps one of the most vital pieces of information as this gives an idea of what type of missions were being flown by the selected carriers. For example, as shown in Figure 33, Northrop Grumman-RQ-4B Global is a drone that is flying at an altitude of 54000 feet and in a peculiar fashion. This shows that it is on a reconnaissance mission in the area of Crimea.
 
 
Figure 33: Q4 on a Reconnaissance mission [Image Source: [8]]
Flight Count of All:
This is the plot that shows number of flights / sorties conducted by each air force on an single plot. This shows which air force was most active and between what dates. Comparing this information with regular news channels will give us a complete picture of nature of missions. For example, from Figure 34, it is clearly evident that RCH was most active between Sep-2022 to mid of Dec-2022. Data prior to Sep-2022 was not collected as the project was initiated in September.
 
Figure 34: All Flights
When compared this data with the types of flights RCH operated (see Figure 35), it is evident that it was carrying out supply missions. This conclusion is based on the very high operation of C17-Globemaster planes, which are cargo carriers.
 
Figure 35: Number of Flights of Flight Types
Conclusion
The project ‘Practical OSINT Investigation - Airplanes, Airspace Monitoring’ has been taken up as part of examination for the subject OSINT. The objective of the project is to ‘monitor’ the airspace between Ukraine, Europe and Russia to understand level of involvement of NATO and its individual member countries.
The project was initiated with search of flight tracking websites that tracked military planes, in addition to providing an Application Programming Interface. Based on this criteria, Flightradar 24 was chosen as preferred website.
Python was chosen as preferred programming language due to its ease of coding and availability of libraries like ‘Requests’, ‘Pandas’ and ‘Matplotlib’.
In order to monitor the airspace, it is imperative to scrape the flight data in regular intervals and therefore, windows task scheduler was used. The scheduler ran every hour for a week to collect enough data for the project and then stored it in local disk.
The data is then plotted to understand the activity of various air forces in and around Europe with the situation Russo-Ukrainian war. The plots have shown that the NATO and its member countries have been actively supporting Ukrainian offensive with providing miliary aid in terms of equipment using C17-Globemaster flights, reconnaissance using Q4 Northrop Grumman drones etc.
Recommendation
The code is published in GitHub under username Vedaprakash88 and therefore, recommended that it can be used as it is.
References
1.	Open-source intelligence - Wikipedia
2.	A Brief History of Open Source Intelligence – bellingcat, Cameron Colquhoun, (2016)
3.	Internet Users by Country 2023 (worldpopulationreview.com)
4.	Tracking the Flow of Military Assets and Logistics for OSINT: The Case of the Syrian Civil War (2019)
5.	NASA - Generic Airspace Research, Phase 5 Report, Richard H. Mogford, Ph.D, Paul U. Lee, Ph.D, Wayne W. Bridges, Vimmy Gujral, William E. Preston, Dan N. Peknik (2014)
6.	Analysis Of The ADS-B Airspace Monitoring System, A. R. Akzigitov, R. A. Akzigitov, U. V. Ogorodnikova, D. V. Dmitriev, A. S. Andronov (2020)
7.	The Evolution of Open Source Intelligence, Schaurer, Florian; Störger, Jan (2010)
8.	Flightradar24: Live Flight Tracker - Real-Time Flight Tracker Map
9.	MarineTraffic: Global Ship Tracking Intelligence | AIS Marine Traffic
10.	Requests: HTTP for Humans™ — Requests 2.28.2 documentation
11.	Getting started — pandas 1.5.3 documentation (pydata.org)
12.	Matplotlib documentation — Matplotlib 3.7.0 documentation
13.	json — JSON encoder and decoder — Python 3.11.2 documentation













Author Bio
Chintha, Veda Prakash received his Bachelor of Computer Applications in 2021 from Dr.C.V.Raman University, India and currently pursuing M.Sc in Computer Science from SRH Berlin University of Applied Sciences, Germany (2022-present). Prior to this, he holds a Degree in Aerospace Engineering (2009) and has worked in the industry for over a decade. 

His research interests include Open-Source Intelligence (OSINT), Artificial Intelligence (AI) and Data Analytics, preferably in Aerospace Industry. His interests include smart factories, AI in Research and Development, and pilotless flights using AI. In addition, as an Intern at Lilium, he is setting up Supply Chain Processes using Data Analytics.

