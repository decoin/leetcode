class Solution {
    public int findKthLargest(int[] nums, int k) {

        buildHeap(nums, k);
        for(int i = k; i < nums.length; i++){
            int number = nums[i];
            if(number > nums[0]){
                nums[0] = number;
                down(0,k,nums);
            }
        }

        return nums[0];
    }

    private void buildHeap(int[] heap, int len){
        for(int i = (len - 2) / 2; i >= 0; i--){
            down(i, len, heap);
        }
    }

    

    private void down(int i, int n, int[] heap){
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        int min = i;

        if(l < n && heap[l] < heap[min])
            min = l;

        if(r < n && heap[r] < heap[min])
            min = r;

        if(min != i){
            swap(heap, min, i);
            down(min, n, heap);
        }
    }

    private void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
