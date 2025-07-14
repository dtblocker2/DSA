process.stdout.write("Enter something: ");

process.stdin.on("data", function (data) {
  var noOfBits = data.toString().trim();
  calculateKMap(noOfBits)
  process.exit();
});

function calculateKMap(noOfBits) {
  const output = [];
  var a = "0";
  var b = "1";
  for (let i = 0; i < noOfBits; i++) {
    if (i == 0) {
      for (let j = 0; j < 2 ** noOfBits; j++) {
        if (j < 2 ** (noOfBits - 1)) {
          output.push("0");
        //   console.log(output);
          continue;
        }
        output.push("1");
        // console.log(output);
      }
      continue;
    }

    var a = "0";
    var b = "1";
    var y = 0;

    for (const j in output) {
      if (j < 2 ** (noOfBits - i - 1)) {
        output[j] += "0";
        continue;
      }

      y += 1;
      output[j] += b;
      if (y == 2 ** (noOfBits - i)) {
        [a, b] = [b, a];
        y = 0;
      }
    }
  }

  console.log('No of Bits:',noOfBits);
//   console.log(output);
  for (const i of output){
    console.log(i);
  }
}



// Doubt
// why isn't const output allowing to change its element as well as adding new element to it doesnt const element orevent change in data?
/* time complexity is O(2^n) ans space complexity is also O(2^n) */
