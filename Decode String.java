import java.util.*;

public class HelloWorld{

     public static void main(String []args){
        decodeString("2[b3[a]]");
     }
     
     public static String decodeString(String s) {
        Stack<Integer> integers = new Stack<>();
        Stack<String> strings = new Stack<>();
        int pointer = 0;
        String result = "";
        while(pointer < s.length()) {
            char current = s.charAt(pointer);
            if(Character.isDigit(current)) {
                int num = 0;
                while(Character.isDigit(s.charAt(pointer))) {
                    num = num * 10 + s.charAt(pointer) - '0';
                    pointer++;
                }
                integers.push(num);
            } else if(current == '[') {
                strings.push(result);
                result = "";
                pointer++;
            } else if(current == ']') {
                StringBuilder sb = new StringBuilder(strings.pop());
                int count = integers.pop();
                for(int i=1; i<=count; i++) {
                    sb.append(result);
                }
                result = sb.toString();
                pointer++;
            } else {
                result += current;
                pointer++;
            }
            
            System.out.println("Index: " + pointer + "  Character: " + current + "  Result: " + result);
            System.out.print("Integer Stack: ");
            for(int q : integers) {
                System.out.print(q + " ");
            }
            System.out.print("\nString stack: ");
            for(String q : strings) {
                if(q.equals("")) {
                    System.out.print("blank ");
                } else {
                    System.out.print(q + " ");
                }
            }
            System.out.println();
            System.out.println("Result: "+result);
            System.out.println("---");
        }
        return result;
    }

}
