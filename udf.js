function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.name = values[0];
    obj.country = values[1];
    obj.created_at = values[2];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }