class Solution {
    public boolean isPalindrome(String s) {
        char[] arr = s.toCharArray();
        Deque<Integer> q = new LinkedList<>();

        for (int i = 0; i < arr.length; i++) {
            if (!(Character.isAlphabetic(arr[i]) || Character.isDigit(arr[i]))) continue;
            q.add((int) Character.toLowerCase(arr[i]));
        }
        while (q.size() > 1) {
            if (q.pollFirst() != q.pollLast()) return false;
        } 
        return true;
    }
}