let users = [ {
        name: "Joe",
        isActive: true
        },    
        {
            name: "Mary",   
            isActive: true},
        {   
            name: "Clarence",
            isActive: false
        }
    ];
/*
let activeUser = [];
for(let i=0; i<users.length; i++){
    if(users[i].isActive){
        activeUser.push(users[i]);
    }
}
*/

const activeUser = users.filter((user) =>  { //make a function inside a functino
    return user.isActive;
})
    


console.log(activeUser);
