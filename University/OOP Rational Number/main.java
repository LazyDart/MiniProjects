class Main{
    public static void main(String[] args){
        Rational u1 = new Rational(0, 10);
        Rational u2 = new Rational(2, 3);
        System.out.println(u1.asString());

        System.out.println(Rational.add(u1, u2).asString());
//        u2.increase(new Rational(1, 3));

        u2.inverse();

        System.out.println(u2.asString());

        System.out.println(u2.asString());

    }
}