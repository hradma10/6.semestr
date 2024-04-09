import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int[] array = new int[]{1, 5, 3, 7, 2, 4, 8, 9, 6, 4};
        System.out.println(Arrays.toString(array));
        HeapSort.sort(array);
        System.out.println(Arrays.toString(array));
    }


}
