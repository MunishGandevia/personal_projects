Question 1. 

-This question was mostly familiarizing myself with how the sessions table is set up
-Understanding how to query hits was the first issue i encountered, the StackOverflow example helped me understand how to access the nested fields.
-The question itself helped me understand how to calculate the other metrics (Users, Events and Unique Sessions) 
-For Unique Sessions - i used the CONCAT function, i found the bigquery documentation to be useful here

Question 2.

-For this question i repeated my approach to get the product info by using the UNNEST clause
-I knew i'd need to use the v2ProductCategory as a grouping as well as the count of the users
-I used a similar approach to filter the appropriate eventActions, the trick was to alias the hits after UNNEST


Question 3.

-This question leveraged UNNEST from question 1 along with a basic Case statement
-The Case statement took me a minute to understand because the underlying field totals.transactions was not nested so i had assumed it was and it threw errors.
-After looking at a few exampls i realized the correct sytax and was able to parse the statement correctly.
-I needed to use a similar approach as in question 2 to access the 'Add to Cart' event action
-Grouping by the output of the case statement allows me to split the result set into the two categories i want.

Question 4.

By combining the lessons learned from the above question i was able to get the basic query and from there i identified a few key fields i think would be helpful.

AvgSessionQuality - i believe this a good indicator of the session quality and would be useful in a predictive model
AvgTimeonSite_Mins - this also is a helpful idicator as there were interesting patterns based on average time on site as it relates to a purchase
Visits/NewVisits - These figures help determine what percentage of visits were unique or return visitors , i derived the additional fields using these two
RepeatVistorPercentage - i think this would be a handy metric to see what percentage return to the site and either complete a purchase or abandon their cart
MobileDevice/DataSource - i added this in becuase i think it would be helpful to see a breakdown of phone/app users vs web

from here i simply aggregated on those columns and grouped on the result, mobile device and datasource fields to get a hollistic picture of the visits.

Conclusions:

-65% of repeat vistors purchased from a non mobile device on the web
-higher AverageSessionQuality visits were often associated with a purchase, lower with an abandoned cart
-longer TimeonSite visits were often associated with a purchase, lower with an abandoned cart

Issues/Questions:

-I tried adding Data Source but the fields weren't populating as i'd expect, it would populate the 'Web' values but not the 'App'.