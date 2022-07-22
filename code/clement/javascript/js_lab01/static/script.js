const input = document.getElementById('input');
const result = document.getElementById('result');
const inputType = document.getElementById('inputType');
const resultType = document.getElementById('resultType');
var inputTypeValue, resultTypeValue;

input.addEventListener('keyup', myResult);
inputType.addEventListener('change', myResult);
resultType.addEventListener('change', myResult);

inputTypeValue = inputType.value;
resultTypeValue = resultType.value;


function myResult(){
    inputTypeValue = inputType.value;
    resultTypeValue = resultType.value;

    if(inputTypeValue === "kilometer" && resultTypeValue === "meter"){
        result.value = Number(input.value)*1000

    }else if(inputTypeValue === "meter" && resultTypeValue === "kilometer"){
        result.value = Number(input.value)*0.001

    }else if(inputTypeValue === "meter" && resultTypeValue === "meter"){
        result.value = input.value

    }else if(inputTypeValue === "kilometer" && resultTypeValue === "kilometer"){
        result.value = input.value

    }else if(inputTypeValue === "kilometer" && resultTypeValue === "feet"){
        result.value = Number(input.value)*3280.84

    }else if(inputTypeValue === "feet" && resultTypeValue === "kilometer"){
        result.value = Number(input.value)*0.0003048

    }

    if(inputTypeValue === "meter" && resultTypeValue === "mile"){
        result.value = Number(input.value)*0.0006214

    }else if(inputTypeValue === "mile" && resultTypeValue === "meter"){
        result.value = Number(input.value)*1609.34

    }else if(inputTypeValue === "mile" && resultTypeValue === "mile"){
        result.value = input.value

    }else if(inputTypeValue === "mile" && resultTypeValue === "kilometer"){
        result.value = Number(input.value)*1.60934
        
    }else if(inputTypeValue === "kilometer" && resultTypeValue === "mile"){
        result.value = Number(input.value)*0.621371
    }


    if(inputTypeValue === "mile" && resultTypeValue === "feet"){
        result.value = Number(input.value)*5280

    }else if(inputTypeValue === "feet" && resultTypeValue === "feet"){
        result.value = input.value

    }else if(inputTypeValue === "feet" && resultTypeValue === "mile"){
        result.value = Number(input.value)*0.000189394

    }else if(inputTypeValue === "feet" && resultTypeValue === "meter"){
        result.value = Number(input.value)*0.3048

    }else if(inputTypeValue === "meter" && resultTypeValue === "feet"){
        result.value = Number(input.value)*3.28084
    }
}


