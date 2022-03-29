class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int array = m + n;
        int[] arr = new int[array];

        System.arraycopy(nums1, 0, arr, 0, m);
        System.arraycopy(nums2, 0, arr, m, n);
        Arrays.sort(arr);
        int mid = arr.length / 2;
        
        // if even 
        if (array % 2 == 0) {
            return ((arr[mid-1] + arr[mid]) / 2.0);
        }
        else {
            return arr[mid];
        }
    }   
}
