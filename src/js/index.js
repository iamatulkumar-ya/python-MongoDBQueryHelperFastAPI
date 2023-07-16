function callConnectToMongoDB(formData) {
  // reading element to show the error messages
  connectionMessage = document.getElementById("connectionMessage");
  connectionMessage.innerHTML = "";

  // reading form data
  connectionString = formData.connectionString.value;
  dbName = formData.dbName.value;
  collectionName = formData.collectionName.value;

  // checking if any field is empty
  if (
    String(connectionString).trim() == "" ||
    String(dbName).trim() == "" ||
    String(collectionName).trim() == ""
  ) {
    console.log("inside IF");
    connectionMessage.innerHTML = "Error: All fields are required.";
  }

  // making server call to connect to db
  else {
    var formData = {
      connectionString: connectionString,
      dbName: dbName,
      collectionName: collectionName,
    };

    // creating request
    xmlhttp = new XMLHttpRequest();

    // xhttp.onreadystatechange =function(){
    //     console.log("logging response text onreadystatechange")
    //     console.log(this.responseText)
    // }

    // below method is to read the response
    xmlhttp.onload = function () {
      if (this.responseText != "") {
        console.log("Response is not blank");
        jsonResponse = JSON.parse(this.responseText);
        console.log(jsonResponse);
        if (jsonResponse.responseStatusCode == 200) {
          console.log("Connected");
        } else {
          connectionMessage.innerHTML = jsonResponse.responseError;
        }
      } else {
        connectionMessage.innerHTML =
          "Error: Some unknown error occured. Kindly verify entered details or rery.";
      }
    };

    xmlhttp.open("POST", "/ConnectToMongo", true);
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    console.log("sending request");
    xmlhttp.send(JSON.stringify(formData));
  }
}



function resetConnectToMongoDB(){
    document.getElementById("connectionMessage").innerHTML = "";
    document.getElementById("connectionFormID").reset()
}
