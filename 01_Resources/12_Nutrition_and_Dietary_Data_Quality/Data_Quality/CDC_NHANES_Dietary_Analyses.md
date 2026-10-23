# NHANES Dietary Analyses Tutorial

Source: https://wwwn.cdc.gov/nchs/nhanes/tutorials/dietaryanalyses.aspx

Retrieved October 23, 2026. Text extraction; figures, layout, and interactive elements are omitted.

NHANES Dietary Analyses
minus
Related Pages
This module provides an overview of the dietary data in the National Health and Nutrition Examination Surveys (NHANES), briefly describing the methodology for collecting dietary data, dietary data structure, and preparation and analysis of these data.
Open All
Close All
NHANES Nutrition Data Collection
NHANES contains a wealth of nutrition information gathered in health interviews, health examinations, and laboratory testing. Survey participants 12 years and older provide their own interview responses. Proxy respondents report for children who are 5 years and younger and for other persons who cannot self-report; and proxy respondents assist children 6-11 years of age.
NHANES Food and Nutrition-related data
Dietary intake
24-hour dietary recall
Food frequency questionnaire
Dietary Supplement use
Laboratory (e.g., measured levels of vitamins and minerals)
Body measures (anthropometry)
Diet behavior & nutrition questionnaire (e.g., Infant feeding; fast foods; school meals; meal preparation; self-rated diet quality)
Consumer behavior (e.g., Food expenditures; use of nutrition facts label)
Food security questionnaire
Weight history questionnaire
IMPORTANT NOTE
See the data file documentation for a description of the component and important information about the data for each survey cycle, see example in table below. It includes a summary of changes, variables in the data file, a codebook, frequencies, and other pertinent information for analysis. The documentation is labeled "Doc File" and is located next to the "Data File Name".
The focus of this tutorial module is analysis of the dietary intake and supplement use data.
Dietary Intake
The dietary interview has included 24-hour dietary recalls, food frequency questionnaires, and dietary supplement use questionnaires.
24-hour Recalls
24-hour dietary recalls have been administered in English or Spanish by trained dietary interviewers, using USDA's Automated Multiple-Pass Method (AMPM). Since the 1999-2000 survey cycle, participants completed a 24-hour dietary recall (First Day ) interview during their health examination in the mobile examination center. Beginning with the 2002-2003 cycle, all participants were asked to complete a second 24-hour dietary recall (Second Day ) interview 3 to 10 days after the first recall. Recall interviews have been conducted in person and over the phone.
During the August 2021-August 2023 cycle, changes were made to the collection of dietary data to minimize in-person interactions during the COVID-19 pandemic. The Day 1 24-hour dietary recall interviews were done over the phone instead of in-person during the MEC visit. The Day 2 interview continued to be collected over the phone as has been done in previous cycles. The 24-hour Day 1 and Day 2 dietary supplement intake questionnaires, which were historically conducted during the Day 1 and Day 2 dietary recall interviews, were dropped. Additional details can be found in the What We Eat in America, Dietary Data: Impact of Mode Change (
What We Eat in America Dietary Data, NHANES: August 2021-August 2023 24-Hour Dietary Recall Interview Mode Change
) and Dietary Supplement Data Collection Mode Changes (
Changes to Dietary Supplement and Non-Prescription Antacid Data Collection During the NHANES August 2021–August 2023 Cycle
).
Since 2002, the dietary interview component represents the integration of two nationwide dietary intake surveys - USDA's Continuing Survey of Food Intakes by Individuals (CSFII) and DHHS's National Health and Nutrition Examination Survey (NHANES). This new integrated dietary component in NHANES is known as What We Eat in America (WWEIA).
For detailed information on 24-hour dietary recall collection methods, see Dietary Interviewer
Procedure Manuals
located under
"Contents in Detail"
, provided within each survey cycle data file.
Dietary Recall Data Files
The 24-hour recall data are captured in
four files
.
Two
Individual Foods
files (IFF), one for each recall, that contain
multiple records per person
. There is one record for each food and beverage reported by the participant. Each record contains a description, the amount, and nutrient content for that food or beverage.
Two
Total Nutrient Intakes
files (TOT), one for each recall, with
one record per person
that contains total daily energy and nutrient intake from all foods and beverages reported.
The differences in the
Individual Foods
versus the
Total Nutrient Intake
files are described below. These First Day and Second Day files can be linked by sequence number (SEQN), the variable that identifies individual NHANES participants, and the observations are indexed by line number. 24-hour Dietary recall data are contained in the following data files:
NHANES 24-hour dietary recall files
Files
Data File
File Name
Data contained in the data File
1
Dietary Interview Individual Foods, First Day
DR1IFF
SEQN
: Participant sequence number
DR1ILINE
: Food/individual component number
DR1EXMER
: Interviewer ID code
DR1DBIH
: Number of days between intake and HH interview
DR1LANG
: Language respondent used mostly
DR1IFDCD
: USDA food code
DR1DRSTZ
: Dietary recall status code
DRABF
: Breast-fed infant (either day)
DR1DAY
: Intake day of the week
DRDINT
: Number of intake days
DR1CCMTX / DR1CCMNM
: Combination food type and number
DR1_020/DR1_030Z
: Time and Name of eating occasion and time
DR1FS / DR1_040Z
: Food source and where consumed
DR1IGRMS
: Amount of food in grams
DR1IKCAL - DR1IP226
: Food energy and nutrients contained in each amount of food consumed
WTDRD1
: Dietary sample weights
2
Dietary Interview Individual Foods, Second Day
DR2IFF
SEQN
: Participant sequence number
DR2ILINE
: Food/individual component number
DR2EXMER
: Interviewer ID code
DR2DBIH
: Number of days between intake and HH interview
DR2LANG
: Language respondent used mostly
DR2IFDCD
: USDA food code
DR2DRSTZ
: Dietary recall status code
DRABF
: Breast-fed infant (either day)
DR2DAY
: Intake day of the week
DRDINT
: Number of intake days
DR2CCMTX / DR2CCMNM
: Combination food type and number
DR2_020/DR2_030Z
: Time and Name of eating occasion and time
DR2FS / DR2_040Z
: Food source and where consumed
DR2IGRMS
: Amount of food in grams
DR2IKCAL - DR2IP226
: Food energy and nutrients contained in each amount of food consumed
WTDRD2
: Dietary sample weights
3
Dietary Interview - Total Nutrient Intakes, First Day
DR1TOT
SEQN
: Participant sequence number (SEQN)
DR1DRSTZ
: Dietary recall status code
DRDINT
: Number of intake days
DRABF
: Breast-fed infant (either day)
DR1EXMER
: Interviewer ID code
DR1DBIH
: Number of days between intake and HH interview
DR1LANG
: Language respondent used mostly
DR1MRESP
: Main respondent for this interview
DR1HELP
: Helped in responding for this interview
DR1_300
: Recall's consumption amount compared to typical diet
DR1_320Z / DR1_330Z / DR1BWATZ
: Total amount of plain, tap,bottled water consumed on recall day
DR1DAY
: Intake day of week
DR1TNUMF
: Number of foods/beverages reported
DR1TWS
: Tap water source
DBQ095Z / DBD100 / DRQSPREP / DR1STY / DR1SKY
: Information on added salt (e.g., frequency and type)
DRQSDIET / DRQSDT1-12 & 91
: Whether on a special diet and type of diet
DRD340 - DRD370V
: Frequency and type of fish and shellfish consumed (past 30 days)
DR1TGRMS
: Amount of food in grams
DR1TKCAL - DR1TP226
: Food energy and nutrients contained in each amount of food consumed
WTDRD1
: Dietary sample weights
4
Dietary Interview - Total Nutrient Intakes, Second Day
DR2TOT
SEQN
: Participant sequence number (SEQN)
DR2DRSTZ
: Dietary recall status code
DRDINT
: Number of intake days
DRABF
: Breast-fed infant (either day)
DR2EXMER
: Interviewer ID code
DR2DBIH
: Number of days between intake and HH interview
DR2LANG
: Language respondent used mostly
DR2MRESP
: Main respondent for this interview
DR2HELP
: Helped in responding for this interview
DR2_300
: Recall's consumption amount compared to typical diet
DR2_320Z / DR2_330Z / DR2BWATZ
: Total amount of plain, tap, bottled water consumed on recall day
DR2DAY
: Intake day of week
DR2TNUMF
: Number of foods/beverages reported
DR2TWS
: Tap water source
DBQ095Z / DBD100 / DRQSPREP / DR2STY / DR2SKY
: Information on added salt (e.g., frequency and type)
DRQSDIET / DRQSDT1-12 & 91
: Whether on a special diet and type of diet
DRD340 - DRD370V
: Frequency and type of fish and shellfish consumed (past 30 days)
DR2TGRMS
: Amount of food in grams
DR2TKCAL - DR2TP226
: Food energy and nutrients contained in each amount of food consumed
WTDRD2
: Dietary sample weights
5
Food Code Descriptions
DRXFCD
DRXFDCD
: a numeric value corresponding to the DR1IFDCD in the Dietary Interview Individual Foods file DR1IFF_ or DR2IFDCD in DR2IFF_
DRXFCSD
: a short description (up to 60 characters) of the food code
DRXFDLD
: a long description (up to 200 characters) of the food code
The individual foods files only contain records for participants with complete intakes considered to be reliable (DR1DRSTZ=1), those reporting water intake, and for breast fed children (DR1DRSTZ=4), excluding those fasting on recall day. The total nutrient intakes files, on the other hand, have records for all persons with complete intakes considered to be reliable, including those who reported fasting (considered to have complete and reliable recalls), breast fed children, those with incomplete/unreliable intakes (DR1DRSTZ=2), and those who did not participate in the dietary recall interview at all (DR1DRSTZ=5), with missing values for these records. If no foods/water or if only water is reported, the record is included in the TOT files have zero values for the nutrients.
Example from Individual Foods Files of Multiple Food Records Per Person
In the illustration below of a partial food record printout from an individual foods file, the participant associated with SEQN 27530 reported consuming 2 foods (denoted by the food codes), while the participant with SEQN 30888 reported consuming 25 foods, which gives this participant 25 records for each variable in the dietary recall file.
Example from Total Nutrient Intakes Files of One Record Per Person
In the illustration below of a partial nutrient record printout from a nutrient file, each SEQN is associated with one record for each of the variables in the table, which represents a total derived from summing an individual's food records.
Dietary Variable Naming Conventions
Some variables with different names and data file locations may have the same labels, as shown in the table below.
In the
Individual Foods
files, the fourth position of the variable name for
nutrients
is always the letter "
I.
" Additionally, the number in the third position of the variable name identifies the collection day.
For the
Total Nutrient
files, the fourth position of the
nutrients
is always the letter "
T
", and the number in the third position of the variable name identifies the collection day.
Sample Individual Foods variables and Total Nutrient variables
Dietary Interview File
Variable Label
Item ID / Variable Name
Item ID Decoded
Individual Foods - First Day
Calcium (mg)
DR1ICALC
DR = Dietary Recall
1 = First Day
I = Individual Foods
CALC = Calcium
Individual Foods - Second Day
Calcium (mg)
DR2ICALC
DR = Dietary Recall
2 = Second Day
I Individual Foods
CALC = Calcium
Total Nutrient Intakes - First Day
Calcium (mg)
DR1TCALC
DR = Dietary Recall
1 = First Day
T = Total Nutrient Intakes
CALC = Calcium
Total Nutrient Intakes - Second Day
Calcium (mg)
DR2TCALC
DR = Dietary Recall
2 = Second Day
T = Total Nutrient Intakes
CALC = Calcium
Food Frequency Questionnaire (FFQ)
Food Frequency Questionnaires (FFQs) in NHANES have included the following.
Seafood FFQ
Since the 1999-2000 NHANES survey cycle, a 30-day FFQ on fish and shellfish intake is in the dietary interview. Data are in the Total Nutrients files, including follow-up questions related to the type of fish and shellfish consumed and frequency of consumption.
Salt FFQ
Since the 2001-2002 NHANES survey cycle, a short FFQ on how often, and type of, ordinary salt or seasoned salt is added in cooking or preparing foods and at the table is included, and data are in the Total Nutrients files.
2009-2010 Dietary Screener Questionnaire
In the 2009-2010 cycle, the National Cancer Institute (NCI) supported the inclusion of a short dietary assessment instrument- the Dietary Screener Questionnaire (DSQ) in NHANES.
The DSQ data, located at the 2009-2010 dietary data page, covered a range of items related to the consumption of fruits and vegetables, fiber, added sugar, dairy/calcium, whole grains, red meat, and processed meat during the previous month. Specifically, there were 25 frequency questions, which include follow-up questions querying intake of certain foods. The DSQ also included responses based on the proportion of the time the foods were eaten over the past month. For more information on the DSQ, see the
Short Dietary Assessment Instruments
on the NCI website.
2003-2006 FFQ
In the 2003-2004 and 2005-2006 cycles, the NCI supported the inclusion of a FFQ based on its Diet History Questionnaire (DHQ) in NHANES, to aid in the examination of usual food intakes and their relationship to health outcomes. For more information on the DHQ, see the
History of the Diet History Questionnaire
on the NCI website.
English and Spanish versions of the FFQ instrument were mailed to participants. The FFQ variables cover a range of items related to the consumption of foods and food groups during the previous 12 months. Specifically, there are 151 frequency questions (stem questions), which include follow-up questions querying intake of certain foods over two seasons (i.e., summer OR winter versus rest of year). The FFQ also includes follow-up questions asking about the proportion of the time certain subtypes of the food were eaten over the past 12 months. In contrast to some other food frequency questionnaires, the NHANES FFQ
does not
query portion size. The FFQ results are not intended to be used for nutrient intake estimation, but rather to assess usual dietary intake.
The 2003-2006 FFQ data are contained in two separate data files that reflect responses to the NHANES FFQ:
The variables in the
FFQ Questionnaire - Raw Questionnaire Responses File
represent the actual questionnaire responses, with one record per participant. These data are not edited. Data are coded using a separate variable for each question. The variable naming convention is FFQXXXXX, where XXXXX equals the question number (e.g., FFQ0009C corresponds to Question 9c).
The raw responses were processed using the NCI DietCalc Software into average daily frequencies over the past year to produce the
FFQ Questionnaire - Output from DietCalc Software File
. This file has multiple records per participant, and separate records for each subtype and season combination of each food asked on the FFQ. Data were imputed in cases where there are inconsistent results for the stem and follow-up questions (e.g., when a participant reports that they never ate a certain food but provided answers to the follow-up questions). More information on these data can be found in the Analytic Notes section of the Documentation ("
Doc File
") of each Data File.
The
FFQ Questionnaire - Raw Questionnaire Responses file
and the
FFQ Questionnaire - Output from DietCalc Software file
can be combined by the participant sequence number, SEQN.
NHANES 2003-2006 FFQ dietary files
File
Data File
File Name
Data contained in the data File
1
FFQ Questionnaire - Raw Questionnaire Responses File
FFQRAW
SEQN
: Participant sequence number
FFQ0001 to FFQ0139d
: FFQ line-item responses
WTS_FFQ
: FFQ sample weight, which was derived from the examination sample weights for the relevant survey cycles and was designed to account for FFQ non-response. Respondents with fewer than ten missing frequency values (i.e.,
FFQ_MISS < 10
) have an FFQ sample weight.
2
FFQ Questionnaire - Output from DietCalc Software
FFQDC
SEQN
: Participant sequence number
FFQ_VAR
: The Variable ID is a numeric code that links to a brief variable description based on the FFQ items. The
VARLOOK
look-up file is used to obtain the variable ID description (
VAR_VALUE
). For example,
FFQ_VAR
code 7 is "Soda in summer" and code 8 is "Soda, rest of year."
FFQ_FOOD
: The Food ID is a numeric code that links to the
FOODLOOK file
containing more detailed description about foods that were queried as follow-up to stem questions (
FOOD_VALUE
).
FFQ_FREQ
: Daily intake frequencies were computed by NCI's DietCalc software. Frequencies can be summed to get the average frequency of consumption for foods queried by season and/or subtype. The frequencies were weighted to account for lengths of time for seasons (e.g., 4 months for summer and 8 months for rest of year) so that summing the frequencies provides the overall daily frequency over the past year. Frequencies for a food or beverage consumed during a season it is necessary to sum by
FFQ_FOOD
(i.e., foods with the same value for
FFQ_FOOD
) to capture the contributions of the different seasons. For foods that are not queried by season, the
FFQ_FREQ
represents the average daily frequency of consumption of that food.
FFQ_CODE
: Average daily intake frequency imputation code. DietCalc imputed frequencies for some foods when responses to FFQ questions were missing or when a scanning error was encountered. This code identifies whether the average daily frequency value is a reported or an imputed value.
Example of using the FFQ soft drink consumption data
The FFQ question includes an introductory "stem" question to ascertain if the food was consumed in the past 12 months, "Over the past 12 months, did you drink soft drinks, soda, or pop?" If the participant answers "No" they are directed to the next question. If the participant answers "Yes", the stem branches to additional questions about seasonal soda consumption and types of soda (e.g., diet soda and caffeine-free soda). The resulting data files provide frequency information for all these questions which can be collapsed to examine intake for all soda combined, or by type.
In the illustration below of a partial record printout for SEQN 21007, to determine the average daily frequency of intake of diet soft drinks, sum all the FFQ_FREQ values designated by FFQ_FOOD values of 182 or 183 (shown in yellow), irrespective of what time of year the
diet soft drinks
were consumed. Thus, participant 21007 consumed diet soft drinks an average of 0.35 times per day, or about once every three days. Similarly, if the FFQ_FREQ values designated by FFQ_FOOD values of 180 or 181 (shaded in orange) are summed, it would give the average daily frequency of 0.35 times per day for
regular soft drink
consumption.
It is also possible to determine how many times per day this participant consumed regular caffeinated soft drinks or regular decaffeinated soft drinks by summing rows where FFQ_FOOD is 180 or 181. Furthermore, the number of times per day the participant consumed all types of caffeinated soda, or all types of decaffeinated soda can be obtained by summing rows where FFQ_FOOD is 180 & 182 OR 181 & 183.
Sample FFQ_FREQ Output for Participant 21007
SEQN
FFQ_FREQ
FFQ_VAR
VAR_VALUE
FFQ_FOOD
FOOD_VALUE
21007
0.06
7
Soda in Summer
180
Soft drinks / reg / caff
21007
0.02
7
Soda in Summer
181
Soft drinks / reg / decaf
21007
0.06
7
Soda in Summer
182
Soft drinks / diet / caff
21007
0.02
7
Soda in Summer
183
Soft drinks / diet / decaf
21007
0.20
8
Soda, Rest of Year
180
Soft drinks / reg / caff
21007
0.07
8
Soda, Rest of Year
181
Soft drinks / reg / decaf
21007
0.20
8
Soda, Rest of Year
182
Soft drinks / diet / caff
21007
0.07
8
Soda, Rest of Year
183
Soft drinks / diet / decaf
Dietary Supplement Data
Information on
use of vitamins, minerals, herbals, and other dietary supplements
are collected from all NHANES participants. This information has been collected during three different interviews in NHANES. Prior to the August 2021-August 2023 cycle, the 30-day dietary supplement use questionnaire has been collected during the interview in participants' homes where participants are asked to show actual product labels to interviewers. Dietary supplement use has also been asked directly following each of the 24-hour dietary recalls.
The August 2021-August 2023 cycle included several modifications to reduce in-person contact time during the COVID-19 pandemic. For the August 2021-August 2023 cycle, the Day 1 dietary recall interview was changed from an in-person interview conducted during the MEC visit to a phone interview that occurred 3-7 days after the MEC visit. As a result, the 30-day dietary supplement use questions were moved from the in-person household interview to the Day 1 dietary phone interview. The 24-hour Day 1 and Day 2 dietary supplement questions, which were historically conducted during the Day 1 and Day 2 dietary recall interviews, were dropped. Additional details can be found in the Dietary Supplement Data Collection Mode Changes (
Changes to Dietary Supplement and Non-Prescription Antacid Data Collection During the NHANES August 2021–August 2023 Cycle
).
Some variables relate to the participants and the supplements they may have taken; other variables relate to the supplements and their formulations and ingredients from the product label. Dietary supplement data are contained in the following data files:
NHANES dietary supplement files
File
Data File
File Name
Data Contained in the Data File
1
Dietary Supplement Use 30-Day - Total Dietary Supplements
DSQTOT
SEQN
: Participant sequence number
DSD010
: Any dietary supplements taken in the past 30 days
DSDCOUNT
: Total number of supplements taken in the past 30 days
DSD010AN
: Any non-prescription antacids taken
DSDANCNT
: Total number of antacids taken
DSQTKCAL - DSQTIODI
: Amounts of 34 nutrients/dietary components from each dietary supplement and antacid
2
Dietary Supplement Use 30-Day - Individual Dietary Supplements
DSQIDS
SEQN
: Participant sequence number
DSDPID
: Supplement ID number (NHANES 2017-2020)
DSDSUPID
: Supplement ID number (NHANES 1999-2016)
DSDSUPP
: Supplement name
DSD070
: Was container seen
DSDMTCH
: Matching code
DSD090
: How long supplement taken (days)
DSD103
: How many days taken past month(days)
DSD122Q
: How much taken each day (quantity)
DSD122U
: How much taken each day (unit)
DSDACTSS
: Reported serving size/label serving size
DSDDAY1
: Product reported during First Day
DSDDAY2
: Product reported during Second Day
DSQ124
: Took product on own or doctor advised
DSQ128A-S
: Reason for taking supplement
RXQ215A
: Product taken as antacid/calcium supplement or both
DSQIKCAL - DSQIIODI
: Amounts of 34 nutrients/dietary components from each dietary supplement and antacid
3
Dietary Supplement Blend Information
DSBI
DSDIID
: Ingredient ID number
DSDINGR
: Ingredient name
DSDBID
: Blend component ID
DSDBCNAM
: Blend component name
DSDBCCAT
: Blend component category
DSDBCID
: Blend component ID - old version
4
Dietary Supplement Ingredient Information
DSII
DSDPID
: Supplement ID number
DSDSUPP
: Supplement name
DSDIID
: Ingredient ID
DSDINGR
: Ingredient name
DSDOPER
: Ingredient operator (<, =, >)
DSDQTY
: Ingredient quantity
DSDUNIT
: Ingredient unit
DSDCAT
: Ingredient category
DSDBLFLG
: Blend flag
DSDINGID
: Ingredient ID # - old version
5
Dietary Supplement Product Information
DSPI
DSDPID
: Supplement ID number
DSDPRDT
: Product type/generic or regular
DSDSUPP
: Supplement name
DSDSRCE
: Supplement information source
DSDTYPE
: Supplement type
DSDSERVQ
: Serving size quantity
DSDSERVU
: Serving size unit
DSDPREID
: Previous product ID
DSDORGID
: Original product ID
DSDSEQF
: Sequential formulation
DSDSGPF
: Sequential group formulation
DSDCNTV
: Count of vitamins in supplement
DSDCNTM
: Count of minerals in supplement
DSDCNTA
: Count of amino acids in supplement
DSDCNTB
: Count of botanicals in supplement
DSDCNTO
: Count of other ingredients in supplement
DSDSUPID
: Supplement ID # - old version (NHANES 1999-2016)
6
Dietary Supplement Use 24-Hour - Total Dietary Supplements, First Day
DS1TOT
SEQN
: Participant sequence number
DR1DRSTZ
: Dietary recall status
DR1EXMER
: Interviewer ID code
DRDINT
: Number of days of intake
DR1DBIH
: # of days between intake and interview
DR1LANG
: Language respondent used mostly
DR1DAY
: Day of the week supplement taken
DR1MRESP
: Main respondent for the interview
DR1HELP
: Helped in responding for this interview
DS1DSCNT
: Total # of dietary supplements taken
DS1DS
: Any dietary supplements taken
DS1ANCNT
: Total # of antacid taken
DS1AN
: Any antacids taken
DS1TKCAL - DS1TIODI
: Amounts of 34 nutrients/dietary components from each dietary supplement and antacid
WTDRD1
: Dietary day one sample weight
7
Dietary Supplement Use 24-Hour - Total Dietary Supplements, Second Day
DS2TOT
SEQN
: Participant sequence number
DR2DRSTZ
: Dietary recall status
DR2EXMER
: Interviewer ID code
DRDINT
: Number of days of intake
DR2DBIH
: # of days between intake and interview
DR2LANG
: Language respondent used mostly
DR2DAY
: Day of the week supplement taken
DR2MRESP
: Main respondent for the interview
DR2HELP
: Helped in responding for this interview
DS2DSCNT
: Total # of dietary supplements taken
DS2DS
: Any dietary supplements taken
DS2ANCNT
: Total # of antacid taken
DS2AN
: Any antacids taken
DS2TKCAL - DS2TIODI
: Amounts of 34 nutrients/dietary components from each dietary supplement and antacid
WTDR2D
: Dietary day one sample weight
8
Dietary Supplement Use 24-Hour - Individual Dietary Supplements, First Day
DS1IDS
SEQN
: Participant sequence number
DR1DRSTZ
: Dietary recall status
DR1EXMER
: Interviewer ID code
DRDINT
: Number of days of intake
DR1DBIH
: # of days between intake and interview
DR1LANG
: Language respondent used mostly
DS1LOC
: Location supplement originally recorded
DSDPID
: Supplement ID number (NHANES 2017-2020)
DSDSUPID
: Supplement ID number (NHANES 1999-2016)
DSDSUPP
: Supplement name
DS1MTCH
: Matching code
DS1ACTSS
: How much supplement taken (quantity); serving size, calculated as the reported amount consumed divided by the serving size from the product label
DS1ANTA
: Whether antacid containing calcium/magnesium was taken in the past 24-hours
DR1DAY
: Day of the week supplement taken
DS1IKCAL - DS1IIODI
: Amounts of 34 nutrients/dietary components from each dietary supplement and antacid
WTDRD1
: Dietary day one sample weight
9
Dietary Supplement Use 24-Hour - Individual Dietary Supplements, Second Day
DS2IDS
SEQN
: Participant sequence number
DR2DRSTZ
: Dietary recall status
DR2EXMER
: Interviewer ID code
DRDINT
: Number of days of intake
DR2DBIH
: # of days between intake and interview
DR2LANG
: Language respondent used mostly
DS2LOC
: Location supplement originally recorded
DSDPID
: Supplement ID number (NHANES 2017-2020)
DSDSUPID
: Supplement ID number (NHANES 1999-2016)
DSDSUPP
: Supplement name
DS2MTCH
: Matching code
DS2ACTSS
: How much supplement taken (quantity); serving size, calculated as the reported amount consumed divided by the serving size from the product label
DS2ANTA
: Whether antacid containing calcium/magnesium was taken in the past 24-hours
DR2DAY
: Day of the week supplement taken
DS2IKCAL - DS2IIODI
: Amounts of 34 nutrients/dietary components from each dietary supplement and antacid
WTDR2D
: Dietary two-day sample weight
Files 1, 6 and 7 contain one record per person. Files 2, 8 and 9 contain multiple records per person, from 0 to X, depending on whether and how many supplements the participant used. Files 3, 4, and 5 contain information only about the supplements and their ingredients. The participant sequence number (SEQN) links 30-day individual and total file and 24-hr individual and total files.
Dietary Data Nutrient Information
The Food and Nutrient Database for Dietary Studies (FNDDS)
The USDA's Food and Nutrient Database for Dietary Studies (
FNDDS
) is a database of nutrient values and gram weights of foods for typical food portions. It consists of three components: food descriptions, food portions and weights, and nutrients. The USDA uses these three components to process NHANES dietary recall data that are included in the two types of 24-hour dietary recall data files (individual foods and total nutrients files) and can also be used by researchers as a resource for analyzing NHANES dietary data.
Food Description Component
The Food Descriptions Component contains descriptions for foods. Every food in the database has an 8-digit code. These codes are the link between the FNDDS and the recall data and are used to identify foods in each of the three FNDDS components.
Each food description has two versions—a complete, 200-character version and an abbreviated, 60-character version, which is written in capital letters. See below for an example of a food description.
Example Food Description
Complete description (DRXFCLD)
Chicken or turkey, rice, and vegetables (including carrots, broccoli, and/or dark- green leafy), cream sauce, white sauce, or mushroom soup-based sauce (mixture)
Abbreviated description (DRXFCSD)
CHIX, RICE, & VEG (INCL CAR/DK GRN), CR/SOUP-BASED SAU
When dietary recall data are coded and processed, the Food Descriptions Component is used to convert the foods reported by participants to the appropriate USDA food code.
Food Portions and Weights Component
The Food Portions and Weights Component contains the weights, in grams, for common portions of each food in the FNDDS. When dietary intake data are coded and processed, this component is used to convert the amount of each food reported by the participant into gram weights. Only the gram weights are included in the Individual Foods File. The gram weights are used, along with the FNDDS nutrient values, to calculate the nutrient content of each food amount.
Nutrients Component
The Nutrients Component includes values for energy and nutrients/food components contained in 100 grams of each food in the database. The FNDDS nutrient values are used to calculate the nutrient amounts provided by each food reported on the dietary recalls.
The FNDDS home page provides a link to some
Special Databases
including the
USDA Database of Vitamin A (mcg RAE) and Vitamin E (mg AT) and Vitamin D (mg AT)
, for some NHANES cycles. For more information on these databases, visit the Documentation, Download Database, and Suggested Citation links that are provided for these databases.
What's In the Foods You Eat Search Tool
The USDA's
What's in the Foods You Eat
is a search tool available on the USDA website for each FNDDS version. The online version of the search tool corresponds to the most recently released version of the FNDDS.
Use the What's in the Foods You Eat search tool to search for foods by food name or keyword, compare nutrients between foods, and search for foods by food code. Every description of a food in the What's in the Foods You Eat search tool is associated with the food's 8-digit USDA food code number. As discussed below under "USDA Food Coding Scheme", the first digit of the food code identifies one of the major food groups. The second, third, and sometimes fourth digits specify increasingly more specific subgroups.
In addition to accessing information about individual foods, this search tool can be useful when grouping foods. Specifically, the search tool can be used to see descriptions of specific foods, to get an idea of how many food codes are available for a prospective group, or to scroll through all the foods in a defined range of numeric food codes.
Grouping Food Codes
Because of the level of detail in the descriptions for many FNDDS foods, it is unlikely that recall data would be examined by individual food codes. It is more likely that food codes representing similar foods would be combined into food groups and examine the data by food group, such as reported in the Dietary Guidelines for Americans. When developing a food grouping scheme, take into consideration the widespread use of foods coded as multiple items and linked by a combination food number and type.
It may be useful to conduct a preliminary review of the data to ensure that food groups are going to be meaningful. Look at how frequently foods in food group(s) are reported and the amounts consumed. Then decide whether to combine groups or to disaggregate to a greater level of detail. The USDA's Food Surveys Research Group has developed a set of food groups for their reports and analyses based on the 8-digit food code.
The USDA Food Coding Scheme
The USDA food coding scheme provides a numeric identifier based on hierarchical grouping for each of the thousands of foods in the FNDDS.
Individual Food Codes
The
first digit
of each USDA food code represents one of nine major commodity groups listed below.
First Digit of USDA Food Codes and Major Commodity Groups
Identifier
Description
1
Milk and milk products
2
Meat, poultry, fish, and mixtures
3
Eggs
4
Legumes, nuts, and seeds
5
Grain products
6
Fruits
7
Vegetables
8
Fats, oils, and salad dressings
9
Sugars, sweets, and beverages
The
second, third, and sometimes fourth digits
of a code identify increasingly more specific subgroups within the major groups. The remaining digits are used to identify specific foods within a numerical sequence. Here is an example for milk and milk products.
Example of Food Code Sequence and Relationship to specific food subgroups
Food Code Digits
Group/subgroup/description
1-
Milk and milk products
11-
Milk and milk drinks
115-
Flavored milk and milk drinks
11511100
Milk, chocolate, whole-milk-based
It is important to note that some individual food codes represent discrete food items while others represent mixed dishes consisting of multiple ingredients. If a food code represents a mixed dish, it is grouped according to its major ingredient. See Mixed Dishes, below, for more information on this topic.
Combination Codes
During the collection and coding of dietary recall data,
many individual food codes are linked together using "combination" codes
. These codes allow investigators to account for individual foods that are consumed simultaneously, such as sugar in coffee or milk on cereal, or for food mixtures that are reported as discrete ingredients, such as a homemade sandwich reported separately as bread, cheese, lettuce, and mayonnaise.
Combinations are defined using two separate variables. The first, the
combination food number
, flags foods as being eaten in combination. Each combination is given a unique combination food number, and these are listed in sequence (i.e., the first food combination reported by a participant is 1, the second is 2, and so on). The second variable, the
combination food type
, designates the type of combination, as shown below in the list.
Combination Food Types
Code
Description
00
Non-combination
01
Beverage with additions
02
Cereal with additions
03
Bread/baked products with additions
04
Salad
05
Sandwiches
06
Soup
07
Frozen meals
08
Ice cream/frozen yogurt with additions
09
Dried beans and vegetable with additions
10
Fruit with additions
11
Tortilla products
12
Meat, poultry, fish
13
Lunchables
14
Chips with additions
90
Other mixtures
The following example shows the relationship of the combination food number and combination food type for three food items. Note that all the foods in a given combination are assigned the same combination food type code and combination food number.
Combination Foods Example
Combinations eaten
Food Items reported
Combination food number
Combination food type
Cereal with fruit and milk
Frosted flakes cereal
01
02
Milk
01
02
Bananas
01
02
Coffee with sugar
Coffee
02
01
Sugar
02
01
Ham and cheese sandwich
Ham
03
05
Cheese
03
05
Bread
03
05
Mustard
03
05
Pickle
03
05
Foods with a value of 00 for both combination number and combination type are either discrete food items that were not eaten in combination or mixed dishes coded with a single food code.
Mixed Dishes Code
Mixed dishes include food items such as stews, soups, casseroles, sandwiches, pasta with meats and sauces, pizzas, and tortilla dishes (such as enchiladas and burritos). As mentioned above,
mixed dishes can be coded either by an individual food code or several food codes
—representing the ingredients of the mixture—linked by a combination food number and combination food type.
Individual food codes representing mixed dishes are included in many food groups and subgroups of the coding scheme. Generally, mixtures represented by individual food codes are placed in food groups based on the primary component or ingredient in the mixture. For example, a cheeseburger on a bun is assigned to the "meat, poultry, fish" group because the hamburger is considered the main ingredient. Lasagna with meat is assigned to the "grain products" group because the noodles are considered the main ingredient.
Certain types of mixtures, such as sandwiches, salads, and soups, can be included in various food groups, depending on their main ingredient. Therefore, it is important to note all the possible food groups that could contain codes related to that mixture. For example, different kinds of sandwiches can be found in various food groups and subgroups.
To access the NHANES food descriptions on the
NHANES website
, select the link titled
Questionnaires, Datasets, and Related Documentation
. Under continuous NHANES, for any cycle of NHANES, click on Dietary Data. This link contains the food descriptions files (DRXFCD_) and related documentation.
What We Eat in America Food Categories
The USDA's FNDDS food codes in the NHANES dietary recall data can be linked to the What We Eat in America (WWEIA) Food Categories, a grouping scheme that combines foods and beverages together that have similar usage and nutrient content with the emphasis on how they are commonly consumed in the American diet. The categories are designed to be flexible and can easily be regrouped into smaller or larger food groupings as needed to address specific research questions. A new version of
WWEIA
Food Categories is produced for each 2-year release cycle of WWEIA, NHANES. Access to the WWEIA Food Categories data and Documentation is on the USDA website.
The Food Patterns Equivalents Database Food Groups
The USDA's FNDDS food codes in the NHANES dietary recall Individual Food Files can be linked to the Food Patterns Equivalents Database (FPED) Individual Food Files, formerly known as the MyPyramid Equivalents Database (MPED). FPED provides 37 Food Patterns components of reported foods reported in NHANES recalls, expressed as numbers of cup equivalents, ounce equivalents, teaspoon equivalents, or grams. All foods in the FNDDS identified by food codes (e.g., lasagna) are disaggregated into their component ingredients (e.g., pasta, mozzarella, beef), and these ingredients are converted to equivalent amounts of relevant food groups (e.g., grains, milk, meat). Access to the
FPED
data and Documentation is on the USDA website.
The FPED contains data for all USDA survey food codes available for use with any nationwide dietary intake survey conducted from 1994 onwards. Data in FPED are of two general types: food data and intake data.
Food data
These data provide the number of Food Pattern Equivalents per 100 grams of food for the 37 USDA food patterns listed in the table below with their respective measures. Food mixtures are separated into their ingredients before Food Pattern Equivalents are calculated.
Food Patterns Equivalents Database Food Groups and Measures
Food Patterns Equivalents Food Group
Measure
Total grain
Ounce equivalents
Whole grain
Non-whole grain
Total vegetables
Cup equivalents
Dark-green vegetables
Total Red and Orange vegetables
Tomatoes
Other Red and Orange vegetables
Total starchy vegetables
Other starchy vegetables
Other vegetables
Total fruits
Citrus fruits, melons, and berries
Other fruits
Fruit juice
Total Dairy
Milk
Yogurt
Cheese
Total Protein Foods
Ounces cooked lean meat
Total Meat, Poultry, and Seafood
Meat (beef, pork, veal, lamb, game)
Organ meats (meat, poultry)
Cured meat
Poultry (chicken, turkey, other)
Seafood high in omega-3 fatty acids
Seafood low in omega-3 fatty acids
Eggs
Ounce equivalents of lean meat
Soy products (tofu, meat analogs)
Nuts and seeds
Cooked dry beans and peas
1
Cup equivalents of vegetables or ounce equivalents of meat
Oils
Grams
Solid fats
Added sugars
Teaspoon equivalents
Alcoholic drinks
Number of alcoholic drinks
1
Cooked dry beans and peas may be counted in either the vegetables group or the meat and beans group.
Intake data
These data represent the number of serving equivalents provided by each food reported by NHANES participants on the First Day and Second Day 24-hour recalls (FPED_DR1IFF and FPED_DR2IFF) and daily totals per individual (FPED_DR1TOTAL and FPED_DR2TOTAL). They are derived by applying FPED food data to NHANES intake data.
FPED includes data for the 1994-96 and 1998 Continuing Survey of Food Intakes by Individuals (CSFII) and is updated to include new information for each 2-year release of NHANES data starting in 1999-2000.
For general information on analyzing NHANES data, see the
Continuous NHANES Tutorials
. See the
Sample Code
module for example code to download and modify.
Dietary Data Analysis
Preparing an NHANES Dietary Analytic Dataset
Dietary data are among the most complex of all the data in NHANES. For this reason, preparing a dataset for dietary analysis involves critical steps and often may be more time-consuming than the analysis itself.
Analysts working with NHANES dietary data frequently want to answer the following types of questions:
What is the mean intake of a given food?
What is the mean intake of a given nutrient from all foods and beverages?
What is the mean intake of a given nutrient from supplements?
Which foods are the major sources of a given nutrient?
What is the distribution of intake of a given food or nutrient across a selected population?
How does dietary intake relate to some health parameter?
The basic unit of analysis in NHANES is the individual participant, identified by the participant sequence ID (SEQN). However, because of the way the dietary data are structured—with individual participants having multiple food and dietary supplement records, which in turn have their own accompanying sets of variables—the unit of analysis for some types of analyses is at the level of the food or supplement, rather than the individual.
Dietary data are also challenging to work with because many analyses require the creation of new variables from variables that are found in the survey data files, grouping similar foods together. For example, to answer the question "What is the mean intake of milk among survey participants?" defining "milk" (e.g., all types of fluid milk consumed as a beverage, or milk also consumed as an ingredient in other foods, or servings of milk) may require the creation of several new variables based on analytic needs.
Analysts can group foods for their own purposes or use previously developed grouping schemes. Examples of such schemes include the What We Eat in America Food Categories and the Food Patterns Equivalents Database described earlier.
Special Considerations in Analysis of Dietary Data
Different Types of Data
The dietary recalls, food frequency questionnaire, and supplement questionnaire each measure different aspects of the diet. Each type of dietary data is gathered differently, which could lead to differential cognition (comprehension, recall, decisions & judgment, and response processes) and how individuals respond. Because of these differences, the various types of dietary data lend themselves to different types of analyses and require different assumptions as shown below. For more information on analysis of different type of dietary data, see the
Dietary Assessment Primer
from the National Cancer Institute (NCI), including the
Summary Tables: Recommendations on Potential Approaches to Dietary Assessment for Different Research Objectives Requiring Group-level Estimates
.
The recall data and supplement questionnaire data can be used alone, but each one does not represent total nutrient intakes. Similarly, the NHANES 2003-2006 food frequency data were not designed to be used alone, but as supplementary (covariate) information in modeling data from the 24-hour recalls in estimating usual intakes when examining them in relation to some other variable of interest. A single 24-hour recall is sufficient for analyzing mean nutrient intakes from foods and beverages, whereas both days of data are required when estimating the usual intake distribution and prevalence of nutrient intake from foods and beverages. There may be a sequence effect—that is, the number and amount of foods is sometimes lower on the first versus subsequent recalls—that can be controlled for by adding a variable for recall day (first versus second) in the usual intake analysis. See
Usual Dietary Intakes
on the NCI, Risk Factor Assessment Branch website for more information and sample statistical programs on the NCI method for estimating usual intake.
Choosing Whether or Not to Include Non-Consumers
Another consideration in estimating mean food intake is whether the mean is among all persons in the population or only among consumers of the food. If interested in the per capita amount consumed, non-consumers with their intake value of zero must be included; if interested in the average amount consumed by users of the food on days when the food is consumed, non-consumers must be excluded.
Measurement Error
Measurement error in dietary data seriously attenuates the association between dietary data and other factors, such as a health outcome. That is, the analysis would be less likely to indicate a relationship between diet and disease even if one truly existed. Measurement error models can be used to analyze diet-disease relationships, and methods have been developed to estimate usual intakes that adjust for the problems associated with large within-person variation. For more information on measurement error, see
Measurement Error: Impact on Nutrition Research and Adjustment for its Effects
on the NCI website.
Data Symmetry
An underlying assumption in many statistical analyses is that the distribution of the data is normal. However, almost all distributions of dietary data are skewed. For some dietary constituents, many people have zero intake, and a few people may have very large intakes. Skewness does not affect simple analyses, such as differences in mean intakes between population subgroups, therefore, no special corrections are necessary. However, for more complex analyses, such as when estimating the distribution of usual intakes, skewness must be considered.
Weighting
Appropriate sample weights, including dietary weights, should be applied if the data are being used to represent the U.S. civilian noninstitutionalized population. The dietary sample weights for each recall day account for day of the week of the 24-hour recall in addition to nonresponse, noncoverage, and unequal probabilities of selection. For more information on selecting correct weights for your analysis, see the
Weighting
module.
In addition, special statistical procedures are required to estimate standard errors when using data from a complex sample such as the NHANES. For more information, see the
Variance Estimation
module.
Statistical Analysis Methods for Dietary Data
See the
Sample Code
module for example code to download and modify.
Usual Intake and Day-to-Day Variation in Dietary Intakes
For most surveillance, epidemiologic, and behavioral research purposes, dietary analyses are concerned with measuring
usual
intake—that is, long-term average daily intake. This is because dietary recommendations are intended to be met over time, and diet-health hypotheses are based on dietary intakes over the long term. For more information on usual intake estimation, please see
Usual Dietary Intakes
on the National Cancer Institute (NCI), Risk Factor Assessment Branch website.
Estimating Mean Food Intakes
Although dietary recall data are known to contain random errors, especially large day-to-day variability, these errors are assumed to cancel out when estimating means.
The mean of the population's intake on a given day can be estimated from a sample of individuals' 24-hour recalls, without sophisticated statistical adjustment
if the data are collected evenly throughout the year and the days of the week are evenly represented. The second day of dietary recall is generally not used to estimate means but is used for more advanced analyses, such as Usual Intake analysis.
Dietary recall data also are known to contain bias, at least insofar as a tendency toward underreporting of energy intake. Little is known regarding the extent to which energy intake underreporting extends to underreporting of different foods. For that reason, and for practical purposes, the current statistical convention is to assume that the recalls are not biased (i.e., that no underreporting of foods occurs). However, this assumption may have greater implication for inferences made from analyses than the one regarding random error and should be noted as a limitation or caveat in any analysis of food intake.
Estimating Mean Nutrient Intakes from Dietary Supplements
Very little is known regarding the extent of bias or random error associated with dietary supplement data. For that reason, and for practical purposes, the supplement data are generally treated as though neither type of error occur. However, the possibility of both should be noted as a caveat in an analysis of dietary supplement intake.
There are a few key points to note when calculating supplement intake.
Intake for 34 nutrients are summarized in the dietary supplement files and therefore researchers do not need to estimate nutrient intake for these specific nutrients. If researchers want to calculate nutrients that are not part of those 34, then the following needs to be considered:
Each supplement could be reported with a different frequency, based on use over the past 30 days, so care must be taken in deriving the intakes from all supplements.
The measurement unit for a given supplement may not be the same across all brands, so conversions may need to be made to combine nutrient values.
Some nutrients may be listed as compounds, and thus may need to be converted to elemental form and amounts (e.g., calcium carbonate should be converted to the corresponding amount of elemental calcium to determine total calcium). This impacts very few products, like antacids, but still needs to be considered.
When linking supplement ID from the product-level files (e.g., DSPI) and the participant-level files, it is important to note that NHANES 1999-2016 cycles are linked by the old ID code (variable DSDSUPID) and the NHANES 2017-March 2020 cycles is linked by the new ID code (variable DSDPID).
Missing data can be a limitation with several dietary supplement variables. The number of cases of missing data and the possible remedies vary by variable, as follows:
Number of days the supplement was taken in the past 30 days: Because this variable is needed to determine usual intake, analysts can either impute number of days or drop these records from the dataset. Imputation requires an assumption that the supplement was taken regularly and is usually based on some other information the respondent provided, such as the number of days that the respondent reported taking certain other types of dietary supplements.
Variable on quantity and units consumed, "On the days you took the supplement, how much did you take?": Analysts may want to impute data, which requires an assumption that the respondent took the serving sizes recorded in the variables that capture label information.
Missing supplement name: It is assumed that individuals did take a supplement, even though the name is unknown so they should be retained for prevalence estimates. It may be best to exclude these data from analyses in which mean intakes are being estimated. This action also would reduce missing data for some other variables.
The calculated total calcium intake from supplements (available on the Total Dietary Supplements files DS1TOT and DS2TOT) include calcium from antacids. Caution is advised because antacids may be used as a medication and not as a supplement.
Similar to the consideration for food intake, mean supplement amount can be obtained among all persons in the population or only among users of the supplement. If interested in the per capita amount consumed, non-consumers with intake value of zero should be included. If interested in the average amount consumed by users of the supplement, non-consumers should be excluded.
NOTE: When estimating the mean of the population distribution of usual nutrient intakes from supplement data, no standard convention for statistical adjustment currently exists.
Estimating Mean Total Nutrient Intakes from Foods and Supplements
Estimating total nutrient intake requires using data from both the 24-hour recalls and dietary supplement questionnaire. Since 2007, 24-hour dietary supplement data are collected during 24-hour recalls so nutrients from all sources can easily be combined. For more information see the
Doc Files
for each 24-hour dietary supplement data.
The 30-day dietary supplement intake files have different reference periods and measurement error characteristics. Therefore, some data manipulation is required to combine and summarize these data with 24-hour recalls (i.e., for survey cycles before 2007). For more information on merging data files, see
Continuous NHANES Tutorials
. Also, sample sizes may differ because some participants who report supplement use do not complete the dietary recall interview and participants who complete the dietary recall may not report supplement use. Exploratory analyses are useful to identify the characteristics of participants who report supplement use versus participants who complete dietary recalls.
All the key concepts and caveats regarding estimating nutrient intakes from dietary (foods and beverages) intake apply when estimating total nutrient intake from both foods and supplements. For these analyses, the sample of participants with reliable data for both supplement intake and the First Day recall are selected. Then, for each participant, nutrient intake from 24-hour dietary supplements is added to the nutrient intake from the 24-hour recall, or the average daily nutrient intake of supplements from the 30-day supplements use files are determined and added to the nutrient intake from the 24-hour recall (for survey cycles before 2007). Finally, a weighted mean of those values is obtained. The assumption is that the sample of participants with satisfactory 24-hour recall and supplement data is representative of the population.
If the units of measure are different in the 24-hour recalls from the supplement data, ingredient units (DSDUNIT) for each nutrient of interest on the supplement files need to be converted to units used in the dietary intake data files. Also, nutrients listed as compounds need to be converted to elemental form and amounts. For example, there may be some instances of calcium carbonate, which will need to be converted to the corresponding amount of elemental calcium.
As in the case of estimating nutrient intakes from supplements alone, analysts must consider the possibility of missing data and whether to include antacids (in the case of calcium or magnesium).
Means should be examined along with their standard errors, to get an indication of the variation around the mean. If the data are highly skewed, as dietary data often are, means may not provide a very good representation of central tendency and the median should also be estimated. The simple median of reported intakes from a sample based on one 24-hour recall per participant represents the median on a given day, not usual intake. In addition to medians, transformations of skewed dietary data which result in normally distributed values could be considered.
Estimating Ratios
Ratios depict the value of one variable divided by the value of another. The mathematical properties of ratios are the same, whether one is considering simple ratios, proportions, or percentages. A proportion, often expressed as a percentage, is a kind of ratio that can be used to represent the value of a single variable for one class divided by the value for all classes combined.
Whenever multiple ratios are involved—either across many individuals in a group or over numerous days of intake for each individual—analysts can use different ways to summarize them. These different calculations can lead to different answers because the calculations involve both summation and division, and an elementary principle of mathematics dictates that the order of these operations matter.
In survey analyses involving multiple dietary recalls per person, consideration of which kind of summary ratio to use must be made at both the group and individual levels. Two different, but equally correct, answers can be given in response to a question such as "What proportion of the calcium that is consumed comes from milk?" This is because the question can have two different meanings:
"How much of all the calcium consumed by the group comes from milk?" (Ratio of Means) or
"What is the group's daily contribution of milk to calcium intake?" (Mean Ratio)
Ratio of Means
The ratio of means
yields information about the diet of the whole population
because both the numerator and the denominator are computed for the whole population before the ratio is derived. The ratio of means can be obtained for various subgroups in the population if comparisons are warranted. The ratio of means is used to answer questions such as, "How much of all the calcium consumed by the group comes from milk?"
It is calculated by summing the amount of calcium from milk for all persons and then dividing that by the sum of the calcium from all foods for all persons
. The answer would be the same if both the numerator and denominator were divided by a constant, such as the sample size. Therefore, it can also be calculated by dividing the group's mean amount of calcium from milk by the group's mean total calcium, and for this reason it is described as a ratio of means.
The ratio of means has been used to identify sources of nutrients in the US diet as a whole and to examine diet quality. There are two different ways to consider food sources of nutrients—as either "important" or "rich" sources.
Important sources
are those that contribute the most to a population's dietary intake;
rich sources
are those foods with the greatest concentration of a nutrient. For example, sardines are a rich source of calcium, but they are not a very important source in the US diet because they are consumed relatively infrequently. A food composition table or database can provide information about rich sources of nutrients, whereas population intake as well as food composition data are needed to identify important sources.
NOTE: When data from one or two 24-hour recalls are used to estimate a ratio of means, the mean in the numerator and the mean in the denominator can each be considered an estimate of usual intake. Therefore, no specific statistical adjustments are necessary.
Mean Ratio
When the intent is to say something about how intake varies among the population, or how the ratio relates to other factors, deriving the ratio for each person before summarizing (as with the mean ratio) is the method of choice. The mean ratio is used to answer questions such as, "What is the group's daily contribution of milk to calcium intake?"
It is determined by first calculating the proportion of calcium from milk for each person and then taking an arithmetic mean of all the proportions
. Often, the mean ratio is close to the ratio of means; however, sometimes they are quite different, depending on the variability in the ratio, variation in the denominator, and the correlation between the ratio and the denominator.
When the ratio itself varies among the population, its distribution can be examined. The distribution of ratios provides other summary statistics, such as the mean and median, the ratio at other percentiles, and the proportion of the population above or below a certain cut-off. The generalizability of mean ratios is subject to whatever data limitations the individual ratios impose. For example, if the individual ratios each represent only a single day, then the mean ratio can only be used to make inferences "for a given day," and relating a single day's ratio to some other factor is rarely of interest.
Individual-Level Ratios
As with group-level ratios, two different questions could be posed: "How much of all the calcium consumed by this person, has come from milk?" or "What is the person's daily contribution of milk to calcium intake?" And again, because the ratios would involve the division of one variable by another, these two ratios could be different from one another. If using only one observation per person—such as a single 24-hour recall—then there is only one value for the numerator and one for the denominator and, therefore, only one way to derive the individual-level ratio. If data were available for each person's intake on every day over an extended period, then the individual's daily ratios would need to be summarized.
More Information and Additional Help
National Cancer Institute
: More information on measurement error and techniques for estimating usual intake of dietary and supplement intake can be viewed from the
National Cancer Institute, Division of Cancer Prevention
. These statistical methods are advanced and may require consultation with a statistician.
Dietary Assessment Primer
: More information on dietary assessment methods and potential analysis approaches can be viewed from the
National Cancer Institute, Risk Factor Assessment Branch
.
NHANES Listserv
: Visit the NCHS
Listservs
page and to subscribe to the NHANES Listserv.
Food Survey Research Group (FSRG) Listserv
: The FSRG Listserv, maintained by USDA, provides email notices to alert subscribers about new data releases and products for What We Eat in America, NHANES. The
FSRG Listserv
does not allow interactive discussion. To subscribe, click on the link and provide your name and email address to join.
Open All
Close All
Content source:
CDC/National Center for Health Statistics
