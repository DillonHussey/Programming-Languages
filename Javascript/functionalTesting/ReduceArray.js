//Get the number of distinct pets

const pets = ['dog', 'cat', 'dog', 'gerbel', 'chicken', 'chicken'];

const petCount = pets.reduce((obj, pet) => {
    if(!obj[pet]) {
        obj[pet] = 1;
    }
    else{
        obj[pet]++;
    }
    return obj;
}, {});
console.log(petCount);