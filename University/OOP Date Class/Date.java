// Create Package.
package calendar;

public class Date {
    // Set default days for different months array used throughout calculations.
    // There is only one case for february. Leap years are calculated separately from this array.
    private static Integer[] monthDays = new Integer[] {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    // Define Data attributes
    private int day;
    private int month;
    private int year;
    
    // Default constructor, sets the date to be 5/10/2023
    public Date() {
        this.day = 5;
        this.month = 10;
        this.year = 2023;
        
        // Validates whether input is correct
        validate(day, month, year);
    }

    // Copy constructor. Copies data from other Data instance.
    public Date(Date date) {
        // Copy values from getter methods.
        this.day = date.getday();
        this.month = date.getmonth();
        this.year = date.getyear();

        // Validates whether input is correct
        validate(day, month, year);
    }

    // Data constructor using 3 integers representing days, months and years.
    public Date(int day, int month, int year) {
        this.day = day;
        this.month = month;
        this.year = year;
    
        // Validates whether input is correct
        validate(day, month, year);
    }

    // Validation function assures all values are in their normal-ranges.
    private static void validate(int val_day, int val_month, int val_year) {
        // Subtract 1 to make it compatible with monthDays array.
        val_month = val_month - 1;

        // Checks for leap year.
        int leap = isLeap(val_year)? 1 : 0;
        // Gets maximum possible days in a given month.
        int upperBound = monthDays[val_month];

        // Checks whether day fits day-ranges.
        assert ((val_day <= upperBound) || ((val_day <= upperBound + leap) && (val_month == 1))) && (1 <= val_day): "Day in invalid Range!";
        // Checcks whether month fits month-ranges. Range is 0 - 11 cause of subtraction few operations ago.
        assert 0 <= val_month && val_month <= 11: "Month in invalid Range! Valid Range = (1-12)";
        
    }

    //  Checks whether a year is a leap year.
    public static Boolean isLeap(int checkYear) {
        // if year is divisible by 4 And it is not divisible by 100 with an exception of 400. - it is a leap year.
        if ((checkYear % 4 == 0) && (!(checkYear % 100 == 0)) || (checkYear % 400 == 0)) {
            return true;
        }
        else {
            return false;
        }

    }

    // How many days in year check.
    public static int dayCount(int rok) {
        if (isLeap(rok)) {
            return 366;
        }
        else {
            return 365;
        }
    }

    // How many days in a particular month and year check.
    public static int dayCount(int miesiąc, int rok) {
        if (isLeap(rok) && (miesiąc == 2)) {
            return 29;
        }
        else {
            return monthDays[miesiąc - 1];
        }
    }

    // Increase current date instance by 1 day.
    public void nextDay() {
        // If increasing by 1 day changes month make necessary calcuations.
        if (day + 1 > (monthDays[month - 1] + ((isLeap(year) && month == 2) ? 1 : 0))) {
            int new_day = 1; // Sets day to 1
            int new_month = month + 1; // Increases month by 1
            int new_year = year; // create a year varaible used for calcuations
            
            // if after increasing months it is greater than 12
            if (new_month > 12) {
                new_month = 1; // set month to 1
                new_year += 1; // increase year by 1
            }

            // Override current attributes with newly calculated ones.
            day = new_day;
            month = new_month;
            year = new_year;

            return;
        }
        // Else just add 1 to a day value.
        else {
            day = day + 1;
        }
    }

    // Check whether a current date instance is earlier than the one passed as an argument.
    public boolean before(Date date) {

        // Calculate difference between each of attributes and assign proper weights to each difference.
        int eval = (year - date.getyear()) * 1200 + (month - date.getmonth()) * 100 + (day - date.getday());
        
        // If sum of weighted differences is smaller than 0. Then in fact instance is earlier.
        if (eval < 0) {
            return true;
        }
        // Else it is equal or greater.
        else {
            return false;
        }
    }

    // Check whether two dates are eqaul
    public boolean isEqual(Date date) {
        // if attributes are equal then the objects represent the same date.
        if ((day == date.getday()) && (month == date.getmonth()) && (year == date.getyear())) {
            return true;
        }
        else {
            return false;
        }
    }

    // Calculate day difference between 2 dates.
    // Particularly (Argument Date) - (Instance Date).
    public int daysBefore(Date date) {

        // Copy current Date instance
        Date compDate = new Date(day, month, year);

        // Check whether this copy *is not* earlier or equal than date passed as an argument.
        if ((!compDate.before(date)) && (!compDate.isEqual(date))) {
            // If it is not earlier then reverse the calculations and multiply by -1.
            // It is a necessary step as my implementation is not symmetrical.
            return -date.daysBefore(compDate);
        }

        // Copy values from current instance
        int calc_year = year;
        int calc_month = month;
        int calc_day = day;    
        
        // Prepare variable to return.
        int days = 0;

        //  Year count is used in calculations of leap years.
        int year_count = calc_year;

        if ((calc_month > 2) 
            || ((calc_month == 2) 
            && calc_day < 29)) {
            // If current date instance already passed the leap then we can skip it from calculations.
            // We are skipping it by increasing by 1.
            year_count += 1;
        }

        int added_leaps = 0;
        
        // For each year between year_count and date.getyear()
        while (year_count <= date.getyear()) {
            // If it is a leap year then increase leap year count.
            if (Date.isLeap(year_count)) {
                added_leaps += 1;
            }
            // Increase year_count
            year_count += 1;
        }
        int month_count = (date.getyear() - calc_year) * 12 + (date.getmonth() - calc_month);
        
        // If final date has not passed the leap subtract 1 from added_leaps
        if (//(calc_year != date.getyear()) && 
        (Date.isLeap(date.getyear())) 
            && ((date.getmonth() < 2) || ((date.getmonth() == 2) && date.getday() <= 29))) {
            
            added_leaps -= 1;
        }
        
        // Calculate the month range between dates.
        int i = 1;
        int current_month = calc_month - 1; // -1 for compatibility with monthDays
        current_month = current_month % 12; 

        // For each month separating Instance date from argument date
        while (i <= month_count) {
            // Add month duration to a total sum.
            days += monthDays[current_month];
            i += 1;
            // Go to next iteration assure values are in their normal-ranges.
            current_month += 1;
            current_month = current_month % 12;
        }
        
        days += added_leaps; // Add Leaps
        days += date.getday(); // Add Days from final month
        days -= calc_day; // Subtract Days from starting month.

        return days;
    }

    // Increases Date Instance by n days.
    public void addDays(int n) {

        // If adding n does not impact months then just add n to days. 
        int restForMonth = monthDays[month - 1] - day + ((isLeap(year) && month == 2) ? 1 : 0);
        if (n <= restForMonth) {
            day = day + n;
            // return new Data(day + n, month, year);
            return;
        }

        // Subtract number of days needed to finish current month from n.
        n -= restForMonth;

        // Set current state of calculations
        
        // Here is a hidden += 1 and -= 1 for current_month value.
        // We add 1 to go to the next month and we subtract 1 to assure compatibility with monthDays.
        int current_month = month;
        int current_year = year;

        // while n is greater than number of days in a current month
        while (n > (monthDays[current_month] + ((isLeap(year) && current_month == 1) ? 1 : 0))) {
            // Subtract number of days this month from n.
            n -= monthDays[current_month];

            // Go to next iteration.
            current_month += 1;
            current_month = current_month % 12;
            
            // Add Year if month passed december
            if (current_month == 0) {
                current_year += 1;
            }

            // If during calculations leap is passed subtract 1 from n.
            if ((current_month == 2) && isLeap(current_year)) {
                n -= 1;
            }
        }

        // Add 1 to display month correctly.
        // Earlier it was smaller for compatibility with monthDays
        current_month += 1;

        // n might be equal to 0 if leap year caused issues
        // In this case reverse n to the last day of last month
        // and subtract month.
        if (n == 0) {
            n = monthDays[current_month];
            current_month -= 1;
        }

        // Override current attributes with new ones.
        day = n;
        month = current_month;
        year = current_year;
    }


    // Getters
    public int getday(){
        return day;
    }
    public int getmonth(){
        return month;
    }
    public int getyear(){
        return year;
    }
    
    // Printing
    public String toString() {
        return Integer.toString(getday()) + "/" + Integer.toString(getmonth()) + "/" + Integer.toString(getyear());
    }

}
