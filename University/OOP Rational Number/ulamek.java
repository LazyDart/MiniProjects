class Rational{
    private int numerator;
    private int denominator;

    public Rational(int x_numerator, int y_denominator) {
        this.numerator = x_numerator;
        this.denominator = y_denominator;

        validate();
    }

    private int nwd() {
        int k = numerator;
        int m = denominator;

        if (k == 0) {
            denominator = 1;
            return 1;
        }

        while (k != m) {
            if (k > m) k -= m;
            if (k < m) m -= k;
        }
        numerator = numerator / k;
        denominator = denominator / k;

        return k;
    }

    private void validate() {
        assert denominator != 0: "Division by Zero Error";

        nwd();

        if (denominator < 0) {
            numerator *= -1;
            denominator *= -1;
        }

        if (numerator == 0) {
            denominator = 1;
        }
    }

    public String asString() {
        String strresult = "";
        strresult = Integer.toString(numerator) + "/" + Integer.toString(denominator);
        return strresult;

    }

    public static Rational add(Rational x, Rational y) {
        int newdenominator = x.denominator * y.denominator;
        int newnumerator_1 = x.numerator * y.denominator;
        int newnumerator_2 = y.numerator * x.denominator;

        return new Rational(newnumerator_1 + newnumerator_2, newdenominator);
    }

    void increase(Rational x) {
        int newdenominator = denominator * x.denominator;
        int newnumerator_1 = numerator * x.denominator;
        int newnumerator_2 = x.numerator * denominator;
        numerator = newnumerator_1 + newnumerator_2;
        denominator = newdenominator;
        nwd();
    }

    public static Rational subtract(Rational x, Rational y) {
        int newdenominator = x.denominator * y.denominator;
        int newnumerator_1 = x.numerator * y.denominator;
        int newnumerator_2 = y.numerator * x.denominator;

        return new Rational(newnumerator_1 - newnumerator_2, newdenominator);
    }

    void decrease(Rational x) {
        int newdenominator = denominator * x.denominator;
        int newnumerator_1 = numerator * x.denominator;
        int newnumerator_2 = x.numerator * denominator;
        numerator = newnumerator_1 - newnumerator_2;
        denominator = newdenominator;
        nwd();
    }

    void inverse() {
        int newdenominator = numerator;
        numerator = denominator;
        denominator = newdenominator;
        validate();
    }

}