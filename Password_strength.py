import re
from datetime import datetime

class MPINindicator:
    def check_date_pattern(self, mpin, date_str): #Check if PIN matches common date patterns from a date string (DD-MM-YYYY)
        if not date_str:
            return False
        
        try:
            date_obj = datetime.strptime(date_str, "%d-%m-%Y")
            # Extract parts
            day = date_obj.day
            month = date_obj.month
            year = date_obj.year
            
            # Format with leading zeros
            day_str = f"{day:02d}"
            month_str = f"{month:02d}"
            year_last_two = f"{year % 100:02d}"
            year_str = str(year)
            
            # Create various date formats to check
            date_formats = []
            
            if len(mpin) == 4:
                date_formats = [
                    day_str + month_str,           # DDMM
                    month_str + day_str,           # MMDD
                    month_str + year_last_two,     # MMYY
                    year_last_two + month_str,     # YYMM
                    year_last_two + day_str,       # YYDD
                    day_str + year_last_two        # DDYY
                    ]
            
            elif len(mpin) == 6:
                date_formats = [
                    day_str + month_str + year_last_two,    # DDMMYY
                    month_str + day_str + year_last_two,    # MMDDYY
                    year_last_two + month_str + day_str,    # YYMMDD
                    year_last_two + day_str + month_str,    # YYDDMM
                    
                    day_str + year_str,     #DDYYYY
                    month_str + year_str,   #MMYYYY
                    year_str + day_str,     #YYYYDD
                    year_str + month_str,   #YYYYMM
                    ]
                
            for format in date_formats:
                if format == mpin:
                    return True
                return False
            
        except ValueError:
            return False
    
    #Part : Strength check and provide specific reasons for weakness
    def indicate_mpin_strength(self, mpin, dob_self=None, dob_spouse=None, anniversary=None):
        if len(mpin) not in [4, 6]:
            return {"strength": "INVALID", "reasons": ["PIN must be 4 or 6 digits"]}
        
        
        reasons = []
           
        # Check demographic info
        if dob_self and self.check_date_pattern(mpin, dob_self):
            reasons.append("DEMOGRAPHIC_DOB_SELF")
        
        if dob_spouse and self.check_date_pattern(mpin, dob_spouse):
            reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
        
        if anniversary and self.check_date_pattern(mpin, anniversary):
            reasons.append("DEMOGRAPHIC_ANNIVERSARY")
        
        # Determine strength based on reasons
        strength = "STRONG" if not reasons else "WEAK"
        
        return {
            "strength": strength,
            "reasons": reasons
        }

if __name__ == "__main__":
    indicator = MPINindicator() 
    mpin = input("Enter your MPIN (4 or 6 digits): ").strip()

    dob = input("Enter your date of birth (DD-MM-YYYY), or press Enter to skip: ").strip()
    dob = dob if dob else None

    spouse_dob = input("Enter your spouse's date of birth (DD-MM-YYYY), or press Enter to skip: ").strip()
    spouse_dob = spouse_dob if spouse_dob else None

    anniversary = input("Enter your anniversary date (DD-MM-YYYY), or press Enter to skip: ").strip()
    anniversary = anniversary if anniversary else None

    if len(mpin) == 4:
        result_4 = indicator.indicate_mpin_strength(mpin, dob, spouse_dob, anniversary)
        print(f"Strength: {result_4['strength']}")
        print(f"Reasons: {result_4['reasons']}")
        
    # Part D example - 6 digit PIN
    if len(mpin) == 6:
        result_6 = indicator.indicate_mpin_strength(mpin, dob, spouse_dob, anniversary)
        print(f"Strength: {result_6['strength']}")
        print(f"Reasons: {result_6['reasons']}")