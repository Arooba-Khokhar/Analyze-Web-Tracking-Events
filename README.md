# Analyze-Web-Tracking-Events

Challenge Overview:
This challenge is to analyze web tracking events data to track the effectiveness of
online marketing campaigns
Write a program that processes the web tracking events to achieve the following:
1. Filter for only successful trace events
a) Only filter where status is 200
2. Extract utm_source information to a new column
a) This is present in the url string. You have to search in the string. Look at
the example below
c) Get this value and create a new column
3. Replaces the utm_source with "unknown" in case the utm_source is null or
an empty string
a) As said, replace if empty or null
4. Return the top 5 utm_source by count of page_type=pageimpression
a) First filter for “pageimpression” from the page_type column
b) Then select the top 5 utm_source (For e.g. bing, google, etc) by count

Challenge 2: Design a consistent Join

Assume the following scenario:
1. You have individual user events in a table you provide to customers
(user_events)
2. A user has sessions which time out after 4h, they can reach from one day to
the next
3. A user_session contains all user events during the course of the session
4. A user_identifier contains all user events that happened
5. You already built a second aggregated table you use to identify bots vs. users (bot_lookup)
6. This lookup stores user_identifiers by date and an inferred bot_status

Challenge 3: Analyze a buffer sequence
In the example:
1. the first chunk has 3 items and a total of 6000
2. the second chunk has 1 item and a total of 4000
3. the third chunk has 2 items and a total of 11000
4. the fourth chunk has 3 items and a total of 24000
5. the last chunk has 1 item and a total of 10000
We have two questions for you:
1. How large is the largest chunk in the input data?
a) First, group each consecutive enteries until a blank is found
b) Then, find the sum of all of these groups
c)Sort according to descending order
d) Select the first entry
2. How large are the largest 3 chunks combined?
a) Using the above procedure, select the first 3 enteries
b) Then sum them
