A simple Python module to evaluate the strength of a 4-digit or 6-digit MPIN (Mobile PIN) by checking if it matches any date patterns based on provided demographic information such as Date of Birth (DOB) or Anniversary. This helps avoid weak MPINs based on easily guessable personal dates.

# Features

Accepts MPIN of 4 or 6 digits

Detects if the MPIN resembles : /n
a> Your Date of Birth /n
b> Your Spouse's Date of Birth /n
c> Your Anniversary /n

Supports common date formats like: /n
-> DDMM, MMDD, MMYY, YYMM, DDYY, YYDD (for 4-digit MPINs) /n
-> DDMMYY, MMDDYY, YYMMDD, YYDDMM, DDYYYY, MMYYYY, YYYYDD, YYYYMM (for 6-digit MPINs) /n

Returns whether the MPIN is STRONG or WEAK, with reasons for weakness
