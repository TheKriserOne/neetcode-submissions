class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> m = Map.of('(', ')', '{', '}', '[', ']');

        for (char c : s.toCharArray()) {
            if (m.containsKey(c)) {
                stack.push(c);
            } else if (stack.isEmpty() || c != m.get(stack.pop())) {
                return false;
            }
        }
        return stack.isEmpty();
    }
}