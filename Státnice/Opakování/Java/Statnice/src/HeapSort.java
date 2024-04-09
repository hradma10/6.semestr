public class HeapSort {

    private static int heapsize;

    private static void MaxHeapify(int[] array, int i) {
        int largest = i;
        int l = Left(i);
        int r = Right(i);

        if (l < heapsize && array[l] > array[largest]) {
            largest = l;
        }

        if (r < heapsize && array[r] > array[largest]) {
            largest = r;
        }

        if (largest != i) {
            swap(array, i, largest);
            MaxHeapify(array, largest);
        }
    }

    private static void swap(int[] array, int firstIndex, int secondIndex){
        int temp = array[firstIndex];
        array[firstIndex] = array[secondIndex];
        array[secondIndex] = temp;
    }


    public static void sort(int[] array){
        BuildMaxHeap(array);
        for (int i = array.length - 1; i >= 1; i--){
            swap(array,0, i);
            heapsize--;
            MaxHeapify(array, 0);
        }
    }

    private static void BuildMaxHeap(int[] array){
        heapsize = array.length;
        for (int i = (int) (Math.floor((double) array.length / 2) - 1); i >= 0 ; i--){
            MaxHeapify(array, i);
        }
    }


    public static int Parent(int i){
        return (int) Math.floor((double) (i - 1) / 2);
    }

    public static int Left(int i){
        return 2 * i + 1;
    }

    public static int Right(int i){
        return 2 * i + 2;
    }
}
