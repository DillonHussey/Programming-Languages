let items = [
    { name: 'Edward', score: 21 },
    { name: 'Sharpe', score: 37 },
    { name: 'And', score: 45 },
    { name: 'the', score: -12 },
    { name: 'Magnetic', score: 13 },
    { name: 'Zeros', score: 37 }
  ];

  function ScoreSort(a,b) { return a.score - b.score };

//example of closure
  function NameSort(a,b) {
    let first = a.name.toUpperCase();
    let second = a.name.toUpperCase();
    if(first < second) {
        return -1;
    }
    if(first > second) {
        return 1
    }
    return 0;
}

  let sortedItems = items.sort(NameSort);
  console.log(sortedItems);

  
