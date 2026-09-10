class Solution {
    private Set<Integer> initial = new HashSet<>();
    public int longestConsecutive(int[] nums) {
        
        for (Integer n: nums) {
            initial.add(n);
        }
        
        Integer max = 0;
        while (!initial.isEmpty()) {
            Integer elem = initial.iterator().next();
            initial.remove(elem);
            
            Set<Integer> dfsSet = new HashSet<>();
            dfsSet.add(elem);
            dfs(dfsSet, elem);
            max = Math.max(max, dfsSet.size());
        }
        return max;
    }
    
    private void dfs(Set<Integer> s, Integer elem) {
        if (initial.contains(elem + 1)) {
            initial.remove(elem + 1);
            s.add(elem + 1);
            dfs(s, elem + 1);
        }
        
        if (initial.contains(elem - 1)) {
            initial.remove(elem - 1);
            s.add(elem - 1);
            dfs(s, elem - 1);
        }
    } 
}

