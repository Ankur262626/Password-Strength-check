A simple Python module to evaluate the strength of a 4-digit or 6-digit MPIN (Mobile PIN) by checking if it matches any date patterns based on provided demographic information such as Date of Birth (DOB) or Anniversary. This helps avoid weak MPINs based on easily guessable personal dates.

# Features

> Accepts MPIN of 4 or 6 digits
>Detects if the MPIN resembles:
> a> Your Date of Birth
> b> Your Spouse's Date of Birth
> c> Your Anniversary

> Supports common date formats like:
> > DDMM, MMDD, MMYY, YYMM, DDYY, YYDD (for 4-digit MPINs)
> > DDMMYY, MMDDYY, YYMMDD, YYDDMM, DDYYYY, MMYYYY, YYYYDD, YYYYMM (for 6-digit MPINs)

Returns whether the MPIN is STRONG or WEAK, with reasons for weakness
