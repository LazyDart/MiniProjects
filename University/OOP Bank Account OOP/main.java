import java.lang.Math;
import java.util.Arrays;

// Main Class uses Account Class to make operations on ban accounts
class Main{
    // Create array of accounts and simulate transactions on them.
    // Show results
    public static void main(String[] args) {
        Account[] bank = new Account[] {new Account("Franek"), new Account("Andrzej")};

        simulateBank(bank, 10);

        displayAccounts(bank);
        System.out.println(bank[0].history);

    }

    // Conduct operation on an account based on n variable which defines whether to decrease or increase balance.
    public static void randomOperation(Integer n, Account account, Float amount){
        if (n == 0) {
            account.paycheck(amount);
        }
        if (n == 1) {
            account.payment(amount);
        }
    }

    // Simulate transactions on every account.
    public static void simulateBank(Account[] bank, Integer n_operations){
        // For every account in bank
        for (Account account: bank) {
            // Until all banks have n_operations
            for (int i = 0; i < n_operations; i++) {
                // pick random operation
                int op_type = (int)(Math.random()*2);
                // pick random amount up to 100
                float op_amount = (float)(Math.random()*100);

                // Make the operation
                randomOperation(op_type, account, op_amount);
            }
        }
    }
    // Display balance of every account in Bank
    public static void displayAccounts(Account[] bank){
        for (Account account: bank) {
            System.out.println(account.name + ": " + Float.toString(account.returnbalance()));
        }
    }
}