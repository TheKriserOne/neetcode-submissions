class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] b = new int[26];

        for (char c : s.toCharArray()) {
            b[c - 'a']++;
        }

        for (char c : t.toCharArray()) {
            b[c - 'a']--;
            if (b[c - 'a'] < 0) return false;
        }

        return true;    
    }
}