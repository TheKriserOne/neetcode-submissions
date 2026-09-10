class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> list = new ArrayList<>();
      
        for (int i = 0; i < strs.length; i++) {
            boolean added = false;

            // Check if the current string fits into an existing group
            for (List<String> group : list) {
                if (isAnagram(group.get(0), strs[i])) {
                    group.add(strs[i]);
                    added = true;
                    break;
                }
            }

            // If no matching group found, create a new group
            if (!added) {
                List<String> newGroup = new ArrayList<>();
                newGroup.add(strs[i]);
                list.add(newGroup);
            }
        }
        return list;
    }
     public boolean isAnagram(String s, String t) {
     if (s.length() != t.length()) return false;
        if ((s + s).contains(t))
            return true;
        int[] b = new int[26];
        int count = 0;

        for (char c : s.toCharArray()) {
            b[c - 'a']++;
            count++;
        }

        for (char c : t.toCharArray()) {
            b[c - 'a']--;
            if (b[c - 'a'] < 0) return false;
            count--;
        }

        return count == 0; 
    }
}