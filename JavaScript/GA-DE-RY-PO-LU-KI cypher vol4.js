function checkKPCount(keyPair) {
    let newBase = new Set();
  
    // Do ASCII value comparison
    for (let pair of [...new Set(keyPair)].sort()) {
      if (pair[0].charCodeAt(0) < pair[2].charCodeAt(0)) {
        newBase.add(pair);
      } else {
        let x = pair.split("").reverse().join("");
        newBase.add(x);
      }
    }
  
    let prefixCounts = {};
  
    for (let item of newBase) {
      let prefix = item.split("-")[0];
      if (prefix in prefixCounts) {
        if (prefixCounts[prefix] == 1) {
          prefixCounts[prefix] += 1;
        } else {
          return "False";
        }
      } else {
        prefixCounts[prefix] = 1;
      }
    }
  
    let x = [...newBase].sort().join("").replace(/-/g, "");
    return x;
  }
  
  function evaluateKP(m, se) {
    // Build Key-Pairs
    let keyPair = [];
    for (let i = 0; i < m.length; i++) {
      for (let j = 0; j < m[i].length; j++) {
        if (m[i][j] != se[i][j]) {
          keyPair.push(m[i][j] + "-" + se[i][j]);
        }
      }
    }
  
    let sortedKP = [...new Set([...keyPair].sort())];
    let checkIfValid = checkKPCount(sortedKP);
  
    if (checkIfValid.length == 12) {
      return checkIfValid;
    } else {
      return null;
    }
  }
  
  function getKP(combination) {
    let m = combination.map((i) => i[0]);
    let s = combination.map((i) => i[1]);
    let x = evaluateKP(m, s);
    if (x != null) {
      return x;
    } else {
      return null;
    }
  }
  
  function searchForKey(messages, secrets) {
    let messagePerms = Array.from(new Set(permutations(secrets)));
    let combos = messagePerms.map((perm) =>
      perm.map((p, i) => [messages[i], p])
    );
  
    for (let combination of combos) {
      let x = getKP(combination);
      if (x == null) {
        continue;
      } else {
        return x;
      }
    }
  }
  
  function permutations(arr) {
    if (arr.length == 1) {
      return [arr];
    }
  
    let result = [];
    for (let i = 0; i < arr.length; i++) {
      let current = arr[i];
      let remaining = arr.slice(0, i).concat(arr.slice(i + 1));
      let remainingPerms = permutations(remaining);
      for (let j = 0; j < remainingPerms.length; j++) {
        let perm = [current].concat(remainingPerms[j]);
        result.push(perm);
      }
    }
  
    return result;
  }