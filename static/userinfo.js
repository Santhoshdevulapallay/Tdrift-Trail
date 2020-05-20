var stationByCategory = {
    ANDHRAPRADESH: ["Araku", "Achar", "Kudgi", "bhgt"],
    ANTPSOLAR: ["kaliki", "rtpp", "rtpp2", "Others"],
    GOA: ["tnlv", "kochi", "trvdm", "coasta", "ilfs"]
}

    function changecat(value) {
        if (value.length == 0) document.getElementById("category").innerHTML = "<option></option>";
        else {
            var catOptions = "";
            for (categoryId in stationByCategory[value]) {
                catOptions += "<option>" + stationByCategory[value][categoryId] + "</option>";
            }
            document.getElementById("category").innerHTML = catOptions;
        }
    }
    
