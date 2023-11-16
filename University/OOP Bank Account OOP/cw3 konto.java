import java.util.ArrayList;
import java.util.List;

class Account{
    // User's Name Required Argument
    public String name;
    // Starting value for balance
    private float balance = 0;
    // History of All Transactions
    public List<String> history = new ArrayList<String>();

    // Initialise Arguments
    public Account(String acc_name) {
        this.name = acc_name;
    }

    // Paycheck Function - increases balance
    public void paycheck(float v) {
        balance = balance + v;
        // Update History
        history.add("Paycheck: " + Float.toString(v));
    }
    // Payment Function - decreases balance
    public void payment(float v) {
        balance = balance - v;
        // Update History
        history.add("Payment: " + Float.toString(v));
    }

    // Returns balance
    public float returnbalance() {
        return balance;
    }
}
