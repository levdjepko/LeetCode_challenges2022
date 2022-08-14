class Solution {
    public void rotate(int[] nums, int k) {
        int[] newArray = nums.clone();
        if (k > nums.length) {
            k = k % nums.length;
        }
        for (int i = 0; i < newArray.length; i++) {
            nums[i] = newArray[(nums.length - k + i) % newArray.length];
        }
        
    }
}
