# Medicaid-Projects
  <a href="https://emrts.us" target="_blank"> ![image](https://github.com/tmwang7324/Medicaid-Analysis/assets/121271571/16e51d9d-e2f7-4e49-b407-1005281d932a) </a>

## Introduction:    
Medicaid, a prominent insurance program in the United States, is a collaborative federal and state initiative designed to subsidize medical expenses for individuals with constrained income and resources. While it bears similarities to Medicare, another significant health insurance program, there are notable differences between the two. Medicare primarily offers federal health insurance to individuals aged 65 and above, as well as to certain individuals below 65 with specific disabilities or conditions. While Medicare mainly caters to seniors and select younger individuals, Medicaid primarily targets those with limited income. In essence, these are distinct programs catering to unique demographics. You can find a detailed comparison between Medicaid and Medicare provided by the HHS (U.S. Department of Health and Human Service) [here](https://www.hhs.gov/answers/medicare-and-medicaid/what-is-the-difference-between-medicare-medicaid/index.html). Notably, while Medicaid receives federal financing, individual states are responsible for its administration. As a result, each state tailors its Medicaid program to suit its residents. Given that both state and federal governments share the cost, accurate future budgeting is paramount. This project aims to use existing Medicaid Enrollment and Expenditure data to forecast trends for the next decade, assisting governments in budget adjustments. This forecasting approach is termed "Time Series Analysis"—a method dedicated to the examination of data points over specific time intervals. The core objective of this project is to apply time series analysis to Medicaid data.

This endeavor is commissioned by [EMRTS](https://emrts.us/) (EMR Technical Solution), a firm specializing in professional Medicaid analyses. Initially named "Reflections on Medicaid Enrollment for the Next Decade", this project aligns with a related blog post on their website. To stay current, this project demands ongoing updates. The most recent update can be found [here](https://emrts.us/2021/07/31/reflections-on-medicaid-enrollment-for-the-next-decade/). For our current iteration, we've enriched the dataset beyond the original blog's scope, incorporating Medicaid expenditure. Additionally, we've transitioned to the Instadeq tool for graphical representation, which will be discussed further.


## Source:
### Source Background:
#### Enrollment:
Drawing from resources provided by the [Kaiser Family Foundation (KFF)](https://www.kff.org/other/state-indicator/medicaid-and-chip-monthly-enrollment/?currentTimeframe=0&sortModel=%7B%22colId%22:%22Location%22,%22sort%22:%22asc%22%7D) and ['Data.Medicaid.gov'](https://data.medicaid.gov/dataset/6165f45b-ca93-5bb5-9d06-db29c692a360/data), the 'data.csv' file encapsulates Medicaid Enrollment figures spanning from 2017 to 2023, recorded on a monthly basis.

The Kaiser Family Foundation stands as an independent authority on health policy research, polling, and journalism, offering objective data on the majority of U.S. health systems. On the other hand, 'Data.Medicaid.gov' is an open-access platform operated by the Centers for Medicare & Medicaid Services (CMS). CMS oversees the health coverage of over 100 million individuals via Medicare, Medicaid, the Children’s Health Insurance Program, and the Health Insurance Marketplace.
#### Expenditure:
Our primary reference for Medicaid Expenditure comes from the [U.S. Department of Health and Human Service](https://oig.hhs.gov/fraud/medicaid-fraud-control-units-mfcu/). Within their "Expenditure & Statistics" section, you'll find detailed charts showcasing Medicaid expenditures from 2010 to 2022, a testament to the reliable data provided by the U.S. federal government. For the scope of this project, we will concentrate solely on the total Medicaid expenditures. An upcoming pie chart will depict 2022's data, as extracted from the "FY 2022 Chart". The 'Medicaid_Expenditure_2010-2022.csv' file holds this comprehensive dataset detailing Medicaid's total expenditures spanning 2010 to 2022.

## Instadeq:
[Instadeq](https://instadeq.com/) is a versatile platform capable of transforming CSV files into various chart formats to meet a wide array of requirements. Its user-friendly interface allows for effortless filtering, grouping, and the creation of multiple charts to cater to specific needs. 

For our dataset, 'data.csv', we've produced two distinct visualizations using Instadeq:
1. A [pie chart](https://mmiscloud.us/s/@zyang/medicaid-enrollment-pie/) displaying Medicaid enrollment by states.
2. A [bar chart](https://mmiscloud.us/s/@zyang/medicaid-enrollment-layout-by-report-date/) showcasing Medicaid enrollment month by month from 2017 to 2023.

Similarly, the file 'Medicaid_Expenditure_2010-2022.csv' has been visualized through three separate charts:
1. A [pie chart](https://mmiscloud.us/s/@zyang/medicaid-expenditure-pie/) representing Medicaid expenditure by states in 2022.
2. A [bar chart](https://mmiscloud.us/s/@zyang/medicaid-expenditure-bar-yearly/) illustrating yearly Medicaid expenditure from 2010 to 2022.
3. Another [bar chart](https://mmiscloud.us/s/@zyang/medicaid-expenditure-bar-monthly/) highlighting Medicaid expenditure on a monthly basis from 2010 to 2022.

**Notice:**
The chart labeled as (3) is derived from the CSV file named 'Expenditure_Monthly_data_2010-2022.csv'. This particular file is generated using the Python script 'Expenditure_Forecasting_Monthly.py'. To craft 'Expenditure_Monthly_data_2010-2022.csv', linear interpolation was applied to the data from 'Expenditure_Yearly_data-2010-2022.csv'. It's noteworthy to mention that while the trends observed in charts (2) and (3) align, chart (3) offers granularity by detailing specific months.

Additionally, we have two forecasting visualizations generated from two distinct CSV files:

1. A [bar chart](https://mmiscloud.us/s/@zyang/layout-of-bar-graph-of-forcasted-medicaid-enrollment/) forecasting **yearly Medicaid enrollment** from 2023 to 2033.
2. Another [bar chart](https://mmiscloud.us/s/@zyang/medicaid-forecast-expenditure-from-2023-to-2032/) projecting the **yearly Medicaid expenditure** from 2023 to 2032.

## Prophet:
Prophet is a library tailored for time series analysis and is compatible with both **Python** and **R** languages. Developed as an open-source project by Facebook, Prophet is designed for forecasting time series data, enabling businesses to better understand and potentially predict market trends. The library uses a decomposable additive model where non-linear trends are fitted with seasonality, and it also factors in the impact of holidays. For an overview, visit the [official Prophet website](https://facebook.github.io/prophet/). For those seeking a more in-depth dive, the [Prophet GitHub repository](https://github.com/facebook/prophet) provides detailed documentation and version-specific information, proving invaluable for learners.

Prophet is our primary tool for forecasting. Both of our forecasting endeavors leverage its capabilities.

## Installation:
Inputting the data, editing it, creating and training the model, and visualizing the results comprise the entire forecasting process. This project utilizes both Python and R. To run the script, the installation of Python, R, and specific libraries is required.
### Python Installation:
**Version of Python:** 3.8.1 or above

**Website:** www.python.org
#### Python Libraries Installtion:
Three libraries are required.
##### **pandas:**
**Version of pandas:** 1.5.3
If you are using Mac OS, in the terminal, type
```
pip3 install pandas
```
##### **matplotlib:**
**Version of maplotlib:** 3.7.2
In the terminal, type
```
pip3 install matplotlib
```
##### **prophet:**
**Version of prophet:** 1.1.4
In the terminal, type
```
pip3 install prophet
```
**Notice:**
If you are using Windows OS, please replace pip3 with pip in the terminal instead.

##### **Version Check:**
```
pip list
```
Type this command in the terminal
### R Installation:
**Version of R:** 4.3.1 or above

**Website:** www.R-project.org
#### R Packages Installation:
To install the packages of R, **you will need to open the console of R**.
##### **prophet:**
**Version of prophet:** 1.0.0
```
install.packages("prophet")
```
##### **tidyverse:**
**Version of tidyverse:** 2.0.0
```
install.packages("tidyverse")
```
##### **lubridate:**
**Version of lubridate:** 1.9.3
```
install.packages("lubridate")
```
##### **Version Check in R:**
In R console, type
```
packageVersion("packagename")
```
'packagename' is the name of the package

## Usage:
To use python and R file in the system, open the PowerShell of the system. 

Before running the scripts, please type command:
```
pip3 install --upgrade pip
```

```
pip3 freeze
```
### Python:
For Medicaid Enrollment, Type 
``` 
python 'Forecasting_for_Enrollment.py'
``` 
For Medicaid Expenditure, Type
```
python 'Expenditure_Forecasting.py'
```
### R:
For Medicaid Enrollment, Type
```
Rscript "Medicaid_Enrollment_Prophet.R"
```
For Medicaid Expenditure, Type
```
Rscript "Medicaid_Expenditure_Prophet.R"
```
For Medicaid Enrollment, Type

Rscript "Medicaid_Enrollment_Prophet.R"
For Medicaid Expenditure, Type

Rscript "Medicaid_Expenditure_Prophet.R"
