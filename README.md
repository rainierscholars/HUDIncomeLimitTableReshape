# HUDIncomeLimitTableReshape

It is ocassionally helpful for us to refer to the [Income Limits set by the U.S. Department of Housing And Urban Development](https://www.huduser.gov/portal/datasets/il.html). 

These income limit tables are formatted with each income level categories as rows and family size as columns. The following example is from King County, WA 2018:

|  Income level  |   1    |    2   |    3   |    4   |    5   |    6   |    7   |    8   |
|----------------|--------|--------|--------|--------|--------|--------|--------|--------|
| Very Low       | 37,450 | 42,800 | 48,150 | 53,500 | 57,800 | 62,100 | 66,350 | 70,650 |
| Extremely Low  | 22,500 | 25,700 | 28,900 | 32,100 | 34,700 | 37,250 | 39,850 | 42,400 |
| Low            | 56,200 | 64,200 | 72,250 | 80,250 | 86,700 | 93,100 | 99,550 | 105,950|


Due to the way some internal systems are set up, we need the tables in a format with each income level cap as a row, and family size as columns. The same example, truncated: 

|  Income  |       1       |       2       |       3       |       4       |       5       |       6       |       7       |       8       |
|----------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|
|  22500   | Extremely Low | Extremely Low | Extremely Low | Extremely Low | Extremely Low | Extremely Low | Extremely Low | Extremely Low | Extremely Low |
|  25700   |  Very Low     | Extremely Low | Extremely Low | Extremely Low | Extremely Low | Extremely Low | Extremely Low | Extremely Low | Extremely Low |
|  28900   |  Very Low     |  Very Low     | Extremely Low | Extremely Low | Extremely Low | Extremely Low | Extremely Low | Extremely Low | Extremely Low |

What's more, a ninth column needs to be added to accomodate families with 9 people. 


## Calculating for families larger than 8
According to [this notice from HUD in 1999](https://www.huduser.gov/portal/datasets/il/fmr99/sect82.html) and coroborated in [this pdf of methodology for calulating the 2019 limits](https://www.huduser.gov/portal/datasets/il/il19/IncomeLimitsMethodology-FY19.pdf), 

>Low-Income Limits:
>Most four-person low-income limits are the higher of 80 percent of the area median family income or 80 percent of the State nonmetropolitan median family income level. Because the very low-income limits are not always based on 50 percent of median, calculating low-income limits as 80 percent of median would produce anomalies inconsistent with statutory intent (e.g., very low-income limits could be higher than low-income limits). The calculation normally used, therefore, is to set the four-person low-income limit at 1.6 (i.e., 80%/50%) times the relevant four-person very low-income limit. The only exception is that the resulting income limit may not exceed the U.S. median family income level ($47,800 for FY 1999) except when justified by high housing costs. Use of very low-income limits as a starting point for calculating other income limits has the effect of adjusting low-income limits in areas where the very low-income limits have been adjusted because of unusually high or low housing-cost-to-income relationships.

>Family Size Adjustments:
>By statute, family size adjustments are required to provide higher income limits for larger families and lower income limits for smaller families. The factors used are as follows:

>Number of Persons in Family and Percentage Adjustments

>|   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |  
>|-------|-------|-------|-------|-------|-------|-------|-------|
>|  70%  |  80%  |  90%  |  Base |  108% |  116% |  124% |  132% |

>Income limits for families with more than eight persons are not included in the printed lists because of space limitations. For each person in excess of eight, 8 percent of the four-person base should be added to the eight-person income limit. (For example, the nine-person limit equals 140 percent [132 + 8] of the relevant four-person income limit.) All income limits are rounded to the nearest $50 to reduce administrative burden."
