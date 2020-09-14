import java.util.*;
public class HelloWorld{

    public static void main(String []args){
        int[] arr = new int[] {4,2,3,8,15,1};
        quickSort(arr, 0, arr.length-1);
        System.out.println(Arrays.toString(arr));
    }
    
    public static void quickSort(int[] arr, int left, int right) {
        if (left >= right) {
            return;
        }
        int p = partition(arr, left, right);
        quickSort(arr, left, p-1);
        quickSort(arr, p+1, right);
    }
    
    public static int partition(int[] arr, int left, int right) {
        int pivot = arr[right];
        int i = left - 1;
        for(int j=left; j < right; j++) {
            if(arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i+1, right);
        return i+1;
    }
    
    public static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
