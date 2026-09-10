class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        if (nums.length == k) return nums;
        Map<Integer, Integer> map = new HashMap<>();
        List<Integer>[] frequent = new List[nums.length + 1];

        for (int i : nums) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }

        map.entrySet().forEach(e -> {
            int val = e.getValue();
            if (frequent[val] == null) frequent[val] = new ArrayList<>();
            frequent[val].add(e.getKey());
        });

        int[] res = new int[k];

        for (int i = nums.length; i > 0 && k > 0; i--) {
            if (frequent[i] == null || frequent[i].isEmpty()) continue;
            var iter = frequent[i].iterator();
            while (k > 0 && iter.hasNext()) {
                res[k - 1] = iter.next();
                k--;
            }
        }

        return res;
       
    }
}