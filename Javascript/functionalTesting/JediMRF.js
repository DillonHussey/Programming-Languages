let personnel = [
    {
      id: 5,
      name: "Luke Skywalker",
      pilotingScore: 98,
      shootingScore: 56,
      isForceUser: true,
    },
    {
      id: 82,
      name: "Sabine Wren",
      pilotingScore: 73,
      shootingScore: 99,
      isForceUser: false,
    },
    {
      id: 22,
      name: "Zeb Orellios",
      pilotingScore: 20,
      shootingScore: 59,
      isForceUser: false,
    },
    {
      id: 15,
      name: "Ezra Bridger",
      pilotingScore: 43,
      shootingScore: 67,
      isForceUser: true,
    },
    {
      id: 11,
      name: "Caleb Dume",
      pilotingScore: 71,
      shootingScore: 85,
      isForceUser: true,
    },
  ];

  //get total score of force users only
/*
  let allJedi = personnel.filter((person) => {
    return person.isForceUser;

  });

  let jediScore = allJedi.map((jedi) => {
      return jedi.pilotingScore + jedi.shootingScore;
  });

  let totalForceScore = jediScore.reduce((jediScore,running) => {
    return jediScore + running
  }, 0)

  console.log(jediScore);
  console.log(totalForceScore)

  
  let jediGrandTotal = personnel
    .filter((person) =>{
        return person.isForceUser;
    })
    .map((jedi) => {
        return jedi.pilotingScore + jedi.shootingScore;
    })
    .reduce((acc, score) =>{
        return acc + score;
    },0);
    */

function findJediScores(pilots)  {
    return pilots
    .filter(person => person.isForceUser)
    .map((jedi) => jedi.pilotingScore + jedi.shootingScore)
    .reduce((acc, score) => acc + score,0);
}
let jediGrandTotal = findJediScores(personnel);
console.log(jediGrandTotal);

