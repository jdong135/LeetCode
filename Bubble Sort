import java.util.*;
public class HelloWorld{

     public static void main(String []args){
        int[] l1 = new int[] {5,3,1,10,15,3,4, 5, 11};
        bubbleSort(l1);
        for(int i=0; i<l1.length; i++) {
            System.out.print(l1[i] + " ");
        }
     }
     
     public static void bubbleSort(int[] arr) {
         for(int i=arr.length-1; i>=0; i--) {
             for(int j=0; j<i; j++) {
                 if(arr[j] > arr[j+1]) {
                     swap(arr, j, j+1);
                 }
             }
         }
     }
     
     public static void swap(int[] arr, int index1, int index2) {
         int temp = arr[index2];
         arr[index2] = arr[index1];
         arr[index1] = temp;
     }
}
