class Solution {
    public int singleNumber(int[] nums) {
        // find the first digit in the array that doesn't have a repeat
        // using the hashmap to avoid sorting and to do it more effectively
        HashMap <Integer, Integer> hm = new HashMap<>();
        int result = -1;
        for (int i = 0; i < nums.length; i++) {
            if (!hm.containsKey(nums[i])) {
                hm.put(nums[i], 1);
            } else {
                // 2 here because we do not care about the exact count of occurrences of that duplicate
                hm.put(nums[i], 2);
            }
        }
        for (int key: hm.keySet()) {
            if (hm.get(key) == 1) {
                result = key;
            }
        }
        return result;
    }
}
