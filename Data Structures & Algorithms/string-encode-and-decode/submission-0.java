public class Solution {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder builder = new StringBuilder();

        for (String str : strs) {
            builder.append(str.length()).append("#").append(str);
        }
        return builder.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> strs = new ArrayList<>();

        while (s.length() > 0) {
            var start = s.indexOf('#');
            var length = Integer.parseInt(s.substring(0, start));
            var end = start + length + 1;
            strs.add(s.substring(start + 1, end));
            s = s.substring(end);
        }

        return strs;
    }
}