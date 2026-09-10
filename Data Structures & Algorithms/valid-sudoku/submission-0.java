class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> r = new HashMap<>();
        Map<Integer, Set<Character>> c = new HashMap<>();
        Map<List<Integer>, Set<Character>> trios = new HashMap<>();
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') continue;

                r.putIfAbsent(i, new HashSet<>());
                if (r.get(i).contains(board[i][j])) return false;
                r.get(i).add(board[i][j]);

                c.putIfAbsent(j, new HashSet<>());
                if (c.get(j).contains(board[i][j])) return false;
                c.get(j).add(board[i][j]);

                List<Integer> key = List.of(i / 3, j / 3);
                trios.putIfAbsent(key, new HashSet<>());
                if (trios.get(key).contains(board[i][j])) return false;
                trios.get(key).add(board[i][j]);
            }
        }
        return true;
    }
}