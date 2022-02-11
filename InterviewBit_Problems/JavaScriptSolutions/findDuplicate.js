var s = {
  findDuplicate: function (A) {
    var map = {};
    for (var i = 0; i < A.length; i++) {
      if (map[A[i]]) {
        return A[i];
      } else {
        map[A[i]] = true;
      }
    }
    return -1;
  },
};

console.log(s.findDuplicate([3, 4, 1, 4, 1]));
