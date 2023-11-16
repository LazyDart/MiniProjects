import java.lang.Math;
import java.util.Arrays;

class NumberGenerator{

    // Show results of the randomTests. 
    // Uses counts table to verify how many times each container was drawn
    public static void calculateResults(Integer[] counts, Integer n_randomTests) {
        
        // Set starting values for sum, max and min.
        // min will always be smaller or equal to n_randomTests
        // max and sum will always be higher than 0
        // Hence the default values, 
        // which assure that those metrics will be updated 
        int sum = 0;
        int max = 0;
        int min = n_randomTests;
        
        // For each container in counts.
        for (int value: counts) {
            // If container has been drawn least frequently update min
            if (value < min) {
                min = value;
            }
            // If container has been drawn most frequently update max
            if (value > max) {
                max = value;
            }
            sum += value; // Sum is a sum of values from all containers.
        }

        // Create String representations of each metric
        String p_diff = Float.toString((float)(max - min)/max * 100);
        String str_sum = Integer.toString(sum);
        String str_min = Integer.toString(min);
        String str_max = Integer.toString(max);

        // Print info about current state to a console.
        System.out.println("Suma liczników = " 
                            + str_sum 
                            + ", różnica procentowo = " 
                            + p_diff 
                            + "%, różnica " 
                            + Integer.toString(max-min) // calculate range 
                            + ", min = " 
                            + str_min 
                            + ", max = " 
                            + str_max);
    }

    public static void randomTest(int n, int n_randomTests, int verbose) {
        
        // print starting message
        System.out.println("randomTest dla liczby przegródek = " 
                           + Integer.toString(n) 
                           + " przy liczbie losowań = " 
                           + Integer.toString(n_randomTests) 
                           + " z pośrednimi wydrukami co " 
                           + Integer.toString(verbose)
                           + " losowań.");

        // Create array of size equal to number of containers.
        Integer[] counter = new Integer[n];
        // Fill values with 0
        Arrays.fill(counter, 0);

        // Until all randomTests are conducted
        for (int i = 0; i < n_randomTests; i++) {
            // pick random container
            int rand_result = (int)(Math.random()*n);
            
            // update container value
            counter[rand_result] += 1;
            
            // if number of randomTest is divisible by verbose
            // show results
            if ((i + 1) % verbose == 0) {
                calculateResults(counter, n_randomTests);
            }
        }

        // show final results
        System.out.println("Ostateczny wynik:");
        calculateResults(counter, n_randomTests);

    }

    public static void main(String[] args) {
        
        // Assert that every argument has been provided.
        assert args.length == 3: "3 Arguments should be provided!";

        // Transform Input Strings into Integers
        // The first one is number of containers
        // The second number of randomTests
        // The last one describes how often results are to be displayed
        int n = Integer.parseInt(args[0]);
        int n_randomTests = Integer.parseInt(args[1]);
        int verbose = Integer.parseInt(args[2]);

        // Assert all arguments are greater than 0
        assert (n > 0) && (n_randomTests > 0) && (verbose > 0): "All arguments must be greater than 0!";

        //Conduct random randomTests. Shows results in the console
        randomTest(n, n_randomTests, verbose);

    }
}