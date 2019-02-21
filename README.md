# yelp-scraper

#### CS 5010

WebScraping user ratings off YELP for Shake Shack,Madison Square,NYC and performing data analysis using the web-scraped data

• This restaurant is the most well known and most rated restaurant of Shake Shack in the US. Also called ‘The Original’ since it was one of the first ones to be opened.

https://www.yelp.com/biz/shake-shack-new-york-2

• I scraped the following from the website:
 user name
 user rating given to the restaurant
 date at which rating was published

• My objective was to scrape all the user ratings of this restaurant and then perform some
analysis on it using Python to gain some insight into the user ratings trends of this restaurant.

• I was able to scrape off all the 5,314 ratings of this restaurant which spanned over 250 pages
and dump it into a CSV file to use it for performing some analysis.


INSIGHTS FROM THE ANALYSIS -

1) Overall, the number of reviews/rating for this restaurant have dropped massively since its surge from 2010 to 2014.
2) However, despite the drop in ratings, the overall average rating still continues to be > 3, in fact the current year to date average rating
stands at 4 and that stays consistent across most of the periods.
3) The distribution of the ratings is also such that most of the ratings are either 4 or 5, hence keeping the average rating up.
4) Despite the strong average rating, the present YTD (year-to-date) trends don’t look very encouraging as the count of ratings continue to dip and that can be correlated to
the number of people visiting this restaurant. However it is imperative to note that this is a very small subset of the actual user base that visits the restaurant.
5) What was interesting to observe was that there was a dip in the count of
ratings towards the end of 2014 and beginning of 2015. I wasn’t inclined to
believe that it could be because the restaurant wasn't doing well since the
average user rating continued to be above 4 during that period. So I did some
research to see if there was a fundamental business reason for this trend or an
external one.
Upon researching I came across many articles that stated that SHAK had close
down its Madison Square restaurant for 7 months from Nov 2014 to May 2015 for
renovation.
I could hence conclude that this was the reason for the drop in the count of
ratings during that period.
(http://fortune.com/2015/05/20/shake-shack-reopens-madison-square-parkrestaurant/)
