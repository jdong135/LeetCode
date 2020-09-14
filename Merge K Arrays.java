import java.util.*;
public class HelloWorld{

     public static void main(String []args){
        int[][] arrays = new int[][]{{1,3,5},{2,3},{2,3,5,8}};
        for(int[] arr : arrays) {
            System.out.print("["+Arrays.toString(arr)+"] ");
        }
        System.out.println("\n");
        System.out.println(mergeKArrays(arrays));
     }
     
    public static List<Integer> mergeKArrays(int[][] arrays) {
        // create array of length k, initially [0,0,...,0]
        // It is used to track the indices in each subarray
        int[] firstUnused = new int[arrays.length];
        
        // result is the final sorted list
        List<Integer> result = new ArrayList<>();
        
        // n represents the total numer of elements that will be sorted
        int n = 0;
        for (int i = 0; i < arrays.length; i++) {
            n += arrays[i].length;
        }
        
        // We cycle through n times because we will pick the min val n times
        for (int i = 0; i < n; i++) {
            // minIndex is the index of the subarray that has the smallest element
            // minValue is the overall current minvalue that is going to be added
            int minIndex = -1;
            int minValue = 0;
            
            // We iterate through the 3 arrays to find the min value
            for (int j = 0; j < arrays.length; j++) {
                System.out.println("First unused: " + Arrays.toString(firstUnused));
                // arrays[j] represents a nested subarray
                System.out.println("arrays[j]: "+Arrays.toString(arrays[j]));
                
                // firstUnused[j] = pointer for subarray arrays[j]
                // If firstUnused[j] >= arrays[j].length, that means we've already extracted all of that subarray's values, so we skip
                if (firstUnused[j] < arrays[j].length) {
                    // minIndex == -1 is for the first iteration
                    if (minIndex == -1 || minValue > arrays[j][firstUnused[j]]) {
                      minIndex = j;
                      // arrays[j] is the subarray
                      // firstUnused[j] is the pointer for that subarray
                      minValue = arrays[j][firstUnused[j]];
                    }
              }
              System.out.println("Min index: " + minIndex + "\tMin value: " + minValue + "\n------");
            }
            result.add(minValue);
            // Move the pointer forward for the array that we took from
            firstUnused[minIndex]++;
            System.out.println("Result: " + result + "\n");
        }
        return result;
    }
}
