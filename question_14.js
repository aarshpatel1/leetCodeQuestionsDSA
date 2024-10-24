var strings = ["apple","banana","cherry"]
var prefix= []

function checkPrefix(prefix_array){
    let isSame = true
    console.log(prefix_array)
    for(let k=0; k<prefix_array.length; k++){
        if(k +1<prefix_array.length -1){
            if(prefix_array[k] !== prefix_array[k+1]){
                return false
            }
        } else {
            return isSame
        }
    }
}

var final_prefix = ""
for(let i =0;i <strings.length; i++){
    let prefixes = []
    for(let j=0; j<strings.length; j++){
        prefixes.push(strings[j][i])
    }
    if(!checkPrefix(prefixes)){
        console.log("loop is broken")
        break
    } else {
        console.log("prefixes: "+prefixes)
        final_prefix +=prefixes[0]
        prefix.push(prefixes)
        console.log("prefix: "+ prefix)
    }
}

console.log(prefix)

console.log("Final Prefix: "+final_prefix)