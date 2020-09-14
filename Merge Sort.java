import java.util.*;
public class HelloWorld{

     public static void main(String []args){
        int[] l1 = new int[] {5,3,1,10,15,3,4, 5, 11};
        mergeSort(l1, l1.length);
        for(int i =0; i< l1.length;++i){
            System.out.print(l1[i]+ " ");
        }
     }
     
     public static void mergeSort(int[] arr, int length) {
        if(length < 2) {
            return;
        }
        int mid = length / 2;
        int[] left = new int[mid];
        int[] right = new int[length - mid];
        
        int k = 0;
        for(int i=0; i<length; i++) {
            if(i < mid) {
                left[i] = arr[i];
            } else {
                right[k++] = arr[i];
            }
        }
        
        mergeSort(left, mid);
        mergeSort(right, length - mid);
        merge(left, right, arr);
     }
     
     public static void merge(int[] l1, int[] l2, int[] arr) {
        int p1 = 0;
        int p2 = 0;
        int count = 0;
        while(p1 < l1.length && p2 < l2.length) {
            if(l1[p1] < l2[p2]) {
                arr[count] = l1[p1];
                p1++;
            } else {
                arr[count] = l2[p2];
                p2++;
            }
            count++;
        }
        while (p2 < l2.length) {
            arr[count++] = l2[p2++];
        }
        while (p1 < l1.length) {
            arr[count++] = l1[p1++];
        }
     }
}
