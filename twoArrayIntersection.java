public int[] intersect(int[] nums1, int[] nums2) {
        HashMap <Integer, Integer> map = new HashMap<>();
        
        // get all the elements of the first array in a hashmap
        for (int i = 0; i < nums1.length; i++) {
            if (!map.containsKey(nums1[i])){
                map.put(nums1[i], 1);
            } else {
                int count = map.get(nums1[i]);
                map.put(nums1[i], count + 1);
            }
        }
        List <Integer> resultsList = new ArrayList();
  
        // check all the elements of the second array
        for (int i = 0; i < nums2.length; i++) {
            if (map.containsKey(nums2[i])){
                int count = map.get(nums2[i]);
                if (count > 0) {
                    resultsList.add(nums2[i]);
                    count--;
                    map.put(nums2[i], count);
                }
            }
                
        }
        
        // convert from list to array
        Integer [] array = resultsList.toArray(new Integer[0]);
        return resultsList.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
