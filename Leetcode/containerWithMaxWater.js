/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    // var max;
    var min;
    var maxArea = 0;
    for (const i in height) {
        for (const j in height) {
            const a = height[i];
            const b =height[j];

            if (a<=b) {
                min =a;
                // max = b;
            } else {
                min = b;
                // max = a;
            };

            const area = min * Math.abs(i-j)

            if (area > maxArea) {
                maxArea = area;
            }
        };
    };

    console.log(maxArea)
};

maxArea([1,8,6,2,5,4,8,3,7])

/* Solution is correct but not efficient with time complexity of O(m^2) */

// below one is correct

// Using two pointer to get width easily and improve time complexity from O(n^2) to O(n).