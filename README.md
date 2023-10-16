![EMR_Technical_Solutions](https://github.com/bravealex1/Medicaid-Enrollment-Prediction/assets/67205873/351769a1-ea10-46d3-9502-a0051c4ec265)

Medicaid stands as one of the principal insurance programs in the United States, operating as a collaborative initiative between federal and state governments to assist with medical costs for individuals with limited income and resources. It bears similarities to Medicare, another major health insurance program, but they serve distinct demographics. While Medicare is a federal health insurance program primarily for people aged 65 or older, and some under 65 with specific disabilities or conditions, Medicaid predominantly focuses on individuals and families with low income.

The distinct nature of Medicaid and Medicare caters to different groups of people, with differences highlighted by the U.S. Department of Health and Human Services (HHS). Unlike Medicare, Medicaid is financed by the federal government but administered at the state level, resulting in unique Medicaid programs in each state. Given that both state and federal governments share the financial responsibilities, accurate forecasting data is vital for future budgeting, underlining the significance of this project.

Leveraging existing data on Medicaid Enrollment and Expenditure, our objective is to forecast these variables for the next decade to aid governments in budget adjustments. This predictive endeavor, known as "Time Series Analysis", involves scrutinizing a sequence of data points collected over specific time intervals, serving as the crux of this project.

EMR Technical Solution (EMRTS), a company specializing in professional Medicaid analysis, has assigned this project, officially titled "Reflections on Medicaid Enrollment for the Next Decade". It forms part of an ongoing series of blogs, with each new entry incorporating the most recent data and insights. For this iteration, we have included more extensive information and data, encompassing Medicaid expenditure. Additionally, we have adopted a new graphical tool, Instadeq, to enhance our presentation of data.

This continuous project represents a commitment to providing the most current and comprehensive analysis, thereby supporting governments in making informed budgetary decisions for Medicaid. By embracing advanced tools and methodologies, we aim to deliver insights that are both accurate and actionable, contributing to the sustainable management of Medicaid programs across states.# Medicaid-Enrollment-Prediction

Inputing the data, editing data, creating and training the model, and ploting the model are the completed processes of forecasting the data. This project is completed by Python and R. The installation of Python and R ,and the specific libraries are required to run the script.

Python Installation:
Version of Python: 3.8.1 or above

Website: www.python.org

Python Libraries Installtion:
Three libraries are required.

pandas:
Version of pandas: 1.5.3 In the terminal,type

pip3 install pandas
matplotlib:
Version of maplotlib: 3.7.2 In the terminal, type

pip3 install matplotlib
prophet:
Version of prophet: 1.1.4 In the terminal, type

pip3 install prophet
Version Check:
pip list
Type this command in terminal

R Installation:
Version of R: 4.3.1 or above

Website: www.R-project.org

R Packages Installtion:
To install the packages of R, you will need to open the console of R.

prophet:
Version of prophet: 1.0.0

install.packages("prophet")
tidyverse:
Version of tidyverse: 2.0.0

install.packages("tidyverse")
lubridate:
Version of lubridate: 1.9.3

install.packages("lubridate")
Version Check in R:
In R console, type

packageVersion("packagename")
'packagename' is the name of the package

Usage:
To use python and R file in the system, open the PowerShell of the system.

Before running the scripts, please type command:

pip3 install --upgrade pip
pip3 freeze
Python:
For Medicaid Enrollment, Type

python 'Forecasting_for_Enrollment.py'
For Medicaid Expenditure, Type

python 'Expenditure_Forecasting.py'
R:
For Medicaid Enrollment, Type

Rscript "Medicaid_Enrollment_Prophet.R"
For Medicaid Expenditure, Type

Rscript "Medicaid_Expenditure_Prophet.R"
