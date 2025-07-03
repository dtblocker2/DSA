class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Trivial cases
        if numRows == 1 or numRows >= len(s):
            return s

        # Prepare a list of rows
        rows = [""] * numRows
        curr_row, step = 0, 1          # step = +1 (down) or -1 (up)

        for ch in s:
            rows[curr_row] += ch
            # Reverse direction at the top or bottom
            if curr_row == 0:
                step = 1
            elif curr_row == numRows - 1:
                step = -1
            curr_row += step

        # Join all rows to get the final string
        return "".join(rows)
