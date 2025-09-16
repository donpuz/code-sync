/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // [2, 11, 7, 15]
    // {2: 0}
    // {2: 0, }

    // [3, 2, 4]
    // {3: 0}
    // {3: 0, 2: 1}
    // {3: 0, 2: 1, }

    // for element in array
    // x = target - element if target >= element
    // check if x exists
    // if x exists, then return d[x], i
    // else, set d[x] = i

    const pair_idx = new Map();
    for (const [i, num] of nums.entries()) {
        const curr = target - num;
        if (pair_idx.has(curr)) {
            return [pair_idx.get(curr), i]
        } else {
            pair_idx.set(num, i)
        }
    }
};